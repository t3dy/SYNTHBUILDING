# SYNTHBUILDING

A knowledge portal for Ted Hand's music-hacking and music-composition work:
synthesizer plugins, NES chiptune extraction, Michael Maier's *Atalanta
Fugiens* set to 8-bit voices, J.S. Bach mashed up with NES timbre, a
35-title music-technology library, and a research map of everything
"symbolic diagram as music controller" ever proposed across the workspace.

**Live site:** https://t3dy.github.io/SYNTHBUILDING/ — cards (50-word
summaries) linking to full pages (~500-word summaries), in the same
JSON-seed → SQLite → static-site pattern as Ted's other digital-humanities
portals (`WitcherPortal`, `ARTHURROBINPORTAL`, `Claudiens`). Every project
and book entry carries a verified path back to where the real thing lives on
disk, a live-URL check (not a claim), and — where relevant — exactly where
the work is stuck and what the next step is.

This repo is also the source for **SYNTHBUILDER**, a practice environment
for building REAPER synth plugins (JSFX now, VST3/JUCE eventually) that
produce keyboard-ready, NES-accurate chiptune tones — built specifically to
get unstuck from where three prior attempts (`NSFRIPPER`, `ReapNES-Studio`,
`NESjamtools`) got stuck trying to do this with AI help.

---

## The project families

### 1. NES / chiptune extraction and synthesis (the deepest cluster)

Reverse-engineering real NES game audio into MIDI, REAPER projects, and a
custom hardware-accurate JSFX synth. The pipeline works; every project in
this family is currently stalled on the same thing — an unmade, 20-minute
"listen and decide" step, not a missing feature.

