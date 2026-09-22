# TOOLKIT.md — Narrative-design frameworks for SYNTHBUILDING

Distilled from the 7 books at `E:\pdf\narrative design\`, read via table of contents plus the
chapters covering dramatic structure, spatial/environmental storytelling, interface-as-narrative,
and instructional narrative (per the brief). Not a book report — a working reference for
`PROJECT_NARRATIVE_SUGGESTIONS.md`. Each entry: **framework name** — book, chapter/concept —
one sentence on how it applies to presenting a real, unfictionalized software project on this
catalog site.

Coverage note: substantive, chapter-level material came from all 7 books. Fox's *Game Interface
Design* is the thinnest of the seven — it has no bookmarked outline (2005, pre-PDF-tagging), and
its printed page numbers don't map 1:1 to PDF physical pages, so the deep-dive chapter (13,
"Designing the HUD") wasn't reachable in this pass; what's cited below comes from its table of
contents (chapter/concept names are real and citable) plus its Chapter 1–2 production text that
was reached. Treat Fox's entries as directionally right but less textually grounded than the other
six.

---

## 1. Dramatic structure (the shape of a story over time)

**Three-Act Structure with named beats** — Ross Berger, *Dramatic Storytelling & Narrative
Design*, Ch.6 "Structure" (Inciting Incident → Refuse/Accept the Call → Point of No Return →
Escalating Burdens → Exposure of Weakness → Midpoint/Low Point → Ticking Time Bomb →
Obligatory Scene/Climax → Reversal → Recognition → Denouement).
→ Gives a vocabulary for *where in the story* a stalled project actually is — "stalled at the
Obligatory Scene" (a decision not yet faced) reads completely differently from "stalled at
Escalating Burdens" (still mid-fight), and the site can say which.

**Freytag's dramatic arc (Pyramid)** — Tricia Austin, *Narrative Environments and Experience
Design*, Ch.5 "Story Telling," citing Freytag (1900): exposition → rising action → climax →
falling action → denouement.
→ The simplest shared vocabulary for a `page_summary` rewrite: name which of the five phases a
project's *current, real* state sits in, rather than describing it as a flat list of facts.

**Dramatic Escalation Warnings** — Berger, Ch.6, "Dramatic Escalation Warnings" (Premature
Character Introduction, Long Missions with No Narrative Interspersed, Arbitrary Bells and
Whistles).
→ A checklist for what makes a project write-up *boring* even when the underlying work is
good — e.g. dumping all 40 architecture rules in one paragraph is "long mission with no
narrative interspersed."

**Plot vs. Story** — Michael Breault, *Narrative Design: The Craft of Writing for Games*, Ch.3
"Story in Games."
→ A catalog entry that lists dates, file counts and commit history is *plot*; naming the specific
moment a person had to make a call and didn't (or did) is *story* — the rewrite target for most
`card_summary` fields here.

**Dramatic Conflict as the engine of story / Greimas' actantial model** — Austin, Ch.3 "Dramatic
Conflict," citing Robert McKee's "Law of Conflict" and A.J. Greimas' three contrary pairs
(sender↔receiver, subject↔object, helper↔opponent).
→ Names the antagonist honestly: for a solo technical project the "opponent" is usually a bug, an
unmade decision, or a missing git remote, never an invented villain — exactly the brief's
"villain is the JSFX pin-declaration bug" instruction, given a formal handle.

---

## 2. Spatial / environmental storytelling (relevant because the site is built as project "rooms")

**Storyshapes: linear vs. non-linear spatial typologies** — Austin, Ch.5 "Story Telling," citing
Duncan McCauley and Tim Gardom Associates: linear (prescribed route, pulsed flow, there-and-back,
inner sanctum) vs. non-linear (hub-and-spokes, matrix, islands).
→ SYNTHBUILDING's own catalog is already a **hub-and-spokes / islands** structure (15 independent
project pages off one landing page, no forced order) — worth naming this explicitly in site copy,
and using "there-and-back" (see an object at entry, re-see it changed at exit) as a specific
technique for a project whose ending recontextualizes its opening claim (FUGUEJUKEBOX's "LIVE ON
THE WEB!" claim vs. the verified 404 is a textbook there-and-back reveal).

**Emotional mapping** — Austin, Ch.5, citing Duncan McCauley's practice of plotting time/sequence
against felt intensity to find where a designed experience sags or peaks.
→ A cheap diagnostic for `page_summary` copy: does the paragraph rise toward the real turning
point (the stuck decision, the verified fact) or just list facts at a flat register throughout?

**Dramatic conflict research applied to placemaking / exhibition-making** — Austin, Ch.3,
"Dramatic Conflicts and Story Dynamics in Exhibition Making" (Their Mortal Remains / V&A case
study: a linear U-shaped gallery whose halfway turn had to be written into the storyline).
→ Each project card is a small "room"; the same discipline applies — what's the one physical/
structural fact of *this* room (a file that doesn't exist, a folder that's a duplicate, a decision
log with one open item) that the copy should be built around, the way an exhibition designer
builds around a gallery's actual turn?

**The "core attraction" / dramatic reveal device** — Austin, Ch.5, citing Christian Mikunda's
commercial-space design vocabulary (landmarks, core attractions, cognitive dissonance released
through a spectacular moment).
→ Every project write-up should have one concrete, quotable "core attraction" — a specific
sentence, number, or artifact (a literal blunder, a specific file count, an exact quote from the
project's own docs) placed where a reader's attention peaks, not buried mid-paragraph.

---

## 3. How games teach without exposition (interface/interaction as narrative)

**Telling Stories Without Writing / environmental storytelling** — Breault, Ch.3 "Story in
Games," the burned-village example: players read scorch marks and ivy rather than being told
"a dragon attacked five years ago."
→ Directly reusable maxim for this site: a project's `page_summary` should let verified facts
(a `.gitignore` with no commits behind it, two finished MP4s next to 117 unrendered ones) imply
the story rather than stating a verdict — the site's own "reportorial density, no marketing"
house style already does this; the toolkit just names the technique so it can be applied
deliberately.

**Narrative Design = story delivery across every available channel** — Tobias Heussner et al.,
*The Game Narrative Toolbox*, Ch.1 "What Is Narrative Design?" (Toiya Kristen Finley: "narrative
design = story delivery... across all parts of the game... UI, or music and sound design").
→ On a catalog site, "the interface" is the card grid, the status badges, and the theme tags —
these are as much narrative-delivery surfaces as the prose, so a `status: ACTIVE, stalled since
2026-04-20` badge is already doing environmental storytelling and shouldn't be redundantly
re-explained in the paragraph beneath it.

**Player Agency and Meaningful Choice** — Heussner et al., Ch.5 "Story" ("Player Agency,"
"Meaningful Choices," "Moral Agency").
→ Where a project's real story is an *unmade decision* (NSFRIPPER's A/B/C, most obviously), the
site can let the *visitor* make the same choice the developer hasn't — turning a stalled decision
into literal interactive agency instead of just reporting it as a stuck status.

**Linear / Branching / Open narrative structures** — Heussner et al., Ch.5.
→ A vocabulary for picking the right shape per project: GlitchMario's story is linear and
finished (tell it straight); NSFRIPPER's is branching and paused mid-fork (show the fork); the
whole 15-project catalog is open/non-linear (no required reading order).

**Screen space / HUD information hierarchy** — Brent Fox, *Game Interface Design*, Ch.13
"Designing the HUD" (Screen Space, In-Game Information, Legibility, Standard vs. Non-Standard
Elements — concept names from the book's table of contents; full chapter text not reached this
pass, see coverage note above).
→ A project card is a HUD: it has to communicate status (ACTIVE/STABLE/ARCHIVED/SCRATCH/STUB),
confidence, and one hook fact at a glance, the same discipline a game HUD applies to health/ammo/
objective — legibility at a glance outranks completeness of detail on the card level.

**Menu flow as a planning discipline** — Fox, Ch.2 "Planning Menu Flow" (chapter/concept names
from TOC; the reached Ch.1 text establishes the book's premise that interface is never an
afterthought).
→ The order in which a visitor can move between the 15 project rooms (via theme tags: nsfripper-
family, atalanta, bach, other) is itself a narrative decision, not just an information-architecture
one — which project a reader hits first inside a theme colors how they read the rest.

---

## 4. How instructional design uses narrative (real, non-fictional professional material)

**Case-Based Reasoning (CBR) / "Stories as Decision Scaffolds"** — Hokanson, Clinton & Kaminski
(eds.), *Educational Technology and Narrative*, ch. by Andrew Tawfik, Matthew Schmidt & Fortunata
Msilu, "Stories as Decision Scaffolds: Understanding Nonlinear Storytelling Using Case-Based
Reasoning and Educational Design Research."
→ The exact model for this whole workspace's habit of writing `BLOOPERS.md`/`AVOIDBLUNDERS.md`:
a case library of narrativized problem/solution pairs that later projects retrieve and reuse —
worth naming explicitly on the site, since SYNTHBUILDER's own CLAUDE.md ("Prior Art In This
Workspace") already *is* a CBR case library in practice.

**Precedent as a narrative practice in design learning** — Hokanson et al., ch. "Use of Precedent
as a Narrative Practice in Design Learning" (precedent = knowledge of prior design solutions,
narrativized, used to generate new design moves).
→ Names why ReapNES-Studio's "archived" status is not a failure story: it is precedent — its
solved MIDI-keyboard-routing and DC-offset problems are exactly the kind of narrativized
precedent this framework describes, inherited whole into NSFRIPPER and SYNTHBUILDER's own
CLAUDE.md rules.

**Narrative qualities of design argumentation** — Hokanson et al., ch. "Narrative Qualities of
Design Argumentation" (a design presentation's rationale, distilled from its process, functions as
a narrative argument for why a solution is appropriate).
→ A `stuck_or_next` field is a design argument in miniature — it should read as a claim with
evidence ("the A/B/C ear-test is the single blocking decision — here's why"), not a status label.

**The Spirit of Storytelling / sender-receiver connection** — Hokanson et al., ch. "The Spirit of
Storytelling" (Stephen Peters): storytelling's value is the "memorable, enlivening connection...
between sender and receiver," independent of delivery technology.
→ A caution against over-mechanizing this whole exercise: applying frameworks should sharpen a
true story's shape, not dress up a status report — the same discipline this book applies to
technology-vs-oral-storytelling applies to structure-vs-decoration here.

**Backward Design / SMART goal-setting for teaching craft** — Breault, Ch.12 "Teaching Narrative
Design and Game Design" (start from the end result, work backward; Specific/Measurable/
Achievable/Relevant/Timely).
→ Useful in reverse for triage: for each project, name the *end state* implied by its
`stuck_or_next` field (a decision logged, a git remote created, a render pass finished) and let
that end state determine how much narrative weight the write-up gives it — small end states don't
need three-act treatment.

---

## Quick-reference: which framework for which project shape

| Real project shape (from the catalog) | Reach for |
|---|---|
| Built a working thing, then stalled on one unmade decision | Three-Act Structure (Berger) — name the exact beat it's stuck at; Player Agency (Heussner) — let the visitor make the choice |
| Shipped clean, complete, no real conflict | Say so plainly (per brief) — at most Freytag's arc as a one-line label, no forced villain |
| Real work, no git history, at risk | Dramatic Conflict/Greimas (Austin) — the antagonist is data loss, not a person; lead with the risk |
| Looks more complete than it is (stale build, inflated count) | "There and back" storyshape (Austin/McCauley) — state the big number, then the reveal |
| Archived/superseded but genuinely solved something | Precedent as Narrative Practice (Hokanson et al.) — frame as case-library contribution, not failure |
| Ambiguous identity / possible duplicate of another project | Greimas' sender/receiver + Case-Based Reasoning framing — pose it as an open question, not a verdict |
