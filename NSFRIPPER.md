# NSFRIPPER.md — the project family SYNTHBUILDER exists to unstick

Scope: what `NSFRIPPER`, `ReapNES-Studio`, and `NESjamtools` actually are, where
each stands right now (verified, not assumed), and what SYNTHBUILDER should do
differently. This is the direct answer to "study the pitfalls I documented
running into problems with NSFRIPPER trying to use AI to build synth plugins."
The pitfalls themselves live in `BUILDINGSYNTHS.md`, `BUILDINGPROJECTS.md`,
`BUILDINGPATCHES.md`, `STUDYINGNESROMS.md` — this file is the project map and
status; those are the technical checklists.

## The family, one paragraph each

**NSFRIPPER** (`C:\Dev\NSFRIPPER`) is the "Archive" layer: NSF/ROM → 6502
emulation (py65) → per-frame APU register capture → MIDI (with CC11=volume,
CC12=duty automation) → REAPER project, with a small number of flagship games
(Castlevania 1, Contra, Wizards & Warriors) additionally trace-validated
against real hardware via the Mesen emulator. It has a genuinely hardened
40-rule architecture doc and an "oracle" SQLite knowledge base
(`ANTIRIPPER/antiripper_v2.db`) that persists lessons across sessions —
structurally the most mature project in this family. Site:
`https://t3dy.github.io/NSFRIPPER/`.

