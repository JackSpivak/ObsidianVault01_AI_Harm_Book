---
fileClass: Idea
type: idea
status: stub
bookmark: HO-II.d.2.a (proposed, not yet confirmed)
canonical_id: ho-classes-and-concepts-representation
territory: new
created: 2026-11-21
---

# Classes and Concepts — How Elements Are Represented

Index: [[_Harm Ontology Bookmark Index]] · Parent (proposed): [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes|HO-II.d.2]] · Related: [[HO-II.d.3 Hub and Spoke Pattern]] · Governing level: [[Harm Ontology v3.1 - Skeleton Schema (proposed)]]

## Why this is distinct
Up to now the vault has used "concept" for two things: an OWL class and a `skos:Concept`. The word also means an idea in plain English. The hub and spoke pattern and the discipline and territory naming both depended on telling these apart, and the 2026-11-21 Decisions Log entry records the rule. This page explains why the rule is what it is, with the reasoning that led to it.

## Anticipated direction
- Test the rule on each element of the skeleton (physics and Integral) in the coverage test.
- Decide the open questions listed in v3.1: `CorePrinciples` as a class or an individual, the holder link for `CollectiveAgent`, and the rule for elements that are both a participant and a term.

## Conceptual territory
- **Two kinds of thing.**
  - An **OWL class** is a kind the reasoner can reason over. It has instances, subclasses and restrictions, and relations are declared with domain and range. Examples: Discipline, PerspectiveType, ConceptualTerritory, FieldOfApplication.
  - A **`skos:Concept`** is a unit of meaning in a vocabulary. It has labels, definitions, notes and mappings, and it belongs to a scheme. The hierarchy (`broader`, `narrower`) is for organising and reading, not for logical inference. Examples: the hubs `hov:congruence` and `hov:omission`.
- **The test.** Ask whether the element needs to be the subject or object of a relation in the model, or whether it needs to be defined, labelled and matched in English. If the first, it is an individual of a class. If the second, it is a skos:Concept.
- **Overloaded words.** "Physics" has at least five senses in use: the territory (the physical world), a field of application (engineering, medicine), a discipline (the practice), a set of core principles, and a community of practitioners. Each sense is a different thing with a different role. So each gets its own skos:Concept with its own definition, and the shared word is an altLabel. Each sense is linked to the individual it describes.
- **Individuals are not concepts.** `PhysicsConceptualTerritory` is an individual of ConceptualTerritory. It is not typed as a skos:Concept, because it takes part in `studies`. The English definition of that territory is a skos:Concept linked to it. Typing the individual as a concept would blur the participant and the word.
- **Skos:Concept is also an OWL class.** So a territory could be an instance of skos:Concept. We rejected that for the participant role because the reasoner works more easily with a class designed for relations, and because the vocabulary is for wording.

## Worked example: physics
| Element | Type | Why |
|---|---|---|
| `Physics` (the practice) | individual of Discipline | studies a territory; practised in settings; anchored to a perspective |
| `physicsPerspective` | individual of PerspectiveType | carries the 0.02 structure; held, used and informed |
| `PhysicsConceptualTerritory` | individual of ConceptualTerritory | target of `studies` |
| `PhysicsFieldOfApplication` (e.g. engineering) | individual of FieldOfApplication | target of `practisedIn` |
| `PhysicsCorePrinciples` | individual or class (open) | a value of `foundationalCommitments`; produces verdicts |
| `PhysicsCommunity` | individual of CollectiveAgent | holds the perspective |
| English sense "physics, the territory" | skos:Concept | definition and mapping |
| English sense "physics, the discipline" | skos:Concept | definition and mapping |

## Open questions
- Is `CorePrinciples` a class with principles as members, or one individual whose members are principles?
- How is CollectiveAgent linked to its perspective? Check against `bearerRole` and `lineage`.
- Does the rule hold for an element that is both a participant and a term, such as ConceptualTerritory?
- Should the vocabulary and the schema live in one namespace family or two? (See the two-layer rule in v3.1.)

## Summary
- An element that takes part in relations is an individual of a class. A word-sense that is defined and mapped is a skos:Concept. Overloaded words get one skos:Concept per sense.

## Original wording
- Author: "PhysicsDiscipline being an instance of Discipline rather than a subclass; PhysicsPerspective an instance of a Perspective; PhysicsConceptualTerritory might be either an instance of a class ConceptualTerritory or a subconcept of a skos:Concept ConceptualTerritory (i am not sure)"
- Author: "This raises a good question. what distinguishes when we use classes vs concepts - certainly the notion of ConceptualTerritory points toward concept at least for this one"
- Author: "I like your distinction as it stands. before logging as a decision, lets examine it in place here."
- Author: "i think we can also log a decision or decisions regarding our agreement on what classes and concepts will be used to represent and how they will be implemented. i think this decision also needs to live at the Governing Commitments level in the Harm Ontology v3.1 And the explanation that you gave ... needs to live as its own idea note and bookmarked appropriately"
- Source: Obsidian Copilot chat, 2026-11-20 to 2026-11-21 (review of physics and Integral placement). The explanation is the assistant's, summarising the author's clarifications.