| Project | Status | Live |
|---|---|---|
| [NSFRIPPER](https://t3dy.github.io/SYNTHBUILDING/project/nsfripper.html) | ACTIVE, stalled since 2026-04-20 | [t3dy.github.io/NSFRIPPER](https://t3dy.github.io/NSFRIPPER/) |
| [ReapNES Studio](https://t3dy.github.io/SYNTHBUILDING/project/reapnes-studio.html) | ARCHIVED (absorbed into NSFRIPPER) | — |
| [NESjamtools](https://t3dy.github.io/SYNTHBUILDING/project/nesjamtools.html) | STABLE, not ear-confirmed | — |
| [GlitchMario](https://t3dy.github.io/SYNTHBUILDING/project/glitchmario.html) | STABLE, complete | [t3dy.github.io/GlitchMario](https://t3dy.github.io/GlitchMario/) |
| [NESMusicStudio](https://t3dy.github.io/SYNTHBUILDING/project/nesmusicstudio.html) | ACTIVE, possibly the current front-runner | [t3dy.github.io/ReapNES](https://t3dy.github.io/ReapNES/) |
| [REAPERBEYONDNES](https://t3dy.github.io/SYNTHBUILDING/project/reaperbeyondnes.html) | ACTIVE, **no git history — loss risk** | — |
| [nes-music-lab](https://t3dy.github.io/SYNTHBUILDING/project/nes-music-lab.html) | stalled, uncommitted | — |
| [arpeggiator-composer](https://t3dy.github.io/SYNTHBUILDING/project/arpeggiator-composer.html) | stalled, uncommitted | — |
| [ChipScribe / ChipTools](https://t3dy.github.io/SYNTHBUILDING/project/chipscribe.html) | ACTIVE, deployed-only | [t3dy.github.io/ChipTools](https://t3dy.github.io/ChipTools/) |

Full pitfall documentation, distilled from these projects' own hard-won
rules (JSFX pin declarations, the JSFX-can't-take-live-keyboard-input wall,
RPP-token guessing, non-linear APU mixing, envelope/length-counter
simulation) so nobody has to rediscover them:
[`STUDYINGNESROMS.md`](STUDYINGNESROMS.md) (ROM/NSF reverse engineering) ·
[`BUILDINGPATCHES.md`](BUILDINGPATCHES.md) (instrument/envelope design) ·
[`BUILDINGSYNTHS.md`](BUILDINGSYNTHS.md) (the JSFX/VST3 plugin itself) ·
[`BUILDINGPROJECTS.md`](BUILDINGPROJECTS.md) (generating `.RPP` files) ·
project map and status: [`NSFRIPPER.md`](NSFRIPPER.md) ·
resume-orchestrator index across the whole family:
[`MUSICHACKING.md`](MUSICHACKING.md).

### 2. Atalanta Fugiens × NES (Michael Maier's 1617 emblem-book fugues)

Maier's *Atalanta Fugiens* is 50 three-voice alchemical canons — "fugues for
the ears." Two independent projects rendered them as chiptune:

- **[FUGUEJUKEBOX](https://t3dy.github.io/SYNTHBUILDING/project/fuguejukebox.html)**
  — 500 MP3s (verified present on disk), offline Python/scipy square-wave
  synthesis. Its companion Next.js site was deployed to Vercel and is now
  **confirmed dead (404)** — checked directly, not assumed.
- **[Emblems in 3D — 8-bit Fugue Engine](https://t3dy.github.io/SYNTHBUILDING/project/emblemsin3d-fugues.html)**
  — the same 50 fugues rendered **live** through a hand-built NES-APU-style
  Web Audio synth, inside a walkable three.js reconstruction of the book.
  **Confirmed live**: [t3dy.github.io/emblems-in-3d](https://t3dy.github.io/emblems-in-3d/)
  (press **M**).
- **[ANTIGRAVFUGIENS](https://t3dy.github.io/SYNTHBUILDING/project/antigravfugiens.html)**
  — ten alchemically-named studio effects plus six interactive audio toys on
  the same fugues. Real, built, unintegrated — the weirdest thing in the
  cluster.

Full writeup, including exactly how to fix FUGUEJUKEBOX's dead deploy:
[`ATALANTA.md`](ATALANTA.md).

### 3. Chipped On Bach

J.S. Bach (Goldberg Variations, Well-Tempered Clavier, Two-Part Inventions,
Cello Suite No. 1) paired with NES instrument timbre presets mined from
Castlevania, Contra, Metroid, and Gradius stage palettes, rendered through
NSFRIPPER's own synth pipeline. Two finished preview videos exist at the
`C:\Dev` root; roughly 117 generated REAPER projects were never rendered to
WAV (a scoped, low-effort follow-on, not a design problem). Full account,
including a note on **Bach Studies** (a separate, unrelated text-only DH
scholarship scaffold with zero audio code — easy to confuse by name, kept
distinct here): [`CHIPPEDONBACH.md`](CHIPPEDONBACH.md).

### 4. Weird / experimental music

**[ANTIGRAVFUGIENS](https://t3dy.github.io/SYNTHBUILDING/project/antigravfugiens.html)**
(above, confirmed directly by Ted) is what "weird experimental Claude music"
actually refers to: ten alchemically-named studio effects plus six
interactive audio toys on the Atalanta fugues — real, built, just
unintegrated. It never showed up in a prompt-archive search because it's a
built agentic-coding artifact, not something planned across chat turns.

Separately, the archive does hold real adjacent material:
- **A "Procedural Music Composer" idea modeled on John Cage's chance
  operations** (2024-09-23) and a real-time astrological-transit-to-music
  generator in the same thread — thin (one paragraph, never coded) but real.
- **A Golden Dawn Rose Cross Lamen synth/looper concept** — the most
  fully-formed *unbuilt* idea in the prompt archive (Feb 2026): a clickable
  Tree-of-Life/Rose-Cross controller gating synth and loop parameters.
- **A much larger adjacent research cluster**, found by a second pass over
  ~230 project folders: [`RESEARCHER/MUSIC_GAME_IDEA_MAP.md`](RESEARCHER/MUSIC_GAME_IDEA_MAP.md)
  maps every "symbolic diagram as music controller" and "puzzle produces
  music" idea Ted has proposed or half-built — including **BRICKSHITSTORM**
  (a shipped game where the falling-brick cascade *is* the music) and an
  early rhythm-Tetris prototype (`TetrisCodex/prototypes/p9-rhythm.html`).
- **[`ALGORITHMICMUSICTOOLS/`](ALGORITHMICMUSICTOOLS/CLAUDE.md)** — a
  distinct idea Ted separately asked about: software that teaches music
  theory by algorithmically composing and transforming examples. Traced to
  a real, fully-spec'd, never-built 2026-03-10 conversation and now scoped
  as its own subproject.
- **[`SYNTHTOY/`](SYNTHTOY/CLAUDE.md)** — occult diagrams (Tree of Life,
  Rose Cross, magic squares) as a 13-family Web Audio prototype lab teaching
  synthesis through play. In active development.

Full account: [`WEIRDMUSIC.md`](WEIRDMUSIC.md) ·
deeper archive sweep: [`RESEARCHER/MEGABASEMUSICCATALOG.md`](RESEARCHER/MEGABASEMUSICCATALOG.md),
[`research/DEEPCUTS.md`](research/DEEPCUTS.md).

### 5. The music-technology library (`E:\pdf`)

35 books, each opened and verified (not filename-guessed): synthesis and
sound-design manuals, Bach scholarship, ludomusicology/game-audio academia,
and a long tail of 33⅓-series album criticism reflecting personal taste
rather than technical use. Three are load-bearing for SYNTHBUILDER's actual
plugin-building work:

- **Will Pirkle, *Designing Software Synthesizer Plug-Ins in C++*** — the
  only book in the library that teaches synth DSP and plugin architecture in
  working code (oscillators, envelopes, a full Moog ladder-filter
  implementation, VST3/AU export). Directly portable to the VST3/JUCE
  problem this whole project family never solved.
- **Karen Collins, *Game Sound*** — the standard academic history of 8-bit
  sound-chip architecture, including the NES 2A03's actual constraints.
- **Geary Yelton, *The Rock Synthesizer Manual*** (1984) — a plain-language
  explanation of the VCO/VCF/VCA/envelope/LFO signal chain a JSFX
  subtractive synth needs to implement.

Browse the full shelf on the site's [Library section](https://t3dy.github.io/SYNTHBUILDING/index.html#library).

### 6. SYNTHTOY — occult diagrams as a synthesis-teaching prototype lab

The concrete answer to "weird" above: not one game but a laboratory of small,
single-screen, single-mechanic Web Audio prototypes turning occult/ceremonial
diagrams (Tree of Life, Rose Cross Lamen, magic squares/sigils, the LBRP,
the hexagram) into playable interfaces that teach real synthesis and music
theory through play — a synthesis-education tool using correspondence
systems as a memory palace, not a game about magic with sound effects
bolted on. Also worth reading together with
[`ALGORITHMICMUSICTOOLS/`](ALGORITHMICMUSICTOOLS/CLAUDE.md) — a related CYOA
teaching idea. Thirteen prototype
families span traversal-as-sequencing, radial-correspondence-as-timbre,
grid-tracing-as-rhythm, and a direct NES/APU-style low-level sound-engine
prototype. Distinct in scope from SYNTHBUILDER proper (browser/Web Audio,
not REAPER/JSFX) but sharing this parent folder and its synthesis-concepts
groundwork. See [`SYNTHTOY/CLAUDE.md`](SYNTHTOY/CLAUDE.md) and
[`SYNTHTOY/DESIGN.md`](SYNTHTOY/DESIGN.md).

### 7. How this portal presents itself — narrative design

[`NARRATIVEDESIGNER/`](NARRATIVEDESIGNER/CLAUDE.md) reads Ted's narrative-
design craft library (`E:\pdf\narrative design` — Paulsen, Heussner et al.,
Austin, Berger, Breault, Hokanson/Clinton/Kaminski, Fox — all 7 read for
substantive content) and applies it to how each project above is actually
presented: a narrative-structure read of the project's real story (not an
invented one — NSFRIPPER's story really is "built a working engine, stalled
on one unmade decision," and that's already a three-act shape worth naming),
a concrete suggestion for the card/page copy, and one gamification idea per
project, honestly labeled as either a cheap copy-only flourish or a real
scoped side-build. Proposal-only, nothing applied to the live catalog yet:
[`NARRATIVEDESIGNER/TOOLKIT.md`](NARRATIVEDESIGNER/TOOLKIT.md) (~20 named
frameworks, each cited to book + chapter) and
[`NARRATIVEDESIGNER/PROJECT_NARRATIVE_SUGGESTIONS.md`](NARRATIVEDESIGNER/PROJECT_NARRATIVE_SUGGESTIONS.md)
(all 15 projects). Favorite ideas so far: an actual "cast your vote: A, B,
or C" audio-picker for NSFRIPPER's three unrendered delivery variants, and a
flip-card "Blunder Bestiary" built from ReapNES-Studio's 14 documented bugs.

---

## How this portal is built

Follows the same pattern as Ted's other DH knowledge portals
(`WitcherPortal`, `ARTHURROBINPORTAL`, `Claudiens`): a JSON seed is the
editable source, loaded into a SQLite database, which a Python script
renders to static HTML. No frameworks, no build tools, no npm — vanilla
HTML/CSS/JS, deployable anywhere static files are served.

```
db/seed_projects.json, db/seed_books.json   the editable source of truth
        |  python db/init_db.py             schema
        |  python scripts/seed_from_json.py   JSON -> SQLite
        v
db/synthbuilding.db
        |  python scripts/build_site.py      SQLite -> static HTML
        v
site/                                        generated, never hand-edited
```

To update an entry: edit the relevant JSON seed file, re-run
`seed_from_json.py` then `build_site.py`, and redeploy `site/`. See
[`DEPLOY_STATE.md`](DEPLOY_STATE.md) for the deploy process and the current
live status.

## Orientation for anyone (human or agent) picking this up

Start with [`MUSICHACKING.md`](MUSICHACKING.md) — it ranks every project in
this catalog by how close it actually is to unstuck, not just what exists.
Then [`CLAUDE.md`](CLAUDE.md) for how this project itself works (its one
governing rule: get one audible note before building anything else — the
lesson every prior attempt in this family paid for the hard way).
[`DECISIONS.md`](DECISIONS.md) records every directional call made along
the way, with the reasoning behind it.
