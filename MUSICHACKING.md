# MUSICHACKING.md — orchestrator's map of every music-hacking project

Purpose: let Claude (or Ted) pick any of these back up cold, from
`SYNTHBUILDER/`, without re-deriving where things stand. Every entry is
**verified**, not assumed — live URLs were actually checked; status claims in
each project's own docs were checked against its actual git history and file
state, and corrected where wrong. Compiled from direct file reads plus four
parallel research passes on 2026-09-21 (see `research/` for full agent
transcripts). Still pending at time of writing: `C:\Dev\megabase` history
(feeds `WEIRDMUSIC.md`) and the `E:\pdf` book library — both noted below where
relevant, and this file should be re-synced once those land.

## Quick-reference table

| Project | Path | Status | Live? | One-liner |
|---|---|---|---|---|
| NSFRIPPER | `C:\Dev\NSFRIPPER` | ACTIVE, stalled since 2026-04-20 | Site: yes | NES ROM/NSF → MIDI/REAPER extraction, 40-rule hardened architecture, mid-way through an unmade A/B/C ear-test decision |
| ReapNES-Studio | `C:\Dev\ReapNES-Studio` | ARCHIVED (absorbed into NSFRIPPER) | No | Where the JSFX-instrument + keyboard-routing problems were first fought; unused JUCE/VST3 build still sits in `vst/` |
| NESjamtools | `C:\Dev\NESjamtools` | STABLE, not ear-confirmed | No, local only, no git remote | Sibling "instrument" layer: one multitimbral JSFX + Python high-fidelity renderer, 50 games |
| GlitchMario | `C:\Dev\GlitchMario` | STABLE, complete | **Confirmed live** `t3dy.github.io/GlitchMario/` | Narrative documentation site of the same struggle — 100 events, 17 blunders, shipped |
| NESMusicStudio | `C:\Dev\NESMusicStudio` | ACTIVE (possibly the real current front-runner of this cluster) | Site: `t3dy.github.io/ReapNES/` | NSF/ROM→MIDI→REAPER/WAV/MP4→YouTube; Castlevania 1 complete, Contra in progress |
| REAPERBEYONDNES | `C:\Dev\REAPERBEYONDNES` | ACTIVE, **not git-tracked (loss risk)** | No | Declared multi-system successor (GBA/SMS/Saturn/Genesis/SNES/GBC/Virtual Boy) |
| nes-music-lab | `C:\Dev\NESMusicLab` | Stalled, uncommitted | No | Research-grade extraction/reconstruction (Castlevania analysis, trace conversion) |
| arpeggiator-composer | `C:\Dev\arpeggiator-composer` | Stalled, uncommitted | No | Deterministic MIDI arpeggiator built for REAPER |
| ChipScribe / ChipTools | *(GitHub-only, no local tree)* | ACTIVE | **Confirmed live** `t3dy.github.io/ChipTools/` | Deployed front-end for the NES-music-tools family |
| FUGUEJUKEBOX | `C:\Dev\FUGUEJUKEBOX` | Music: STABLE/complete. Site: **broken** | Claimed `fuguejukebox.vercel.app` — **confirmed 404, dead** | Atalanta Fugiens x NES chiptune, 500 MP3s (verified present), website never actually served them |
| EMBLEMSIN3D (8-bit fugues) | `C:\Dev\EMBLEMSIN3D` | ACTIVE (whole project); audio subsystem STABLE | **Confirmed live**, in-world at `t3dy.github.io/emblems-in-3d/` (press M) | Same 50 Atalanta fugues, live NES-APU-style Web Audio synth inside the walkable 3D world |
| ANTIGRAVFUGIENS | `C:\Dev\EMBLEMSIN3D\ANTIGRAVFUGIENS` | SCRATCH, unintegrated | Local only | Ten weird studio-effect variants + six interactive audio toys on the same fugues |
| ANTIGRAVEMBLEMSIN3D | `C:\Dev\ANTIGRAVEMBLEMSIN3D` | Abandoned fork | No | Vite-based mirror carrying the chiptune files for unrelated visual experiments |
| Chipped On Bach | `NSFRIPPER/scripts/bach_*.py` | Artifacts complete, some renders pending | Two MP4s at `C:\Dev` root | Bach MIDI x NES game-palette timbre mashup; 117 generated projects, most never rendered to WAV (WISH16, open) |
| BachStudies | `C:\Dev\BachStudies` | STUB, text-only | Never pushed to remote | Bach **scholarship** DH scaffold — no audio/music code at all; don't confuse with Chipped On Bach |
| SYNTHBUILDER | `C:\Dev\SYNTHBUILDER` | Just-created, planning-stage | N/A | This project — practice ground + `SYNTHBUILDING` catalog site |

## What's actually stuck, ranked by how close it is to unstuck

1. **NSFRIPPER's A/B/C ear-test decision.** Everything else about the pipeline
   works. It's a 20-minute listening session (open the three variant
   projects, listen, pick one) plus logging the decision — the single
   highest-leverage thing anyone could do in this whole family. See
   `NSFRIPPER.md`.
