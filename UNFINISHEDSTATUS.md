# UNFINISHEDSTATUS.md — what's left undone, project by project

Purpose: a single place that says, for every music project under the
SYNTHBUILDER umbrella, *specifically* what's unfinished — not what the
project is (that's `MUSICHACKING.md`) or how it's broken in code-level detail
(that's `ATALANTA.md` for the Atalanta cluster) — but the honest gap between
"what exists" and "what was meant to exist." Synthesized from
`MUSICHACKING.md`, `ATALANTA.md`, `DESIRES.md`'s "Not yet done" section, and
each subproject's own docs, current as of 2026-09-22. Re-derive rather than
let drift, same discipline as `DESIRES.md`.

Ranked within each cluster by how close it is to done, per `MUSICHACKING.md`'s
own framing — the smallest next step first.

## The NES/chiptune-extraction family

### NSFRIPPER — one decision away from unstuck
Everything about the pipeline (40-rule hardened architecture: bankswitching,
non-linear APU mixing, noise length-counter simulation, bandlimited
synthesis) is built. **What's unfinished:** a single A/B/C ear-test decision
was never made — three synthesis variants exist, nobody has sat down and
listened to all three and picked one. This is a 20-minute task, not an
engineering one, and it's the single highest-leverage unfinished item in the
entire family because everything downstream of NSFRIPPER (NESjamtools,
NESMusicStudio, SYNTHBUILDER's own JSFX rules) inherits its choices.

### ReapNES-Studio — archived with one live thread still hanging
Absorbed into NSFRIPPER, but **the VST3/JUCE build in `vst/` was never wired
to scriptable project generation.** It solves live-keyboard-input (JSFX
can't receive it; VST3 can) but the RPP reference format needed to generate
a project file around it is an opaque REAPER-only binary blob, and nobody
extracted the pattern from a manually-saved project to template from. This
is the one genuinely open *technical* problem in the whole cluster, not
just an unmade decision — and it's the problem SYNTHBUILDER itself exists to
eventually re-attempt, carefully, one verified step at a time.

### NESjamtools — one bug from stable
Bug log says everything is Fixed except one: "W&W Map: rhythm feels wrong."
Same shape as NSFRIPPER's stuck point — waiting on someone to listen, not on
more code. No git remote yet either (local only).

### NESMusicStudio — mid-catalog, actively worked
Castlevania 1 is complete end-to-end (NSF→MIDI→REAPER→WAV→MP4→YouTube).
**Contra is in progress** — unfinished by definition, currently the
project's live front. Nothing else flagged as blocked; this one just isn't
done yet because the per-game pipeline hasn't been run on the rest of the
intended catalog.

### REAPERBEYONDNES — active but unprotected
Declared successor covering GBA/SMS/Saturn/Genesis/SNES/GBC/Virtual Boy.
**Not git-tracked at all** — this is a loss-risk unfinished item, not a
creative one: a disk failure or accidental delete loses everything with no
recovery path. `git init` + first commit is a five-minute fix nobody has
done. Per `DESIRES.md`, Ted hasn't said whether he wants this actually
fixed — flagged, not yet actioned.

### nes-music-lab — stalled and unprotected
Research-grade Castlevania trace/reconstruction work, uncommitted, same
loss-risk as REAPERBEYONDNES. Unclear if it's paused because it's genuinely
stuck or just deprioritized — no blocker documented, just no recent activity.

### arpeggiator-composer — stalled, uncommitted, undocumented reason
A deterministic MIDI arpeggiator for REAPER. Stalled with no recorded reason
why — this is the one project in the catalog where "what's unfinished" isn't
even clearly diagnosed, because nobody has gone back to ask.

### ChipScribe / ChipTools — the one exception
Live and deployed (`t3dy.github.io/ChipTools/`). No local tree exists
(GitHub-only), which makes it hard to say anything is *actively* unfinished
here versus simply "not being worked on right now."

## The Atalanta Fugiens cluster (Michael Maier x chiptune)

### FUGUEJUKEBOX — music finished, delivery entirely unfinished
The actual creative work — 500 MP3s + 500 WAVs, 50 emblems x 10 variation
types — is **complete and verified present on disk.** What's unfinished is
100% delivery infrastructure:
- The claimed-live site (`fuguejukebox.vercel.app`) is dead (404), and two
  divergent codebases (`FUGUEJUKEBOX-website/`, `FugueJukebox-repo/`) both
  have the same two bugs: a filesystem-relative audio path that can't
  resolve over real HTTP, and a git history that excludes all 500 MP3s from
  the push (so even a working deploy would be silent).
- A ~140MB duplicate of the MP3s sits in `FUGUEJUKEBOX/music/emblems/` next
  to the canonical copy, unresolved.
- Nobody has decided how to actually ship ~1.8GB of audio through git
  (bitrate reduction vs. Git LFS vs. shipping a subset) — this is a real
  open decision, not just a bug to fix.
- **This is the exact gap `WEBSITEFIXER/` (sibling folder to this file) now
  exists to close.**

### EMBLEMSIN3D's 8-bit fugues — the live half is done; the extra pages aren't
The in-world player is **confirmed live and working**
(`t3dy.github.io/emblems-in-3d/`, press M) — this half is not unfinished.
What's unfinished: the standalone `jukebox.html`, `fugue.html?n=NN`, and
`grandtour.html` pages were **deliberately** never ported to the Pages
build, because they load sibling-project assets by absolute `C:\Dev`-rooted
path. "Deliberately deferred" is still unfinished — it's a scoped, known gap
with a stated reason, which is better than most items on this list, but
nobody has done the path-rewrite work to close it.

### ANTIGRAVFUGIENS — a complete experiment nobody surfaced
Ten studio-effect variants (tape delay, mercury vibrato, gated black-fire
envelopes, rubedo phasing, ouroboric feedback, projection glitch) plus six
interactive audio toys, built and apparently functional, but **not linked
from any site nav and not deployed anywhere.** Per `DESIRES.md`, Ted
identified this specifically as his "weird music" — the unfinished step is
purely presentational: it exists, nobody's shown it to anyone.

### ANTIGRAVEMBLEMSIN3D — abandoned, arguably correctly
A Vite-based fork carrying copies of the chiptune synth files, repurposed
for unrelated visual/game-design experiments. No git history, not deployed.
Not really "unfinished" so much as "not a real project" — the chiptune code
just rode along. Safe to leave alone unless someone wants the specific
three.js experiments inside it.

## Bach x chiptune

### Chipped On Bach — generation done, rendering mostly not
117 REAPER projects were generated (Bach MIDI x NES-game-palette timbre
mashups) — **the expensive, creative part is finished.** Most were never
rendered to WAV; only two MP4s exist at the `C:\Dev` root as output. What's
unfinished is a batch-render pass, which is mechanical, not creative — the
lowest-risk, most shovel-ready unfinished item in the whole survey.

### BachStudies — not actually a music project, and that's the finding
Text-only DH scholarship scaffold on Bach, never pushed to a remote, **no
audio or music code at all.** Listed here only to say plainly: this is not
an unfinished music project, it's a different kind of project entirely that
happens to share a composer's name with Chipped On Bach. Don't conflate them
when picking up either.

## SYNTHBUILDER itself and its internal subprojects

### SYNTHBUILDER-proper (the JSFX practice ground) — nothing built yet
Per `DESIRES.md`'s own "Not yet done" list: **no JSFX practice file exists
in `jsfx/` yet.** Every hour spent on SYNTHBUILDER so far has gone into
research, documentation (`ATALANTA.md`, `NSFRIPPER.md`, `CHIPPEDONBACH.md`,
`WEIRDMUSIC.md`, the four `BUILDING*`/`STUDYING*` pitfall docs), and the
`SYNTHBUILDING` catalog site — all real work, but none of it is the "get one
audible note" deliverable the project's own `CLAUDE.md` names as the rule
that outranks everything else here. This is the single most important
unfinished item in this whole document, because it's the thing the project
exists to do and hasn't started.

### SYNTHBUILDING (the catalog site) — deployed, with real gaps stated
Live and confirmed working (`t3dy.github.io/SYNTHBUILDING/`). Its own
`DEPLOY_STATE.md` honestly lists what's unfinished: mobile/narrow-viewport
layout untested, and it doesn't yet reflect the FUGUEJUKEBOX fix (once
WEBSITEFIXER lands one) or NARRATIVEDESIGNER's suggestions (see below).

### SYNTHTOY — mid-build
A 13-family Web Audio prototype lab teaching synthesis through
occult-diagram puzzle interfaces. Actively being built in a concurrent
session as of this writing; unfinished by virtue of being in progress, not
blocked. See `SYNTHTOY/CLAUDE.md` for its own state.

### ALGORITHMICMUSICTOOLS — scoped, zero lines written
A theory-education algorithmic-composition tool, sourced from a real
previously-unbuilt idea found in the megabase archive (2026-03-10 "AI-
assisted Music Engineering Workbench" thread). Fully scoped in its own
`CLAUDE.md`. Unfinished status: **has not been started at all** — this is a
planning-stage-only entry, listed so nobody assumes "scoped" means "underway."

### NARRATIVEDESIGNER — proposals delivered, nothing applied
Read all 7 books in `E:\pdf\narrative design` and produced a ~20-framework
toolkit plus per-project presentation/gamification suggestions covering all
15 catalog projects. **What's unfinished is the entire second half of the
job**: applying any of those suggestions to `db/seed_projects.json` and
rebuilding/redeploying the site is explicitly called out in `DESIRES.md` as
"a separate, deliberate step not yet taken." Right now this is a stack of
good ideas sitting next to a site that doesn't use any of them yet.

### RESEARCHER (Scarlatti Jones) — open-ended, ongoing by design
Maps ~230 project folders' worth of related music/game-design thinking
(`MUSIC_GAME_IDEA_MAP.md`). Not "unfinished" in the sense of having a
stopping point — it's a standing research role. Its one concretely open
deliverable is **`DEEPCUTS.md`**, a fuller sweep of megabase for
remote/obscure music ideas beyond the initial "weird music" pass, which was
running as a background agent as of this writing and had not yet landed.

## Cross-cutting unfinished items (not owned by any single project)

- **Git-history loss risk**: `REAPERBEYONDNES` and `nes-music-lab` remain
  uncommitted. Not creatively stuck, stuck *unsafely* — this is pure
  downside risk sitting unaddressed with a five-minute fix available.
- **NARRATIVEDESIGNER's suggestions vs. reality**: the site's project cards
  don't yet reflect any narrative-framing or gamification work proposed for
  them — an entire delivered-but-unapplied layer.
- **The FUGUEJUKEBOX site fix**: the largest concrete, scoped, ready-to-run
  unfinished item in this whole survey. See `WEBSITEFIXER/` in this folder.
- **`DEEPCUTS.md`**: pending, in progress at time of writing.

## Method note

This file answers "what's left," not "what's wrong" (`ATALANTA.md`) or
"where does everything live" (`MUSICHACKING.md`). When a project's status
changes — a fix ships, a decision gets made, a build finishes — update this
file in the same pass, the same discipline `DESIRES.md` already keeps for
what Ted has asked for. Don't let this drift into a snapshot nobody trusts.
