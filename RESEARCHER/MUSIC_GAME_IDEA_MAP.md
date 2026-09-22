# MUSIC_GAME_IDEA_MAP.md — a map of Ted's own music/game-design thinking

Compiled by Scarlatti Jones (RESEARCHER), 2026-09-21, from a direct read of
`SYNTHBUILDER`'s own prior research (`ATALANTA.md`, `CHIPPEDONBACH.md`,
`MUSICHACKING.md`, `NSFRIPPER.md`, `BUILDING*.md`, `STUDYINGNESROMS.md`,
`DESIRES.md`, `research/megabase_music_history.md`) plus five parallel research
passes over roughly 230 project folders and the `wiki/` knowledge base. Full
source list at the end.

**Method note on labels used throughout:** every idea below is tagged with
where it came from. Untagged text is a direct finding — something that exists
on disk, or a quote/close paraphrase of something Ted actually said, with a
file pointer. `[INFERENCE]` marks a connection I'm drawing that Ted didn't
state explicitly. `[SYNTHESIS]` marks a new combination of two things that do
each exist separately. `[REDISCOVERED]` flags something strange, forgotten, or
buried in a place nobody would think to look. Nothing here is invented from
nothing — if I had no source for a claim, I left it out rather than filling
the gap.

**Correspondence-status key, used in §6–§8:** **(A)** = a historical Golden
Dawn / Kabbalistic / Renaissance-magic correspondence Ted has actually
recorded somewhere in these projects (with a citation trail behind it).
**(B)** = a game mechanic Ted has proposed or a project has designed. **(C)** =
a rule that is purely invented (by Ted, by a past Claude session, or by me
just now) with no historical claim behind it at all. Golden Dawn/Kabbalistic
correspondences are contested between traditions even in the primary
literature (see CrowleyDB's `is_swapped` flag, TarotAttributions' whole
premise) — "historical" here means "attested in a source Ted's projects cite,"
not "the one true version."

---

# 1. Things I Have Already Built

This is the part of the music/game map that's finished, not proposed. Grouped
by cluster, pointer-first.

**NES/chiptune synthesis pipeline** (the deepest, most mature cluster —
already fully mapped in this project's own `NSFRIPPER.md` and
`MUSICHACKING.md`, not re-derived here):
- **NSFRIPPER** — NSF/ROM → 6502 emulation → APU register capture → MIDI →
  REAPER, 40-rule hardened architecture, 54K extracted presets. Site live.
- **NESjamtools** — multitimbral live JSFX + Python high-fidelity renderer,
  50 games as ready REAPER projects.
- **NESMusicStudio** — NSF/ROM → MIDI → REAPER/WAV/MP4 → YouTube, git-tracked,
  actively worked, live at `t3dy.github.io/ReapNES/`.
- **ChipTools/ChipScribe** — deployed front-end, live.
- **GlitchMario** — narrative documentation of the whole struggle, live.

**Atalanta Fugiens × chiptune** (Michael Maier's 1617 alchemical emblem
book, 50 three-voice "fugues," transcribed to MIDI):
- **FUGUEJUKEBOX** — 500 MP3s (50 emblems × 10 variations), offline
  Python/scipy square-wave synthesis. Verified complete on disk.
- **EMBLEMSIN3D**'s `chiptune.js`/`gamesynths.js` — a hand-built NES-APU-style
  Web Audio synth playing the same 50 fugues **live**, inside a walkable
  three.js reconstruction of the emblem book. **Confirmed live**
  (`t3dy.github.io/emblems-in-3d/`, press M).
- **ANTIGRAVFUGIENS** (inside EMBLEMSIN3D) — ten weird studio-effect variants
  plus six interactive audio toys on the same fugues (see §3).

**Bach × NES**: `NSFRIPPER/scripts/bach_*.py` pairs Bach MIDI (Goldberg
Variations, WTC, Two-Part Inventions, Cello Suite No. 1) with NES timbre
presets extracted from Castlevania/Contra/Metroid/Gradius. Two finished video
artifacts (`Chipped_On_Bach_Preview.mp4`, 39 tracks; a curated 4-track re-cut).

