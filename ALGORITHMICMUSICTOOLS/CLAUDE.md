# ALGORITHMICMUSICTOOLS — Claude Code Instructions

## Project identity

A tool for **exploring music-theory structures by algorithmically generating
and manipulating musical examples** — chord progressions, counterpoint,
motif transformations, scale/mode relationships — so a learner (Ted, or
anyone) understands theory by playing with it rather than memorizing
definitions. The LLM orchestrates deterministic music-theory/composition
engines; it does not compose the examples itself, and it does not replace
theory explanation with vibes.

## Origin — this is a real, specific, previously unbuilt idea

Found via a `C:\Dev\megabase` sweep (2026-09-22) after Ted described wanting
"software [to] give the user ability to play around with automatically
composing examples to learn music theory by playing with all the structures
described by music theory in a music sequence creating software." That
description matches, closely and specifically, a single ChatGPT conversation
from **2026-03-10** ("Karpathy AutoResearch Overview") that fully spec'd an
"AI-assisted Music Engineering Workbench" — preserved verbatim at
`sources/chatgpt_music_workbench_2026-03-10.txt`. **This idea was never built.**
No project folder anywhere in `C:\Dev` implements it; the closest existing
fragments (NSFRIPPER's extraction pipeline, NESjamtools' synth, `arpeggiator-
composer`'s deterministic MIDI arpeggiator) each cover one small corner of it
without the theory-education framing or the algorithmic-transformation
engine at its center. See `IDEA_SOURCE.md` for the full distillation.

## Product philosophy (stated directly in the source conversation, keep it)

> "The LLM is NOT primarily composing music directly. The LLM acts as an
> orchestration and interpretation layer over deterministic music-analysis
> engines, symbolic music-processing pipelines... Do not make the LLM the
> source of truth for musical state. The source of truth should be
> structured project data."

Concretely: natural language → structured command → deterministic
transformation engine → inspectable symbolic output → theory explanation.
Every transformation (invert this motif, reharmonize this progression, turn
this theme into a fugue, add counterpoint to this melody) should be a named,
deterministic operation with a visible before/after, not an LLM freehand
rewrite.

## Scope discipline — this is a scaled-down vertical slice, not the full workbench

The source conversation specs an enormous system (audio transcription, MIR
analysis, guitar tablature solving, ROM/chiptune reverse engineering, DAW
automation, a branchable composition graph...). Most of that is out of
scope here and already covered elsewhere in this workspace (NSFRIPPER does
the chiptune/ROM piece; `arpeggiator-composer` and the REAPER family do DAW
automation). **ALGORITHMICMUSICTOOLS keeps only the piece nothing else in
this workspace covers: the algorithmic-composition engine + theory-analysis
subsystem, as a standalone educational playground.** The source
conversation's own recommended first vertical slice (adapted, dropping the
guitar-tab-specific parts which belong to a different project's scope):

> Natural language command → symbolic melody import → theory-analysis
> overlay (roman numerals, intervals, cadence detection) → algorithmic
> transformation (invert, retrograde, reharmonize, add counterpoint) →
> inspectable before/after output + plain-language theory explanation.

See `DESIGN.md` for the actual scoped design.

## SYNTHBUILDER family discipline applies here too

This project inherits SYNTHBUILDER's verification-first rule, adapted: **get
one working transformation (e.g. "invert this melody" on one hardcoded
example) producing correct, inspectable, explainable output before building
a UI, a library of transformations, or theory-analysis overlays.** The
source conversation's own risk register (if extracted) will likely name
"scope creep before one thing works" as the top risk — the pattern is
already proven costly elsewhere in this workspace (see `../NSFRIPPER.md`,
`../ReapNES-Studio`'s docs) and there is no reason to assume this project is
immune.

## Directory layout

```
ALGORITHMICMUSICTOOLS/
  CLAUDE.md          this file
  IDEA_SOURCE.md      full distillation of the founding conversation
  DESIGN.md            the scoped vertical-slice design
  DECISIONS.md         directional calls, recorded immediately
  sources/              raw source material, unedited
```
