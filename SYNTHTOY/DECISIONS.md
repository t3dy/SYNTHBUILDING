# DECISIONS.md — SYNTHTOY, directional calls recorded immediately

## 2026-09-21 — SYNTHTOY scaffolded as a subfolder of SYNTHBUILDER, design-stage only

**Decision:** `SYNTHBUILDER/SYNTHTOY/` holds the prototype-laboratory design
distilled from a long ChatGPT conversation Ted pasted directly. Scaffolded
per this workspace's established occult-app-scaffold pattern (`CLAUDE.md` +
`DESIGN.md`, no code yet), matching SigilForge/SigillumDei/KabbalahTrainer/
GoldenDawnBlocks.
**Why:** the source conversation itself already argues against building
before playing anything ("do not spend a long time designing an
architecture before showing me anything") — but Ted's own instruction this
session was to create the subfolder, not to start building prototype code,
so scaffolding (preserve source, distill design) is the right amount of
work before the next real decision (which prototype to build first).
**Where:** `sources/chatgpt_synthtoy_prototype_lab.md` (verbatim source),
`CLAUDE.md` (project identity + reuse pointers), `DESIGN.md` (distilled
design).

## 2026-09-21 — Reuse RESEARCHER's existing map instead of re-searching

**Decision:** the source conversation's own first instruction ("search my
existing work" — CrowleyDB, Tree Tapper, magic squares, sigils, Golden
Dawn, NSFRIPPER, ANTIRIPPER) is treated as already satisfied by
`SYNTHBUILDER/RESEARCHER/MUSIC_GAME_IDEA_MAP.md`, compiled the same day.
**Why:** re-running that search would duplicate real work already done
across five parallel research passes over ~230 folders; `CLAUDE.md` points
directly at the specific reusable assets that document already identified
(CrowleyDB's `TreeOfLife.tsx`, `EMBLEMSIN3D/chiptune.js`, TurkaGame's
lettrist engine, BRICKSHITSTORM's rhythm-scoring core, SigilForge's kamea
algorithm) rather than re-deriving the list.
**Open gap carried forward:** no Rose Cross Lamen correspondence data
exists anywhere in the workspace (same gap `MUSIC_GAME_IDEA_MAP.md` §7
flags) — Prototype Family 2 needs a real RESEARCHER pass on a primary
Golden Dawn source before any of its correspondences can be called
historical rather than invented.

## 2026-09-21 — Always-on recording + marks + grade-gated song structure

**Decision:** every prototype records the player's session by default (no
manual start/stop), the player can drop marks at any point for later
editing reference, and song-structure/loop-sequencing tools are introduced
at Adeptus Minor (5=6) and above rather than being available from the
start.
**Why:** Ted's direct instruction, given mid-session: "everything the
player is doing should be accessible as recordings so they don't need to
worry about turning a recording off... should be given ways to play with
their song structure and sequence their loops as part of the adept
grades." Grading song-structure to Adeptus Minor fits that grade's
already-designed character (composition and synthesis becoming one
system) rather than being an arbitrary new tier.
**Not yet decided:** whether the always-on recording is an unbounded
buffer or a rolling window anchored by marks — flagged in `DESIGN.md` §5
for whoever builds the first prototype that actually needs persistent
recording.

## Not yet decided — flagged for Ted

- **Which prototype family to build first.** `CLAUDE.md` suggests Middle
  Pillar as Envelope (Family 6) as the smallest, most self-contained
  candidate, but this hasn't been confirmed as the actual starting point.
- **Whether SYNTHTOY should eventually become its own top-level `C:\Dev`
  project rather than a SYNTHBUILDER subfolder**, given it's a genuinely
  different kind of project (browser educational game vs. REAPER/JSFX
  practice) sharing a parent folder only by naming convention. Not acted
  on unilaterally — flagging rather than moving anything.
