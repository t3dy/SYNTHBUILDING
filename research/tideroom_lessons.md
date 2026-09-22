# tide-room: what it is and what transfers to SYNTHBUILDER / NSFRIPPER

Source: https://github.com/EricRuud/tide-room (public, AGPL-3.0-only, one contributor,
Eric Ruud + Codex). Read via README.md, EVALUATION.md, native/DEVELOPMENT.md,
native/FX-QUICKSTART.md, criteria.json, and the native/Room directory listing.
Documentation-level study, not a code read; not cloned.

## What tide-room is

A generative spatial synthesizer for Apple Silicon macOS (native standalone + VST3/AU),
C++17/JUCE 8.0.9 + Metal shaders. Three synth voices are visualized as glass towers of
plates in a 3D room; a physics-like "Ocean" model drives their position and feeds back
into synthesis (wavefolding, ring mod, AM, metallic voices). It layers measured binaural
spatialization (MIT KEMAR HRTF data), a custom reverb (ClearRoom), and a tape stage: an
original "Worn tape" design plus a behaviorally reverse-engineered clone of a commercial
821 unit built via ML model identification, not circuit modeling. It is **not** a
JSFX/REAPER project, not NES/chiptune, and mac-first (an experimental Windows x64 port
exists, CPU-rendered, audio engine shared). It's a from-scratch JUCE plugin/app with an
unusually heavy, well-documented DSP validation apparatus — that apparatus, not the sound
design, is what's transferable.

## Architecture notes

- Root: `native/` (C++/JUCE/Metal app + checks), `native/Lab/` (60+ one-hypothesis-per-file
  `p821_*.py` ML research scripts, kept even when rejected), root Python (`lab.py`,
  `doubles_reference.py`) for the original offline synthesis/listening lab, `criteria.json`
  (numeric pass/fail gates), `EVALUATION.md` (methodology, separate from code),
  `native/DEVELOPMENT.md` (build/test commands + architecture).
- `native/Room/` (~100 files) pairs almost every subsystem file with a same-named
  `*Checks.cpp`: `Ocean.h`/`OceanChecks.cpp`, `Binaural.cpp`/`SpatialChecks.cpp`,
  `WornTape.cpp`/`WornChecks.cpp`, `ClearRoom.cpp`/`ClearChecks.cpp`, `GpuEffects.mm`/
  `GpuChecks.cpp`, `EightTwentyOneTape.cpp`/`EightTwentyOneChecks.cpp`. Each check is a
  standalone executable writing to a fresh, timestamped output directory — never
  overwriting a prior run (`native/DEVELOPMENT.md` "Checks" section).
- `criteria.json`: flat versioned JSON of numeric gates (sample rates, FFT size, pitch
  bins, `max_stationary_reference_residual_db: -90.0`, `min_output_rms_dbfs: -35.0`,
  `max_output_peak: 0.99`, fixed RNG `seed`). Its own `status` field says `"provisional
  engineering limits; musical preferences not calibrated"` — machine-checkable limits are
  deliberately kept separate from taste.
- `native/evaluate.py`: snapshot source → build → run technical gates → compare output
  against an independently implemented Fourier/Bessel reference → **load the actual built
  VST3 in a real plugin host** → render presets for listening. A failed stage stops the
  loop. This last step is the closest analog to "does REAPER actually load this and make
  sound," done automatically instead of by hand.

## Concrete lessons for SYNTHBUILDER / NSFRIPPER

1. **Hard constraints belong in a machine-checked spec file, not just prose memory.**
   `criteria.json` is what `feedback_reaper_jsfx.md` currently is for Ted, except a script
   enforces it instead of an LLM having to recall it. Translation: a `jsfx_criteria.json`
   / lint script encoding `tags:instrument`, `in_pin:none`/`out_pin:Left`/`out_pin:Right`,
   sequential slider numbers, ASCII-only, `^`-is-power — run on every generated `.jsfx`
   before it reaches REAPER, so a violation fails the build instead of silently shipping.
2. **Colocate the validator with the thing it validates, same name.** The `Foo.cpp`/
   `FooChecks.cpp` pairing (100+ files, near-total coverage) means nothing ships without a
   check sitting beside it. For NSFRIPPER: a `validate_rpp.py` beside RPP generation that
   asserts the `REC` field has 8 tokens, MIDI uses `<SOURCE MIDI`+`FILE`, etc. — mirroring
   the exact pitfalls in `feedback_reaper_jsfx.md` — run automatically before "done."
3. **Every check run gets a fresh, timestamped output directory**, never overwriting a
   prior pass ("Use a new output folder per iteration," DEVELOPMENT.md, repeated per
   check). Applied to NSFRIPPER: write each generated JSFX/RPP candidate to
   `artifacts/<timestamp>-<name>/`, which also sidesteps REAPER's filename-based JSFX
   compile cache — a fresh name becomes the default, not a manual workaround remembered
   after the fact.
4. **The last gate is loading the real artifact in the real host**, not just DSP unit
   tests (`TideHostCheck`/`TideFXCheck` load the built VST3 in an actual plugin host).
   Passing spectral checks is explicitly necessary but not sufficient. Direct analog: a
   scripted check that opens the generated `.RPP` in REAPER (or parses it with REAPER's
   own tokenizer) and confirms the JSFX loads as an *instrument* and produces non-silent
   output on a MIDI note — the exact failure Ted hit ("REAPER silently treats it as an
   effect not an instrument").
5. **Rejected experiments are kept, with a note on why**, not deleted. `native/Lab/`'s
   60+ `p821_*.py` files, plus prose like "an early 4× nonlinear path was rejected after
   strong-drive probes exposed unwanted components." For iterative JSFX work: log a failed
   approach (e.g. a slider scheme that broke RPP loading) as "tried, failed, symptom X"
   at per-experiment granularity, not just folded into one lessons doc.
6. **Docs are split by audience, each stating its own scope and limits.** README (what/
   why), EVALUATION.md (methodology), DEVELOPMENT.md (exact commands/architecture) — each
   flags what it does *not* establish ("This does not replace the live editor/device
   test"). Worth copying: separate "how to build/test" from "what this proves" from "what
   still needs a human ear," so an AI agent doesn't mistake a passing script for a shipped,
   verified plugin.

## What doesn't transfer

- **Platform/toolchain**: macOS/Metal/Accelerate/Xcode/CMake/JUCE producing VST3/AU vs.
  Ted's Windows/REAPER/JSFX (a plain text format REAPER JIT-compiles at load, no separate
  compiler toolchain). None of the build/signing machinery applies.
- **Subject matter**: no APU register emulation, no NES channel modeling, no duty-cycle
  pulse synthesis discussion. Its DSP problems (tape saturation, spatial reverb,
  wavefolding) are unrelated to NES tone accuracy.
- **Scale of the harness**: hundreds of test cases and a full ML reverse-engineering
  program against a commercial plugin (training/validation/freeze protocol, blind
  listening with tie/uncertain options) is disproportionate to a JSFX synth, which is a
  few hundred lines of text with no compiled binary or plugin packaging step. Only the
  structural habits above are worth taking, not the specific tooling or its scale.
- **The 821 ML identification work** has no NES counterpart: NES target waveforms
  (square/triangle/noise/DMC) are exactly specified already, not an unknown black box
  requiring behavioral cloning.
