# SYNTHBUILDER — Claude Code Instructions

## Project Identity

A practice ground for building REAPER synthesizer plugins (JSFX, and eventually
VST3/JUCE) that produce keyboard-ready, NES-accurate chiptune tones — and, later,
original synth design beyond NES emulation. This is a **deliberately smaller,
verification-first** sibling to `NSFRIPPER` and `ReapNES-Studio`, which both got
deep into infrastructure (54K preset corpora, driver census tooling, a 40-rule
architecture doc) before verifying that a single plugin produced sound from a
project file. SYNTHBUILDER's whole reason to exist is to not repeat that.

Also home to **SYNTHBUILDING**, the public site (deployed to
`https://t3dy.github.io/SYNTHBUILDING/` from `github.com/t3dy/SYNTHBUILDING`)
cataloging all of Ted's music-hacking and music-composition projects plus his
music-book library, in the cards+pages style of the DH portals (`WitcherPortal`,
`ARTHURROBINPORTAL`, `Claudiens`). See `site/` and `SITE.md`.

## The One Rule That Outranks Everything Else Here

**Get one audible note before building anything else.** Every prior attempt in
this family (`ReapNES-Studio/docs/SUCCESSANDFAIL.md`,
`ReapNES-Studio/docs/AVOIDBLUNDERS.md`, `NSFRIPPER/docs/MISTAKEBAKED.md`) failed
the same way: infrastructure (catalogs, song sets, batch generators, sweep units)
got built on top of a synthesis layer that was never confirmed to make sound when
loaded from a project file rather than added by hand in the REAPER FX browser.
Blunder 10 in `AVOIDBLUNDERS.md` names it exactly: *"Over-Engineering Before
Ear-Testing."* Do not let SYNTHBUILDER become the fifth instance of this pattern.

**Correct order, every time** (from `ReapNES-Studio/docs/AVOIDBLUNDERS.md`):
1. Write a minimal JSFX synth with correct pins → test manually in REAPER (FX
   browser, not a generated project) → confirm you hear sound.
2. Save that working track as `.RPP` → read the file → learn the real token
   format for this REAPER version. Never guess RPP tokens.
3. Generate a minimal RPP matching the examined format → open it → confirm you
   still hear sound with zero manual configuration.
4. Add features to the JSFX one at a time → re-test after each addition.
5. Add MIDI items manually in REAPER, save, examine how REAPER actually stored
   them → only then attempt to generate MIDI-bearing projects.
6. Only after all of the above: automation, presets, song sets, catalogs.

## Prior Art In This Workspace (read before writing any JSFX)

| Project | What it proved | Where |
|---|---|---|
| `NSFRIPPER` | NES-accurate audio extraction + a 40-rule hardened architecture (bankswitching, non-linear APU mixing, noise length-counter simulation, bandlimited synthesis). The **stems approach** (Rule 31) — render per-channel audio, not a live multi-track JSFX sum — is the current answer to "why doesn't my REAPER project sound like the game." | `NSFRIPPER/CLAUDE.md`, `NSFRIPPER/.claude/rules/*.md` |
| `ReapNES-Studio` | The JSFX-vs-VST3 keyboard problem, in full: JSFX can't receive live MIDI keyboard input in REAPER (no "instrument" flag), VST3 can but its RPP reference format is an opaque REAPER-only binary blob. Never fully resolved — see `SYNTHPROBLEM.md`. | `ReapNES-Studio/CLAUDE.md`, `SYNTHPROBLEM.md`, `docs/SUCCESSANDFAIL.md`, `docs/AVOIDBLUNDERS.md`, `docs/BLOOPERS.md` |
| `GlitchMario` | The narrative version of the same blunders (100 events, 17 blunders, told as a five-day timeline), shipped as a public site. Good source for what an honest "we failed a lot and here's what we learned" page looks like. | `GlitchMario/README.md`, live at `https://t3dy.github.io/GlitchMario/` |
| `FUGUEJUKEBOX`, `EMBLEMSIN3D` (`chiptune.js`) | Proof that offline square-wave synthesis (no REAPER, no JSFX, pure Python/JS) is a reliable fallback when the REAPER integration layer is the blocker, not the synthesis math. | `ATALANTA.md` in this folder |

Read `NSFRIPPER.md`, `ATALANTA.md`, `CHIPPEDONBACH.md`, `WEIRDMUSIC.md` in this
folder before starting — they distill the parts of each project relevant to
synth/plugin building specifically, so you don't have to re-read four full
projects' worth of docs.

## Hard-Won JSFX Rules (do not rediscover these)

Condensed from `NSFRIPPER/.claude/rules/*.md`, `ReapNES-Studio/docs/BLOOPERS.md`,
and `C:\Users\PC\.claude\projects\C--Dev\memory\feedback_reaper_jsfx.md`. Full
detail lives in those files — this is the checklist to run through before
writing or shipping any JSFX file.

```
desc:Plugin Name
tags:instrument synthesizer
in_pin:none
out_pin:Left
out_pin:Right
```
- `tags:` not `//tags:` — the `//` makes it a comment and REAPER silently treats
  the plugin as an effect.
