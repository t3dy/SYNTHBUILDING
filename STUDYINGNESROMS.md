# STUDYINGNESROMS — reverse-engineering NES sound drivers without hallucinating

Scope: the layer BEFORE synthesis — getting real APU register data out of a ROM
or NSF file and trusting it correctly. Distilled from `NSFRIPPER`'s ~40 hardened
architecture rules (`.claude/rules/architecture.md`, `docs/MISTAKEBAKED.md`) and
its "Anti-Hallucination Mandate" (`wiki/project_nsfripper.md`). This is the part
of the pipeline where NSFRIPPER has the most mileage; SYNTHBUILDER's synth work
should trust its ground-truth data, not rediscover how to get it.

## The core discipline: three layers, never conflated

1. **Observed** — raw APU register writes. Authoritative, not interpreted.
2. **Intent** — a parser's interpretation of those writes (Frame IR). A
   HYPOTHESIS until validated against ground truth.
3. **Projection** — MIDI, RPP, synth output. PROVISIONAL until Intent passes a
   validation gate.

Debug in this order, always: SysEx/register replay first, then Frame IR, then
MIDI. **Never debug MIDI before confirming Frame State is correct** — NSFRIPPER
burned 3+ prompts more than once from reasoning about wrong output at the wrong
layer.

## Anti-hallucination mandate

Zero tolerance for guessing hardware/driver behavior. Concretely:
- **Dump trace data before modeling anything.** NSFRIPPER guessed 3 envelope
  hypotheses before looking at actual frame data — cost 5 prompts.
- **Manifests before code.** Every new game needs a manifest in
  `extraction/manifests/` (mapper, pointer table, command format, facts vs.
  hypotheses) BEFORE parser code is written.
- **Same driver code ≠ same ROM layout.** Running a CV1 parser on other ROMs
  assuming it would just work cost 3 prompts.
- **Same period table ≠ same driver.** Assuming CV2 used the same pointer table
  as a sibling game cost 4 prompts scanning for something that didn't exist.
- **Same opcode ≠ same semantics.** `DX` reads 2 bytes in one driver, 3 in
  another — never copy command handling across drivers without checking.
- **Zero parse errors ≠ musical correctness.** A parser can report 0 errors and
  still be wrong (Battletoads: duration 1.52x off, arpeggio unmodeled, cost 5+
  prompts) — structural success is not semantic success. Run execution-
  semantics validation (simulate the driver frame-by-frame, compare to trace)
  before trusting parser output.
- **Automated tests can't catch systematic errors.** An octave-off-by-exactly-12
  bug showed zero mismatches in trace comparison — always also *listen*.

## Per-game checklist (before writing any parser code)

1. Check mapper type.
2. Search for existing disassembly.
3. Identify the driver (scan for its DX/FE/FD-style command patterns).
4. Find the pointer table from disassembly — never by scanning blind.
5. Check the DX byte count for THIS driver (how many bytes follow?).
6. Check `$C0-$CF`-range semantics (rest vs. mute — drivers differ).
7. Check percussion format (inline vs. separate channel).
8. Parse ONE track and listen before batch-extracting anything.

## Debugging protocol (when output doesn't match the game)

1. Identify the symptom precisely — which channel, which aspect.
2. Extract trace data for the exact frames in question. Don't reason in the
   abstract.
3. Compare at frame level — look at the FIRST mismatch, not a summary.
4. Form ONE hypothesis and test it. Don't try three fixes at once.
5. If trace shows zero mismatches but it still sounds wrong, suspect octave
   mapping — compare by ear against the actual game.

## Hardware facts worth memorizing (not driver-specific, always true)

- Triangle channel is always 1 octave lower than pulse for the same period
  value (32-step vs. 16-step sequencer).
- Triangle has no hardware volume — only a gate (linear counter + length
  counter). CC11 for triangle is always 127; duration alone shapes it.
- Noise channel period index is *inverted*: index 0 = longest period (lowest
  pitch), index 15 = shortest (highest pitch) — opposite of melodic channels.
- The NES DAC mixes non-linearly (impedance-based), not additively. Two pulses
  at max volume produce ~0.278, not 2x one pulse. See `BUILDINGSYNTHS.md`.
- `$4015` (channel enable) is written once at init by most drivers and
  silencing is done via `vol=0` instead — **except** the noise channel in many
  first-party/Capcom drivers, which relies on the hardware length counter to
  silence each hit, not on `vol=0` or `$4015`. Test each channel type
  separately; don't generalize one channel's silencing behavior to another.
- An NSF player MUST write `$4015 = $0F` and `$4017 = $40` before calling
  INIT, or every driver that doesn't re-enable `$4015` itself will have its
  noise channel silently gated off for the whole song — with no error, just
  missing audio. (NSFRIPPER lost this for an entire pipeline generation before
  catching it; see architecture.md Rule 36.)

## Fidelity hierarchy — truth flows downhill

1. Mesen hardware trace (frame-level ground truth; NSF can diverge from actual
   game audio — proven on Battletoads, Mario).
2. SysEx-encoded register replay in MIDI (lossless).
3. NSF emulation (6502 CPU runs the real sound driver; convenient, not always
   faithful).
4. CC11/CC12 in MIDI (volume + duty; loses sweep, noise mode, phase).
5. ADSR approximation (only for live keyboard play with no file data).

Never let a lower layer override a higher one when both are available.

## For SYNTHBUILDER practice work

You will not usually need ROM-level reverse engineering — NSFRIPPER's NSF
emulation pipeline (`nsf_to_reaper.py`) already produces trustworthy MIDI +
CC11/CC12 automation for hundreds of games. Reuse that output as your test
material for patch and plugin design (`BUILDINGPATCHES.md`,
`BUILDINGSYNTHS.md`) rather than re-deriving driver behavior from scratch. Only
reach for this document's checklist if you're extracting a game NSFRIPPER
hasn't covered, or auditing why its output sounds wrong for one you're
building a patch against.
