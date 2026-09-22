# DESIGN.md — SYNTHTOY prototype laboratory

Distilled from `sources/chatgpt_synthtoy_prototype_lab.md` (read that for
full fidelity) plus one directional addition given directly in the Claude
Code session (§5). Nothing here should be treated as historically authentic
Golden Dawn practice unless explicitly marked — see the correspondence-
status discipline in `C:\Dev\SYNTHBUILDER\RESEARCHER\MUSIC_GAME_IDEA_MAP.md`
and the caveats reproduced inline below.

---

## 1. What this is, in one paragraph

Not one game — a field of 20+ small, single-screen, single-mechanic
experiments, each turning one occult/ceremonial diagram into a musical
control surface. The player opens a prototype, understands the interaction
within a couple minutes, hears what happens, and moves on. Every prototype
must actually produce sound; none are mockups. The point of building many
small things instead of one big thing is to discover, empirically, which
diagram→interaction→sound mappings are actually fun and actually teach
something — not to decide that in advance.

**The three questions every prototype must be evaluated against** (Ted's
own framing, unchanged):
1. Is this interaction actually fun?
2. Does this make the musical concept easier to understand?
3. Does the occult structure genuinely improve the interface, or is it
   merely decoration?

## 2. The 13 prototype families

Full detail in the source file; one-line summaries here, with interaction
verb and what's explored:

| # | Family | Verb | Teaches |
|---|---|---|---|
| 1A | Tree Walker | navigate/traverse | sequencing, motif, phrase structure |
| 1B | Middle Pillar | traverse (restricted) | a musical skill-tree unlock structure |
| 1C | Tree as Scale | traverse | pitch class, interval, scale, mode |
| 1D | Tree as Rhythmic Machine | traverse | subdivision, syncopation, polyrhythm |
| 1E | Tree as Synthesizer | traverse | oscillator, filter, envelope, modulation |
| 2A | Rose Cross Sequencer | click/radial | letter→pitch, color→timbre, planet→synth param (as game mappings, not history — see §4) |
| 2B | Rose Cross Memory Game | reproduce a shown sequence | pitch/rhythm/timbre memory |
| 2C | Rose Cross Construction | assemble | structure, symmetry, correspondence |
| 3A | Magic Square Rhythm Machine | trace a grid path | rhythmic values, pattern, constraint |
| 3B | Sigil Melody | draw/type a name | letter→number→coordinate→melody |
| 3C | Sigil Synthesis | draw | geometry→cutoff/resonance/oscillator/envelope |
| 4 | LBRP / Elemental Space | navigate 4 directions | musical dimensions, cyclic composition |
| 5 | Hexagram Rituals | trace vertices | voices, pitches, timbres from geometry |
| 6 | Middle Pillar as Envelope | traverse (4 states) | ADSR, taught before the term is given |
| 7 | Filter Temple | walk through rooms | low/high/band-pass, cutoff, resonance |
| 8 | Ritual as Loop Builder | perform a repeating procedure | loop architecture from ritual repetition |
| 9 | Ritual Memory | watch → reset → reproduce | sequence/symbolic/musical memory |
| 10 | Musical Labyrinth | navigate a maze | spatial reasoning + sound engineering together |
| 11 | Ritual Automaton | drive a finite-state machine | state, transition, event, automation |
| 12 | Sound Alchemist | perform symbolic operations (SOLVE, COAGULA...) | alchemical-operation→synthesis-transform mappings (game mechanics, not historical claims) |
| 13 | NES / Low-Level Sound Engine | control raw APU-style parameters | that a synthesizer is an interacting system, not a black box |

**Interaction should follow structure, not be arbitrary:** a sigil implies
drawing; a magic square implies grids/paths; a ritual implies sequence and
space; a Tree implies traversal and topology; a Rose Cross implies radial
organization and correspondence; a synthesis puzzle implies transformation.
Do not build twenty variations on one clicking interface.

## 3. The core sound-design pedagogy

Five nested questions, asked in order, each introducing one more link in
the causal chain **waveform → amplitude envelope → filter → filter envelope
→ LFO/modulation → resulting timbre**:

