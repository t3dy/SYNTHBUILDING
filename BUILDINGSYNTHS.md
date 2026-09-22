# BUILDINGSYNTHS — writing the actual JSFX / VST3 plugin

Scope: the plugin file itself — what makes REAPER recognize it as an
instrument, route MIDI to it, and produce correct audio. This is where the
single most expensive class of silent failure in this workspace's music
projects lives: a plugin that compiles cleanly, shows a UI, and produces
*nothing* when triggered, with no error anywhere. Distilled from
`ReapNES-Studio/docs/BLOOPERS.md`, `AVOIDBLUNDERS.md`, `SYNTHPROBLEM.md`, and
`NSFRIPPER/.claude/rules/{architecture,synth_fidelity,jsfx_deploy}.md`.

## Minimum viable JSFX instrument header

```
desc:Plugin Name
tags:instrument synthesizer
in_pin:none
out_pin:Left
out_pin:Right
```

Every one of these lines is load-bearing:
- `tags:` — not `//tags:`. The `//` comments it out and REAPER silently treats
  the plugin as an effect, not an instrument.
- `in_pin:none` — without it, REAPER expects audio input (effect behavior) and
  a synth fed only MIDI produces silence. This single missing line cost an
  entire ReapNES-Studio debugging session before being found.
- ASCII only, anywhere in the file (comments included). Unicode em-dashes or
  arrows can break compilation silently on Windows/cp1252 systems.

## Slider and operator gotchas

- Slider numbers must be sequential — a gap (e.g. slider15 jumping to
  slider20) risks REAPER misassigning values when it serializes the 64
  positional slots into an RPP file. Renumber before shipping, don't leave
  gaps "for future use."
- `^` in JSFX is **exponentiation**, not XOR. For single-bit XOR use
  `((a + b) & 1)`. (Confirmed cause of "the noise channel produces alien
  transmissions" — GlitchMario blunder B05.)
- REAPER caches compiled JSFX **by filename**. If a plugin stops working right
  after you edit it, that's very likely a stale cached compile, not a new bug
  — rename the file (or run a sync script that renames/rehashes) to force a
  fresh compile before debugging further.

## The JSFX-vs-VST3 keyboard problem (read before choosing a plugin format)

This is the central unsolved tension across every synth attempt in this
workspace (see `ReapNES-Studio/SYNTHPROBLEM.md` in full):

| | JSFX | VST3 (e.g. via JUCE) |
|---|---|---|
| MIDI file playback | Works | Works |
| Live MIDI keyboard input | **Does not work** — JSFX lacks the VST "instrument" flag, so REAPER routes live keyboard input as if to an effect, not a synth. This looks like a REAPER limitation, not a fixable bug in your plugin code. | Works — REAPER natively routes MIDI to VST3 instruments. |
| RPP generation (scripted, no REAPER involved) | Trivial — a text path + slider values in the FXCHAIN block. | Hard — REAPER's RPP reference for a VST3 plugin instance requires a base64-encoded binary state blob and a plugin FUID, both effectively only producible by REAPER itself. |

**No clean resolution was found.** The least-bad workaround documented
(`SYNTHPROBLEM.md` Option D): have the user add the VST3 to one track manually
in REAPER once, save the project, and extract the exact VST3 reference block
from that file to use as a template for all future generated projects. Don't
re-attempt to reverse-engineer the FUID/state-blob format from scratch —
templating from a real saved project is faster and was already identified as
the recommended path.

If your goal is "MIDI file playback + editable project," JSFX alone is
sufficient and much simpler — don't reach for VST3/JUCE unless live keyboard
input is a hard requirement.

## Non-linear APU mixing (mandatory if emulating NES channels)

The real NES DAC mixes channels non-linearly (impedance-based), not
additively:

```
pulse_out = 95.88 / ((8128.0 / (sq1 + sq2)) + 100.0)
tnd_out   = 159.79 / ((1.0 / (tri/8227 + noise/12241 + dpcm/22638)) + 100.0)
```

Two pulse channels at max volume (15+15) produce ~0.278, not 2x one pulse
(~0.184) — adding a second pulse *compresses* the first. This is not a
loudness cap, it's the actual analog interaction. **Never mix with
`out += channel_a + channel_b`** for NES-style synthesis; route both pins
through these formulas. UI gain/mix knobs should scale per-channel amplitude
*before* this stage, so the hardware-interaction character is preserved.

## The "one synth plugin, priority cascade" design pattern

NSFRIPPER's answer to needing archival fidelity, editable-project playback,
and live keyboard play from a single plugin (`docs/SYNTHMERGE.md`): one JSFX
file that auto-detects its input and picks the highest-priority mode
available per note:

1. **SysEx register replay** (if SysEx `F0 7D 01 ...` arrives) — maximum
   fidelity, the raw APU register bytes drive the waveform directly. This
   reproduces sweep, phase reset, noise mode — everything MIDI CC encoding
   loses.
2. **CC-driven mode** (CC11 volume + CC12 duty arrive, no SysEx) — file
   playback without full hardware fidelity. Period comes from MIDI note
   number, semitone-quantized.
3. **ADSR keyboard mode** (no file data at all) — for live composing; shaped
   by knob/slider-set envelope, per driver-family preset (see
   `BUILDINGPATCHES.md`).

`CC123`/`CC121` (all-notes-off / reset) resets back to ADSR mode. This pattern
is worth reusing for SYNTHBUILDER practice plugins even at small scale — it
avoids needing separate plugin files for "play my extracted MIDI" vs. "let me
noodle on a keyboard."

## Before calling any plugin done

From `ReapNES-Studio/docs/AVOIDBLUNDERS.md`'s "Correct Order of Operations":
1. Does it produce a beep from one MIDI note, added **manually** via the FX
   browser? Confirm before anything else.
2. Save that track as `.RPP`, read the file, confirm you understand the exact
   token format REAPER used.
3. Does a **minimal** generated RPP (no custom slider values, defaults only)
   load and still produce sound?
4. Only then add slider values, features, and automation — one at a time,
   re-testing after each.

Never build a batch pipeline, preset catalog, or song-set system before step 1
is confirmed. See `CLAUDE.md`'s top rule.
