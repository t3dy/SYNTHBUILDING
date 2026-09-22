# ATALANTA.md — Michael Maier's *Atalanta Fugiens* set to NES sounds

Scope: everywhere Ted has taken Maier's 1617 emblem-book of 50 three-voice
alchemical canons ("fugues for the ears") and run it through chiptune/8-bit
synthesis. Two independent projects did this, from the same source data
(`EmblemRoguelike/assets/fugues.json`, the transcribed MIDI of all 50 canons),
in different ways — plus two unintegrated experimental offshoots.

## FUGUEJUKEBOX (`C:\Dev\FUGUEJUKEBOX`) — the batch-rendered version

500 MP3s (50 emblems x 10 variations: 3 harmonic elaborations, 3 scale-run/
improvisation variants, 4 digital-effects treatments — cathedral reverb,
vibrato wobble, echo cascade, spacious chorus), synthesized offline as square
waves via a Python/scipy pipeline (`generate_variations.py` -> `render_to_audio.py`).
**Verified on disk: all 500 MP3s + 500 WAVs actually exist.** The music side of
this project is genuinely, completely done.

**The website half is broken, and its own docs are wrong about that.**
`FUGUEJUKEBOX-website/` and `FugueJukebox-repo/` are two divergent copies of a
Next.js browsing site. The claimed live URL, `https://fuguejukebox.vercel.app`,
**was checked directly and returns HTTP 404 — the site is dead**, contrary to
the README's "LIVE ON THE WEB!" and DEPLOYMENT.md's "Status: Live and
Operational." Two compounding bugs: the audio path in `app/emblem/[id]/page.tsx`
is a filesystem-relative path (`../../../FUGUEJUKEBOX/emblems/...`) that never
resolves under real HTTP serving, and the git-tracked copy
(`FugueJukebox-repo`) excludes all 500 MP3s from the push entirely
(DEPLOYMENT.md: "GitHub has file size limits... not included"). So even a
working deploy of that code would have nothing to play. There's also a
duplicate ~140MB copy of all 500 MP3s sitting in `FUGUEJUKEBOX/music/emblems/`
serving no purpose.

**Fix, in order, per workspace hosting policy (GitHub Pages default, this is
fully static and has no business on Vercel):**
1. Decide the canonical copy of the 500 MP3s (delete the `music/emblems/`
   duplicate once decided).
2. Get the audio into a servable path — `public/` folder or Git LFS (the
   project's own DEPLOYMENT.md suggests LFS but never executed it).
3. Redeploy static to GitHub Pages, not Vercel.

## EMBLEMSIN3D's 8-bit fugues (`C:\Dev\EMBLEMSIN3D`) — the live, in-world version

A hand-built NES-APU-style Web Audio synth (`chiptune.js`: two pulse
oscillators via `PeriodicWave` at 50%/25% duty + one triangle bass, per-note
ADSR) plays the same 50 fugues **live inside the walkable three.js
reconstruction of the book**, transcribed playback (not generative — the
notes are Maier/Merian's actual counterpoint). `gamesynths.js` supplies ten
"game palettes" mined from "nsfripper's CODEXSYNTH bench" (Mario, Zelda,
Metroid, Castlevania, Contra, Final Fantasy, Kirby, Bubble Bobble, Bionic
Commando, Wizards & Warriors) — every emblem cycles through all ten as it
loops. This is the direct link between the Atalanta work and the NSFRIPPER
family: the timbre palettes are literally sourced from NSFRIPPER's extraction
work.

**Confirmed live** inside the walkable world at
`https://t3dy.github.io/emblems-in-3d/` (press **M**, or `&sound=1`). The
standalone jukebox/fugue-browser pages (`jukebox.html`, `fugue.html?n=NN`) and
the cinematic tour (`grandtour.html`, plays each fugue as the camera arrives)
are **local-only by design** — they load sibling-project image assets by
absolute `C:\Dev`-rooted path and were deliberately never ported to the Pages
build (see `EMBLEMSIN3D/DEPLOY_STATE.md`). Run locally with
`python -m http.server 5184` from `C:\Dev`, browse to
`http://localhost:5184/EMBLEMSIN3D/jukebox.html`.

## Unintegrated offshoots

- **`EMBLEMSIN3D\ANTIGRAVFUGIENS\`** — a small self-contained experiment
  adding a second axis of ten "studio tricks" per emblem (tape delay, mercury
  vibrato, gated black-fire envelopes, rubedo phasing, ouroboric feedback,
  projection glitch...) plus six deliberately weird interactive audio toys
  (Levitating Athanor, Ouroboric Dub, Sword/Egg Breakbeat, Rose-Garden
  Lockstep, Sublimation Pinball, Dewpoint Runner). Not linked from the main
  site nav, not deployed — genuinely worth a look for `WEIRDMUSIC.md`
  material, since it's the weirdest thing in this whole cluster.
- **`C:\Dev\ANTIGRAVEMBLEMSIN3D`** — a full static mirror of EMBLEMSIN3D
  (unchanged copies of `chiptune.js`/`gamesynths.js`), rebuilt around Vite,
  used as a sandbox for unrelated visual/game-design experiments
  (`antigrav.html`, `gameforge.html`). No git history, not deployed, not a
  music project in its own right — the chiptune files just came along for the
  ride. Abandoned fork; safe to ignore unless resurrecting the specific
  three.js experiments it carries.

## What to reuse for SYNTHBUILDER practice work

Both real implementations here (`chiptune.js` and FUGUEJUKEBOX's
`render_to_audio.py`) prove square-wave/triangle chiptune synthesis in *pure
Python or pure Web Audio* is reliable and doesn't need REAPER/JSFX at all —
useful as a reference implementation to check a JSFX patch against, or as a
fallback delivery path when the REAPER integration layer is the blocker (see
`NSFRIPPER.md`'s stems-approach discussion). If SYNTHBUILDER wants a
non-NES-game test case for a new JSFX patch, the Atalanta fugues are
ready-transcribed, public-domain, and already have a known-good reference
rendering to compare against.
