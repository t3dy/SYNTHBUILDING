# DECISIONS.md — directional calls, recorded immediately

## 2026-09-21 — SYNTHBUILDER created, scoped as verification-first practice ground

**Decision:** SYNTHBUILDER is deliberately smaller in ambition than NSFRIPPER/
ReapNES-Studio. Its top rule is "get one audible note before building
anything else" — a direct response to the pattern found across every prior
project in this family (infrastructure built before the plugin was confirmed
to make sound).
**Why:** `ReapNES-Studio/docs/AVOIDBLUNDERS.md` Blunder 10 and
`docs/SUCCESSANDFAIL.md`'s own verdict both name this as the dominant failure
mode across ~4 prior attempts. Confirmed independently by the megabase sweep
(`research/megabase_music_history.md`): the REAPER+MIDI-keyboard setup
problem was asked from scratch three separate times across 15 months with no
carried-over notes.
**Who decided:** Ted, via the session's framing ("practice building reaper
plugins" as a distinct, smaller goal from finishing NSFRIPPER itself).

## 2026-09-21 — SYNTHBUILDING site follows the DH-portal pattern, not a custom design

**Decision:** JSON seed -> SQLite -> Python static-site generator -> vanilla
HTML/CSS/JS -> GitHub Pages, matching `WitcherPortal`/`ARTHURROBINPORTAL`/
`Claudiens`. No frameworks, no build tools, no npm.
**Why:** Ted explicitly asked for "the cards and pages style from my
knowledge portals" — this is that pattern, verbatim, not a reinterpretation.
**Where implemented:** `db/init_db.py`, `db/seed_projects.json`,
`scripts/seed_from_json.py`, `scripts/build_site.py`.

## 2026-09-21 — Site design: dark "console" theme, not the parchment/codex aesthetic

**Decision:** SYNTHBUILDING uses a dark, monospace-accented "oscilloscope
console" theme (amber/green on near-black) rather than the parchment/codex
aesthetic used by the occult-app scaffolds (SigilForge, SigillumDei, etc.).
**Why:** The subject matter is synth consoles and chiptune hardware, not
grimoires — `ReapNES-Studio`'s own UI direction ("vintage analog synth
console — knobs, sliders, oscilloscope") is the more honest visual reference
point for this specific project family.
**Reversible:** Yes, trivially — it's one CSS block in `scripts/build_site.py`.

## 2026-09-21 — BachStudies excluded from the music-hacking catalog proper

**Decision:** `BachStudies` (`C:\Dev\BachStudies`) is documented in
`CHIPPEDONBACH.md` and included in the site's Bach section for
cross-reference, but explicitly labeled as non-music (pure DH scholarship,
zero audio/MIDI/synthesis code) rather than counted as a real music-hacking
project.
**Why:** Verified directly — the project has no audio component anywhere in
its codebase; only its name overlaps with "Chipped On Bach." Conflating the
two would misrepresent both.

## 2026-09-21 — "Weird experimental Claude music" — honest null result, not papered over

**Decision:** `WEIRDMUSIC.md` and the site's "weird/experimental" section
lead with the fact that no generative/algorithmic/weird AI-music experiments
were found anywhere in a full megabase sweep (1.45M prompts). The section is
framed as "weird ideas, some built, most not" (ANTIGRAVFUGIENS + the unbuilt
Golden Dawn Rose Cross Lamen synth concept) rather than implying a shipped
catalog that doesn't exist.
**Why:** Per this workspace's "honesty before completion" wiki principle —
the original task assumed this thread exists; the archaeology says it
doesn't. Better to say so than to inflate ANTIGRAVFUGIENS's scope to fill the
gap.

## 2026-09-21 — RESEARCHER subfolder created, scoped to research only

