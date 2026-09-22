# PROJECT_NARRATIVE_SUGGESTIONS.md — toolkit applied to the 15 SYNTHBUILDING projects

Applies `TOOLKIT.md` to each project in `db/seed_projects.json` (15 entries). Per project: (a) a
one-line narrative-structure read of its *real* arc, (b) one concrete copy-edit suggestion
specific enough to apply directly to `card_summary`/`page_summary`, (c) exactly one gamification
idea, labeled GAMIFICATION-COPY (free, in-text framing) or GAMIFICATION-BUILD (a real
small/medium/large side-build, sized honestly).

This is proposal-only. Nothing here edits `db/seed_projects.json`, `site/`, or any other file —
applying any of it is a separate, deliberate follow-up per this role's CLAUDE.md.

---

## nsfripper

**Arc:** Three-act structure, complete through Act 2 — every escalating technical burden (fidelity
hierarchy, oracle DB, ROM-trace validation) got resolved — then frozen exactly at the threshold of
Act 3's Obligatory Scene: the A/B/C ear-test *is* the climax, and it was never played.

**Copy suggestion:** Open `page_summary` with the cliffhanger instead of burying it in the fourth
paragraph: lead with "Three finished variants have sat untested since April 2026" and only then
walk back through the 40-rule architecture that produced them. Right now the copy front-loads
infrastructure (plot) and saves the actual unresolved decision (story) for last, exactly inverted
from where Berger's Act-3 beats say the weight should sit.

**Gamification — GAMIFICATION-BUILD (small):** Embed the three actual variant audio renders (or
short clips of them) as an inline "cast your vote: A, B, or C" widget on the project page — three
players/buttons, no scoring needed. The content already exists (Variant A/B stems + JSFX render
projects); this only needs a simple audio-picker UI, and it turns the site into the literal
listening session the project itself is waiting on.

---

## reapnes-studio

**Arc:** Not a failure story — a precedent story. It fought and *won* its two hardest fights (MIDI
keyboard routing, DC-offset), documented both as institutional memory (14 blunders in
`BLOOPERS.md`), then was retired because its solutions got inherited whole into NSFRIPPER and this
workspace's own CLAUDE.md rules. Its "ARCHIVED" status is a graduation, not a stall.

**Copy suggestion:** Reframe the opening of `page_summary` away from "REAPER-based NES 2A03 synth
that... was folded into NSFRIPPER" (reads as absorption/obsolescence) toward "Every hard-won JSFX
rule this workspace uses today traces back to a blunder first logged here" — precedent framing
(Hokanson et al.) rather than status framing.

