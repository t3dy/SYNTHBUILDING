# CHIPPEDONBACH.md — J.S. Bach through NES timbre

Scope: the project literally titled "Chipped On Bach" — Bach MIDI paired with
NES-instrument presets extracted from real game soundtracks. Distinct from
`BachStudies` (see below, a separate and unrelated text-only DH scaffold that
happens to share the composer's name).

## What it is

`NSFRIPPER/scripts/bach_nes_mashup.py` (+ `bach_render_mashup.py`,
`build_bach_preview.py`) pairs Bach MIDI files (Goldberg Variations, BWV 988;
Well-Tempered Clavier fugues/preludes; the Two-Part Inventions; Cello Suite
No. 1, BWV 1007) with NES instrument timbre presets extracted from
Castlevania, Contra, Metroid, and Gradius stage palettes — each stage having a
distinct pulse-duty-cycle character — and renders the combination through the
same `ReapNES` JSFX synth family the rest of NSFRIPPER uses. This is not a
separate synthesis engine; it's the NSFRIPPER/ReapNES pipeline pointed at
classical MIDI instead of extracted game MIDI.

## What actually exists on disk (verified)

Two finished video artifacts sit at the `C:\Dev` root:
- `Chipped_On_Bach_Preview.mp4` (70.6MB) — 39 tracks, 1:12:36 total.
- `Chipped_on_Bach_Preview_less_glitchy.mp4` (39MB) — a 4-track, 7:28 re-cut,
  presumably curated down from the first pass after listening.

Both have `.txt` sidecars (YouTube-description drafts) confirming "All
synthesis uses the NES Audio Processing Unit (2A03) via ReapNES JSFX" — i.e.
these render through the real synth pipeline, not a mockup. `BACH_MAP` in
`build_bach_preview.py` expands short filenames (`Fugue2`, `invent1`,
`var3c1`...) to full catalog titles (BWV numbers included) for the YouTube
description — worth reusing verbatim if these ever get published.

**Known open item, from NSFRIPPER's own wishlist (`state/wishes.json`,
WISH16):** roughly 117 Bach-fugue x game-palette REAPER projects were
generated, but most were never rendered to WAV — flagged as "likely
interrupted by crash," still open, low priority. This is real, low-effort,
already-scoped follow-on work if anyone wants to pick it back up: the
generation step already ran, only the render step is incomplete.

## A hardcoded path worth checking before reusing these scripts

`build_bach_preview.py` reads its source WAVs from
`C:\Dev\NESMusicStudio\output\bach_mashups` — the **pre-rename** repo path
(the project was later reorganized as `NSFRIPPER`, and there is also now a
separate, currently-more-active `C:\Dev\NESMusicStudio` folder — see
`NSFRIPPER.md`'s "wider family" section). Before re-running this script,
confirm which folder actually holds the bach_mashups output now; don't assume
the hardcoded path still points at the right place.

## BachStudies — not the same project, despite the name

`C:\Dev\BachStudies` is a separate, unrelated digital-humanities scaffold: a
SQLite -> Python -> static-HTML pipeline for Bach *scholarship* (13 books
converted to a corpus, a dictionary of terms like Fugue/Cantata/Chorale,
timeline events). **It contains zero audio, MIDI, synthesis, or REAPER code
anywhere.** It's a stub — only 12 real dictionary entries exist behind
13,815 largely-empty auto-generated stub pages left over from an indiscriminate
extraction pass that was never pruned after the DB was reset. It has never
been pushed to a git remote, so its GitHub Actions Pages deploy has never run.
**For the music-hacking catalog, this project does not belong** — it's
pure-text Bach *scholarship*, not Bach *music-making*. `BACHPEDAGOGY.md`
proposes adding short public-domain-MIDI audio snippets to a future "Works"
tab, but that's unbuilt planning-doc content, not a real feature. Worth a
one-line cross-reference from the site (in case Ted wants the scholarly
grounding for a future Bach-related music piece) but not a card in the
music-hacking catalog itself.

## What to reuse for SYNTHBUILDER practice work

This is a good template for a "practice patch, real repertoire" test: Bach's
counterpoint is public domain, well-transcribed (many free MIDI sources), and
harmonically dense enough to stress-test a new JSFX patch's polyphony and
envelope behavior in ways a single game's soundtrack might not. If
SYNTHBUILDER wants a repeatable ear-test corpus beyond NES game MIDI, the
Bach MIDI collection already staged in NSFRIPPER's `studio/midi/classical/`
directories is ready to use — check `bach_nes_mashup.py`'s `MIDI_DIRS` list
for the exact paths before assuming they're still populated.
