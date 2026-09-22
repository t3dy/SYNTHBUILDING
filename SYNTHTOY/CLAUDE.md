# SYNTHTOY — Claude Code Instructions

## Project identity

A **prototype laboratory**, not one game: a collection of small, single-
screen, single-mechanic playable experiments turning occult/ceremonial
diagrams (Tree of Life, Rose Cross Lamen, magic squares/sigils, LBRP,
hexagram) into musical-puzzle interfaces that teach synthesis and music
theory to a beginner through play, without a synthesizer manual.

Origin: distilled from a long ChatGPT design conversation, pasted into
Claude Code on 2026-09-21 and preserved verbatim at
`sources/chatgpt_synthtoy_prototype_lab.md` — read that file for full
fidelity; this file and `DESIGN.md` are the working distillation.

**Who this is for, stated directly in the source conversation:** Ted, 46,
has smart musician/producer friends whose synthesis vocabulary he's
struggled to keep up with — "a frustrated musician because this stuff was
hard to learn." The design goal is not a game about magic that happens to
have sound effects; it's a real synthesis-education tool that uses occult
correspondence systems as a memory palace so arbitrary-sounding vocabulary
(attack, cutoff, resonance, LFO) attaches to an already-formed experiential
memory instead of a definition to memorize cold.

## Relationship to SYNTHBUILDER (the parent project)

Different scope, shared assets, **do not let one derail the other.**
SYNTHBUILDER proper is REAPER/JSFX chiptune-synthesis practice work, governed
by a strict "get one audible note before building anything else" discipline
and explicit anti-scope-creep rules (`../CLAUDE.md`). SYNTHTOY is a
browser-based (Web Audio, not REAPER) educational puzzle-game laboratory —
a genuinely different kind of project sharing a parent folder. Reuse
synthesis knowledge and code where it actually transfers (see below); don't
let SYNTHTOY's much larger surface area (13 prototype families, 20+ named
prototypes) pull SYNTHBUILDER's own JSFX work off its narrower discipline,
and don't let SYNTHBUILDER's "small and disciplined" framing talk you out
of the scope Ted actually asked for here — he asked for a laboratory of many
small things, and that's a different shape of "small" than one plugin.

**Borrow SYNTHBUILDER's actual discipline anyway, at the per-prototype
level:** each of the 20+ prototypes should individually pass "does this
prototype's core interaction produce sound, confirmed by actually running
it" before the next prototype starts, and before any cross-prototype
infrastructure (the shared data model, the gallery page framework) gets
built out. The parent project's top rule generalizes: **get one prototype
actually playable and audible before building the gallery around it.**

## The source conversation's own first instruction — already satisfied

The ChatGPT prompt's first substantive instruction was "SEARCH MY EXISTING
WORK" — named targets included Tree Tapper, CrowleyDB, magic square apps,
sigil apps, Tree of Life/Rose Cross interfaces, Golden Dawn projects, Tarot
interfaces, alchemical diagrams, correspondence databases, NSFRIPPER,
ANTIRIPPER, ReapNES_APU2, any prior symbolic-structure-controls-music work.

**This search already happened, thoroughly, as a separate RESEARCHER pass:**
`C:\Dev\SYNTHBUILDER\RESEARCHER\MUSIC_GAME_IDEA_MAP.md` (compiled by
Scarlatti Jones, 2026-09-21) covers exactly this ground across ~230 project
folders, with a correspondence-status key (A=historical/cited,
B=proposed mechanic, C=invented) that directly matches this conversation's
own repeated caution ("these are GAME MAPPINGS... do not represent them as
historical facts unless the source material supports that attribution").
**Read that document before writing any prototype code** — it already
identifies the specific reusable assets:

- `CROWLEYDB/frontend/src/pages/TreeOfLife.tsx` + `thelemic_tree.json` — a
  built, working, clickable Tree of Life (10 sephiroth + 22 paths, SVG,
  five attribution lenses) with a real 32-row correspondence table
  (Hebrew letter, planet/sign, Thoth+GD tarot cards, four color scales,
  god-name, archangel, angel-choir). This is prototype family 1's starting
  geometry and data — don't rebuild it.
- `EMBLEMSIN3D/chiptune.js` — proven, working NES-APU-style Web Audio synth
  (pure browser, no REAPER dependency) — a real starting point for the
  synthesis layer every prototype family needs.
- `TurkaGame/v2/engine/*.js` — a proven, portable "a symbol's operation is
  derived from its own form, discovered by watching it act" engine
  (already ported once, Arabic→Hebrew). Directly relevant to any prototype
  where the player has to discover a mapping rather than be told it.
- `BRICKSHITSTORM/src/groove.js` — a working hidden-constraint rhythm-
  scoring core (pocket/placement/sparseness), reusable for rhythm-based
  prototype families (1D, 3A).
- `SigilForge`'s designed (not yet built) Agrippa kamea sigil algorithm —
  directly matches Prototype Family 3B/3C's sigil mechanics.
- `GoldenDawnBlocks`'s parked lettrist port + `CrowleyDB`'s `is_swapped`
  data — relevant to any prototype exposing competing correspondence
  systems (per the source conversation's own "quotations from Crowley and
  other Golden Dawn magi... serving as the texts of the game" idea).
- **Open gap, not yet filled:** no project in the workspace has actual
  extracted Rose Cross Lamen correspondence data (letter/color/planet
  layout) — flagged in the map's §7. Prototype Family 2 needs a real
  RESEARCHER pass on a primary Golden Dawn source before any Rose Cross
  mapping in this project can be labeled historical rather than invented.

**Tree Tapper**, named explicitly in the ChatGPT prompt, is a generic
mobile clicker/incremental game (`C:\olddevprojects\TreeTapper`) — no
Kabbalah/Tree-of-Life content of its own, despite the name. CrowleyDB's
`TreeOfLife.tsx` cites it only as a UI/state-management ancestor
("managing complex incremental states"). Don't confuse the two.

## What exists in this folder right now

- `sources/chatgpt_synthtoy_prototype_lab.md` — the full source
  conversation, verbatim.
- `DESIGN.md` — the distilled design: 13 prototype families, the core
  sound-design pedagogy (5 nested questions, the "freeze one variable"
  mechanic, the three-timescale visualization), 50 named quests, the
  Golden Dawn grade-based capability-unlock curriculum, and the
  always-on-recording/marker/song-structure system.
- `DECISIONS.md` — directional calls, recorded per this workspace's own
  discipline.

## Next steps (not yet done — don't skip ahead)

1. Pick **one** prototype family to build first (Middle Pillar as Envelope,
   Prototype Family 6, is the smallest and most self-contained — a good
   first candidate, but this is a real decision to make and record, not
   assumed here).
2. Confirm it's actually fun and actually teaches the concept, by playing
   it, before starting a second prototype.
3. Only then build the shared gallery/data-model infrastructure the source
   conversation describes — building that first, before any single
   prototype is confirmed to work, is exactly the "infrastructure before
   verified sound" trap SYNTHBUILDER's own `CLAUDE.md` was written to name
   and avoid.
