---
fileClass: DesignDecision
type: design-decision
status: pending
decision_id:
bookmark: draft
roadmap_id: HD28
log_row:
supersedes:
created: 2026-11-25
tags: [decision/design, ontology/harm]
aliases: [Vocabulary Placement Decision, Narrative or Classes Decision]
---

# Design Decision: Vocabulary Placement - Narrative, OWL Classes or Mixed

## Decision or question
Where should the richness of harm-type language live: only in the SKOS vocabulary, as OWL classes and subclasses, or split between the two? **Open.** Not yet chosen.

## Options considered
- **Option A: strictly narrative.** Every harm type (council and discipline terms) is a `skos:Concept` in a discipline scheme. The OWL schema holds no harm-type classes. Harm types are labels and mappings only.
  - *Schema effect:* the question-answered axis is a property with a SKOS range.
  - *Query effect:* type questions ("all psychological determinations") need a property filter, which the reasoner does not check.
- **Option B: OWL classes and subclasses.** Harm types are `owl:Class` with subclasses, as in v1 and v2.
  - *Schema effect:* the class tree grows with each lens or sub-lens. A term that fits two lenses must sit under one parent.
  - *Query effect:* type queries are direct, and SHACL can target classes.
- **Option C: mixed.** A small set of stable reasoning axes is modelled as classes: the `HarmDetermination` subclasses by question answered (substrate and function). Narrative stays in SKOS. Determinations carry facets (`manifestsAs`, `hasModality`, `isSubstrateOf`) that point to SKOS concepts.
  - *Schema effect:* a few classes plus facet properties with SKOS ranges.
  - *Query effect:* divergence is a comparison of facets across assessments. Queries span both layers.

## Summary
*(Paraphrase.)* The schema has to reason over harm types without making lens-specific terms into ontic classes. The premise is that harm is an assessment, never an intrinsic property ([[Decisions_Log]] 2026-11-14). Option B conflicts with that premise when one event fits two lenses. Option A keeps the premise but moves all type inference outside the reasoner. Option C keeps inference on a few stable axes and keeps the narrative pluralism in SKOS.

## Rationale
- **Against Option B.** A harm type that a lens defines cannot be a fixed class without taking a side between lenses. The same event may be a harm under one standard and not under another.
- **Against Option A alone.** Competency questions that depend on class membership (for example CQ1 and CQ5 in the test note) need a reasoner-visible type. Without one, those answers depend on query conventions that nothing enforces.
- **For Option C.** It places reasoner-visible types only where the question answered is stable across lenses. Narrative and lens-specific terms stay in SKOS, where they can be mapped and graded without conflict.
- **Still unknown.** Option C's facets have not been tested on a real case. The surgeon-sued case is the test: whether a facet comparison answers "which two perspectives differ on this harm, and why, at horizon H" ([[Decisions_Log]] HD19 in the ledger).
- **Related settled rule.** An element that takes part in relations is an individual of a class, and a defined, mapped word-sense is a `skos:Concept` ([[Decisions_Log]] 2026-11-21). That rule covers individuals versus concepts, not which richness goes in which layer, so it does not decide this question.

## Consequences
- **If A:** remove harm-type classes from the schema. Express the question-answered axis as a property with a SKOS range. Rewrite class-membership competency questions as property queries.
- **If B:** keep and extend the v1/v2 class tree. Accept that lens-specific terms become classes, and check each addition against the premise.
- **If C:** keep the determination subclasses (ledger HD2). Add facet properties with SKOS ranges (HD18). Write a placement test that says which layer each term goes in (HD28 depends on it, with ledger S28).

## Open questions
- Which option? Option C is the working recommendation, not a decision.
- What rule decides whether a term is a class, a facet value or a SKOS concept? Candidate: the placement test in ledger S28.
- Should facet values be SKOS concepts, or controlled literals?
- Does the surgeon-sued case show the divergence query working under Option C (ledger HD19)?
- Should the chosen rule be written into the Governing Commitments section of v3.1?

## Original wording
> "I think narrative richness is properly assigned to the vocabulary layer but dont they need to b things in order to reason about them?"
- **Attribution:** Author
- **Source:** `copilot/copilot-conversations/agent__i_want_to_develop_a_common_schema_that_will_organize@20261124_213159.md`, 2026/11/25 00:16:10

> "i am still concerned as you point out in the cons that we lose the ability to reason over the richness unless we address it somehow in a different way. if i want to know which two perspectives differ on the assessment of harm and why at a given temporalhorizon how can we create an affordance for that?"
- **Attribution:** Author
- **Source:** same transcript, 2026/11/25 00:37:07

> "This raises a good question. what distinguishes when we use classes vs concepts - certainly the notion of ConceptualTerritory points toward concept at least for this one"
- **Attribution:** Author
- **Source:** `copilot/copilot-conversations/agent__have_any_of_our_logged_discussions_or_decisions_or_directions@20261120_092528.md` (line 1041), 2026-11-20

Quotes are verbatim. The rest of the note is paraphrase.

## External references
| Reference | Used for | Status |
|---|---|---|
| [[Decisions_Log]] 2026-11-14 (valence and premise) | Why harm types cannot be fixed classes | Logged |
| [[Decisions_Log]] 2026-11-21 (classes or concepts) | Individuals versus skos:Concept | Logged |
| SKOS (`skos:broadMatch`, `skos:related`, `skos:closeMatch`) | Bridges in Option C | W3C standard; from memory, not re-checked |

## Related
- Roadmap row: HD28
- Decisions_Log row: none (pending)
- Idea notes: [[Classes and Concepts - How Elements Are Represented]]
- Session record: [[2026-11-24 Harm Ontology Common Schema and DUL Alignment Session]]
