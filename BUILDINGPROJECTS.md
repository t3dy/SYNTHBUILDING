# BUILDINGPROJECTS — generating .RPP REAPER project files programmatically

Scope: the layer that wires a working plugin into a REAPER project file that
opens with zero manual configuration. This is where NSFRIPPER and
ReapNES-Studio lost the most time relative to how "solved" each individual
piece looked — a working plugin plus a syntactically valid RPP can still
produce total silence, because REAPER's project format has undocumented
structural requirements. Distilled from `NSFRIPPER/.claude/rules/reaper_projects.md`
and `ReapNES-Studio/docs/{BLOOPERS,AVOIDBLUNDERS,SUCCESSANDFAIL}.md`.

## The one rule above all others: never hand-roll an RPP template

NSFRIPPER hit two separate REAPER parse errors (a `NOTES` block syntax error
and a `MASTERNCHAN` token-order error) from bypassing its own project
generator to build a "minimal template" from scratch. A single working track
saved by REAPER itself contains on the order of 100 lines of boilerplate
(`ENVATTACH`, `SAMPLERATE`, `METRONOME`, `RECORD_CFG`, `RENDER_CFG`,
`MASTERPLAYSPEEDENV`, `TEMPOENVEX`, `PROJBAY`, etc.) that the loader silently
depends on. A minimal template misses structural elements that don't error —
they just produce a project that loads "fine" and doesn't work.

**Practical rule:** write one generator function (or reuse NSFRIPPER's
`generate_project.py`) that always emits the full header. If you need a new
project shape, add a flag to the existing generator rather than writing a new
template from scratch. Last resort: post-process the generator's output
rather than bypassing it.

## Never guess RPP tokens

All of these were guessed and all were rejected by REAPER v7.27:
`MASTER_SEND`, `REC_INPUT`, `RECINPUT`, `RECMON`. The correct tokens:
- `MAINSEND 1 0` (not `MASTER_SEND`).
- MIDI input configuration is a **runtime setting tied to the user's
  hardware**, not a project-file property — REAPER v7.27 has no working RPP
  token for it. Stop trying to set it programmatically; document the one
  manual step ("set MIDI input on this track after opening") instead of
  treating it as an unsolved bug.

**When in doubt about any token: open a project the user actually saved from
their own REAPER version and copy the exact syntax.** Referencing the Cockos
wiki (`wiki.cockos.com/wiki/index.php/RPP`) is the fallback if no real example
exists yet — but a real saved file beats documentation every time, because
token format has changed across REAPER versions.

## Embedding MIDI data: don't

Two approaches were tried and both failed to produce playable items:
- `SOURCE MIDIPOOL FILE "..."` — items appear in the timeline but produce no
  audio.
- Inline `SOURCE MIDI` with raw `E`/`X` event lines — items appear empty, no
  audio.

**Why:** REAPER v7 stores MIDI data internally via a `POOLEDEVTS` (pooled
event) system referencing events by GUID — not a format anyone outside REAPER
has successfully replicated by hand.

**What actually works:**
- `<SOURCE MIDI` with `FILE "path/to/file.mid"` — reference an external `.mid`
  file rather than trying to embed the events. This loads and plays correctly.
- Accept a two-step workflow for anything more dynamic: generate the project
  with tracks/plugins ready, then drag-and-drop MIDI into it by hand — or
  write a ReaScript (REAPER's own Lua/Python API, running *inside* REAPER)
  that inserts MIDI items using REAPER's actual item-creation API instead of
  raw RPP text manipulation.

## Track structure requirements (all of these, every track)

```
PANLAWFLAGS 3
SHOWINMIX 1 0.6667 0.5 1 0.5 0 0 0
FIXEDLANES 9 0 0 0 0
SEL {0|1}
REC {armed} <all-8-fields>
TRACKHEIGHT 0 0 0 0 0 0 0
INQ 0 0 0 0.5 100 0 0 100
```

- Missing `PANLAWFLAGS`/`SHOWINMIX`/`FIXEDLANES` causes REAPER layout glitches
  (not silence, but a broken-looking project).
- `REC` line: use the "all MIDI inputs, all channels" value **even on
  unarmed tracks** — if input is 0 on an unarmed track, REAPER forgets MIDI
  routing entirely, and when the user later arms it manually, it defaults to
  *audio* input instead, silently breaking keyboard play. The exact
  all-devices numeric value is version/system-dependent (NSFRIPPER found
  `6112` after an earlier `5088` turned out to reference one specific,
  sometimes-disconnected hardware device slot on one machine) — **verify
  against a real saved project on the target machine, never copy a number
  from another project's notes.**
- Track colors: `PEAKCOL = 0x1000000 | (blue<<16) | (green<<8) | red` — this
  is Windows `COLORREF` byte order (not plain RGB) plus a custom-color flag
  bit. Omitting the `0x1000000` flag makes REAPER ignore the color entirely;
  plain RGB order produces visibly wrong hues.

## Multi-track NES-style architecture (if building a multi-channel project)

- Each track's synth instance must be set to its own single-channel mode via
  the relevant slider (NSFRIPPER: slider13 — 0=Pulse1, 1=Pulse2, 2=Triangle,
  3=Noise). **Never** use a "full APU, all channels merged" mode on a
  multi-track project — it plays all channels on every track simultaneously.
  Full-APU mode is only correct for a single-track, all-channels-in-one-JSFX
  setup (e.g. one generic keyboard-play track).

## Verification order before calling any generated project "ready"

1. Run whatever validation/lint script exists for the plugin family (JSFX
   lint, RPP lint, MIDI quality) — catches known-blunder regressions before
   REAPER ever opens the file.
2. Does the plugin produce sound added **manually** in REAPER? (Test this
   before touching project generation at all — see `BUILDINGSYNTHS.md`.)
3. Does a **minimal** RPP with the plugin (no custom parameters) produce
   sound?
4. Only after 2-3 pass: does a full generated project — with your actual
   MIDI, slider values, and track layout — produce sound with **zero manual
   configuration** beyond the one unavoidable manual step (setting MIDI input
   device, which is not scriptable)?

Never generate a batch of projects before one project passes all four steps.
This was the single largest time-cost across every REAPER-project-generation
attempt in this workspace (`ReapNES-Studio/docs/SUCCESSANDFAIL.md`: "we built
song sets, preset catalog, project generator, MIDI mapper, drum kits — then
discovered the fundamental plugin didn't produce sound").
