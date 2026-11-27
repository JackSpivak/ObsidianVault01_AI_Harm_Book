---
fileClass: Idea
type: idea
status: seed
bookmark: draft
canonical_id:
territory: new
tags: []
aliases: [Governance Gap, Training-Governed vs Ontology-Governed Harm]
created: 2026-11-16
---

# The Governance Gap - Training-Governed vs Ontology-Governed Harm

## Why this is distinct
- [[Advantages of a Harm Ontology vs Strict LLM Training]] lists what an ontology *can* do. This note makes a claim about the real world: labs apparently govern harm through training on principles written in prose, not through explicit ontologies. The difference between the two is a gap the book can name.

## Anticipated direction
- A possible book thesis or chapter argument: harm that is governed only inside model weights can't be audited, contested or migrated like harm defined in an explicit ontology.
- Needs firmer evidence: read Claude's Constitution and other labs' published policies directly, and check whether any lab uses AIRO, VAIR or similar internally.

## Conceptual territory
- New as a claim. It grows out of the research section in [[Advantages of a Harm Ontology vs Strict LLM Training]] and connects to the AIRO/VAIR mapping to-do in [[Harm Ontology Migration Plan]].

## Summary
- Governing harm through model training and governing it through an explicit, auditable ontology are different things, and the difference is a real gap.
- I found no public evidence that Anthropic uses a formal, machine-readable harm ontology. It publishes principles in prose: Claude's Constitution (January 2026, CC0) and its Usage Policy.
- Training on principles turns them into model weights, and nothing in the weights enforces guarantees such as completeness checks, explicit exclusion boundaries or migration of past assessments (inference, not sourced).
- Open formal AI-risk ontologies (AIRO, VAIR) and taxonomies (MIT AI Risk Repository, CSET, MLCommons AILuminate) exist, but none match the philosophical and legal depth of this project's compendium.

## Original wording
> "does claude use standard, well established, explicit, rich ontologies like this one in the prodction of their llms to guarantee that the benefits mentioned above are persistant and governed across development, training and use?  are these standard ontologies of harm available in the public domain?  if not are they published by anthropic anywhere and available for use"
- **Attribution:** Author

> "I found no public evidence that Anthropic trains or governs Claude with a formal, machine-readable harm ontology (OWL/SKOS) like yours. What it publishes is written in prose."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

> "The benefits in your note belong to an ontology *alongside* a model, not to a model trained on principles."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5). Inference, not sourced.

> "The comparison holds up as a real gap: governing harm through model training versus governing it through an explicit, auditable ontology."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

> "also, please add the language you mentioned above regarding a gap to the summary material in the advantages note if you did not already do that"
- **Attribution:** Author

- **Source:** Obsidian Copilot agent session, 2026-11-16 (`copilot/copilot-conversations/agent__are_you_able_to_find_a_conversation_segment_in_which@20261115_182550.md`).
- **External references** (seen in search results; not opened, so unverified):
	- [Claude's Constitution (PDF)](https://www-cdn.anthropic.com/cffd979fd050fbc0d8874b8c58b24cc10554e208/claudes-constitution_webPDF_26-01.26a.pdf)
	- [AIRO](https://w3id.org/AIRO) · [VAIR](https://w3id.org/vair)
	- [MIT AI Risk Repository paper](https://futuretech.mit.edu/publication/the-ai-risk-repository-a-meta-review-database-and-taxonomy-of-risks-from-artificial-intelligence)

## Real-world examples
- Claude's Constitution: harm guidance written as prose principles, released under CC0 (not yet read directly).

## Why it matters to the book
- A model's harm judgments can't be inspected the way an ontology can. If harm is governed only through training, the public can't audit, contest or reproduce how harm is defined. That opacity is itself an AI-harm theme.

## Open questions
- Do labs use internal, unpublished taxonomies? Absence of public evidence isn't evidence of absence.
- Is a hybrid possible, with an ontology governing evaluation and training data while the model handles judgment?
- Would an external ontology simply move the opacity to whoever controls the ontology? Compare advantage 11 (multi-stakeholder deliberation).

## Related
- [[Advantages of a Harm Ontology vs Strict LLM Training]]
- [[Harm Ontology Migration Plan]]
- [[HO-000 Harm as Perspective-Relative Assessment]]
