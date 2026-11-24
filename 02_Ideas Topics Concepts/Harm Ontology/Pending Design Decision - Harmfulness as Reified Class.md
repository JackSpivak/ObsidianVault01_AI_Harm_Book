---
fileClass: Idea
type: design-decision
status: pending
bookmark: draft
canonical_id: ho-pending-decision-harmfulness-reified
tags: [ontology/harm, decision/pending, harmfulness, assessed-imagined-harm]
aliases: [Pending Decision - Harmfulness, Harmfulness Reification Decision]
created: 2026-11-23
updated: 2026-11-23
---

# Pending Design Decision: Harmfulness as a Reified Class

*A pending design decision is not yet an accepted commitment. It records the options, the arguments for each, and the question that must be answered before the decision is logged in [[Decisions_Log]]. Source: [[Harm Ontology v3 Design Notes - Harmfulness, Imagined Harm and Causal Chains]], Sections 4 and 5.*

## Decision to be made
What is the status of `Harmfulness` in the ontology, and how does it relate to `AssessedHarmfulness` and `AssessedHarm`?

## Status
**Pending.** The author has not confirmed a choice. Ontological Commitment 02 (relational emergence of harmfulness) was proposed in the chat and then withheld for further discussion.

## Options

**Option A: Reified Harmfulness as a class (subclass route).**
- `AssessedHarmfulness` is a subclass of `Harmfulness`, as the author first suggested.
- `Harmfulness` is a class with properties `hasAssessor`, `hasObjectiveStandard`, `hasHarmfulnessCriterion`.
- For: keeps a single class for the concept while letting assessments carry the epistemic detail.
- Against: the author observed that "Harmfulness" as an objective, unassessed property has no observable instance. A parent class with no unassessed instances may be a ghost entity.

**Option B: Drop ontic Harmfulness; make AssessedHarmfulness first-class.**
- Physical objects and actors have capabilities only. Every harm-related judgment is an instance of `AssessedHarmfulness`.
- For: removes the view from nowhere. Every instance is traceable to an assessor, a mechanism and a criterion.
- Against: loses a shared parent term for cases where the concept is used loosely.

## Arguments raised in the session
- A storm is classed as harmful only through a mechanism model (for example, sea temperature driving intensification). If the sensor data is skewed, the classification is an assessment error, not a fact about the storm.
- The gun-rights argument turns on whether harm is intrinsic to the object or relational. Capability is intrinsic. Harm depends on the actor, the mechanism and the criteria.
- `AssessedHarm` should refer only to past or present harm. Future-oriented judgments need `AssessedImaginedHarm` (see the design notes, Sections 1 to 3).

## Question that decides it
Does any useful reasoning require an unassessed harmfulness? If yes, Option A. If every harmfulness judgment can be traced to an assessor, Option B.

## Linked decisions
- Ontological Commitment 01 (modular TBox, shared ABox). Proposed, not yet logged.
- Temporal split of AssessedHarm (past or present only). Proposed, not yet logged.
- Grounding requirement for AssessedImaginedHarm. Proposed, not yet logged.

## Next step
Author decides between Option A and Option B. Once decided, record the choice in [[Decisions_Log]] and update the design notes.
