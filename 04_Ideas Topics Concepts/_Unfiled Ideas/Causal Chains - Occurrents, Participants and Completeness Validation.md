---
fileClass: Idea
type: idea
status: seed
bookmark: draft
canonical_id:
territory: new
tags: [ontology/harm, causal-chain, dul, shacl, participants]
aliases: [Causal Chain Schema, Participants and Agents]
created: 2026-11-23
---

# Causal Chains - Occurrents, Participants and Completeness Validation

## Why this is distinct
It models a causal chain as an occurrent structure linked by object properties, and keeps the judgment of completeness in a separate constraint layer. It also separates agents from participants, so storms and witness error fit in the same schema.

## Anticipated direction
A DUL-aligned causal chain schema where membership is expressed structurally, completeness is validated with SHACL, and non-agents enter as sources or participants.

## Conceptual territory
Occurrents and participants (DOLCE+DnS Ultralite); agency versus causal origin; epistemic error as a causal input; open-world versus closed-world validation.

## Summary
- A causal chain is a structure whose members are linked by object properties. Completeness is a separate judgment, layered on with SHACL. (Paraphrase.)
- Only objects and agents participate in events. A process is not a participant. An impaired memory is a quality of a person, and faulty recall is part of their cognitive life. (Paraphrase.)
- A storm is not an agent, but it is the source of a cascade: surge, debris, structural collapse. The cascade is a chain of events and mechanisms. (Paraphrase.)
- A witness's false testimony is an event, and the data it produces is an information object that an institution can rely on. A wrongful arrest can follow with no malicious actor. (Paraphrase.)
- **Caution:** the DUL-aligned classes were drafted from memory and must be checked against the published DUL OWL file.

## Original wording
> "so it sounds like the notion of membership in the chain can be represented structurally through the use of classes and object properties however the assessment of completeness or flawedness must be layered on through shacl rules (most likely)"
- **Attribution:** Author
- **Source:** Structured inquiry session, 2026-11-23, `copilot/copilot-conversations/agent__structured_inquiry@20261123_184258.md`

> "if a storm causes harm, who would be the required ex:Actor?  the storm? the kinetic impact of waves? floodwater due to surge? windblown debris?  waterborne debris damaging structures and infrastructure?  how is this represented"
- **Attribution:** Author
- **Source:** Same session

> "can people be participants or only agents?  how about a person who was a wittness but has an impaired memory and remembers details of looting activity that is incorrect and gets the wrong person arrested who then incurrs hundreds of thousands of dollars in legal defence and private investigative fees"
- **Attribution:** Author
- **Source:** Same session

> "is the internal impaired memory process a participant too?  can a process be a participant or only things/objects"
- **Attribution:** Author
- **Source:** Same session

> "so a falsetestimony might be an event where falsetestimonydata might be the actual data that arose from that event"
- **Attribution:** Author
- **Source:** Same session

- **External references:** DOLCE+DnS Ultralite (DUL), the upper ontology used as the basis for the schema. Its classes and properties were not verified against the published file during this session. Event-Model-F was mentioned in search results as a DUL-based event model, not checked.

## Real-world examples
- Hurricane, storm surge and debris damage to coastal structures.
- Eyewitness misidentification leading to a wrongful arrest and legal costs.

## Why it matters to the book
It gives the book a precise way to show that harm can arise without a villain, and that natural forces and epistemic error both enter causal accounts without being mistaken for moral agents.

## Open questions
- Are the parent classes for Mechanism and HarmfulOutcome correct under DUL?
- Should the psychological and legal outcomes of one chain be split into modules, as in the modular schema note?

## Related
- [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] (S41)
- [[Modular Schema over a Shared Instance Graph]]
- [[Harm Ontology v0.03.01 Design Notes - Harmfulness, Imagined Harm and Causal Chains]]
