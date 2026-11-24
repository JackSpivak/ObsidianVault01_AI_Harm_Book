---
fileClass: Idea
type: idea
status: seed
bookmark: draft
canonical_id:
territory: new
tags: [ontology/harm, modular-ontology, namespaces, abox, tbox, commitment/proposed]
aliases: [Ontological Commitment 01, Modular TBox Shared ABox]
created: 2026-11-23
---

# Modular Schema over a Shared Instance Graph

## Why this is distinct
It answers a design question about where namespaces belong. Domain modules define vocabulary, and individuals keep one identity across all of them.

## Anticipated direction
Domain-specific properties (psychological, legal, financial) live in separate schema modules with their own namespaces. Instances share one namespace, so a single person can carry assertions from several modules.

## Conceptual territory
Modular ontology design; TBox versus ABox; identity across perspectives; analytic isolation.

## Summary
- Domain properties such as `psych:` and `legal:` belong to separate schema modules that extend a shared core. (Paraphrase.)
- Instances do not need their own namespaces. A namespace marks where a term is defined, not what kind of thing an individual is. (Paraphrase.)
- Splitting one person into a psychological record and a legal record would make it impossible to join them reliably. (Paraphrase.)
- A query can load only the psychological module and ignore legal assertions about the same individual. (Paraphrase.)
- **Status:** proposed as Ontological Commitment 01 in chat. Not yet confirmed by the author and not yet logged.

## Original wording
> "if you implement the modular approach with appropriate namespaces, would the instances that carry the domain-specific values for these domain-specific properties have to be modular and have their own respective namespaces as well?"
- **Attribution:** Author
- **Source:** Structured inquiry session, 2026-11-23, `copilot/copilot-conversations/agent__structured_inquiry@20261123_184258.md`

- **External references:** None checked in this session.

## Real-world examples
- A person who is both a victim of harm and a party to a legal dispute about it, where the psychological and legal records must refer to the same individual.

## Why it matters to the book
It shows how the harm ontology can represent one person's harm through several lenses without splitting the person into several records.

## Open questions
- Should the commitment be logged in `Decisions_Log` once confirmed?
- How are cross-module assertions about one individual checked for contradictions?

## Related
- [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] (S40)
- [[Causal Chains - Occurrents, Participants and Completeness Validation]]
- [[Harm Ontology v3 Design Notes - Harmfulness, Imagined Harm and Causal Chains]]