**Gamification — GAMIFICATION-BUILD (medium):** A "Blunder Bestiary" flip-card interactive: 14
cards (one per BLOOPERS.md entry), front shows the symptom as the developer experienced it
("noise channel produces alien transmissions"), back reveals the root cause ("`^` is POWER not
XOR in JSFX"). Medium effort — needs the 14 blunders transcribed into structured data plus a
flip-card component — but it's a direct, honest demonstration of the site's own "recover
symbolism from behavior" gate: a reader has to guess the cause before flipping.

---

## nesjamtools

**Arc:** Genuinely undramatic and nearly done — every logged complaint in its own bug tracker
(`output.md`) is marked Fixed except one, which is explicitly waiting on an ear-test. This is a
punch list almost cleared, not a stalled project with an unmade decision to dramatize.

**Copy suggestion:** Say the undramatic thing plainly, per the brief's carve-out: rewrite the
`stuck_or_next` sentence as a literal tally ("5 of 6 logged issues fixed; 1 open, pending your
ears") rather than reaching for a structural beat that isn't really there.

**Gamification — GAMIFICATION-COPY:** Frame it in one line as "the last bug standing" — no build
needed; the honesty of "everything else got fixed" is the interesting fact, not a device layered
on top of it.

---

## glitchmario

**Arc:** Already narratively complete on its own terms — it *is* Freytag's five-part arc, built
deliberately as a five-day documentary timeline (100 events, 17 blunders, 30 milestones) that
ends at "80% fidelity and climbing." Nothing here needs restructuring; the brief's "shipped
clean, no real conflict to invent" applies, except the conflict is already fully told, just
by the source project itself.

**Copy suggestion:** SYNTHBUILDING's own `card_summary` currently paraphrases GlitchMario's
content in flat reportorial style. Pull one of its own blunders as a direct quote/pull-quote
instead of a paraphrase — Austin's "core attraction" device — e.g. lead with the literal fact that
`^` meaning exponentiation, not XOR, made the noise channel produce "alien transmissions" (the
project's own words), then summarize the rest.

**Gamification — GAMIFICATION-COPY:** Label the existing blunder list on the linked site as "17
blunders, ranked" in SYNTHBUILDING's copy — a framing device pointing at content that already
exists there, not something new to build here.

---

## nesmusicstudio

**Arc:** A doppelgänger mystery, unresolved — real, verified progress (Castlevania 1 complete,
Contra at 96.6%) sits inside an identity question: is this the same lineage as NSFRIPPER under a
different name, continued after NSFRIPPER's last commit? A hardcoded path inside NSFRIPPER's own
scripts points at this project's folder, which is the one hard clue. This is Greimas'
sender/receiver axis (the hardcoded path is the "sender," Ted is the "receiver" of an unresolved
message) more than a hero's-journey arc.

**Copy suggestion:** Reframe `page_summary`'s opening away from a features list toward the actual
open question: "A hardcoded path in NSFRIPPER's own code points here — is this project NSFRIPPER's
true successor, or a parallel line?" — state the mystery as the hook, then give the verified
progress numbers as evidence toward resolving it.

**Gamification — GAMIFICATION-BUILD (small-medium):** A side-by-side "spot the difference"
comparison widget: NSFRIPPER vs. NESMusicStudio, columns for git activity, live URL, track
completion — literally the comparison table this research pass already produced, republished as
an interactive toggle instead of static prose. Small-medium because the data already exists; only
the compare UI is new.

---

## reaperbeyondnes

**Arc:** A hero of real accomplishment standing without armor — heavily structured, substantial,
multi-system extraction work (GBA/SMS/Saturn/Genesis/SNES/GBC/Virtual Boy) that exists in exactly
one uncommitted copy on one disk. The dramatic conflict here (per Austin/Greimas) is not creative,
it's existential: the antagonist is data loss, and it's still an open threat.

**Copy suggestion:** Reorder `card_summary` so the risk sentence leads instead of trails: currently
it opens with scope ("declared successor... GBA, SMS, Saturn...") and only reaches "not a git
repository" at the end. Lead with the risk — that's the actual dramatic conflict — then list scope
as what's at stake.

**Gamification — GAMIFICATION-COPY:** A one-line "one uncommitted step from oblivion" framing
device in the card. No build proposed — a countdown/urgency widget would be decorative pressure on
a real, unresolved risk, which cuts against the brief's anti-embellishment rule; the honest move
here is copy emphasis, not a game layered over someone's actual data-loss exposure.

---

## nes-music-lab

**Arc:** An identity-orphan, not a failure — real research code (Castlevania trace analysis,
MIDI export) sitting stalled and uncommitted, with a genuinely open question about whether it's
superseded, parallel, or complementary to NSFRIPPER's own Castlevania work. Lowest-confidence
entry in the catalog; the honest story is "unresolved case file," not a dramatized struggle.

**Copy suggestion:** State the open question directly in `card_summary` rather than implying
completeness through a features description: "Is this the same Castlevania work NSFRIPPER later
redid, or a separate line worth reconciling? Unconfirmed."

**Gamification — GAMIFICATION-COPY:** "Unsolved case file" framing, one line, matching its LOW
confidence rating. No build — investing build effort in a project whose own status is unverified
would misrepresent how settled the underlying work is.

---

## arpeggiator-composer

**Arc:** The unopened envelope — a properly structured small software project (core/jsfx/
reascript/reaper_projects/tests) that has its own verification tool sitting right there, unused.
The irony is structural: the project contains the means to resolve its own uncertainty and hasn't
used it.

**Copy suggestion:** Make that irony the hook line instead of a throwaway detail: "It has a
`tests/` folder. Nobody has run it yet" as the opening of `page_summary`, ahead of the description
of its project structure.

**Gamification — GAMIFICATION-BUILD (small):** Actually running `tests/` once and displaying the
honest pass/fail result as a status badge on the card is a real, small, truthful build — not a
"game," but it directly resolves the one open narrative question the copy suggestion above raises,
which is more valuable here than an invented framing device.

---

## chipscribe

**Arc:** A ghost story, literally — a live, functioning deployed site (t3dy.github.io/ChipTools/)
with no local body anywhere on disk. The Greimas sender/receiver relationship is inverted from
every other entry: there's no visible author-side artifact left to narrate, only the effect.

**Copy suggestion:** Lean into the true ghost framing rather than writing around the absence:
"ChipScribe has no home on this machine — it exists only because a server somewhere still
remembers it," ahead of the functional description.

**Gamification — GAMIFICATION-COPY:** "The ghost in the machine" one-liner. No build possible or
appropriate — there is no local source to build anything against, and cloning it down (per its own
`stuck_or_next`) is a prerequisite to any future work, not a gamification opportunity.

---

## fuguejukebox

**Arc:** Dramatic irony, textbook case — the music half is genuinely, verifiably complete (500/500
MP3s and WAVs on disk), while the project's own README confidently declares "LIVE ON THE WEB!"
about a site that returns HTTP 404. The story is the gap between the project's self-report and the
verified fact.

**Copy suggestion:** Use Austin's "there-and-back" storyshape directly in the copy: quote the
README's own "LIVE ON THE WEB!" line first, then immediately follow with the verified 404 result,
letting the contradiction carry the narrative weight instead of stating "the site is broken" as a
flat verdict.

**Gamification — GAMIFICATION-BUILD (small):** An embedded "fix-it checklist" widget on the page
mirroring the three already-documented repair steps (pick canonical MP3 copy, get audio into a
servable path, redeploy to Pages) as checkable list items — small, because the fix plan is already
fully specified in `stuck_or_next`; this only turns it into an interactive artifact instead of
prose.

---

## emblemsin3d-fugues

**Arc:** A clean, mostly-finished success with one explicit, documented non-goal — the standalone
jukebox was deliberately never ported to GitHub Pages (an absolute-path dependency, called out by
the project's own deploy notes as intentional). Per the brief, this should be stated plainly rather
than dramatized as a stall, since it would otherwise read like its stuck siblings.

**Copy suggestion:** Make the "by design, not neglect" distinction its own sentence, early, so it
doesn't blur into the catalog's many genuinely-stalled entries: "The standalone jukebox was never
ported to Pages on purpose, not because work stopped" — currently this nuance is present but
buried near the end of `page_summary`.

**Gamification — GAMIFICATION-BUILD (small):** A "palette roulette" micro-interaction: since the
ten NES game-palettes and the engine already exist, add a button on the card that randomizes which
of the ten palette names (Mario, Zelda, Metroid, Castlevania, Contra, Final Fantasy, Kirby, Bubble
Bobble, Bionic Commando, Wizards & Warriors) is quoted in the card text on reload — small, since it
reuses existing data and needs only a tiny bit of client-side JS.

---

## antigravfugiens

**Arc:** Buried treasure — the richest, weirdest content in the entire NES-music cluster
(alchemically-named studio effects, six deliberately strange interactive toys) with zero audience,
not because it failed but because it was never linked from anywhere. Unlike most entries here, the
conflict isn't an unmade decision — it's pure distribution neglect of genuinely good material.

**Copy suggestion:** The six toy names (Levitating Athanor, Ouroboric Dub, Dewpoint Runner, Sword/
Egg Breakbeat, Rose-Garden Lockstep, Sublimation Pinball) are currently a flat list mid-paragraph
in `page_summary`; promote them into the `card_summary` itself as the hook — they're better copy
than anything else describing this project.

**Gamification — GAMIFICATION-BUILD (small):** Literally embed one of the six existing toys
(Sublimation Pinball is the most self-explanatory) directly on the SYNTHBUILDING project page via
iframe/link-through — the smallest possible build, since the interactive content already exists
and just needs surfacing rather than being invented.

---

## antigravemblemsin3d

**Arc:** Genuinely not a music project — its chiptune files are unmodified passengers in a sandbox
built for unrelated visual/game-design experiments. Per the brief's carve-out, this should be
stated plainly rather than stretched into a music narrative it doesn't have. Its one real hook is a
single orphaned idea (fugue/orbit synchronization) that was proposed in the project's own notes and
never implemented.

**Copy suggestion:** Shrink and re-center `card_summary` around the honest fact ("the chiptune
files here are unchanged copies, along for the ride — this is not a music project") rather than
implying music relevance by proximity to EMBLEMSIN3D's name.

**Gamification — GAMIFICATION-COPY:** A single line naming the orphaned idea — "an idea filed and
forgotten: syncing the fugues to orbital motion, never built." No build proposed; this project's
low confidence and off-topic status make further investment premature.

---

## chippedonbach

**Arc:** The hard climb is over; only the final button-push remains — 117 Bach × game-palette
projects were generated (the expensive, creative step), but most were never rendered to WAV,
apparently interrupted by a crash. Two finished preview videos prove the concept works end to end;
the rest is unlit.

**Copy suggestion:** Open with the number as a pull-quote rather than mid-paragraph: "117 fireworks
built. Two lit." ahead of the technical description of the pairing/rendering pipeline — Austin's
"core attraction" placement, moving the single most quotable fact to where attention peaks.

**Gamification — GAMIFICATION-BUILD (small):** A literal progress-counter widget on the card:
"2 of 117 rendered" with the two finished MP4s embedded as proof, so a visitor sees the actual gap
rather than reading about it. Small — it's a static stat display plus two existing video embeds, no
new engineering against the render backlog itself.

---

## bachstudies

**Arc:** A scale illusion — 13,815 HTML pages suggest a finished reference work; only 12 are real,
reviewed entries, the rest are stale stub output from an abandoned corpus pass that no longer
matches the reseeded database. The dramatic conflict is precisely "looks done, isn't," which is an
environmental-storytelling failure (the space itself overstates its own contents).

**Copy suggestion:** Use Austin's "there and back" reveal structure directly: state the big number
first ("13,815 pages"), then the correction immediately after ("12 are real; the rest are leftover
stubs") — the same "sugar looks harmless on the way in, understood differently on the way out"
device Austin cites from exhibition design, applied to a stale build instead of a museum object.

**Gamification — GAMIFICATION-COPY:** "13,803 ghost pages" as the one-line framing device. No build
proposed — pruning stale output is housekeeping, not a gamification opportunity, and inventing an
interactive layer over a known-broken build would misrepresent its actual state.

---

## Summary of gamification ideas by type

**GAMIFICATION-BUILD proposed** (7 of 15): nsfripper (small — A/B/C audio picker), reapnes-studio
(medium — blunder bestiary flip-cards), nesmusicstudio (small-medium — comparison widget),
arpeggiator-composer (small — run tests, show real badge), fuguejukebox (small — fix-it checklist),
emblemsin3d-fugues (small — palette roulette), antigravfugiens (small — embed existing toy),
chippedonbach (small — render-progress counter).

**GAMIFICATION-COPY only** (8 of 15): nesjamtools, glitchmario, reaperbeyondnes, nes-music-lab,
chipscribe, antigravemblemsin3d, bachstudies, and (implicitly, as the "no forced gamification"
case) glitchmario's pull-quote treatment.

No project received a "large" build estimate — the catalog's real stories are mostly small,
specific unresolved facts (a fork, a missing test run, a stale build), and the honest-sized
gamification response to a small fact is a small build, not an invented large one.
