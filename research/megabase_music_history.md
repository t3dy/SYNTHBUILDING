# Megabase Music History — Prompt Archaeology

Read-only survey of `C:\Dev\megabase\megabase.db` (1.45M user prompts, 5,271 conversations,
11 sources) for everything touching synth/plugin building, REAPER, NES/chiptune sound
programming, JSFX/VST, music theory, Bach/Maier fugues set to 8-bit, and generative/
algorithmic/"weird" AI music experiments.

## Method

Used the `promptarchaeology-heldscalla` skill's TEMP views (`pa_prompts`, `role='user'`
only) over `megabase.db` opened `mode=ro`; no writes, no new persistent views (schema:
`C:\Dev\promptarchaeology\schema\views.sql`). Two passes:

1. **Keyword-family LIKE queries** across all 11 sources, then narrowed to AI-conversation
   sources only (`chatgpt`, `chatgpt-md`, `claude`, `llm_logs_html`, `llm_logs_pdf`,
   `google_chat`, `pkd_chats` — excluding sms/facebook/twitter/gmail, noisy false positives
   like "nes " matching "genes"). Counts (AI sources): synth_build 239, bach/maier 202,
   midi 73, nes/chiptune 45, music_theory 34, daw_general 27, reaper/jsfx 26, sound_design 10,
   generative_algo 2. Union: 565 prompts.
2. **Targeted "weird music" pass**: glitch, algorave, max/msp, pure data, supercollider,
   csound, drone/noise/ambient music, aleatoric, markov music, cellular automata, fractal
   music, circuit bending, bytebeat, tracker music, modular synth, eurorack — every hit
   inspected by hand.

Conversations were ranked by match density, then the first several prompts of each
were pulled verbatim. Results were cross-checked against what actually exists on disk in
`C:\Dev` (NSFRIPPER, ReapNES-Studio, FUGUEJUKEBOX, GlitchMario, EMBLEMSIN3D/`chiptune.js`,
and the brand-new SYNTHBUILDER scaffold) to separate talk from build.

## Recurring themes

1. **Reverse-engineer NES/Capcom synth settings from ROMs.** The identical question recurs
   across 17+ months: "Recreating Nintendo Synth Sounds" (Oct 2024), "Chiptune Sound Design
   Tutorial" (Nov 2024), "NES Chiptune Hacking Tutorials" and "Using Claude Code for Synths"
   (Feb 2026) all ask, in near-identical phrasing, whether anyone has extracted the exact
   ADSR/oscillator settings behind a game's tones.
2. **Learn music theory by dissecting beloved scores.** Metroid, Castlevania, Kraid's Lair,
   Radiohead's *OK Computer* — treated as textbooks, with requests for chord tables, guitar
   tablature, voice-leading and bass-line breakdowns.
3. **Basic REAPER+MIDI-keyboard setup friction, every time from zero.** Three separate
   threads (Nov 2024, Feb 2025, Feb 2026) start "I just installed Reaper" and get stuck on
   device routing / ReaSynth silence, with no evidence of carried-over setup notes between
   them.
4. **Automate DAW setup with AI/NLP.** "Load a DAW with all the sounds from a particular
   game," "natural language... automating loading synthesizer programs and midi sequences" —
   recurs across "DAW Automation with NLP" (Oct 2024), "Modify MIDI Sequences" (Jan 2025),
   "AI Tool for Music Production" (Mar 2026).
5. **Atalanta Fugiens scholarship runs parallel, mostly separate.** Heavy bibliography/emblem
   work (Sept 2024) references Maier's 50 "fugues" as an early multimedia gesture and cites
   the *Furnace and Fugue* digital edition, but rarely crosses into the synth-tooling track.

## Abandoned or never-built ideas

- **"Nintendo Cover Song App"** (Oct 31 2024): pick a game/level, auto-populate a DAW with
  matching instrument tracks, import a MIDI cover, map to NES timbres, visualize the
  programming — spec'd to 40 features across two follow-ups, no project folder exists for it.
- **ROM-to-editable-synth-preset extractor**, browsable by stage/song (Oct 2024, re-asked
  Feb 2026) — adjacent to NSFRIPPER (audio extraction) but distinct (preset recovery for
  hand-tweaking), and never became code.
- **Disney "Alice in Wonderland" chiptune covers**, each song mapped to a different NES
  game's sound palette (Oct 19 2024) — one thread, never resurfaced.
