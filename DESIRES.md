# DESIRES.md — distillation of what Ted actually wants (living doc)

Source: `PROMPTS.md` (verbatim log). This file is my synthesis, kept current as
the session evolves — re-derive it from PROMPTS.md rather than letting it drift
from what was actually asked.

## Top-level goal

A new project, `C:\Dev\SYNTHBUILDER\`, that is both:
1. **A practice environment** for building REAPER synth plugins (JSFX, and
   later VST3) that produce keyboard-ready, NES-accurate chiptune tones —
   specifically to get unstuck from where `NSFRIPPER` and `ReapNES-Studio`
   got stuck trying to do this with AI help.
2. **A public documentation site**, `SYNTHBUILDING`, deployed to
   `https://t3dy.github.io/SYNTHBUILDING/` from `github.com/t3dy/SYNTHBUILDING`,
   cataloging *all* of Ted's music-hacking and music-composition work, in the
   cards (50-word) + pages (500-word) style of his existing DH knowledge
   portals (`WitcherPortal`, `ARTHURROBINPORTAL`, `Claudiens` pattern: JSON
   seed → SQLite → static-site generator, no frameworks).

## Concrete deliverables requested, in the order asked for

1. **Research tide-room** (`github.com/EricRuud/tide-room`, a friend's repo) —
   extract anything transferable to the synth-plugin/REAPER-project struggle.
   → `research/tideroom_lessons.md` (done — it's a JUCE/Metal spatial synth,
   not NES-related in subject matter, but its DSP-validation discipline
   transfers).
2. **Study Ted's own prior music projects** in `C:\Dev`, specifically:
   - NSFRIPPER (NES ROM/NSF → MIDI/REAPER extraction + synth)
   - Atalanta Fugiens set to NES sounds (FUGUEJUKEBOX, EMBLEMSIN3D's 8-bit
     fugues)
   - Bach set to NES sounds ("Chipped On Bach")
   - "Weird experimental music" made with Claude
3. **Search `C:\Dev\megabase`** (his 1.45M-prompt personal LLM archive) and
   his archived LLM conversations for any other music-related discussion,
   especially forgotten/never-built ideas and the "weird experimental music"
   thread specifically.
4. **Search `E:\pdf`** for his music books and catalog them the same
   card+page way, as a library section of the site.
5. **Deploy the site** to `github.com/t3dy/SYNTHBUILDING` (GitHub Pages, per
   workspace hosting policy) — explicit confirmation needed before the actual
   push/repo-creation, per standing safety convention, even though the target
   was named up front.
6. **`MUSICHACKING.md`** — a catalog of every music-hacking project, written
   so the *orchestrator* (Claude, working from `SYNTHBUILDER/`) can find and
   resume any of them later. This is a resume-map, not just a list.
7. **Initialize `SYNTHBUILDER/` as "a sophisticated agentic coding
   environment"** — meaning: role/contract structure, hard-won-lessons files
   loaded up front, verification discipline, checkpointing — following this
   workspace's existing `AGENTS.md`/`ORCHESTRATION.md` conventions, adapted
   from the game-design pipeline to synth/plugin building.
8. **A themed set of system files / project-goal docs / style guides**,
   explicitly named:
   - `WEIRDMUSIC.md`, `ATALANTA.md`, `CHIPPEDONBACH.md`, `NSFRIPPER.md` — one
     per theme Ted has "touched on," each also carrying ideas for **borrowing
     tide-room's technologies/methods** into that theme.
   - `STUDYINGNESROMS.md`, `BUILDINGPATCHES.md`, `BUILDINGSYNTHS.md`,
     `BUILDINGPROJECTS.md` — split by pipeline layer (ROM/NSF analysis →
     patch/instrument design → plugin/synth code → RPP project generation),
     each one specifically distilling the **pitfalls Ted already documented**
     in `NSFRIPPER` and `ReapNES-Studio` trying to use AI to build synth
     plugins. "etc" — more topic docs are plausible if a gap surfaces; don't
     treat this list as necessarily final.
9. **`PROMPTS.md`** (verbatim running log of everything Ted asks in this
   session) and **`DESIRES.md`** (this file) — kept current, not just
   written once.

## Standing preferences inferred (not stated as rules, but consistent across asks)

- **Prefers many small, precisely-named topic files over one giant document.**
  Every request so far has been "give me a document named X for topic Y," not
  "write me a report." Keep splitting this way rather than consolidating.
- **Wants pitfalls preserved as load-bearing content, not summarized away.**
  The repeated ask to study exactly where NSFRIPPER/ReapNES-Studio got stuck
  means the value is in the specific failure modes (JSFX pin declarations,
  the JSFX-can't-take-keyboard-input wall, RPP token guessing, etc.), not a
  generic "REAPER is hard" gloss.
- **Wants provenance to real, resumable artifacts** — every project doc
  should point at the actual folder/file/live URL, not just describe it in
  the abstract, because the express purpose is letting him or an orchestrator
  pick work back up.
- Matches this workspace's existing convention (root `CLAUDE.md`) that
  verification claims must be checked against a real running artifact before
  being called "done" — no indication Ted wants that relaxed here.

## Done this session (2026-09-21)

- [x] Megabase query — honest null result on "weird music," Rose Cross Lamen
      idea surfaced (`research/megabase_music_history.md`, `WEIRDMUSIC.md`)
- [x] E:\pdf music-book library catalog — 35 books, verified by opening each
      (`research/music_library_catalog.json` → `db/seed_books.json`)
- [x] Full local music-projects catalog — 15 verified projects
      (`MUSICHACKING.md`, `db/seed_projects.json`)
- [x] `NSFRIPPER.md`, `ATALANTA.md`, `CHIPPEDONBACH.md`, `WEIRDMUSIC.md`
- [x] `STUDYINGNESROMS.md`, `BUILDINGPATCHES.md`, `BUILDINGSYNTHS.md`,
      `BUILDINGPROJECTS.md`
- [x] `MUSICHACKING.md`
- [x] `PROMPTS.md`, `DESIRES.md`
- [x] Site build (JSON seed → SQLite → static HTML, cards+pages) —
      built and **verified rendering correctly** via local server + browser
      (index, project pages, library pages all checked)
- [x] `DECISIONS.md`

## Done, second wave (2026-09-22)

- [x] Deployed — live at https://t3dy.github.io/SYNTHBUILDING/, repo at
      github.com/t3dy/SYNTHBUILDING, comprehensive README documenting every
      project family, confirmed with explicit go-ahead.
- [x] "Weird music" clarified directly by Ted: it's ANTIGRAVFUGIENS, not a
      megabase-archaeology find. `WEIRDMUSIC.md` corrected accordingly.
- [x] `ALGORITHMICMUSICTOOLS/` — new subproject, scoped from a real
      previously-unbuilt idea found in megabase (the 2026-03-10 "AI-assisted
      Music Engineering Workbench" conversation).
- [x] `NARRATIVEDESIGNER/` — new subproject/role, reading `E:\pdf\narrative
      design`'s 7 books to produce a toolkit + per-project presentation and
      gamification suggestions for the site (research agent running).

## Not yet done

- [ ] `DEEPCUTS.md` — full(er) sweep of uncovered LLM conversations for
      remote/obscure music ideas (research agent running).
- [ ] NARRATIVEDESIGNER's suggestions are proposals only — applying any of
      them to `db/seed_projects.json` and rebuilding/redeploying the site is
      a separate, deliberate step not yet taken.
- [ ] The first actual JSFX practice file (`jsfx/`) — nothing built yet on
      SYNTHBUILDER-proper's "get one audible note" front; all work so far
      has been research, documentation, and the catalog site/subprojects,
      which is honest and worth saying plainly rather than implying practice
      has started. (Separately, `SYNTHTOY` — a concurrent session's project —
      has its own build underway; not the same thing.)
- [ ] `REAPERBEYONDNES` / `nes-music-lab` git-history loss risk — still
      unaddressed, Ted hasn't said whether he wants it fixed.
