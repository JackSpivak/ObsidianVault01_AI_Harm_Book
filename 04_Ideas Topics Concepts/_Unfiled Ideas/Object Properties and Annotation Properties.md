---
fileClass: Idea
type: idea
status: stub
bookmark: draft
canonical_id:
territory: new
tags:
  - ontology/modelling
  - ontology/properties
aliases:
  - Object vs annotation properties
created: 2026-11-27
---

# Object Properties and Annotation Properties

## Why this is distinct
- It is a modelling decision. Object properties link one thing to another (a harm has a victim), while annotation properties attach information that does not affect the logic (a note about certainty or source). The author wants this split made explicit in the harm ontology.

## Anticipated direction
- Mark every property as object or annotation.
- Keep assessment values (for example, a severity judgment) as annotations unless they change the inferences the ontology makes, and check that rule against the test cases.

## Conceptual territory
- Relates to the instance-property discussion in [[Harm Ontology - Explanations from 2026-11-19 (Agents and Instance Properties)]], which already notes that annotation properties behave like object properties in how they are inherited.

## Summary
- Object properties connect entities (perpetrator, victim, cause).
- Annotation properties record information about the statement (who assessed it, when, with what confidence).
- The distinction matters for reasoning: an object property affects what can be inferred, an annotation does not.

## Original wording
> "eventually somehow need to distinguish in the ontology between object properties and annotation properties"
- **Attribution:** the author
- **Source:** Obsidian Copilot chat, 2026-11-27, the author's brainstorm dump.
- **External references:** the OWL 2 specification defines annotation properties as non-logical. Not yet re-checked for this card.

## Real-world examples
- A harm's `hasVictim` is an object property. Its `assessedBy` is usually an annotation.

## Why it matters to the book
- Without the split, an assessor's note could accidentally change the ontology's logic, which would undermine the claim that harm is a perspective-relative assessment.

## Open questions
- Is a severity rating an object property or an annotation?
- Which properties must be inherited by instances, and which stay on the statement?

## Related
- [[Harm Ontology - Explanations from 2026-11-19 (Agents and Instance Properties)]]
- [[Mirror Roles - Rescuer, Mitigator, Beneficiary and Intermediary]]
- [[Modular Schema over a Shared Instance Graph]]
