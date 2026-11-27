---
type: session
status: closed-for-chat
workstream: Harm Ontology
created: 2026-11-20
source: "copilot/copilot-conversations/agent__have_any_of_our_logged_discussions_or_decisions_or_directions@20261120_092528.md"
continued_in: "[[Handoff - Harm Ontology]]"
harvested_through: "2026-11-20 (end of long chat)"
---

# 2026-11-20 Harm Ontology: sample review and methodology

## Summary
- Began by asking whether the v3 structure had changed since the 2026-11-15 draft. Found decisions from 2026-11-17 and 2026-11-18 (Perspective split, CausalCandidate, FactorAssembly, AffectedEntity rename). See [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)]].
- Reviewed the draft line by line. Revised it as a new note. The original stays unchanged.
- Asked about Boxes A to D. They are the same in both versions. Box D was added on 2026-11-17.
- Examined the three-layer and editor-first mini samples in Protégé. Found that the same local name is used for three elements, that narrative placement differs between samples, and that no written rule decides placement.
- Concluded that the samples cannot yet test the three-layer strategy fairly, because the implementation methodology is undefined. Proposed a methodology review (see the handoff note).
- Clarified the hub and spoke pattern (see [[HO-II.d.3 Hub and Spoke Pattern]]).

## Decisions made
None logged. All items are proposals. See [[Decisions_Log]] for the current logged state.

## How the thinking moved
- Started with "what changed since v3 draft?" and ended with "the samples expose an unfinished methodology."
- The three-layer decision (2026-11-17) is logged, but the separate-file layout is not. The schema-layer rename from "ontology" to "schema" was proposed on 2026-11-18 and is not logged.
- The hub was first described as organizing narratives about one concept, then corrected. The concept carries the narrative. The collection is a scheme.

## Concepts introduced (flagged for idea notes)
- Hub and spoke pattern: [[HO-II.d.3 Hub and Spoke Pattern]] (proposed bookmark)
- Methodology rules 1 to 7 (identity, scheme, layer, narrative, mapping, check, test): in [[Handoff - Harm Ontology Methodology Re-evaluation]]

## Open questions
- Is the Integral vocabulary a discipline scheme or a tradition scheme?
- Where does `psy:moralStages` belong?
- Should the scheme `hov:hubs` be renamed, or should each idea become its own scheme?
- Where should hub narrative live?
- Which of the two `developmentalAltitude` elements should carry the label, and how should the untyped `rdf:Description` be handled?

## Corrections made during the chat
- An earlier claim that a misplaced item existed was not located. Unresolved.
- An earlier claim that the `.owl` and `.ttl` copies differ was not verified. Only the untyped `rdf:Description` was observed, in `.owl`.
- Editor-first uses `ho:`; `hov:` belongs to the three-layer sample.
- A proposal to rename the scheme `hov:hubs` was made in error, and the naming was described poorly. The scheme organizes concepts. The concepts do not organize schemes.

## Artifacts touched
- Created: [[HO-II.d.3 Hub and Spoke Pattern]] (stub, proposed)
- Created: [[Handoff - Harm Ontology Methodology Re-evaluation]] (proposed)
- Created: [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)]] (revised draft; original unchanged)
- Created: this session note
- No changes to samples, [[Decisions_Log]], or the bookmark index

## Follow-ups
- Confirm or adjust the proposed bookmark HO-II.d.3 and add it to [[_Harm Ontology Bookmark Index]] (not yet done; needs approval).
- Start a new chat with the handoff note and the rev 2026-11-20 draft attached.
- Draft the one-page methodology note (rules 1 to 7), marked proposed.

## Original wording
- Author: "we need to jump up a level and propose a ruleset or methodology specification for properly categorizing and associating vocabulary elements consistently that prevents things that have unique IRI but non unique human readable names and labels."
- Author: "i am still confused. perhaps we can jump up a level."
