# IDEA_SOURCE.md — the founding conversations, distilled

Two independent sources, found in two separate megabase sweeps, turned out
to converge on the same project. Source 2 (found later, in a deeper sweep)
is the stronger, more concrete, more personally-motivated spec — read it
first if choosing one.

## Source 2 (the stronger match) — "Harmony Sonata Adventure"

*Harmony Sonata Adventure Guide*, ChatGPT (`chatgpt-md`), 2026-02-23. Found
via `research/DEEPCUTS.md` (a deeper, broader-net megabase sweep than the
one that found Source 1 below). Ted's opening ask, verbatim:

> "I'd like to build a website that walks a user through writing s four part
> harmony or sonata as a choose your own adventure" ... "also canons, fugue,
> rondo, ragtime, any structure that is used in final fantasy tunes"

And, crucially, the personal motivation stated directly:

> "I am very interested in music but have always struggled to learn theory
> and practice the fundamentals"

This conversation is a **complete product spec**, not a sketch: a "Form
Engine" architecture (`Piece, Section, Motif, Node, Option, Transform,
Validator, LessonTrigger`), a concrete stack (FastAPI + Pydantic backend,
`music21` for theory/MusicXML, React + TypeScript + Vite frontend,
OpenSheetMusicDisplay for notation, Tone.js for playback), a
constraint-based SATB voicing solver, and per-form "adventure spines"
written out node-by-node for chorale harmonization, canon, fugue
exposition, rondo, and game-loop forms explicitly modeled on Final Fantasy
music structures. The assistant redesigned the pedagogy around Ted's stated
struggle: "sound first, labels second" (contrast-mode A/B playback, a
"break the rule" toggle so you hear *why* a rule exists, bass-first
teaching, forced closure so every session ends in one finished 8-bar
piece). The thread ends with a ready-to-paste Claude Code initiation prompt
and a milestone/acceptance-criteria plan.

**This is the design ALGORITHMICMUSICTOOLS should actually build toward** —
its **choose-your-own-adventure framing** (you don't just watch a
transformation happen, you're offered a small set of theoretically-valid
next moves and choose one, at each step) is a stronger pedagogical hook
than this project's original "apply a named transformation and read an
explanation" framing, and its "Form Engine" node/option/validator model is
effectively a more fully-worked version of this project's
`TransformationOperation` data model (`DESIGN.md`). Full text search:
`DEEPCUTS.md` §1 for the complete distillation with more verbatim quotes.

## Source 1 (found first, broader but shallower) — "AI-assisted Music Engineering Workbench"

Source: `sources/chatgpt_music_workbench_2026-03-10.txt` (ChatGPT, source
`chatgpt-md`, conversation "Karpathy AutoResearch Overview", 2026-03-10,
found via `C:\Dev\megabase\megabase.db` FTS search). Full text preserved
verbatim in that file — read it directly for anything not captured below.
Still useful for its broader subsystem decomposition and shared data-model
vocabulary (below); Source 2 above is the better guide for the actual
CYOA/theory-teaching interaction design.

## What Ted actually asked for (his own words, verbatim)

> "AI-assisted music engineering workbench; hybrid DAW controller + analysis
> engine + reverse-engineering toolkit + transcription system; designed for
> musicians, programmers, musicologists; goal: turn audio, scores, ROM
> music, MIDI, and natural language instructions into playable arrangements,
> guitar tabs, chiptune tracks, DAW sessions, theory explanations."

> "Algorithmic composition engine manipulates symbolic sequences; operations
> include motif inversion, retrograde, sequencing, reharmonization, cadence
> insertion, phrase expansion, variation generation; deterministic rules
> combined with probabilistic models."

> "Theory analysis subsystem computes harmonic function, roman numeral
> analysis, tonal tension graphs, motif recurrence networks, phrase
> boundaries, style similarity metrics; visual overlays on score and
> sequence views."

> "Designed both as composition tool and educational environment; user sees
> relationships between sound design, musical structure, instrument
> constraints, performance ergonomics."

> "Target users include composers exploring retro hardware, guitarists
> needing playable arrangements, programmers studying algorithmic music,
> **and learners wanting theory explanations embedded in music workflows.**"

That last line is the closest direct match to what Ted described wanting in
2026-09-22: software that lets you "play around with automatically
composing examples to learn music theory by playing with all the structures
described by music theory."

## The full subsystem list (as specified, for reference — not all in scope here)

Ingestion/import, MIR/audio analysis, transcription engine, symbolic music
representation, guitar tablature engine, fretboard/ergonomics
visualization, chiptune/ROM reverse-engineering, patch/synthesis library,
**algorithmic composition/transformation engine**, **theory analysis
subsystem**, DAW integration, rendering/export, project state/persistence,
natural-language orchestration, UI workbench layer.

Bold = the two subsystems ALGORITHMICMUSICTOOLS actually scopes to build
(see `DESIGN.md`). Everything else either belongs to a different existing
project in this workspace (chiptune/ROM → NSFRIPPER; DAW integration →
NESjamtools/arpeggiator-composer) or is out of scope entirely (guitar
tablature, audio transcription — no existing groundwork, not what Ted asked
for on 2026-09-22).

## Proposed shared data models (from the source spec)

`Project`, `SourceAsset`, `AudioAnalysisResult`, `SymbolicScore`,
`NoteEvent`, `Phrase`, `HarmonyLabel`, `TempoMap`, `GuitarArrangement`,
`FingeringOption`, `PatchDefinition`, `ChipChannelEvent`, `TheoryAnalysis`,
`TransformationOperation`, `CommandRequest`, `CommandPlan`, `RenderArtifact`,
`DAWSessionSpec`.

For the scoped slice, the load-bearing subset is: `SymbolicScore`,
`NoteEvent`, `Phrase`, `HarmonyLabel`, `TheoryAnalysis`,
`TransformationOperation`, `CommandRequest`/`CommandPlan`. The rest
(`GuitarArrangement`, `ChipChannelEvent`, `DAWSessionSpec`, ...) belong to
subsystems out of scope here.

## The architectural principle worth keeping verbatim

> "I want a branchable composition / transformation graph, not just
> destructive edits." ... "Every operation should ideally create a history
> entry." ... "The system must remain educational, not just generative."

This maps directly onto SYNTHBUILDER's own verification/inspectability
discipline (`../CLAUDE.md`) — before/after transformation visibility is not
a nice-to-have, it's the actual pedagogical mechanism: a learner sees
*exactly* what "add counterpoint to this melody" did, not just a new melody
that supposedly has counterpoint now.

## The source's own recommended first vertical slice (guitar-flavored original)

> "Natural language command → symbolic melody import → beginner guitar tab
> simplification → fretboard candidate scoring → tab/text/JSON export +
> theory explanation."

Not adopted as-is — see `DESIGN.md` for why (guitar tablature is a distinct,
unrelated subsystem with its own hard problems, and isn't what Ted asked
for on 2026-09-22). The theory-education core of this recommendation (NL
command → symbolic input → deterministic transformation → inspectable
output → explanation) is adopted; the guitar-specific parts are not.
