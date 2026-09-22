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

## Not yet decided — flagged for Ted

- **Whether to actually push to `github.com/t3dy/SYNTHBUILDING`.** The repo
  doesn't exist yet. Per this session's safety convention, pushing/creating
  the remote repo needs an explicit go-ahead even though Ted named the target
  up front — see `DEPLOY_STATE.md`.
- **REAPERBEYONDNES and nes-music-lab have no git history** (see
  `MUSICHACKING.md`). Recommended action (git init + first commit) has not
  been taken — flagging rather than acting unilaterally on projects outside
  SYNTHBUILDER's own scope.