**ReapNES-Studio** (`C:\Dev\ReapNES-Studio`) is where the JSFX-instrument and
MIDI-keyboard-routing problems were first fought and mostly won (see
`BUILDINGSYNTHS.md`'s JSFX-vs-VST3 section). It was folded into NSFRIPPER on
2026-03-31 — its `ReapNES_Console.jsfx` synth is the one NSFRIPPER's pipeline
uses today. Its `vst/` JUCE/VST3 build (CMake + generated MSVC solution)
remains an unused parallel track: it solves live keyboard input, but nobody
executed the documented fix (`SYNTHPROBLEM.md` Option D — extract a real VST3
RPP reference block from one manually-saved project, template from it) to
make it scriptable.

**NESjamtools** (`C:\Dev\NESjamtools`) is the sibling "Instrument" layer: a
single multitimbral JSFX (`NESJam.jsfx`) playing all four 2A03 voices live off
a keyboard or MIDI file, plus a separate hand-tuned Python renderer
(`nesjam/nes_render.py`) for high-fidelity WAV bounces. 50 games shipped as
ready REAPER projects; 4 games (Contra, Battletoads, Zelda, Wizards &
Warriors) additionally ship as "hybrid" projects (accurate audio stems, muted
editable MIDI underneath). Local-only, no git remote, never pushed anywhere.

**GlitchMario** (`C:\Dev\GlitchMario`) isn't a tool — it's the narrative
documentation of the same struggle (100 events, 17 blunders, 5 days,
"80% fidelity and climbing"), shipped as a small static site. **Confirmed
live** at `https://t3dy.github.io/GlitchMario/` (HTTP 200). Worth reading as a
model for how to narrate a failure-heavy build honestly, and worth reusing its
timeline-card format if SYNTHBUILDING wants a "how we got here" page.

## Where each one actually stands (verified, 2026-09-21)

| Project | Status | Verified live? | The real blocker |
|---|---|---|---|
| NSFRIPPER | ACTIVE but stalled — no commits since 2026-04-20 | Site: yes | An unmade decision. The last commit shipped three delivery variants (A "Double Dose" = stems+JSFX, B "Live Wire" = pure JSFX/MIDI, C "Ditto Head" = deferred/unbuilt) specifically so Ted could ear-test and pick one. That ear-test and decision never happened. |
| ReapNES-Studio | ARCHIVED (absorbed into NSFRIPPER) | N/A, no deploy | The VST3/JUCE build in `vst/` is a dead end nobody finished connecting to scriptable project generation. |
| NESjamtools | STABLE by its own docs, but explicitly **not** ear-confirmed | N/A, local only | One bug ("W&W Map: rhythm feels wrong") is marked "Awaiting your ears" in its own `output.md` — everything else it lists is marked Fixed. |
| GlitchMario | STABLE, complete | **Confirmed live, HTTP 200** | None — this one actually shipped. |

**The pattern across all four:** synthesis and extraction code is consistently
the *strong* part (NSFRIPPER's 40 rules are genuinely hard-won and correct;
NESjamtools' bug-fix log is thorough and mostly resolved). What stalls every
project at the finish line is the same thing SYNTHBUILDER's `CLAUDE.md` top
rule names: **an unmade "does a human confirm this by ear" decision.** Not a
missing feature — a missing 20-minute listening session.

## What this means for SYNTHBUILDER specifically

- Don't start SYNTHBUILDER by re-deriving NES synthesis math — NSFRIPPER's
  `.claude/rules/synth_fidelity.md` and `architecture.md` (40 rules, current
  and correct as of 2026-04-20) already encode it. Reuse or reference it.
- Don't build a fifth "big" NES-synth project. If SYNTHBUILDER's practice work
  produces something genuinely better, the highest-leverage move is finishing
  NSFRIPPER's pending A/B/C decision or NESjamtools' one open bug — not
  starting a sixth parallel implementation.
- The actual open technical gap worth SYNTHBUILDER's practice time is the one
  nothing in this family solved: **scriptable VST3 project generation for
  live-keyboard synths.** `ReapNES-Studio/SYNTHPROBLEM.md` Option D was
  identified as the answer and never executed. That is a concrete, bounded,
  worth-doing SYNTHBUILDER exercise.

## The wider family (found after the four above — same cluster, less examined)

- **NESMusicStudio** (`C:\Dev\NESMusicStudio`) — the largest/most active member
  of the whole cluster, possibly the actual current front-runner: NSF/ROM →
  MIDI → REAPER/WAV/MP4 → YouTube, live at `https://t3dy.github.io/ReapNES/`,
  git-committed and actively worked (Castlevania 1 complete 15/15 tracks 0
  pitch mismatches; Contra 11/11 tracks, 96.6% volume match). This may be
  where NSFRIPPER's lineage actually continued past 2026-04-20 under a
  different folder name — worth checking before assuming NSFRIPPER itself is
  the latest state.
- **REAPERBEYONDNES** (`C:\Dev\REAPERBEYONDNES`) — a declared successor
  extending the same pipeline past the NES to GBA/SMS/Saturn/Genesis/SNES/
  GBC/Virtual Boy, heavily structured (per-chip project folders, its own
  agent-protocol doc). **Not a git repository — real loss risk** if anything
  happens to this machine's disk.
- **nes-music-lab** (`C:\Dev\NESMusicLab`) — research-grade extraction/
  reconstruction work (Castlevania analysis, trace conversion, MIDI export).
  Has real code but is stalled/uncommitted.
- **arpeggiator-composer** (`C:\Dev\arpeggiator-composer`) — a deterministic
  MIDI arpeggiator built specifically for REAPER (`core/`, `jsfx/`,
  `reascript/`, `reaper_projects/`, `tests/`). Stalled/uncommitted.
- **ChipScribe/ChipTools** — live at `https://t3dy.github.io/ChipTools/`
  (`github.com/t3dy/ChipTools`), a deployed front-end for this family. No
  local source tree exists under `C:\Dev` — it's GitHub-only.
- **NESARPEGDESIGNS** — confirmed empty stub, never started.

**Action item, not just an observation:** `REAPERBEYONDNES` and
`nes-music-lab` hold real, uncommitted work with no git history. If
SYNTHBUILDER's agentic-environment discipline (checkpointing, one-writer-
per-file, verify-before-done) is worth adopting here, `git init` + first
commit on both is a five-minute, zero-risk action worth taking before
anything else touches those folders.

## Borrowing from tide-room (Eric Ruud's repo) for this specific family

Full findings: `research/tideroom_lessons.md`. tide-room is a JUCE/Metal
spatial synth for macOS — nothing about NES tone design transfers — but its
validation discipline maps directly onto exactly the failure pattern above:

- **`criteria.json`-style machine-checked gates, not prose memory.** tide-room
  encodes its hard constraints as a versioned JSON file a script enforces on
  every run. NSFRIPPER's equivalent constraints currently live only in
  `feedback_reaper_jsfx.md` and `.claude/rules/*.md` — true and thorough, but
  enforced by an LLM remembering to check them, not by a script that fails the
  build. A `jsfx_criteria.json` + lint step (tags:instrument present,
  in_pin/out_pin declared, sequential sliders, ASCII-only, `^` isn't XOR)
  run on every generated `.jsfx` before it reaches REAPER would catch the
  exact class of bug that cost NSFRIPPER/ReapNES-Studio the most prompts.
- **Colocated validators (`Foo.cpp` / `FooChecks.cpp`), same name, no
  exceptions.** A `generate_project.py` / `validate_rpp.py` pairing, always
  run together, would have caught the `MASTER_SEND`/`REC_INPUT` token-guessing
  blunders immediately instead of after a REAPER load failure.
- **The last gate is the real host, not a unit test.** tide-room's
  `evaluate.py` finishes by loading the actual built VST3 in a real plugin
  host. NSFRIPPER's equivalent — "does REAPER actually load this .RPP and
  produce sound" — is exactly the check that's been missing every time a
  project got "delivered" without it (see `SUCCESSANDFAIL.md`'s own verdict:
  "the user still cannot open a generated project and hear sound without
  manual intervention"). Automating that check, even crudely (parse the RPP
  with REAPER's own token rules; or a scripted REAPER-headless render that
  asserts non-silent output on a test MIDI note) is the single highest-value
  borrowed idea here.
- **Fresh, timestamped output per run, never overwritten.** Directly fixes two
  separate real problems in this family: REAPER's filename-based JSFX compile
  cache (Blunder 4 — a fresh filename becomes the default behavior, not a
  remembered manual workaround), and NSFRIPPER's own disk-bloat incidents
  (Rule 38 — two separate times the project filled the C: drive from
  un-versioned/un-cleaned batch output).
