# BUILDINGPATCHES — designing NES-accurate instrument patches

Scope: the layer between "we have trustworthy register/MIDI data" and "the
plugin renders correct sound" — envelope shape, timbre, per-channel behavior.
This is where a patch sounds *structurally* right (correct notes, correct
timing) but *texturally* wrong, which is the hardest class of bug to notice
because nothing errors and nothing looks broken in the RPP. Distilled from
`NSFRIPPER/.claude/rules/synth_fidelity.md` and architecture.md rules 27, 29,
30, 32-35, 39-40.

## CC11 = volume, CC12 = duty — and they are independent of note duration

- `CC11` maps to NES volume: `nes_vol = floor(cc_value * 15 / 127)`.
- `CC12` maps to duty cycle (pulse only): 0-31→12.5%, 32-63→25%, 64-95→50%,
  96-127→75%.
- **Note duration is NOT volume-driven.** In NSF-extracted MIDI, a note's
  duration is set by when the APU *period register* changes — not by when
  volume hits zero. A note can go silent for its last several frames (CC11
  decays to 0 before the period changes) and that is correct NES behavior, not
  a bug to "fix" by truncating the note early.
- Do not override CC11/CC12 automation with a live ADSR envelope when file data
  is present — that discards the actual per-frame envelope the original driver
  wrote. ADSR is for live keyboard play only, when there is no file data to
  play back (see the three-priority cascade in `BUILDINGSYNTHS.md`).

## Hardware envelope vs. constant volume — these are not the same signal

`$4000`/`$400C` bit 5 selects the mode:
- **Bit 5 = 1 (const_vol):** the volume bits ARE the volume. Read them
  directly.
- **Bit 5 = 0 (hardware envelope):** the volume bits are the **envelope
  period**, not volume. Real volume starts at 15 on every trigger write and
  decays once per `(period+1)` envelope clocks (240 Hz, 4 clocks/frame),
  looping if `env_loop` is set. Treating the raw bits as volume when this mode
  is active makes the channel sound ~10x too quiet and flat — confirmed on
  Wizards & Warriors, where the raw vol bits read 0-2 but the actual envelope
  peaked at 15. **Simulate the envelope; don't read the bits as volume.**

## Noise-channel patches are their own semantic domain — do not reuse melodic logic

- Drum "hits" are not reliably `vol 0→positive` transitions. Two driver
  classes never produce that transition: continuous-vol drivers (volume stays
  nonzero the whole song, hits are marked only by trigger writes) and
  hardware-envelope drivers (volume bits are envelope period, not volume, so
  "vol" may read 0 forever while drums play loudly). A drum hit is:
  `(vol>0 and prev_vol<=0) OR (trigger_write and audible)`.
- Many drivers (Nintendo 1st-party, Capcom) silence each noise hit via the
  **hardware length counter**, not via `vol=0` or clearing `$4015`. Gate noise
  output on `vol>0 AND enabled AND length_counter>0` — the length counter must
  actually be simulated (reload on trigger write, decrement twice per 60Hz
  frame unless halted), or a continuous "wash of noise" results where the
  reference has discrete drum bursts. Confirmed impact on Super Mario Bros:
  noise-active frames dropped from 92% (wash) to 25% (bursts) once simulated.
- Noise period index is inverted relative to melodic channels (see
  `STUDYINGNESROMS.md`) — don't reuse the melodic pitch→period mapping.

## Avoiding audible artifacts (clicks, pops, "overdrive")

- **DC offset:** never derive silence from a subtracted constant (e.g.
  `mixed - 0.35`, which is nonzero when `mixed=0`). Use a real 1-pole high-pass
  DC blocker (~10 Hz cutoff) so silent regions land at true zero — otherwise a
  DAW will show every frame as "active" even during silence.
- **Triangle gate-off "vinyl pop":** on gate-off (linear or length counter hits
  zero), the real hardware *holds* the sequencer at its current step — it does
  NOT jump to zero. Zeroing the wave on gate-off produces an audible ~38% step
  that reads as a vinyl-pop. Hold the last sample value on gate-off (don't
  advance phase) and let the DC blocker resolve it to silence over ~50ms
  instead.
- **Pulse-wave aliasing ("overdrive" character on sustained notes):** naive
  point-sampling of a pulse wave is an infinite-bandwidth step function; a
  simple 2-pole low-pass only removes 12dB/octave of the resulting aliasing.
  Compute each sample as the time-averaged integral of the ideal pulse across
  the sample window (an analytic anti-alias at synthesis time) rather than
  sampling the raw square wave, especially for high-pitched sustained pulse
  notes.
- **Non-linear mixing is mandatory**, not a nice-to-have — see
  `BUILDINGSYNTHS.md` for the formulas. Linear (additive) mixing of multiple
  channels makes everything too loud and changes the character of chords.

## Per-driver-family ADSR presets, for the live-keyboard fallback

NSFRIPPER classifies games into four families by CC11/CC12 density
(`docs/NEWDRIVERFAMILIES414.md`). When designing keyboard-mode presets (no
file data, so ADSR must approximate a family's character), aim for:

| Family | Character | Example games | Rough ADSR |
|---|---|---|---|
| 1A: Sparse/pure HW decay | instant attack, full linear decay to silence, no sustain | Mega Man 1, Marble Madness | A=1f, D=8-15f to 0, S=0 |
| 1B: Sparse/occasional SW vol | instant attack, short decay to a held sustain | Castlevania, DuckTales | A=1f, D=4-6f, S=3-6, R=2-3f |
| 2: Active envelope | instant attack at 15, per-frame SW volume | Contra, Ninja Gaiden | A=1f, D=3-4f, S=4-8, R=2-3f |
| 3: Duty animators | Family 2 ADSR + duty cycle sweeps per note (12.5→25→50%) | SMB3, Konami Hyper Soccer | as Family 2 + duty LFO |
| 4: Dense automators | rapid per-frame volume table, tremolo/shimmer character | Metroid, Kid Icarus | multi-stage/tremolo envelope |

These are starting points for patch design, not a substitute for listening to
the actual reference game — NSFRIPPER's `preset_catalog.py` has 54K extracted
presets if you want real examples rather than hand-tuned approximations.