1. What is the sound made of? (waveform, frequency, harmonics)
2. How does it change over time? (amplitude envelope)
3. Which frequencies pass? (filter)
4. How does the filter itself change over time? (filter envelope)
5. What makes changes repeat or move independently? (LFO/modulation)

**The core teaching trick: hear the causal relationship before being given
the vocabulary.** Don't say "increase attack" — give two paths, one
instant-onset, one swelling, ask which is the "slow awakening," and reveal
the term ATTACK only after the player solves it by ear.

**Two mechanics worth building early, in any prototype family:**
- **Freeze everything except one variable.** Lock every parameter but one
  (e.g. only resonance is live), let the player hear that parameter in
  isolation, then swap which one is frozen next. The scientific method as a
  puzzle mechanic — probably the single highest-leverage teaching device in
  the whole design.
- **Three simultaneous timescale visualization.** Show the microscopic
  waveform, the mesoscopic amplitude envelope, and the spectral filter
  curve (marked with cutoff) at once; later, add the filter envelope moving
  that curve through time; later still, remove the visualization entirely —
  the expert player hears it without seeing it.

**Quest progression, in general, across all families:** "discover what this
does" → "predict what will happen" → "deliberately construct a desired
sound." That three-stage arc is what turns experimentation into actual
musical understanding, not just button-mashing.

The full 50-quest list (organized: waveform/frequency #1–10, amplitude
envelope #11–20, filter fundamentals #21–30, filter envelope #31–40,
LFO/modulation #41–45, integrated synthesis puzzles #46–50) is preserved in
full in `sources/chatgpt_synthtoy_prototype_lab.md` — don't duplicate it
here; pull specific quests into whichever prototype is being built.

## 4. The Golden Dawn grade curriculum (capability gating)

**Historical/game-design separation, stated up front and binding:** the
grade *sequence* (Neophyte 0=0 → Zelator → Theoricus → Practicus →
Philosophus → Portal → Adeptus Minor → Adeptus Major → Adeptus Exemptus →
Magister Templi → Magus → Ipsissimus) and its elemental/planetary
attributions per grade are **(A) historically attested** — Golden Dawn
grade structure, itself adapted from the Societas Rosicruciana in Anglia's
three-orders/nine-grades Masonic-Rosicrucian system. The mapping of each
grade to a specific bundle of *musical/synthesis capabilities* is **(C)
this project's own invented curriculum** — explicitly stated as such in the
source conversation: *"the Golden Dawn grade system should be the
structural inspiration, not a claim that these musical abilities correspond
to actual Golden Dawn curriculum."*

| Grade | Historical association (A) | Musical capability unlocked (C) |
|---|---|---|
| Neophyte 0=0 | Initiation, no Sephirah | Beat grid, basic pitch/velocity/note-length, presets, delay, distortion, play/record/undo. No filters, ADSR editing, LFO, or synthesis. |
| Zelator 1=10 | Earth / Malkuth | Waveform selection, oscillator pitch/tuning, pulse width, waveform mixing, amplitude, velocity response. |
| Theoricus 2=9 | Air / Yesod / Moon | ADSR amplitude envelope, tremolo, basic LFO, tempo-synced modulation, swing, arpeggiation. |
| Practicus 3=8 | Water / Hod / Mercury | Low/high/band-pass filters, cutoff, resonance, filter envelope, envelope amount, filter LFO. |
| Philosophus 4=7 | Fire / Netzach / Venus | Complex modulation, multiple LFOs, oscillator FM, cross-modulation, velocity routing, automation. |
| Portal | Spirit, transition | Full signal-flow model exposed; reconstruct a signal chain from disconnected modules given only the target sound. |
| Adeptus Minor 5=6 | Sun / Tiphareth | Multiple oscillators/voices, polyphony, layered patches, MIDI routing, generative composition, probability. **+ song-structure/arrangement tools and loop sequencing — see §5.** |
| Adeptus Major 6=5 | Mars / Geburah | Advanced routing, audio-rate modulation, FM, ring modulation, waveshaping, feedback, conditional/probabilistic sequencing. |
| Adeptus Exemptus 7=4 | Jupiter / Chesed | Build custom instruments, define parameter mappings, design generative rules and custom sequencers. |
| Magister Templi 8=3 | Saturn / Binah | Design whole musical-symbolic worlds (new diagrams, new correspondence sets). |
| Magus 9=2 | Chokmah | Algorithmic/generative composition — design a *process*, not a melody. |
| Ipsissimus 10=1 | Kether | Move freely between sound/synthesis/signal-flow/sequence/composition/algorithm/symbolic-system; publish a new instrument. |

**Why gate this way at all:** a modern synthesizer exposes everything at
once, which is exactly what a beginner finds intimidating. Feature-gating
by grade turns "I don't understand any of this" into a legible sequence:
"I can make beats" → "I can make sounds" → "I can shape sounds through
time" → "I can shape their frequency content" → "I can make one part of the
machine control another" → "I understand the signal path" → "I can compose
with the synthesizer itself" → "I can design the system that makes the
music."

## 5. Always-on recording, marks, and song structure (added 2026-09-21)

Ted's directional instruction, given directly to Claude Code (not part of
the original ChatGPT conversation): *"everything the player is doing should
be accessible as recordings so they don't need to worry about turning a
recording off, however they can put in marks for later editing purposes and
should be given ways to play with their song structure and sequence their
loops as part of the adept grades."*