2. **NESjamtools' one open bug** ("W&W Map: rhythm feels wrong") — also
   waiting purely on an ear-test, everything else in its bug log is Fixed.
3. **REAPERBEYONDNES and nes-music-lab have no git history.** Not stuck
   creatively, stuck safely — `git init` + first commit is a five-minute,
   zero-risk fix that should happen before either is touched further.
4. **FUGUEJUKEBOX's site is dead** (404) despite its own docs claiming it's
   live — the music is done, the deploy just needs redoing correctly (static,
   GitHub Pages, actual servable audio paths). See `ATALANTA.md`.
5. **117 Chipped-On-Bach projects generated, not rendered** — the expensive
   part (composition/generation) is done; only a batch-render pass remains.
   See `CHIPPEDONBACH.md`.
6. **ReapNES-Studio's VST3/JUCE build** solves live keyboard input but was
   never wired to scriptable project generation — the one genuinely open
   *technical* problem (not just an unmade decision) in this family, and the
   best candidate for SYNTHBUILDER's own practice work. See `NSFRIPPER.md`.

## Where the pitfalls are documented (read before touching any of the above)

`STUDYINGNESROMS.md`, `BUILDINGPATCHES.md`, `BUILDINGSYNTHS.md`,
`BUILDINGPROJECTS.md` in this folder — split by pipeline layer, each
distilling the specific hard-won rules from `NSFRIPPER/.claude/rules/*.md` and
`ReapNES-Studio/docs/{BLOOPERS,AVOIDBLUNDERS,SUCCESSANDFAIL}.md` so a fresh
session doesn't re-pay the cost of rediscovering them.

## Not music-hacking (ruled out during this survey, noted so nobody re-checks them)

`GPTREAPERPRODUCTS.txt` (a chat-log dump, not a project), `JAMMING_ALONE.md`
(a general play-session ritual doc, touches chiptune only in passing prompt
examples), `EsotericBeatNews`/`ESOFEED` (podcast aggregators, no music-making),
`MTGOverlay` family (MTG draft tools, no audio), `AlchemyBeatEmUp` ("Beat" =
combat, not music), the `AUDIOBOOKMAKER*` family and `audiobook-app`
(spoken-word/TTS, not music/synth), `reaper-agent`/`desktop-agent-harness`
(spec-only architecture docs, no built REAPER tooling), `NESARPEGDESIGNS`
(empty stub).

## Megabase sweep — closed out

Full findings in `WEIRDMUSIC.md` and `research/megabase_music_history.md`.
Headline: no generative/algorithmic "weird music" experiments exist in 1.45M
archived prompts — that's new territory, not a resumed thread. The one
genuinely novel unbuilt idea surfaced: a **Golden Dawn Rose Cross Lamen
synth/looper** (clickable Tree-of-Life controller gating synth/loop
parameters, Feb 2026 thread) — the strongest "weird" practice-project
candidate on the table if SYNTHBUILDER wants something other than another
NES-tone exercise.

## Music-book library — closed out (35 books, `E:\pdf`)

Full catalog: `research/music_library_catalog.json` (seeded into the site as
`db/seed_books.json`). Most of the library is criticism/musicology (33 1/3
series, ludomusicology) with no technical content — flagged honestly per-book
rather than inflated. Three stand out as actually load-bearing for
SYNTHBUILDER's practice work:

- **Will Pirkle, *Designing Software Synthesizer Plug-Ins in C++*** —
  the single most directly useful technical book in the library: a
  code-level guide to building a real synth plugin (oscillators, envelopes,
  filters including a full Moog ladder-filter implementation) across
  RackAFX/VST3/AU. Directly portable to the VST3/JUCE problem
  `NSFRIPPER.md` identifies as SYNTHBUILDER's best-scoped open technical
  exercise.
- **Karen Collins, *Game Sound*** — the standard academic history of 8-bit
  sound-chip architecture (NES 2A03 included) and the compositional
  constraints it imposed; domain knowledge for making NES-tone choices that
  are accurate for a reason, not just imitative.
- **Geary Yelton, *The Rock Synthesizer Manual*** (1984) — a plain-language
  VCO/VCF/VCA/envelope/LFO explanation of the exact subtractive-synthesis
  signal chain a JSFX synth needs to implement; good conceptual bridge
  between Simon Cann's patch-oriented book and Pirkle's code.

Also worth noting: **Andra Ivănescu's *Popular Music in the Nostalgia Video
Game*** names, in scholarly terms, the exact accuracy-vs-idealized-"retro"-
sound distinction NSFRIPPER's 40-rule architecture is built around ("the way
it never sounded") — good citation if the site ever wants to justify why
NES-*accurate* synthesis is the harder, more interesting goal than generic
chiptune-flavored sound.

Every project catalog table above is now current as of this session's full
survey (megabase + PDF library + direct file reads across 4 parallel research
passes). Re-run a pass over this file if a future session surfaces a project
not listed here.
