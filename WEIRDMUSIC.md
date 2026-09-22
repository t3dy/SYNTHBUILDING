# WEIRDMUSIC.md — experimental / generative music made with Claude

## Honest headline finding

A full read-only sweep of `C:\Dev\megabase` (1.45M prompts, 5,271 conversations,
11 sources — see `research/megabase_music_history.md` for the query method)
found **no generative, algorithmic, or "weird" AI-music experiments anywhere
in Ted's prompt history.** Targeted searches for SuperCollider, Csound,
Max/MSP, Pure Data, bytebeat, circuit-bending, modular/Eurorack, drone/noise
composition, and Markov/cellular-automata music all came back empty — every
apparent hit was a false positive (a speedrun-glitch thread, a physics
article, an unrelated snake-game doc). Per this workspace's own "honesty
before completion" principle: **this is not a rediscovered thread. If
SYNTHBUILDER builds something here, it's new territory, not a resumed
project.** Worth flagging directly to Ted rather than papering over — the
original ask assumed a "when I experimented with using claude to create weird
experimental music" project exists; the archaeology says it doesn't, at least
not under any of these search terms.

## What's actually closest to "weird" in the real project corpus

**ANTIGRAVFUGIENS** (`C:\Dev\EMBLEMSIN3D\ANTIGRAVFUGIENS`, see `ATALANTA.md`)
is the closest real artifact to what "weird experimental music" would look
like: ten alchemically-named studio effects (mercury vibrato, gated
black-fire envelopes, rubedo phasing, ouroboric feedback, projection glitch)
layered onto the Atalanta Fugiens chiptune fugues, plus six genuinely odd
interactive audio toys — the Levitating Athanor, Ouroboric Dub, Dewpoint
Runner, Sword/Egg Breakbeat, Rose-Garden Lockstep, and Sublimation Pinball.
It's real, it's built, it's just unintegrated and undeployed. If the goal is
"showcase the weird stuff," this is the strongest existing candidate — not a
new build.

## The one genuinely novel unbuilt idea worth surfacing

Buried in an unrelated thread ("Music-making website design," chatgpt-md,
2026-02-08) is the single most fully-formed *unbuilt* concept anywhere in the
corpus: a **Golden Dawn Rose Cross Lamen synth/looper web toy** — a clickable
rose / Tree-of-Life controller where clicking a Sephirah or a path gates synth
and loop parameters, with Mellotron-style sample pads. Ted's own words from
the thread:

> "What if we also use the... clickable tree of life as a basis for this,
> where they could click on the spheres and the paths, and these two things
> could sort of both be on the screen at the same time, and that becomes your
> controller for your synthesizer and loops."

This is multi-turn, iteratively refined, and concretely specified — not a
passing one-liner. It's also a natural fit for this workspace's existing
esoteric/occult tooling (SigilForge, KabbalahTrainer, the Tree-of-Life
attribution work already cataloged in `wiki/`) and nobody has built it. If
SYNTHBUILDER wants a genuinely "weird" practice project rather than another
NES-tone exercise, this is the strongest candidate on the table.

## Other unbuilt threads surfaced by the sweep (not music-weird, but worth knowing about)

- **"Nintendo Cover Song App"** (Oct 2024) — auto-populate a DAW with
  matching instrument tracks from a chosen game/level, import a MIDI cover,
  map to NES timbres, visualize the programming. Spec'd across 40 features
  in two follow-up conversations. No project folder exists for it — this is
  essentially the ambition NSFRIPPER/NESjamtools partially realized, asked
  for a year before either existed.
- **ROM-to-editable-synth-preset extractor** — distinct from what NSFRIPPER
  does (audio *extraction*): this would recover hand-tweakable synth presets,
  browsable by stage/song, from a ROM. Asked in near-identical language at
  least three separate times (Oct 2024, Feb 2026) and never became code.
- **Disney "Alice in Wonderland" chiptune covers**, one song per NES game's
  sound palette (Oct 2024) — a single thread, never resurfaced.
- **A home-grown "vibe-coded" Suno-style composition aid** (Mar 2026) —
  explicitly scoped as automating drudgery, not generating music from
  scratch. Researched, not built.

## The pattern this sweep confirms

The megabase search also independently confirms `NSFRIPPER.md`'s diagnosis:
the REAPER-plus-MIDI-keyboard setup problem was asked from scratch three
separate times across 15 months (Nov 2024, Feb 2025, Feb 2026), each time
starting fresh with no carried-over notes:

> "Well, I have created a instrument. It says ReaSynth on it, but when I
> press my keyboard, I'm not seeing anything." — *Chiptune Sound Design
> Tutorial*, Nov 2024

SYNTHBUILDER's own top rule ("get one audible note before building anything
else," `CLAUDE.md`) is a direct, if unintentional, answer to this exact
repeating failure — the problem long predates any of the project folders in
`MUSICHACKING.md`.

## Addendum — a much larger adjacent cluster, found separately (2026-09-21)

A parallel research pass (Scarlatti Jones, the RESEARCHER agent scoped in
`RESEARCHER/`, reading ~230 project folders rather than the prompt archive)
found something the megabase sweep above couldn't see: while literal
generative/algorithmic AI-music experiments don't exist, **a large cluster of
"symbolic diagram as music controller" thinking does** — proposed, half-built,
or built-but-unwired-to-audio across a dozen projects. Full map:
`RESEARCHER/MUSIC_GAME_IDEA_MAP.md` (1000+ lines, source-cited throughout,
with a correspondence-status key distinguishing historically-attested claims
from invented ones — read that key before reusing anything from it).

Highlights genuinely worth knowing about:
- **BRICKSHITSTORM** (`C:\Dev\BRICKSHITSTORM`) — a *built*, shipped puzzle
  game where the falling-brick cascade IS the music, scheduled into Web Audio
  against a bar clock. The most fully realized "puzzle produces music" system
  in the whole workspace, and the closest thing to a working answer to "weird
  experimental music" that actually exists.
- **`TetrisCodex/prototypes/p9-rhythm.html`** — an even earlier working
  prototype: beat-synced piece placement with a pitched note per tetromino
  and a filter cutoff warped by a balance-platform tilt angle.
- **TurkaGame's lettrism engine** — letters as physics objects whose
  behavior derives from their written form, ported successfully onto Hebrew
  letters (`GoldenDawnBlocks`) as a genuinely different ruleset. No audio
  yet, but named directly as the right chassis for a Tree-of-Life or Rose
  Cross music controller.
- **The Rose Cross Lamen idea from `WEIRDMUSIC.md` above has a real gap**:
  no extracted historical Golden Dawn correspondence data exists anywhere in
  this workspace for it (CrowleyDB's rich data is the *Tree of Life*, a
  related but distinct diagram) — flagged as open research debt, not
  something to fake with plausible-sounding placeholder correspondences.

This is the strongest candidate for what a genuinely "weird" SYNTHBUILDER
side-project would look like, if one is wanted: not new-from-nothing, but
finally wiring one of these existing symbolic-controller chassis to a synth.

## For the SYNTHBUILDING site

Given the honest finding above, this theme's site section should be framed
as **"weird ideas, some built, most not"** rather than a catalog of shipped
work: ANTIGRAVFUGIENS (real, built, unintegrated) alongside the Rose Cross
Lamen concept and the other unbuilt threads (clearly labeled as
proposals/never-built, not finished projects) — consistent with this
workspace's provenance conventions (`confidence: LOW` / `review_status:
DRAFT` for anything that's an idea rather than a shipped artifact).