Three distinct requirements, worth keeping separate:

**(a) Always-on recording, no manual start/stop.** Every prototype should
capture the player's session as a recording by default — no record button
to remember to press, no risk of losing a good take because recording
wasn't on. This is a platform-level mechanic, not grade-gated: it applies
from Neophyte onward, since the Neophyte's very first four-beat loop is
exactly the kind of thing worth not losing.

**(b) Marks for later editing.** The player can drop a marker at any point
during play — a lightweight, always-available action (distinct from the
heavier editing capabilities gated by grade) that flags a moment in the
recording as worth returning to. Marks are metadata on the always-on
recording stream, not an edit in themselves; actually *acting* on a mark
(cutting, rearranging, layering) is arrangement-level work and belongs to
the capability tier below.

**(c) Song-structure / loop-sequencing tools, gated to the Adept grades.**
Playing with arrangement — sequencing multiple recorded loops into a larger
song structure — is introduced starting at **Adeptus Minor (5=6)**, folded
into that grade's existing "composition and synthesis become one system"
capability bundle (§4's table has been updated to say so directly). This
fits the grade's own described character in the source conversation
("Adeptus Minor... the player now has access to almost the entire basic
synthesizer... a patch and a composition are not separate things") — song
structure is the composition side of that same threshold, arriving at the
same grade as multi-voice/polyphonic capability rather than before it.
Adeptus Major and above should be able to sequence with more computational
control (conditional/probabilistic arrangement, per that grade's existing
"complex sequencing, conditional events, probability systems" entry).

**Design question left open, not yet decided:** whether "always recording"
means an unbounded session-length buffer (simplest, but has real storage
implications for longer sessions) or a rolling window with marks anchoring
what gets kept past a certain age. Flag this for whoever plays DESIGNER
next on the first prototype that actually needs persistent recording (most
of the early Neophyte/Zelator-tier prototypes are short enough that it
likely doesn't matter yet).

## 6. Anti-creep discipline for this specific project

Twenty-plus prototype families is a large surface by design — that's the
point, it's a laboratory. The discipline that keeps it from becoming
infrastructure-before-verification (this workspace's most repeated failure
mode, per `SYNTHBUILDER/CLAUDE.md`'s whole reason for existing) is: **one
prototype confirmed playable and audible before the next one starts, and
the shared gallery/data-model framework built only after at least two or
three individual prototypes already work independently** — building the
"cross-prototype data model" (§ in the source conversation) before any
single prototype proves the underlying interaction is fun would be
repeating the exact mistake this whole project family already learned from.