**Decision:** `SYNTHBUILDER/RESEARCHER/` holds Scarlatti Jones, a
RESEARCHER-role agent (per `C:\Dev\AGENTS.md`'s contract: reads sources,
writes notes, touches no code) scoped to Ted's existing music/game-design
ideas specifically. His first output, `MUSIC_GAME_IDEA_MAP.md`, is a full
map of everything found across ~230 project folders touching algorithmic
music, symbolic-diagram-as-controller ideas, and puzzle-produces-music
mechanics — structured to remind Ted of what he's already proposed/built
rather than invent new projects. Registered in
`C:\Dev\research-artifacts\INDEX.md` under `music-symbolic-diagram-
controllers` so no other RESEARCHER re-mines the same ground.
**Why:** Ted explicitly asked to be reminded of existing ideas, not given new
ones, and the workspace already has a defined RESEARCHER contract (file-based
handover, no game design in the artifact) that this should follow rather than
inventing a bespoke format.
**Open debt this surfaced:** the Golden Dawn Rose Cross Lamen has no
extracted historical correspondence data anywhere in `C:\Dev` — flagged in
both the map (§7) and `research-artifacts/INDEX.md`'s "Not yet touched"
table as a real gap, not filled with placeholder data.

## 2026-09-22 — Deployed to github.com/t3dy/SYNTHBUILDING

**Decision:** Pushed `main` (full source) and a `gh-pages` branch (built
`site/`, via `git subtree split`) to `github.com/t3dy/SYNTHBUILDING`,
enabled GitHub Pages from `gh-pages`/root, verified the live URL loads
correctly including subpath-relative links on a real project page.
**Why:** Ted's explicit go-ahead ("deploy and make sure we have detailed
documentation..."). Superseded the earlier "not yet decided" entry below.
**Verified, not assumed:** loaded `https://t3dy.github.io/SYNTHBUILDING/`
and `.../project/nsfripper.html` directly in the browser pane after the
Pages build finished; see `DEPLOY_STATE.md` for the full record.

## 2026-09-22 — ANTIGRAVFUGIENS confirmed as "weird music," WEIRDMUSIC.md corrected

**Decision:** Updated `WEIRDMUSIC.md` to state ANTIGRAVFUGIENS is what Ted
meant, not merely "the closest candidate" as originally hedged.
**Why:** Ted said so directly. Also explains why the megabase sweep found
nothing under that name — ANTIGRAVFUGIENS is a built agentic-coding
artifact, not something planned across chat turns, so a prompt-archive
search was never going to surface it. Worth remembering: not every real
project has a paper trail in the prompt archive.

## 2026-09-22 — ALGORITHMICMUSICTOOLS created, scoped to the theory-education slice only

**Decision:** New subproject at `ALGORITHMICMUSICTOOLS/`, built from a real
previously-unbuilt idea (a 2026-03-10 ChatGPT conversation spec'ing an
"AI-assisted Music Engineering Workbench"), but scoped down to only the
algorithmic-composition + theory-analysis subsystems — not the full
workbench (audio transcription, guitar tab, chiptune/DAW automation, which
either belong to other existing projects or weren't what Ted asked for).
**Why:** Building the full original spec would repeat the "infrastructure
before one thing works" failure pattern this whole workspace has already
paid for multiple times (see `NSFRIPPER.md`). See
`ALGORITHMICMUSICTOOLS/DECISIONS.md` for the project's own decision log.

## 2026-09-22 — NARRATIVEDESIGNER created as a proposal-only role

**Decision:** New subproject/role at `NARRATIVEDESIGNER/`, reading
`E:\pdf\narrative design`'s 7 books to build a narrative-design toolkit and
apply it to how SYNTHBUILDING's 15 projects are presented, plus a
gamification idea per project. Explicitly scoped as **proposals only** — it
does not edit `db/seed_projects.json` or the live site itself.
**Why:** Ted asked for suggestions, not a unilateral rewrite of already-
verified, carefully-fact-checked catalog copy. Keeps the narrative-design
pass separate from the verification discipline the rest of this project
depends on — a suggestion can be creative; a shipped fact about a real
project can't drift from what was actually verified.

## Not yet decided — flagged for Ted

- **REAPERBEYONDNES and nes-music-lab have no git history** (see
  `MUSICHACKING.md`). Recommended action (git init + first commit) has not
  been taken — flagging rather than acting unilaterally on projects outside
  SYNTHBUILDER's own scope.
- **Whether to apply any of NARRATIVEDESIGNER's suggestions** once it
  reports back — a deliberate follow-up, not automatic.
