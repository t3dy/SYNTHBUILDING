# DECISIONS.md — ALGORITHMICMUSICTOOLS

## 2026-09-22 — Project created, scoped to the theory-education slice only

**Decision:** Build only the algorithmic-composition + theory-analysis
subsystems from the source conversation's full workbench spec, as a
standalone educational tool, not the full multi-subsystem workbench.
**Why:** Ted's 2026-09-22 description specifically named the theory-
education use case ("play around with automatically composing examples to
learn music theory"); the other subsystems (guitar tab, chiptune/ROM, DAW
automation, audio transcription) are either already covered by other
projects in this workspace or unrelated to what was actually asked for.
Building the full spec would repeat the exact "infrastructure before one
thing works" failure pattern documented across `NSFRIPPER`/`ReapNES-Studio`.

## 2026-09-22 — Deterministic transformations only for v1, no probabilistic model

**Decision:** `invert`, `retrograde`, `transpose`, `diatonic_reharmonize`,
`add_parallel_interval` are all mechanically deterministic. No
probabilistic/generative component in v1, despite the source spec wanting
one eventually.
**Why:** A tool can't correctly *explain* a transformation it can't fully
account for. Deterministic operations have unambiguous, checkable
explanations; a probabilistic model's output would need its own separate
"why did it do that" explanation layer that doesn't exist yet. Add
probabilistic composition only after the deterministic explanation layer is
proven correct on real test cases.

## 2026-09-22 — Guitar tablature dropped from the adopted vertical slice

**Decision:** The source conversation's own recommended first vertical
slice ends in guitar-tab output; this project's adopted slice ends in
theory-explanation output instead, dropping tablature entirely.
**Why:** Guitar fretboard/ergonomics modeling is a distinct hard problem
with no relationship to music-theory education, and nothing in this
workspace has any groundwork for it. Including it would double the v1 scope
for no benefit to the actual stated goal.

## 2026-09-22 — Redesigned around a second, stronger source (CYOA framing adopted)

**Decision:** A deeper megabase sweep (`../research/DEEPCUTS.md`) surfaced a
second, more concrete founding conversation ("Harmony Sonata Adventure,"
2026-02-23) with a fully-worked choose-your-own-adventure design (a "Form
Engine": Piece/Section/Motif/Node/Option/Transform/Validator/LessonTrigger)
and a stated personal motivation from Ted. Adopted its CYOA interaction
model over this project's original "apply a named transformation freely"
framing; kept the underlying deterministic-transformation engine concept
from Source 1, now expressed as a `Node`'s set of `Option`s.
**Why:** Source 2 is more concrete, more finishable (one complete 8-bar
piece per session, not an open sandbox), and directly answers a struggle
Ted described in his own words ("I've always struggled to learn theory and
practice the fundamentals") rather than a generic workbench spec. See
`IDEA_SOURCE.md` for both sources in full.

## Not yet decided

- Whether "correct by hand" verification in `DESIGN.md`'s build order should
  be formalized as an actual test suite (recommended, not yet set up — no
  code exists yet at all).
- Whether this eventually gets any UI, or stays a library + CLI + JSON
  output tool indefinitely.