- Without `in_pin:none`, REAPER treats a JSFX as an audio effect (needs audio
  input), not an instrument (generates audio from MIDI) → silence.
- ASCII only, anywhere in the file. Unicode (em dashes, arrows) can break
  compilation silently on Windows/cp1252.
- Slider numbers sequential, no gaps — RPP stores 64 positional values and a
  gap (e.g. slider15 → slider20) risks misaligned values on load.
- `^` is POWER in JSFX, not XOR. Use `((a + b) & 1)` for single-bit XOR.
- REAPER caches compiled JSFX by filename. If a plugin stops working after an
  edit, rename the file to force recompilation (or run a sync script that does
  this — see `NSFRIPPER/.claude/rules/jsfx_deploy.md`).
- Output must be exactly 0.0 when nothing is playing. Never produce DC offset
  (`mixed - 0.35` outputs nonzero at `mixed=0`) — use a proper DC blocker
  (1-pole HP ~10 Hz), not a subtracted constant.
- **JSFX cannot receive live MIDI keyboard input in REAPER — this is a
  documented hardware/format limitation, not a bug to keep chasing.** VST3
  (e.g. via JUCE) can, but its RPP reference requires binary state data only
  REAPER itself can produce; see `ReapNES-Studio/SYNTHPROBLEM.md` Option D
  (extract the block from one manually-saved REAPER project, template from
  there) for the least-bad workaround anyone in this workspace has found.
- Never guess RPP tokens (`MASTER_SEND`, `REC_INPUT`, `RECINPUT`, `RECMON` were
  all guessed and all rejected by REAPER v7.27). Copy exact syntax from a real
  `.RPP` saved by the user's own REAPER version, or the Cockos wiki
  (`wiki.cockos.com/wiki/index.php/RPP`).
- `REC` line for MIDI input on a track needs all 8 fields; the all-devices
  value is version/system-dependent (NSFRIPPER found `6112`, an older note
  found `5088` — device index varies by system). **Verify against a real saved
  project on the machine you're targeting; do not copy a number from another
  project blind.**

## External Reference (Eric Ruud's `tide-room`, github.com/EricRuud/tide-room)

Ted's friend shared this repo as a possible source of transferable technique
for the exact problem above. Research findings and concrete borrowable
patterns: `research/tideroom_lessons.md`. Read it before starting new plugin
work — if it has a cleaner answer to the JSFX-instrument or plugin-packaging
problem than anything above, use that instead of re-deriving it.

## Directory Layout

```
SYNTHBUILDER/
  CLAUDE.md              this file
  NSFRIPPER.md            NES-extraction + synth-fidelity project, condensed for plugin work
  ATALANTA.md             Atalanta Fugiens x NES/chiptune cluster (FUGUEJUKEBOX, EMBLEMSIN3D)
  CHIPPEDONBACH.md         Bach x NES mashup project
  WEIRDMUSIC.md            experimental / generative music made with Claude — megabase-sourced
  MUSICHACKING.md          full catalog + orchestrator map of every music project on disk
  research/                background-agent research artifacts (this session)
  jsfx/                    practice JSFX plugins — start here, one audible note at a time
  db/                      SQLite source of truth for the SYNTHBUILDING site
  scripts/                 site build pipeline (JSON seed -> SQLite -> static HTML)
  site/                    generated static site (SYNTHBUILDING) -- never hand-edit
  DECISIONS.md             directional calls, recorded immediately
  DEPLOY_STATE.md          canonical URL, host, gotchas (GitHub Pages default per workspace policy)
```

## Site Architecture (SYNTHBUILDING)

Follows the workspace's standard DH-portal pattern (`WitcherPortal`,
`ARTHURROBINPORTAL`): JSON seed -> SQLite -> Python static-site generator ->
vanilla HTML/CSS/JS -> GitHub Pages. No frameworks, no build tools, no npm.
Every entity (project, book) carries a `card_summary` (~50 words) and
`page_summary` (~500 words), plus `source_method`/`review_status`/`confidence`
provenance fields per `WitcherPortal/docs/WRITING_TEMPLATES.md` conventions.

- **Do not deploy to Vercel.** Workspace hosting policy (root `CLAUDE.md`,
  2026-09-06): GitHub Pages is the default; this project has no server-side
  need.
- Pages serves from a repo subpath — `GITHUB_PAGES` env var / relative paths
  matter. Check `DEPLOY_STATE.md` before touching deploy config.
- **Deploying (pushing to `github.com/t3dy/SYNTHBUILDING`, or creating the
  remote repo) is a publish action — confirm with Ted before doing it, per
  workspace/session convention, even though he named the target repo up
  front.**

## Anti-Creep Rules (from ReapNES-Studio, proven necessary)

- Do not expand into unrelated ambitions before the first note plays.
- Do not prioritize infrastructure (catalogs, presets, song sets) over a
  verified single-plugin, single-note deliverable.
- Do not build automation before verifying the plugin works in REAPER, by ear,
  added manually.
- A working single-note test beats a speculative framework.
- Verify after every change, not just at the end of a session.