- **Golden Dawn Rose Cross Lamen "music toy"**: a clickable rose/Tree-of-Life web
  controller where Sephirothic/path attributions gate synth and loop parameters, Mellotron-
  style sample pads (Feb 8 2026) — genuinely novel esoteric-synth hybrid, currently unbuilt,
  absent from SYNTHBUILDER's own prior-art table.
- **Home-grown Suno-style "vibe coded" composition aid** (Mar 8 2026): dozens of features
  ranked easy-to-hard, scoped as automating drudgery rather than generate-from-scratch —
  researched, not built.
- **Python MIDI-tampering scripts** ("Modify MIDI Sequences," Jan 5 2025) — one session,
  no follow-through.
- **Generative/algorithmic/"weird" music is essentially absent from the corpus.** No
  SuperCollider, Csound, Max/MSP, Pure Data, bytebeat, circuit-bending, modular/Eurorack,
  drone/noise, or Markov/cellular-automata music prompts turned up anywhere in 1.45M
  prompts. Every "glitch"/"ambient music"/"cellular automata" hit was a false positive
  (speedrun glitches, a physics article, an unrelated snake-game doc). This hypothesized
  thread does not exist yet — it would be new territory, not a rediscovery.

## Representative quotes

- "is it possible to analyze a Rom file and get the synth settings for the sounds or samples
  used in nes and snes chiptunes" — *Using Claude Code for Synths*, chatgpt-md, 2026-02-23
- "I want to create synthesizer sounds that exactly resemble the sounds used in my favorite
  Nintendo music. I[s] this easy to do by reverse engineering a ROM or having an AI listen to
  the soundtrack?" — *Recreating Nintendo Synth Sounds*, chatgpt, 2024-10-14
- "I want to do composition exercises like in music theory classes and have ai solve them and
  explain concepts, like how could you turn this theme into a fugue or add counterpoint to
  this melody." — *AI Music Composition MIDI*, chatgpt, 2025-01-01
- "I want to teach myself concepts like harmony voice leading and bass line construction
  through studying ok computer by radiohead" — *Studying Harmony in OK Computer*, chatgpt,
  2024-10-21
- "What if we also use the... clickable tree of life as a basis for this, where they could
  click on the spheres and the paths, and these two things could sort of both be on the
  screen at the same time, and that becomes your controller for your synthesizer and loops."
  — *Music-making website design*, chatgpt-md, 2026-02-08
- "how hard would it be to vibe code my own tool to do features similar to what suno does...
  I'm less interested in having it generate music from scratch and more interested in using
  ai tools as an aid to automating the boring or difficult stuff" — *AI Tool for Music
  Production*, chatgpt-md, 2026-03-08
- "Well, I have created a instrument. It says ReaSynth on it, but when I press my keyboard,
  I'm not seeing anything." — *Chiptune Sound Design Tutorial*, chatgpt, 2024-11-23

## Gaps between talk and build

- The REAPER+MIDI-keyboard troubleshooting loop repeats almost verbatim three times across
  15 months with no persistent notes carried forward — SYNTHBUILDER's own "Get one audible
  note before building anything else" rule reads as a direct, if implicit, answer to this
  exact recurring failure.
- "ROM to synth preset" has been asked in near-identical language at least three times
  (Oct 2024, Feb 2026) without ever becoming a script; NSFRIPPER solves the adjacent problem
  of audio extraction, not preset recovery into an editable synth.
- Bach is essentially absent from the corpus in connection with chiptune; the corpus's
  "fugue" prompts are ~95% about Maier's *Atalanta Fugiens* (the Renaissance emblem book),
  not J.S. Bach. FUGUEJUKEBOX did close that loop for Maier — it renders the *Atalanta
  Fugiens* fugues as offline square-wave audio — so that specific idea is built, just not the
  Bach half the task brief anticipated.
- Generative/algorithmic/glitch/noise music has no seed material anywhere in 1.45M prompts.
  If SYNTHBUILDER's planned `WEIRDMUSIC.md` is meant to cover that ground, it has nothing to
  mine from Ted's own prompt history — it's new territory, not an abandoned thread to revive.
- The Golden Dawn Rose Cross synth-toy concept (Feb 2026) is the single most fully-formed
  unbuilt idea in the corpus — multi-message, iteratively refined, concrete interaction
  model — but it sits in an unrelated thread ("Music-making website design"), disconnected
  from the NES/chiptune or REAPER work, so it's easy to miss without a full-corpus pass.