**BRICKSHITSTORM** (`C:\Dev\BRICKSHITSTORM\`) — a puzzle-demolition game
where **the cascade *is* the music**: falling/struck bricks trigger a
simulated collapse, and every impact is scheduled into Web Audio at its exact
timestamp against a bar clock. Nine playable prototypes (five reflex, four
turn-based), thirteen synthesized voices, headless regression harness
(`node tools/sweep.mjs`, 300 random strikes/tower). This is the single most
fully realized "puzzle-solving produces music" system anywhere in the
workspace. Full writeup in §9.

**ALCHEMYBLOCKSHOOTER** (`C:\Dev\ALCHEMYBLOCKSHOOTER\`) — 132-level shooter
with a masonry reaction matrix, 72 Goetia enemies (public-domain seals from
`GoetiaRevEng`) each weak to its own attributed planet/element, and a
**generated-riddle discovery system** (`src/trials.js`): SEAL GATES ask
riddles built entirely from the game's own attribution data, so "no answer
can be wrong" and nothing is invented. Procedural audio (`src/audio.js`,
13 matter voices) exists but is reactive SFX, not rhythm-scored.

**TetrisCodex `p9-rhythm.html`** (`C:\Dev\TetrisCodex\prototypes\`) — a
working, self-contained browser prototype (~290 lines): a 90 BPM metronome, a
pitched note per tetromino type, and a lowpass filter whose cutoff is warped
live by the balance-platform's tilt angle. This is the **earliest
puzzle-produces-music prototype in the workspace**, and BRICKSHITSTORM's own
design doc names it as an ancestor. Full writeup in §9.

**TurkaGame's lettrism engine** (Abjad Tower → Letter Machine → v2:
Scriptorium/Pushing Floor/Standing Word) — the strongest "discover what the
control does" chassis anywhere in `C:\Dev`. Letters are physics objects whose
**operation is derived from their written form** (a closed letter binds, a
tailed letter pours, dots raise/lower, an upright stroke holds an axis) —
never assigned by the designer. Verified alphabet-agnostic by porting the same
engine onto Hebrew letters (`GoldenDawnBlocks`, see below) and finding a
genuinely different rule (12 of 22 Hebrew letters do nothing alone). No
music — but see §6 and §12 for why this is the chassis a Tree-of-Life
controller would want.

**CrowleyDB's `TreeOfLife.tsx`** (`C:\Dev\CROWLEYDB\frontend\src\pages\`) —
a **built, working, clickable Tree of Life**: all 10 sephiroth and 22 paths
as SVG circles/lines, five switchable attribution lenses (tree/tarot/
names/colors/angels), backed by a fully populated 32-row correspondence table
(`thelemic_tree.json`) with planet/sign, four parallel Golden-Dawn color
scales, god-name, archangel, angel-choir, and a flag for the two paths where
Crowley's Thoth attribution diverges from Golden Dawn's. No audio. Full
writeup in §6.

**GoetiaRevEng** (`C:\Dev\GoetiaRevEng\`) — a 22-script computer-vision/graph-
theory pipeline testing whether the 72 Goetia seals are traced on planetary
kamea (magic square) grids. Live dashboard. Ships a genuine rank→planet→kamea
table (King→Sun/6×6, Duke→Venus/7×7, ... President/Knight→Saturn/3×3) and a
calibrated, honest "neither supported nor refuted" verdict on the sigil-
geometry question — the house standard for testing a claimed correspondence
before shipping a mechanic on it.

**AngelPOV / "Spoken Backward"** (`C:\Dev\VisualNovels\angelpov\`, deployed
inside `DeeVisualNovel`) — you play the Enochian angels, Kelley is the only
channel, seven historically-drawn "modes of appearing" including **spell**
("letter-by-letter, backward — reading forward was held to release the
power"). Implemented, verified (4,000-run distribution test), live. Has a
non-semantic three.js scrying chamber (Sigillum Dei Aemeth heptagram
geometry, floating letters) — deliberately not transcribed Enochian, "so
nothing here can be misread as a working table." **No audio at all** despite
being the single most natural fit in the workspace for vocalized-letter sound
design. See §12.

**GoldenDawnBlocks** (`C:\Dev\GoldenDawnBlocks\`) — TurkaGame's lettrism
engine, re-derived from scratch onto the 22 Hebrew letters via the Sefer
Yetsirah's own 3 mothers / 7 doubles / 12 simples division. Vendored engine,
verified data (`build_letters.py --verify`), **no app yet** — deliberately
parked, with planetary/zodiacal attribution withheld ("that is the part the
traditions disagree about"). Full writeup in §6.

**ARTHURCRAWL's Dossier engine / ROBINCRAWL Slice 1** — both live at
`HistoryCrawlers`. No music, but a mature "discover the rules by violating
them" design (anachronism flagged as a rule violation, derivation-copying
detectable 98.9% of the time by the tuning harness). Relevant precedent for
§9/§10.

---

# 2. Things I Have Already Proposed

Ideas Ted stated (in a chat, in a project doc) that are not yet built, or are
only partially designed.

- **"Tree of Life as a musical controller."** Ted's own words, from a
  Feb 8 2026 conversation ("Music-making website design," `chatgpt-md`,
  recovered by prompt archaeology): *"What if we also use the... clickable
  tree of life as a basis for this, where they could click on the spheres and
  the paths, and these two things could sort of both be on the screen at the
  same time, and that becomes your controller for your synthesizer and
  loops."* — `SYNTHBUILDER/research/megabase_music_history.md`. This is the
  idea the current SYNTHBUILDER session was asked to recover and develop.
  Never built. Full writeup in §6.

- **"Golden Dawn Rose Cross Lamen 'music toy.'"** Same conversation
  (Feb 8 2026): a clickable rose/Tree-of-Life web controller where
  Sephirothic/path attributions gate synth and loop parameters, with
  Mellotron-style sample pads. Flagged by prompt archaeology as *"the single
  most fully-formed unbuilt idea in the corpus — multi-message, iteratively
  refined, concrete interaction model"* — and it sat in a thread unrelated to
  any NES/chiptune/REAPER project, easy to lose. Never built. Full writeup
  in §7.

- **Web Audio voice-isolation for Atalanta Fugiens, synced to emblem
  highlighting.** From `wiki/concept_dh_evaluation.md`'s critique of
  Claudiens: *"Integrate the Web Audio API to allow the researcher to isolate
  the three voices of the fugue (Atalanta, Hippomenes, the Apple) while
  simultaneously highlighting the corresponding visual elements in the
  emblem."* This is a literal, explicit "symbolic diagram as instrument"
  proposal for material Ted has already transcribed to MIDI (FUGUEJUKEBOX)
  and already synthesizes live (EMBLEMSIN3D) — the pieces exist, the
  voice-isolation UI does not. Idea only.

- **GoldenDawnBlocks' three-ruleset design** — Sefer Yetsirah (bare
  3/7/12 division), Golden Dawn (full planetary/zodiacal attribution),
  Thelemic (Golden Dawn + Crowley's two swapped paths) — the *same* 22-letter
  substrate behaving differently depending which historical ruleset is
  active. Designed, not built (`GoldenDawnBlocks/README.md`).

- **Glass Bead Game's Rose Cross Lamen / Tree of Life board modes.**
  Specced in `docs/AESTHETIC.md`/`docs/PROGRESSION.md` as alternate
  "skins" for picking glyphs and viewing skill-tree progress — then
  explicitly **demoted**: *"The occult diagrams should not be the center —
  they're optional tools players may bring in"* (`docs/narrative-reviews/
  006-recenter-core-glyph-bank.md`). Also specced: a **Sigil-on-Kamea board
  mode** — spell a word, convert letters to numbers (gematria/AIQ BKR), trace
  a path across a planetary kamea grid, the polyline *is* the sigil. Neither
  built. This tracing-a-path-generates-a-sequence mechanic is structurally
  identical to what a Tree-of-Life note sequencer needs — see §8, §12.

- **SigilForge's Agrippa kamea sigil method** — name → transliterate to
  Hebrew → gematria value per letter → locate each on the correct planetary
  magic square (Saturn 3×3 up to Moon 9×9) → trace the connecting path.
  Deterministic, checkable against published Agrippa-tradition examples.
  Designed (`DESIGN.md`), not built. `[SYNTHESIS opportunity flagged by the
  design doc itself]`: this is a generative pattern (word → pitch sequence
  traced across a grid) whether or not it's ever drawn as a sigil.

- **"Alchemical Pinball Machine"** (`TODO_SOON.md`, 2026-06-28) — a
  Three.js + Cannon.js pinball table shaped like a cross-section of an
  alchemist's tower: ball = prima materia, **7 planetary bumpers, each with
  distinct physics** (Saturn slows the ball, Mercury doubles its speed, Sol
  illuminates targets), 7 process lanes, completing lanes in order advances
  the magnum opus. A schema stub exists (`games/ideas.json`, id
  `alchemical-pinball`), sourced from older "Pinball Mechanics" and
  "Planetary Obstacles" chat threads. This is a real planet→physics mapping
  discovery mechanic — no music component, but structurally the same shape a
  planet→synth-parameter mapping would need. See §12 #6.

- **"MTG × Alchemy Puzzle Editor"** (`TODO_SOON.md` item 12) — explicit
  color→element mapping (White=Salt, Blue=Mercury, Black=Saturn/Lead,
  Red=Sulfur, Green=Prima Materia), puzzle solution = reaching an alchemical
  state via MTG card mechanics. Idea only, explicitly deferred.

- **`roadmap esoteric game projects.txt`** — an older AI-assisted technical
  roadmap for a Renaissance-esoteric roguelike (Jim Adams-style C++ engine
  architecture). Two relevant, unbuilt threads: a `cSound` module for
  "ambient liturgical soundscapes" that survive scene transitions, and "The
  Celestial Court"/"The Grimoire Duel" — planetary/elemental attributes
  mapped directly onto NPC behavior structs and spell generation from
  Renaissance planetary squares. Brainstorm-level, no real spec.

- **`CS_CURRICULUM_TED.md`**'s proposed synthesis curriculum unit (additive/
  subtractive/FM/wavetable), with the exercise *"build a 30-line wavetable
  synth that matches your NES triangle channel"* and a debugging prompt
  *"Compare my JSFX synth to my Python stems for one frame. Where exactly do
  they diverge?"* — idea only, but notably pre-aligned with SYNTHBUILDER's own
  "one audible note first" discipline.

- **`ONESCREEN_PROJECTS.md`**'s "audio toys (low-energy chiptune flavor)":
  a NES note-name↔register converter, a chiptune band-name generator, and a
  stdlib WAV-header inspector. Each capped at "one file, under 200 lines."
  Idea only.

- **Megabase-recorded abandoned/never-built threads** (from
  `research/megabase_music_history.md`): a "Nintendo Cover Song App"
  (auto-populate a DAW with matching NES timbres from a chosen
  game/level, spec'd to 40 features, no project folder exists); a
  ROM-to-editable-synth-preset extractor (asked at least 3 times across 17
  months, never built — distinct from NSFRIPPER's audio extraction); Disney
  "Alice in Wonderland" chiptune covers, one game-palette per song (never
  resurfaced); a home-grown "vibe coded" Suno-style composition aid (scoped
  as automating drudgery, researched not built).

- **`multimedia-research-renderer/CLAUDE.md`** (ecosystem spec) names
  **"music, sound"** as a first-class target render medium alongside
  podcasts/video/slides, from canonical research artifacts. Spec-stage only,
  no music renderer built — but it's the ecosystem-level hook a future
  correspondence-music generator could plug into rather than being an orphan
  project.

---

# 3. Forgotten / Half-Finished Music Ideas

- **The Golden Dawn Rose Cross Lamen music toy** (§2, §7) — the standout.
  Fully-formed, iteratively refined across a real conversation, and it just
  sat in a thread titled "Music-making website design" that had nothing to do
  with any of Ted's NES/chiptune projects, so nobody revisited it. `[REDISCOVERED]`

- **"Tree of Life as a DAG" essay.** `[REDISCOVERED]` Buried inside
  `C:\Dev\GTPaiENG.txt` (a loose transcript, not a project): a completed
  ~9,200-word, 16-section essay ("The Craft: Software, Freemasonry, and the
  Architecture of Initiation") whose thesis line reads: *"The Tree of Life
  from Kabbalistic mysticism is interpreted as a conceptual data structure
  organizing symbolic relationships"* — alongside "Tree of Life as a DAG,"
  "PKD's Exegesis as a git log," "Dreambase as the Vault of the Adepti." This
  is the one place in the whole workspace where "Tree of Life = computational
  structure" is stated as an explicit thesis rather than implied by a UI
  choice — and it's sitting untagged in a raw chat transcript, not in any
  project's docs. The essay file itself wasn't relocated in this pass; flagged
  for a follow-up read if Ted wants the full argument.

- **"Magic Square Sigil App" and "Geomancy Calculator App"** — two "dark
  horse" buildable ideas logged in `GTPaiENG.txt`'s idea-scoring pass,
  distinct from the Esoteric Sigil Creation App that became SigilForge. No
  scaffolded project exists for either anywhere in `C:\Dev` — genuinely
  unbuilt and unclaimed. `[REDISCOVERED]`

- **117 Chipped-On-Bach REAPER projects, generated but never rendered**
  (NSFRIPPER's `state/wishes.json`, WISH16) — the expensive step (pairing
  Bach fugues with NES game-palette timbres, generating the projects) is
  done; only the batch-render pass is missing. Low-effort, already-scoped.

- **ANTIGRAVFUGIENS's six interactive audio toys** (inside EMBLEMSIN3D,
  never linked from the main site nav, never deployed): Levitating Athanor,
  Ouroboric Dub, Sword/Egg Breakbeat, Rose-Garden Lockstep, Sublimation
  Pinball, Dewpoint Runner — plus ten weird studio-effect variants (tape
  delay, mercury vibrato, gated black-fire envelopes, rubedo phasing,
  ouroboric feedback, projection glitch) on the same 50 fugues. Ted's own
  `ATALANTA.md` flags this as "genuinely worth a look... since it's the
  weirdest thing in this whole cluster." `[REDISCOVERED]`

- **NESjamtools' one open ear-test bug** ("W&W Map: rhythm feels wrong") —
  everything else in its bug log is Fixed; this is a 20-minute listening
  session away from done.

- **ReapNES-Studio's VST3/JUCE scriptable-generation gap** — live keyboard
  input works, but nobody executed the documented fix (extract a real VST3
  reference block from one manually-saved project, template from it) to make
  it scriptable. The one genuinely open *technical* problem (not just an
  unmade decision) in the whole NES-synthesis family.

- **Generative/algorithmic/"weird" music is essentially absent from the
  1.45M-prompt megabase corpus.** No SuperCollider, Csound, Max/MSP, Pure
  Data, bytebeat, circuit-bending, modular/Eurorack, drone/noise, or
  Markov/cellular-automata prompts turned up anywhere. If SYNTHBUILDER's
  planned `WEIRDMUSIC.md` is meant to be a *revival* of an old thread, there
  isn't one — it would be genuinely new territory, not a rediscovery. Worth
  knowing before assuming this is "forgotten" rather than "never started."

---

# 4. Existing Code That Could Be Reused

Grouped by what it does, not what project it's in — this is the actual
inventory a builder would want.

**Rhythm/cascade scoring engines:**
- `BRICKSHITSTORM/src/groove.js` — bar clock, asymmetric pocket-timing window,
  sixteenth-note placement weighting, sparseness penalty. The most reusable
  "is this timed well" scoring core in the workspace.
- `BRICKSHITSTORM/src/{kit,bricks,wall,press}.js` — 13-voice synthesized band,
  DOM-free cascade/support physics (headlessly testable), 4-plate CMYK
  renderer whose registration follows the beat.
- `BRICKSHITSTORM/tools/sweep.mjs` — headless verification harness (300
  random strikes/tower, termination + meter-inequality assertions). A
  genuinely reusable pattern for verifying *any* music-puzzle build without a
  human ear every time.
- `ALCHEMYBLOCKSHOOTER/src/cascade.js` — timed-queue death-rite engine
  (generation counter, runaway-chain guards) — the direct architectural
  ancestor of BRICKSHITSTORM's cascade engine.
- `ALCHEMYBLOCKSHOOTER/src/physics.js` — support flood-fill + debris bodies.
- `TetrisCodex/prototypes/p9-rhythm.html` — the whole file (~290 lines):
  `scheduleBeat()`, `getBeatMult()`, and a pitch-per-piece-type mapping.

**Discovery/riddle engines:**
- `ALCHEMYBLOCKSHOOTER/src/trials.js` — generates riddles entirely from the
  game's own attribution data (never invented), confusable-not-random
  distractors, a "Hermetic mode" that hides cribs, a 3,000-riddle regression
  suite. Directly portable to "which sound is this sephirah" ear-training.
- `TurkaGame/v2/engine/{world,agent,reader,vm}.js` + `correspondences.json`
  (tagged PORTAL/CORPUS/REPORTED/INTERPRETATION) + `src/notebook.js` — the
  evidence-before-rule teaching loop and the shared hypothesis-confirmation
  ledger. Proven alphabet-agnostic (ported once already, to Hebrew).
- `GoldenDawnBlocks/vendor/lettrist-engine/` + `data/letters.json` +
  `data/build_letters.py --verify` — the Hebrew-letter port, with typed
  letter-behavior classes (mother→ELEMENT, double→INVERT, simple→COMBINE,
  final→SEAL) already verified against the Sefer Yetsirah's 3/7/12 division.

**Tree of Life / correspondence data, ready to query:**
- `CROWLEYDB/frontend/public/data/thelemic_tree.json` — all 32 paths
  (10 sephiroth + 22 paths): Hebrew letter, astrological attribution, Thoth
  and GD tarot cards, `is_swapped` flag, four parallel color scales, god-name,
  archangel, angel-choir.
- `CROWLEYDB/frontend/src/pages/TreeOfLife.tsx` + `../lib/treeLayouts` —
  working SVG click-handling, hover-to-inspect, node/path coordinate geometry
  for all 10 nodes and 22 paths. Directly portable.
- `CROWLEYDB/scripts/seed_thelemic_tree.py` — the ingestion script, useful if
  the data needs extending.
- `GoetiaRevEng/{gematria_path_scores.json, sigil_metadata.json,
  cluster_assignments.json}` — per-sigil theoretical kamea paths, rank→planet→
  kamea-size table, 8 structural sigil families with feature vectors.
- `TurkaGame/v2/apps/shared/glyphs.js` — 26 elemental/planetary/zodiacal
  glyphs as tested, drawn SVG paths (both hands of e.g. Mercury), ready to
  vendor into any diagram UI.

**Symbolic-diagram-as-board precedent:**
- `glassbeadgame/docs/BOARD_MODES.md` — a formal `BoardMode` interface
  (`id, layout, read(state): Signature[]`) already generalizing "diagram as
  alternate input surface" across freegrid/tarot/geomancy/iching/kamea modes.
  Directly adaptable to "diagram as alternate *controller* surface."
- `glassbeadgame/docs/SYMBOL_SETS.md` — full glyph-bank data model
  (elements, metals, 12 zodiac process-verbs, kamea, geomantic figures,
  I Ching trigrams↔circuits) with Unicode codepoints, including an already-
  specced but unbuilt **musical bead set** (fugue subjects, intervals,
  resonance/counterpoint scoring vocabulary).

**Chiptune synthesis, proven and reusable outside REAPER:**
- `EMBLEMSIN3D/chiptune.js` + `gamesynths.js` — pure Web Audio NES-APU-style
  synth (two pulse + triangle, ten game-derived timbre palettes sourced from
  NSFRIPPER's extraction work), proven live in production.
- `FUGUEJUKEBOX/render_to_audio.py` — pure Python/scipy square-wave synth
  with ADSR/reverb/vibrato/delay, proven at 500-file batch scale.
- `NSFRIPPER`'s `ReapNES_Console.jsfx`, `NESjamtools`'s `NESJam.jsfx`, and
  `nesjam/nes_render.py` — the REAPER-side synthesis engines, plus
  `generate_project.py` for RPP generation (never hand-roll a template — see
  this project's own `BUILDINGPROJECTS.md`).

**Emblem/image assets:**
- `OCCULTIMGDB` — 918 catalogued public-domain images across 31 works and
  10 traditions, including "music of the spheres" / musica-mundana motifs
  already tagged as an index category.
- `GoetiaRevEng/docs/sigil_database.json` + `demon_metadata.json` — all 72
  Goetia seals, structural feature vectors, ready as visual assets (flagged
  in `research-artifacts/INDEX.md` as "still unused as game art").

---

# 5. The "Symbolic Diagram as Instrument" Concept

The workspace already has a general law that governs this, and it's stricter
than "make it feel thematic." From `PIPELINE.md` (quoted in `AGENTS.md`'s
EXTRACTOR contract):

> "if a player cannot recover the symbolism from the behaviour without being
> told, the mechanic is rejected"

with a worked example: Jupiter's tin (astrological "Greater Benefic,"
expansion) becomes a block that swells and shoves neighbours before bursting
on the third hit — the *behavior itself* teaches "this is Jupiter," nothing
is captioned. This is already enforced in shipped code (AlchemyBlockInvaders'
glyphs). **Any Tree-of-Life or Rose Cross music controller should be held to
exactly this bar**: a player should be able to guess "this node is Mars"
from what it *does to the sound*, not from a tooltip.

`wiki/workflow_game_mechanics_extraction.md` states the softer, more literal
version of the same law as an explicit translation table: *"Spiritual
correspondences (element, planet, archangel) → character stats or
color-coded resources."* Between the two documents, the workspace already has
a named, general pattern for "symbolic system becomes mechanic" — it has just
never been pointed at audio.

The single most direct existing proposal for "symbolic diagram as
instrument," specifically, is `wiki/concept_dh_evaluation.md`'s suggestion to
isolate the three voices of an *Atalanta Fugiens* fugue via Web Audio, synced
to which part of the emblem is highlighted (§2). That's a real, named,
unbuilt design for turning a period emblem into a playable/audible object —
closer to Ted's Tree-of-Life idea than anything else on record, just aimed at
a different diagram.

`[SYNTHESIS]` Every piece needed to close the loop already exists
*separately* and nowhere *together*:
- Correspondence data that's actually populated and query-ready (CrowleyDB's
  `thelemic_tree.json`, GoetiaRevEng's rank→planet→kamea table).
- A proven, portable "letter/symbol has typed behavior derived from its own
  form" engine (TurkaGame's lettrist engine, ported once already).
- A proven "diagram is an alternate input surface" abstraction
  (Glass Bead Game's `BoardMode`).
- A proven "geometry of the puzzle IS its rhythm" design (BRICKSHITSTORM).
- Working, reusable chiptune synthesis in pure Web Audio, outside REAPER
  entirely (`chiptune.js`).

No project has ever wired the correspondence data to sound. That gap —
confirmed independently by the correspondence-database research pass — is
the actual opening SYNTHBUILDER's Tree-of-Life work would be filling, not a
green field.

`ZorziHarmoniaMundi` (`C:\Dev\ZorziHarmoniaMundi`, live, 163/163 sections
summarized) is worth knowing about as *why*-material, not code: a full
scholarly digest of Francesco Zorzi's 1525 *De Harmonia Mundi*, arguing for
one harmonic order running through the divine, angelic, celestial, and human
realms — the actual historical Christian-Kabbalist source for "the Tree of
Life's structure just is a musical structure," if a citation-grounded
"why does this path control pitch" tooltip is ever wanted (matching Glass
Bead Game's own "Grounding Rule": no player-facing content without a cited
source).

---

# 6. Tree of Life Music Game

**(B) Ted's proposal** (§2, verbatim quote above): a clickable Tree of Life
where spheres and paths are a synth/loop controller, and the player discovers
the mapping through experimentation.

**What already exists to build it from, and what it's missing:**

- **(built, no audio)** CrowleyDB's `TreeOfLife.tsx` — the diagram itself,
  the geometry, and a full correspondence dataset are done. Its own
  five-lens switcher (tree/tarot/names/colors/angels) already demonstrates
  re-skinning one diagram through multiple correspondence views, which is
  exactly the UI move a "discover the mapping" game needs.
- **(planned, demoted)** Glass Bead Game specced a Tree-of-Life skill-tree
  view and explicitly deprioritized it as "optional decoration" — worth
  noting to Ted directly, because a *musical* Tree of Life is a different
  proposition than a *browsing* Tree of Life, and the reason it got demoted
  (it was competing with the core card game, not adding a new kind of
  interaction) doesn't apply to a standalone instrument.
- **(designed, contrasting)** KabbalahTrainer is the nearest literal match to
  a Feb-2026 mobile sketch Ted described (megabase idea #922: a 3×7 grid Tree
  of Life, tap-to-cycle attributions, save/compare against an answer key) —
  but it's a **fixed-answer-key trainer**, the opposite of "discover the
  mapping through experimentation." Useful as a contrast case: KabbalahTrainer
  teaches a known correspondence; the music-controller concept wants the
  mapping to feel undiscovered even if it's secretly fixed under the hood.
- **(built, transferable, not about Kabbalah)** TurkaGame's lettrism engine —
  the actual mechanism for "a symbol's operation is derived from its own
  form, and the player has to watch it happen to learn the rule" — is proven
  and portable (already re-derived once, onto Hebrew, in GoldenDawnBlocks).
  Nothing currently connects it to the Tree of Life *diagram itself* (as
  opposed to the bare 22-letter alphabet) or to audio, but the machinery —
  evidence-before-rule, rival hidden-ground-truth schemes, a shared Notebook
  for confirmed/disproven hypotheses — would transfer close to directly.
- **(parked)** GoldenDawnBlocks — same engine, Hebrew letters typed as
  mother/double/simple/final with distinct primitive operations
  (ELEMENT/INVERT/COMBINE/SEAL). Three ruleset variants sketched but
  undata'd: Sefer Yetsirah (bare), Golden Dawn (full attribution),
  Thelemic (GD + Crowley's swaps). `[SYNTHESIS]` if each ruleset also
  changed what the diagram *sounds* like, swapping rulesets would be an
  audible demonstration that "the correspondences are contested" — a design
  idea with no direct precedent but built from two things that do exist
  (the ruleset architecture, and CrowleyDB's `is_swapped` data).

**Correspondence data actually available (A), ready to consume:**
`thelemic_tree.json`'s 32 rows: path number, Hebrew letter, astrological
attribution (planet or sign), Thoth/GD tarot cards, `is_swapped`, four color
scales, god-name, archangel, angel-choir. This is real, cited data (CrowleyDB
is a scholarly DH project, not an invented game) — but see the correspondence-
status key at the top: it represents *the Golden Dawn/Thelemic tradition's*
attributions, not a single universally agreed table, and the `is_swapped`
flag is the data model's own admission of that.

**Ted's proposed parameter space** (pitch, pitch class, octave, scale/mode,
rhythm, duration, velocity, instrument, oscillator, waveform, filter cutoff,
resonance, ADSR, delay, reverb, panning, modulation, tempo, subdivision,
probability, sequencing) — **(C), purely Ted's own invention**, no historical
claim attached, and nothing in the searched material assigns specific
sephiroth/paths to specific synth parameters. This is exactly the kind of
mapping the discovery-mechanic loop is supposed to hide from the player, not
something to source from a grimoire.

**Ted's proposed challenge/achievement list** (Middle Pillar, Tenfold, One
Touch, Return to Kether, Lightning Flash, Serpent, Balanced Pillars, etc.) —
**(C) mostly invented rules**, with two partial exceptions worth flagging:
"Middle Pillar" and "Lightning Flash"/"Serpent" name **(A)** real structural
features of the traditional diagram (the Middle Pillar is a standard
three-sephirah column; the Lightning Flash and the Serpent of Wisdom are
historically real teaching devices describing two directions of traversal
through the ten spheres) — but the specific *scoring rules* attached to them
("touch only," "fewest interactions," etc.) are Ted's own game design, not
historical. Nothing found in the workspace records a historical rule that
resembles "touch every sephirah exactly once" as a magical practice.

---

# 7. Rose Cross Lamen Music Game

**(B) Ted's proposal** (§2, same Feb 8 2026 conversation as the Tree of Life
idea): a clickable Rose Cross Lamen controller — symbols, colors, letters,
planetary/zodiacal/elemental correspondences, paths, and geometric
organization as musical parameters, with Mellotron-style sample pads.

**Honest gap, stated plainly:** no project searched in this pass contains an
actual extracted Rose Cross Lamen correspondence table — i.e., which letter
sits on which petal, which color goes where, the specific planetary/zodiacal
layout around the cross. CrowleyDB's rich data is the **Tree of Life**
(32 paths), not the Rose Cross Lamen specifically — a related but distinct
Golden Dawn diagram. GoldenDawnBlocks deliberately withholds planetary/
zodiacal attribution ("that is the part the traditions disagree about").
Nothing in `IslamicateOccultPortal`, `ChristianCabalaDB`, or the other
correspondence databases carries Rose Cross Lamen data either. **This means
the Rose Cross Lamen game genuinely needs a RESEARCHER pass over a primary
source before any correspondence claim can be labeled (A)** — the workspace's
own convention (see `AGENTS.md`) would be to route this through
`GrimoireMechanics` once built, or a direct RESEARCHER pass over a Golden
Dawn primary text (e.g. Israel Regardie's published *The Golden Dawn*, or
equivalent material under `renaissance magic/` per `PIPELINE.md`), citing
page numbers, before treating any letter/color/planet placement as historical
rather than invented. I have not done that pass here — flagging it as the
next concrete research step rather than fabricating placeholder attributions.

**What already exists to build the *mechanism* from, even without the data:**
- Glass Bead Game's demoted Rose Cross Lamen spec (§2) — the only place in
  the workspace where the Rose Cross Lamen was actually turned into UI design
  (as a glyph-bank picker, not an instrument), and its `BoardMode` interface
  is directly reusable for "diagram is a controller."
- GoldenDawnBlocks' typed-letter-behavior engine (mother/double/simple/final
  → ELEMENT/INVERT/COMBINE/SEAL) — the Rose Cross Lamen carries the same
  22 Hebrew letters around its petals in Golden Dawn iconography, so the
  same engine, once given real Rose Cross attribution data, would drive it.
- The general symbol→parameter interpretation Ted proposed (symbol→
  parameter, color→timbre, planet→synthesis parameter, zodiac→pitch/rhythm,
  element→modulation behavior, letter→pitch class, geometric position→
  spatialization, cross/rose structure→routing) — **(C), Ted's own
  hypothesis**, explicitly framed by Ted as a hypothesis to test, not a claim
  of authenticity, which matches this workspace's own house standard
  (GoetiaRevEng's calibrated, honest-verdict methodology) for how a claimed
  correspondence should be treated before it's built on.

---

# 8. Other Symbolic Music Machines

Treating each as "what happens if the symbolic structure becomes the
sequencer," per the brief, with correspondence status marked.

**Kamea / magic squares (A data exists, B/C mechanic unbuilt).** SigilForge's
Agrippa method (name → gematria → path traced across a planetary kamea grid)
and GoetiaRevEng's rank→planet→kamea-size table are both real (A) — a
concrete grid-coordinate system with historical grounding. `[SYNTHESIS]`
grid coordinates → pitch/rhythm (x = pitch step, y = duration or octave) is
the natural next move nobody has made; Glass Bead Game's own unbuilt
Sigil-on-Kamea spec already frames the trace as "the polyline *is* the
sigil" — swapping "is the sigil" for "is the melody" is a small, well-
grounded step.

**Goetia 72 spirits (A data exists, used for combat not sound).**
GoetiaRevEng's rank→planet→kamea table and `AlchemyBlockInvaders/invaders/
goetia-text.json`'s per-spirit rank/legions/offices/planet/element data are
both real, cited, and already load-bearing for one shipped game (enemy
bearing, retinue size, weakness — see `research-artifacts/INDEX.md`'s
"goetia-72" entry). `[SYNTHESIS]` the same table, unused for sound: 72
distinct planet/element/rank combinations is enough data to drive a full
72-voice/72-preset instrument, and the "derived from the text, not invented"
discipline that built the combat mechanic would transfer directly to a sound
mechanic (e.g., rank → envelope shape, per BUILDINGPATCHES.md's own
per-driver-family ADSR table, which is an unrelated but structurally similar
existing pattern in this very project).

**Atalanta Fugiens (A: real period fugues, B: proposed instrument).** The
`concept_dh_evaluation.md` voice-isolation proposal (§2, §5) is the most
direct existing "symbolic diagram as instrument" design on record — real
emblem, real transcribed music, unbuilt UI. `[SYNTHESIS]` see §12 #5 for
marrying this to BRICKSHITSTORM's rhythm-scoring engine instead of (or
alongside) a straight voice-isolation player.

**TurkaGame's abjad-value-as-mass (B: built for physics, not sound).**
`[SYNTHESIS]` The same abjad numeral value currently driving a letter's
*physics mass* could as easily drive its *pitch or duration* — the engine
doesn't care what domain it's wired to, only that the operation is legible
from the letter's own form. This is the single most portable "existing
engine, new output domain" swap found in this whole survey.

**BRICKSHITSTORM's cascade-is-rhythm (not a symbolic diagram, but the same
design law).** Not esoteric at all, but worth stating as a precedent: "the
geometry of a puzzle sets its rhythm" (`fall time = sqrt(2h/g)`) is the exact
same move as "the geometry of a symbolic diagram sets its music" — just
proven out in physics rather than correspondence tables. The lesson
BRICKSHITSTORM's own design doc states — "stop treating the times as
animation and start treating them as rhythm" (of ALCHEMYBLOCKSHOOTER's
cascade queue) — is directly reusable advice for turning any of the above
correspondence engines audible: they already produce *timed* events, they
just aren't scheduled as music yet.

---

# 9. Puzzle/Challenge Mechanics

What's already built, that a Tree-of-Life or Rose Cross game could borrow
wholesale:

- **BRICKSHITSTORM** — fully hidden scoring on three axes (pocket:
  asymmetric ±window around the beat, peak *after* the beat, not on it;
  placement: sixteenth-note slot weighting; sparseness: density penalty
  defeating the "detonate everything at once" degenerate strategy). Nothing
  is explained on screen — only felt out through a HUD quality signal
  (RUSHING/DEAD ON/LAID BACK, GREASY/MUSH).
- **ALCHEMYBLOCKSHOOTER** — SEAL GATES generate riddles from the game's own
  data (never invented, confusable-not-random distractors, 87% sharing a
  register with the answer), THE OFFERING telegraphs a hazard and lets the
  player pre-charge the counter, HERMETIC MODE hides all cribs for higher
  score, and correctness is validated by a 3,000-riddle regression sweep
  (0 secretly-valid distractors).
- **TurkaGame** — evidence always shown, rule only learned by watching it
  happen; a hidden ground-truth correspondence scheme the player must
  disprove-or-confirm via a shared Notebook (HYPOTHESIS → EXPERIMENT →
  OBSERVED → CONFIRMED/DISPROVEN); "dead" letters that do nothing, explicitly
  named as what makes the rule feel discovered rather than listed.
- **ARTHURCRAWL's Dossier engine** — rules taught by violation (an
  anachronism the game names out loud), and a derivation-detection mechanic
  (a naive player who counts every "agreeing" witness independently is
  discredited 98.9% of the time in the tuning harness) — a genuinely
  different flavor of "figure out the hidden structure" than TurkaGame's.
- **PLOTINUSGAME** — rival scholarly hypotheses over the same evidence, the
  player commits to one and is scored against their *own* gathered evidence,
  never a hidden designer's answer key ("the game must not know which
  hypothesis is right" — CLAUDE.md rule #10).
- **Glass Bead Game** — adjacent beads reveal a grounded historical relation
  when juxtaposed (reveal-through-adjacency), gated by a hard "no
  player-facing content without a citation" rule.
- **TetrisCodex `p9-rhythm.html`** — the simplest version of "timing
  accuracy is graded, spatial fit competes with it" (visible HUD, not
  hidden — a useful contrast to BRICKSHITSTORM's fully-hidden version).

Ted's proposed Tree-of-Life challenge list (§6) fits this pattern well as a
**(C) design language**, not as historical practice — "Touch only the
spheres on the Middle Pillar," "Create a loop with no repeated note," "Reach
a particular musical state without touching a particular sphere" are the same
shape of thing as BRICKSHITSTORM's hidden constraint scoring (pocket/
placement/sparseness) and could reuse its verification pattern directly (see
§10).

---

# 10. Achievement System

Treating achievements as compositional constraints, per the brief, rather
than completion badges — this workspace already has the infrastructure to
verify constraint-style achievements headlessly, which is worth reusing
rather than re-inventing:

- **BRICKSHITSTORM's `tools/sweep.mjs`** — asserts termination and two
  meter-inequality properties across 300 random runs. The same pattern
  (simulate many random play sessions, assert a scoring property holds)
  is directly adaptable to verifying "is 'Tenfold' actually achievable, and
  is it actually hard" before shipping it as a named challenge.
- **ALCHEMYBLOCKSHOOTER's 3,000-riddle regression suite** — verifies a
  generated-content system (riddles) stays fair at scale; the same harness
  shape would verify a generated-content achievement system (e.g., "Discover
  a combination that produces an unusual sonic effect" needs some
  machine-checkable definition of "unusual," which a sweep-style script could
  calibrate the way GoetiaRevEng calibrated "structured vs. scribble").
- **ARTHURCRAWL/PLOTINUSGAME's hypothesis-scoring pattern** — scoring a
  player's claim against their own gathered evidence, not a hidden answer
  key, is directly relevant to "Discover what a path does" as an achievement:
  credit for a *correct, evidenced* guess about a hidden mapping, not for
  matching a designer's secret table by luck.

`[SYNTHESIS]` A concrete recommendation, following this workspace's own
verification discipline (`AGENTS.md`'s VERIFIER role: "drive the artifact,
don't just read the diff"): any achievement list adapted from Ted's proposed
set (Middle Pillar, Tenfold, One Touch, Return to Kether, Lightning Flash,
Serpent, Balanced Pillars, and the rest) should get a `sweep.mjs`-style
headless harness before being called "done" — the same instinct that caught
BRICKSHITSTORM's "detonate everything at once" degenerate strategy would
likely catch degenerate solutions to these too (e.g. "Fewest interactions"
achievements are exactly the kind of goal a script should try to minimize
adversarially before a human is asked to solve them by hand).

---

# 11. Cross-Project Connections

The lineages worth knowing about, because they show which pieces were
already built to fit together even when nobody has assembled them yet:

- **Rhythm-scoring lineage:** TetrisCodex's `p9-rhythm.html` (simple, visible
  beat-multiplier) → ALCHEMYBLOCKSHOOTER's `cascade.js` (timed-queue death
  rites, reactive SFX only) → BRICKSHITSTORM's `groove.js`/`kit.js` (the same
  timed-queue architecture, reinterpreted as hidden rhythm scoring instead of
  animation). BRICKSHITSTORM's own design doc names both ancestors directly.
- **Letter-engine lineage:** TurkaGame v2's lettrist engine (Arabic abjad,
  physics output) → GoldenDawnBlocks (same engine, Hebrew letters, verified
  alphabet-agnostic, physics/mechanics output still, no diagram UI) → could
  extend to the Tree of Life or Rose Cross Lamen (same 22 Hebrew letters, but
  now placed on a specific historical diagram rather than a bare alphabet) →
  could extend again to audio output instead of physics. Three of these four
  links exist; the diagram-placement and audio-output links do not.
- **Correspondence-data lineage:** CrowleyDB's `thelemic_tree.json`
  (32-path Tree of Life, real data) → cited/reused-by-reference in Glass Bead
  Game's planned Tree-of-Life view, KabbalahTrainer's planned deck data, and
  GoldenDawnBlocks' caution note about CrowleyDB's own pre/post-swap column
  inconsistency → GoetiaRevEng's independent 72-spirit rank→planet→kamea
  table (same domain, different diagram, same "real cited data, unused for
  sound" status).
- **Atalanta Fugiens lineage:** Claudiens (scholarship, the source PDFs and
  `atalanta.db`) → FUGUEJUKEBOX (transcribes the same fugues, renders 500
  chiptune variations offline) → EMBLEMSIN3D (renders the same fugues live,
  in-world, via `chiptune.js`) → `concept_dh_evaluation.md`'s unbuilt
  voice-isolation proposal (wants to expose the *same* fugues' three voices
  interactively, synced to the emblem) → NSFRIPPER (the synthesis-fidelity
  rules both chiptune implementations draw from). Every link in this chain
  except the last one is built; the interactive/discovery layer is the one
  piece missing.
- **Discovery-mechanic family, non-musical but same design law:** TurkaGame
  ↔ GoldenDawnBlocks ↔ ALCHEMYBLOCKSHOOTER ↔ BRICKSHITSTORM ↔ ARTHURCRAWL ↔
  PLOTINUSGAME all independently arrived at some version of "show evidence,
  hide the rule, let the player earn the rule by acting" — this is close to
  a house style at this point, not a coincidence across five unrelated
  projects. `[INFERENCE]` A Tree-of-Life/Rose-Cross music game built in
  SYNTHBUILDER would be the sixth instance of this pattern, and the first
  one aimed at sound instead of physics, combat, or historiography.
- **The workspace's own constitutional law tying all of this together:**
  `PIPELINE.md`'s legibility gate (§5) — cited from `AGENTS.md`, enforced in
  shipped code (AlchemyBlockInvaders), and independently reinvented in
  TurkaGame's "evidence, not exposition" design principle before either
  project's authors necessarily knew the other's exact wording.
- **A live integration point that doesn't exist yet:** `multimedia-
  research-renderer/CLAUDE.md` already names "music, sound" as a target
  medium rendered from canonical research artifacts (spec stage only). A
  correspondence-driven Tree-of-Life instrument, if it ever gets built,
  would be a natural first real answer to that spec rather than a one-off.

---

# 12. The Most Promising Prototypes Already Latent in My Codebase

Not ranked — eight concrete assemblies of existing code/ideas, in no
particular order, each buildable without inventing new correspondence data
from scratch (beyond what §7 already flags as a real, separate research gap
for the Rose Cross Lamen specifically).

### 1. "The Living Tree" — Tree of Life as a controller

- **Existing ingredients:** CrowleyDB's `TreeOfLife.tsx` (SVG geometry, click
  handling) + `thelemic_tree.json` (32-row correspondence data) +
  `EMBLEMSIN3D/chiptune.js` (proven Web Audio NES-style synth, no REAPER
  dependency).
- **Missing ingredient:** any audio layer at all — the diagram exists, the
  data exists, nothing plays a sound yet.
- **Core interaction loop:** click a sephirah or path; it changes one
  parameter of an ongoing loop; the player keeps clicking and listening.
- **What the player discovers:** which node maps to which musical
  parameter, purely by ear (per the §5 legibility gate).
- **What music it produces:** an evolving loop/sequence, chiptune-voiced.
- **Minimum viable prototype:** port `TreeOfLife.tsx`'s SVG + `thelemic_tree`
  data, wire the 10 sephiroth to 10 `chiptune.js` oscillator parameters
  (start with a fixed, undisclosed mapping — pitch class by sephirah, say).
- **Likely reusable files:** `CROWLEYDB/frontend/src/pages/TreeOfLife.tsx`,
  `.../lib/treeLayouts`, `.../public/data/thelemic_tree.json`,
  `EMBLEMSIN3D/chiptune.js`.

### 2. "Rose Cross Player" — the idea Ted actually asked to recover

- **Existing ingredients:** Glass Bead Game's demoted Rose Cross Lamen
  board-mode spec + `BoardMode` interface, `chiptune.js`.
- **Missing ingredient:** real Rose Cross Lamen correspondence data (§7's
  flagged research gap — needs a RESEARCHER pass on a primary source before
  any mapping can be called historical), plus the audio wiring itself.
- **Core interaction loop:** click petals/symbols on the lamen; discover
  which color/letter/planet gates which parameter.
- **What the player discovers:** the same "which control does what" loop as
  #1, on a denser, more symbol-rich diagram.
- **What music it produces:** loop/texture, likely closer to Mellotron-style
  pads per Ted's own Feb-2026 description.
- **Minimum viable prototype:** start with a static SVG of the lamen and
  placeholder attributions **explicitly marked as game-invented (C)** until
  a real source pass is done; wire the 22 letters to pitch classes, colors
  to timbre, via `chiptune.js`.
- **Likely reusable files:** `glassbeadgame/docs/BOARD_MODES.md`,
  `glassbeadgame/docs/SYMBOL_SETS.md`, `EMBLEMSIN3D/chiptune.js`.

### 3. "Kamea Sequencer" `[SYNTHESIS]`

- **Existing ingredients:** SigilForge's Agrippa kamea-tracing algorithm
  (designed, not coded) + GoetiaRevEng's kamea grid infrastructure and
  gematria-path data + Glass Bead Game's planned Sigil-on-Kamea board mode.
- **Missing ingredient:** the grid→sound mapping (x/y → pitch/duration) —
  currently the trace only ever becomes a drawn line.
- **Core interaction loop:** type a name or intent; watch the sigil trace
  across the planetary square; hear it simultaneously as a melody.
- **What the player discovers:** that the sigil *is* the melody — same
  data, two representations.
- **What music it produces:** a short melodic phrase per traced word/name,
  deterministic and checkable (SigilForge's own stated virtue).
- **Minimum viable prototype:** implement SigilForge's designed
  transliteration→gematria→kamea-path algorithm, map grid coordinates to a
  scale.
- **Likely reusable files:** `SigilForge/DESIGN.md` (algorithm spec),
  `GoetiaRevEng` kamea infrastructure/`gematria_path_scores.json`.

### 4. "Abjad Tones" `[SYNTHESIS]`

- **Existing ingredients:** TurkaGame v2's full lettrist engine
  (`engine/{world,agent,reader,vm}.js`, `correspondences.json`,
  `notebook.js`) — currently outputs physics.
- **Missing ingredient:** an audio backend; currently the VM only drives
  cannon-es physics, never Web Audio.
- **Core interaction loop:** place/write letters; hear the operation as
  sound instead of (or alongside) watching it move a block; the Notebook
  tracks which rules have been confirmed.
- **What the player discovers:** letter-form → sound-operation mappings
  (ELEMENT→timbre select, INVERT→filter/formant flip, COMBINE→chord stack,
  SEAL→sustain/hold), by ear.
- **What music it produces:** a sequence built from discrete letter
  "operations," closer to a step sequencer than a continuous loop.
- **Minimum viable prototype:** swap the VM's physics output stage for a Web
  Audio scheduling stage; reuse the existing evidence-before-rule task
  scripting unchanged.
- **Likely reusable files:** `TurkaGame/v2/engine/*.js`,
  `TurkaGame/v2/apps/shared/glyphs.js`, `src/notebook.js`.

### 5. "Cascade Fugue" `[SYNTHESIS]` — flagged directly by the puzzle-cluster
research pass as "a plausible next cross-pollination... that nothing
currently in the workspace has attempted"

- **Existing ingredients:** BRICKSHITSTORM's `src/{kit,groove,bricks,
  wall}.js` (rhythm-scoring cascade engine) + FUGUEJUKEBOX's transcribed
  Atalanta Fugiens MIDI data / EMBLEMSIN3D's `chiptune.js` voices (real
  period fugue material, already synthesized).
- **Missing ingredient:** mapping cascade impacts to the three fugue voices
  (Atalanta/Hippomenes/the Apple) instead of a 13-voice funk kit.
- **Core interaction loop:** identical to BRICKSHITSTORM's, but the three
  brick registers now correspond to the fugue's three voices.
- **What the player discovers:** which register of the collapsing wall
  triggers which voice of a real period canon.
- **What music it produces:** a fragment of an actual Maier/Merian fugue,
  re-triggered and re-timed by physics rather than played back verbatim.
- **Minimum viable prototype:** re-skin `kit.js`'s 13 voices down to 3,
  source their pitches from one fugue's transcribed MIDI instead of a
  drum/bass/horn kit.
- **Likely reusable files:** `BRICKSHITSTORM/src/{kit,groove,bricks,
  wall}.js`, `FUGUEJUKEBOX/generate_variations.py`'s source data parsing,
  `EmblemRoguelike/assets/fugues.json`.

### 6. "Planetary Pinball Synth" `[SYNTHESIS]`

- **Existing ingredients:** the unbuilt Alchemical Pinball Machine idea
  (`games/ideas.json`, id `alchemical-pinball`) + CrowleyDB/GoetiaRevEng
  planet attribution data.
- **Missing ingredient:** everything is idea-only right now, even the
  physics; this is the least-built of the eight.
- **Core interaction loop:** ball bounces off seven planetary bumpers; each
  bumper's physics behavior *and* its pitch/timbre are both keyed to the
  same planet attribution, so the physical and musical legibility reinforce
  each other (a direct, clean fit for the §5 legibility gate: Saturn slows
  the ball *and* sounds low/slow).
- **What the player discovers:** which bumper is which planet, from touch
  and sound together, faster than from either alone.
- **What music it produces:** an emergent rhythm/texture from ball-bumper
  collisions — closer to a generative percussion instrument than a
  composed melody.
- **Minimum viable prototype:** start from `ALCHEMYBLOCKSHOOTER/src/
  physics.js` for collision handling rather than building pinball physics
  from scratch; attach one oscillator per bumper.
- **Likely reusable files:** `games/ideas.json`, `ALCHEMYBLOCKSHOOTER/src/
  physics.js`, CrowleyDB/GoetiaRevEng planet tables.

### 7. "Tome of Tones" `[SYNTHESIS]`

- **Existing ingredients:** ALCHEMYBLOCKSHOOTER's `src/trials.js`
  generated-riddle engine (confusable distractors, difficulty ramp,
  Hermetic mode, 3,000-riddle regression pattern).
- **Missing ingredient:** an audio-based riddle domain — `trials.js`
  currently only asks about masonry/matter/hazard relationships, never
  about sound.
- **Core interaction loop:** hear a tone/timbre; identify its symbolic
  attribution (or the reverse: given an attribution, pick the matching
  sound) — an ear-training game built on the same generation discipline
  as ALCHEMYBLOCKSHOOTER's SEAL GATES.
- **What the player discovers:** the sound↔symbol mapping, through
  generated multiple-choice play rather than free exploration — a different
  *kind* of discovery than the click-and-listen loops above, useful as a
  contrast or a late-game "test what you've learned" mode.
- **What music it produces:** no ongoing composition — short, discrete
  tones/timbres as quiz content, not a performance instrument.
- **Minimum viable prototype:** port `trials.js`'s riddle-generation logic
  to a new answer-domain of "sounds," reuse the regression-testing pattern
  to keep it fair.
- **Likely reusable files:** `ALCHEMYBLOCKSHOOTER/src/trials.js`.

### 8. "Sefer Yetsirah Band" `[SYNTHESIS]`

- **Existing ingredients:** GoldenDawnBlocks' three unbuilt ruleset
  architecture (Sefer Yetsirah/Golden Dawn/Thelemic) over the same 22-letter
  diagram, plus CrowleyDB's `is_swapped` data for the two paths where GD and
  Thelemic attribution disagree.
- **Missing ingredient:** any ruleset beyond the bare Sefer Yetsirah
  division, and any audio at all.
- **Core interaction loop:** swap which historical ruleset is active; the
  *same* 22-letter diagram sounds different depending which tradition's
  correspondences are driving it.
- **What the player discovers:** not just what a letter does, but that
  different Golden Dawn-lineage traditions genuinely disagree about what it
  does — turning a historiographical fact (§7's correspondence-dispute
  problem) into the actual content of the game, rather than papering over
  it with one invented "correct" table.
- **What music it produces:** the same short phrase or drone, audibly
  different (e.g., two notes literally swap) depending on active ruleset —
  a direct, audible demonstration of `is_swapped`.
- **Minimum viable prototype:** hardcode one real Golden Dawn planetary/
  zodiacal attribution table for the 22 letters (needs sourcing — same gap
  as §7), wire mother/double/simple typed classes to ELEMENT=drone,
  INVERT=interval-flip, COMBINE=chord-stack, SEAL=sustain.
- **Likely reusable files:** `GoldenDawnBlocks/vendor/lettrist-engine/`,
  `data/letters.json`, `CROWLEYDB/.../thelemic_tree.json`'s `is_swapped`
  column.

---

# MUSICAL IDEA INVENTORY

Every distinct mechanic found, one line each, source-pointed. `(A)`/`(B)`/
`(C)` marks correspondence status where relevant; `[TAG]` marks inference/
synthesis/rediscovery per the key at the top.

| Idea | One-line description | Source |
|---|---|---|
| Tree of Life as synth/loop controller | Click spheres/paths, discover which musical param each gates | `research/megabase_music_history.md` (Feb 8 2026 quote) |
| Golden Dawn Rose Cross Lamen music toy | Clickable RCL, correspondences gate synth/loop params, Mellotron pads | `research/megabase_music_history.md` |
| Atalanta Fugiens voice-isolation player | Web Audio isolates the fugue's 3 voices, synced to emblem highlighting | `wiki/concept_dh_evaluation.md` |
| Cascade-is-rhythm puzzle game | Falling/struck bricks scheduled into Web Audio as a scored drum break | BRICKSHITSTORM (built) |
| Beat-synced piece placement | Place a tetromino on-beat for a score multiplier + pitched note + filter | `TetrisCodex/prototypes/p9-rhythm.html` (built) |
| Masonry reaction-matrix SFX | Procedural per-material event audio, reactive not rhythm-scored | ALCHEMYBLOCKSHOOTER (built) |
| Generated-riddle discovery (SEAL GATES) | Riddles built from the game's own data, never invented | ALCHEMYBLOCKSHOOTER `src/trials.js` |
| Letter-form-derived physics ops | A letter's operation (bind/pour/raise/hold) comes from its written shape | TurkaGame lettrist engine (built) |
| Rival hidden-correspondence schemes | A seed secretly picks which of several real schemes is "true"; player must find where they disagree | TurkaGame "Temperament/mizāj" mode |
| Shared hypothesis notebook | HYPOTHESIS→EXPERIMENT→OBSERVED→CONFIRMED/DISPROVEN, reused across games | TurkaGame/PLOTINUSGAME `notebook.js` pattern |
| Alphabet-agnostic lettrist engine, ported | Same engine re-derives a genuinely different rule on Hebrew letters | GoldenDawnBlocks (built) |
| Typed letter-behavior classes | mother→ELEMENT, double→INVERT, simple→COMBINE, final→SEAL | GoldenDawnBlocks `letters.json` |
| Three competing correspondence rulesets, one diagram | Sefer Yetsirah / Golden Dawn / Thelemic, same 22 letters, different behavior | GoldenDawnBlocks (designed) |
| Clickable, multi-lens Tree of Life | 10 sephiroth + 22 paths, 5 switchable attribution lenses, no audio | CrowleyDB `TreeOfLife.tsx` (built) |
| 32-path Tree of Life correspondence table | Letter/planet/tarot/4 color scales/god-name/archangel per path | CrowleyDB `thelemic_tree.json` (A, built) |
| Rose Cross Lamen as glyph-bank picker | RCL/Tree diagrams as alternate skins for selecting glyphs, not an instrument | Glass Bead Game (designed, demoted) |
| `BoardMode` diagram-as-input-surface abstraction | Formal interface generalizing tarot/geomancy/iching/kamea/freegrid as alt input | Glass Bead Game `docs/BOARD_MODES.md` |
| Sigil-on-Kamea tracing | Spell a word → gematria → trace path across a planetary kamea → polyline = sigil | Glass Bead Game (designed, unbuilt) |
| Agrippa kamea sigil method | Name → Hebrew letters → gematria → path across the correct planetary square | SigilForge (designed, unbuilt) |
| 72-spirit rank→planet→kamea table | King→Sun/6×6 ... President/Knight→Saturn/3×3, gematria per spirit | GoetiaRevEng (A, built) |
| Calibrated correspondence-testing method | Null-model statistical test of "is this sigil really grid-traced," honest inconclusive verdict | GoetiaRevEng (built) |
| Fixed-answer Tree of Life trainer | Tap-to-cycle attributions, test mode scores recall against an answer key | KabbalahTrainer (designed, contrasts with discovery goal) |
| Slopegraph of correspondence disagreement | Visualizes where French/GD/Thelemic/Etteilla tarot-path systems diverge | TarotAttributions (built) |
| Anachronism-as-rule-violation teaching | A Grail in the wrong worldview is a named rule violation, not an accident | ARTHURCRAWL Dossier engine (built) |
| Derivation-spotting (copied-witness detection) | Player must notice when "agreeing" sources are really just copies | ARTHURCRAWL Dossier engine (built) |
| Rival-hypothesis historiography dossier | Player commits to one of 6 rival scholarly readings, scored against own evidence | PLOTINUSGAME (built) |
| Enochian "spell backward" mode | Letter-by-letter reversed speech, historically framed as releasing power; no audio | AngelPOV (built, audio gap) |
| Non-semantic ritual-geometry 3D chamber | Sigillum Dei heptagram + floating letters, deliberately not real Enochian | AngelPOV `engine/chamber.js` (built) |
| Alchemical Pinball Machine | 7 planetary bumpers, each with distinct physics (Saturn slows, Mercury speeds) | `TODO_SOON.md` / `games/ideas.json` (idea only) |
| MTG-color-to-element puzzle editor | White=Salt/Blue=Mercury/Black=Saturn/Red=Sulfur/Green=Prima Materia | `TODO_SOON.md` item 12 (idea only) |
| Ambient liturgical soundscape module | Persistent ambient audio surviving scene transitions, managed by a process manager | `roadmap esoteric game projects.txt` (brainstorm only) |
| Planetary-attribute NPC behavior mapping | Mars=aggression, Luna=mutability, Mercury=cryptic dialogue+good trade | `roadmap esoteric game projects.txt` (brainstorm only) |
| Wavetable-synth-matches-NES-triangle exercise | Curriculum exercise comparing a hand-built synth against real APU output | `CS_CURRICULUM_TED.md` (idea only) |
| NES note-name↔register converter toy | One-file MIDI note number → NES register value utility | `ONESCREEN_PROJECTS.md` (idea only) |
| "Tree of Life as a DAG" thesis | Explicit essay framing the Tree as a computational data structure | `GTPaiENG.txt` [REDISCOVERED] |
| Magic Square Sigil App | Unclaimed dark-horse idea, distinct from SigilForge | `GTPaiENG.txt` [REDISCOVERED] |
| Geomancy Calculator App | Unclaimed dark-horse idea | `GTPaiENG.txt` [REDISCOVERED] |
| ANTIGRAVFUGIENS interactive audio toys | 6 named toys (Levitating Athanor, Ouroboric Dub, etc.) on the Atalanta fugues | EMBLEMSIN3D subproject (built, unlinked) [REDISCOVERED] |
| "Music, sound" as a research-artifact render target | Ecosystem spec naming music as a first-class output medium alongside podcasts/video | `multimedia-research-renderer/CLAUDE.md` (spec only) |
| musica universalis scholarly grounding | 163-section digest of Zorzi's *De Harmonia Mundi*, cosmic-to-human harmonic order | ZorziHarmoniaMundi (built, scholarship only) |
| "Music of the spheres" image motif catalog | Public-domain period imagery of cosmic-harmony diagrams, cataloged | OCCULTIMGDB (built, asset source) |
| Cascade-fugue cross-pollination | Marry BRICKSHITSTORM's rhythm engine to real Atalanta Fugiens voices | [SYNTHESIS], see §12 #5 |
| Abjad-value-as-pitch | Swap TurkaGame's abjad-value-as-physics-mass for abjad-value-as-pitch/duration | [SYNTHESIS], see §12 #4 |
| Kamea-trace-as-melody | Swap Glass Bead Game's kamea-trace-as-sigil for kamea-trace-as-melody | [SYNTHESIS], see §12 #3 |
| Planet-bumper-as-instrument-voice | Give each Alchemical Pinball bumper a synth voice matching its physics | [SYNTHESIS], see §12 #6 |
| Sound-domain SEAL GATES | Port ALCHEMYBLOCKSHOOTER's riddle generator to ear-training content | [SYNTHESIS], see §12 #7 |
| Audible ruleset-swap demonstration | Swapping GD/Thelemic/SY rulesets changes what the same diagram sounds like | [SYNTHESIS], see §12 #8 |

---

## Full source list

**Read directly (primary):** `SYNTHBUILDER/{ATALANTA,CHIPPEDONBACH,
MUSICHACKING,NSFRIPPER,DESIRES,PROMPTS,BUILDINGSYNTHS,BUILDINGPATCHES,
BUILDINGPROJECTS,STUDYINGNESROMS}.md`, `SYNTHBUILDER/research/
megabase_music_history.md`, `C:\Dev\AGENTS.md`, `C:\Dev\research-artifacts\
INDEX.md`.

**Five parallel research passes, 2026-09-21** (full agent transcripts not
retained, findings integrated above): (1) symbolic-diagram-as-controller
cluster — Tree of Life, Kabbalah, Rose Cross Lamen, Tarot, Glass Bead Game,
memory systems; (2) alchemy/emblem puzzle-block games — BRICKSHITSTORM,
ALCHEMYBLOCKSHOOTER, TetrisCodex family, Claudiens; (3) DH portals and
narrative games — TurkaGame, IslamicateOccultPortal, Arthur/Robin cluster,
PLOTINUSGAME, VisualNovels/AngelPOV, GoetiaRevEng; (4) correspondence
databases and scattered root notes — CROWLEYDB and siblings, MTG tooling,
GoldenDawnBlocks, `TODO_SOON.md` and other root planning files; (5) workspace
meta-framework docs — `wiki/framework_*`, `wiki/workflow_*`,
`wiki/concept_*`, `registry.tsv`, `log.md`, `PIPELINE.md`, `AGENTS.md`,
`research-artifacts/INDEX.md`, `ecosystem/`.

**Not yet pulled into this pass** (tracked so nothing gets silently
dropped): the `E:\pdf` music-book library (already flagged as a separate,
still-pending SYNTHBUILDER deliverable in `DESIRES.md`); a direct read of the
full "Tree of Life as a DAG" essay inside `GTPaiENG.txt` (location noted,
content not extracted); a primary-source RESEARCHER pass on the actual
historical Golden Dawn Rose Cross Lamen correspondences (flagged in §7 as the
concrete next step before building §12 #2 or #8 on real rather than
placeholder data).
