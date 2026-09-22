# DESIGN.md — ALGORITHMICMUSICTOOLS scoped vertical slice

## The one sentence

A choose-your-own-adventure harmony/counterpoint teacher: at each step you're
offered a small set of theoretically-valid next moves, you pick one, hear
it, see why it works, and the piece keeps building toward a finished result
— per the stronger of this project's two founding sources
(`IDEA_SOURCE.md` §"Source 2"), which reframes this project's original
"apply a named transformation, read an explanation" design (kept below,
still valid for the underlying engine) as a CYOA interaction: the same
`TransformationOperation` model becomes a `Node`'s set of `Option`s.

**Revised v1 framing**: rather than a general transformation library applied
freely, v1 is one complete, short CYOA "spine" — e.g. harmonizing an 8-bar
soprano melody in four-part harmony, one chord at a time, choosing among 2-3
valid next chords at each step, each choice explained (why is this a valid
progression move, what would break if you picked the "wrong" one). This is
narrower and more finishable than a general transformation toolkit, and
matches the source conversation's own emphasis on "forced closure" — every
session ends in one complete, real 8-bar piece, not an open-ended sandbox.

## What's in scope (v1)

- **Symbolic input**: a melody as a plain note-event list (pitch, start
  beat, duration beat — the same shape NSFRIPPER/EMBLEMSIN3D already use
  for fugue data, no need to invent a new format) or a simple MIDI file
  import.
- **Theory analysis overlay**: given a melody + an assumed key/scale, label
  each note by scale degree; given a chord-symbol sequence, label each
  chord by roman numeral and flag cadences (authentic, plagal, half,
  deceptive) by the standard functional-harmony rules.
- **A small, named set of deterministic transformations** — not a
  probabilistic/generative model for v1:
  - `invert(melody, axis_pitch)` — melodic inversion around a pivot.
  - `retrograde(melody)` — reverse note order, durations preserved per-note.
  - `transpose(melody, interval)`.
  - `diatonic_reharmonize(chords, target_degree_substitution)` — swap one
    functionally-equivalent chord for another (e.g. vi for I, ii for IV)
    and explain *why* they're substitutable (shared tones).
  - `add_parallel_interval(melody, interval)` — the simplest possible
    "add counterpoint" operation, explicitly labeled as the crude starting
    case, not real species counterpoint.
- **Explanation layer**: each transformation returns not just the new note
  data but a short, specific, correct sentence — "inverted around A4: each
  interval above/below the pivot is now the same size in the opposite
  direction" — not a generic "here's your transformed melody!" filler line.
- **Before/after inspection**: both versions visible together (as data at
  minimum for v1; simple notation or piano-roll rendering is a stretch
  goal, not a blocker).

## What's explicitly out of scope (v1, and possibly ever, here)

- Audio transcription, MIR analysis of real recordings — no existing
  groundwork anywhere in this workspace, and not what Ted described wanting.
- Guitar tablature / fretboard ergonomics — a distinct, hard subsystem with
  no relationship to the theory-education goal.
- Chiptune/ROM reverse engineering, DAW session generation — already
  NSFRIPPER's and `arpeggiator-composer`'s territory respectively; don't
  duplicate.
- Probabilistic/ML-based composition — the source conversation explicitly
  wants "deterministic rules combined with probabilistic models" eventually,
  but a v1 that can't yet explain *why* a deterministic transformation is
  theoretically correct has no business adding a probabilistic layer on top.
- A polished UI. Correct data + correct explanation text, inspectable as
  JSON or plain console output, is the actual v1 deliverable.

## Data model (minimal subset of the source spec's list)

```python
NoteEvent: pitch: int (MIDI note number), start_beat: float, dur_beat: float
Phrase: list[NoteEvent], key: str, meter: tuple[int, int]
HarmonyLabel: chord_symbol: str, roman_numeral: str, beat: float
TheoryAnalysis: phrase: Phrase, scale_degrees: list[int], harmony: list[HarmonyLabel], cadences: list[(beat, cadence_type)]
TransformationOperation: name: str, params: dict, input: Phrase, output: Phrase, explanation: str
```

`TransformationOperation` always carries both `input` and `output` — never
mutate a `Phrase` in place. This is the "branchable transformation graph,
not destructive edits" principle from the source conversation, kept at the
smallest scale that still means something (a linear history of operations,
not a full branching graph, for v1).

## Build order (verification-first, per SYNTHBUILDER family discipline)

1. **One hardcoded melody, one transformation (`invert`), correct output,
   correct explanation, verified by hand against known music-theory
   truth.** Nothing else exists yet at this point — not even a CLI.
2. Add `retrograde` and `transpose` — the two other purely mechanical,
   unambiguous transformations. Still one hardcoded test melody.
3. Add scale-degree labeling for a diatonic melody in a known key. Verify
   against a melody you can check by hand (e.g. a major scale run).
4. Add roman-numeral chord labeling + cadence detection for a short,
   unambiguous progression (I-IV-V-I). Verify against a textbook example
   before trusting it on anything ambiguous.
5. Only after 1-4 are individually correct: `diatonic_reharmonize` and
   `add_parallel_interval`, which depend on the harmony-labeling machinery
   from step 4.
6. Only after all transformations work on a hardcoded melody: accept
   arbitrary MIDI/note-list input.
7. UI/notation rendering is a stretch goal after all of the above, not a
   parallel track.

## Open risk, named honestly

Music-theory "correctness" has real edge cases and disagreement (secondary
dominants, modal mixture, jazz reharmonization conventions vary by
tradition) — this is a much softer ground truth than NSFRIPPER's hardware
register facts. **Do not let the theory-analysis subsystem claim more
certainty than it has.** When a case is genuinely ambiguous or
tradition-dependent, the explanation text should say so rather than picking
one convention silently and presenting it as the only correct answer — the
same "honesty before completion" principle the rest of this workspace's
wiki runs on.
