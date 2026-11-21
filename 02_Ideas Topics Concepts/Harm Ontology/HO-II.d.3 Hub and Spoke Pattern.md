---
fileClass: Idea
type: idea
status: stub
bookmark: HO-II.d.3 (proposed, not yet confirmed)
canonical_id: ho-ii-d-3-hub-spoke-pattern
territory: new
created: 2026-11-20
---

# HO-II.d.3 — The hub and spoke pattern

Index: [[_Harm Ontology Bookmark Index]] · Parent (proposed): [[HO-II.d Perspective - Ten Optional Properties|HO-II.d]] · Related: [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes|HO-II.d.2]]

## Why this is distinct
HO-II.d.2 says that a hub is a `skos:Concept` and that spokes map to it. It does not explain *why* the pattern exists, what each level holds, or how the pattern is confused with the schema layer. This page records that explanation, using examples from the v3 samples.

## Anticipated direction
A stable rule for placing each narrative in the right layer (see [[Handoff - Harm Ontology Methodology Re-evaluation]], rules 1 to 4). Until that rule is agreed, the examples below describe the intent, not a tested implementation.

## Conceptual territory
- **The problem it solves.** Five disciplines name the same gap between what a lens says it does and what it does: law (congruence), Confucian ethics (*zhengming*), Kantian ethics (the operative maxim), political theory (euphemism), and philosophy of science (form without substance). A single discipline's term should not become the official name, and no discipline's account should be lost.
- **Hub = one shared idea.** A hub is a plain-English name for the idea across disciplines. It holds the cross-discipline definition, the boundary tests that separate it from neighbouring ideas, a status, and the explanation of why the ontology has it. Its number of spokes measures how many disciplines converge on it.
- **Spoke = one discipline's version.** A spoke keeps one discipline's own term, source, example and explanation, plus its scope difference from the hub and its mapping grade (`skos:closeMatch`, `skos:narrowMatch`, `skos:broadMatch`, `skos:relatedMatch`) with a one-line reason.
- **Split rule.** Anything true of the idea as a whole goes to the hub. Anything about one discipline's wording, source or scope goes to its spoke.

## Examples
| Element | Level | What it holds |
|---|---|---|
| `hov:congruence` | hub (`skos:Concept`) | shared definition; explanation that five disciplines name one gap |
| `law:congruence` (Fuller) | spoke | Fuller's "rules declared versus rules applied"; testable from enforcement records; scope difference (rule systems, not one agent's maxim) |
| `eth:operativeMaxim` (Kant) | spoke | the principle actually acted on; closeMatch, because it is one agent's will, not an institution's practice |
| `phil:zhengming` (Confucius, Xunzi) | spoke | a name as a promise about function; naming disputes recorded as Divergences |
| `ho:developmentalAltitude` | schema property (`owl:ObjectProperty`) | the recordable thing: an Assessment with `assessedBy` |
| `hov:developmentalAltitude` | hub (`skos:Concept`) | how widely a lens extends concern; warns that every altitude scale is built from somewhere |
| `psy:moralStages` | spoke (psychology, Kohlberg and Gilligan) | stages of moral development; closeMatch to the altitude hub |
| `int:altitude` and the Integral bands | spoke or scheme, unresolved | Wilber's reporting of Gilligan and Gebser; see the open question below |

## The confusion, and why it happens
1. **One local name, three elements.** `developmentalAltitude` is the schema property (`ho:`), the hub concept (`hov:`), and an untyped `rdf:Description` on the property's IRI in the `.owl` file. They are different things with the same label. The same name at two levels is allowed in RDF, but Protégé shows them as if they were the same.
2. **"Hub" names both a collection and its members.** The `skos:ConceptScheme` that groups the hubs is called `hov:hubs`, while each member is also called a hub. In English, a scheme organizes concepts, so the collection should be named for what it contains, not for the thing it contains.
3. **A hub is conceptual first, and a `skos:Concept` second.** The idea is a shared English concept. The `skos:Concept` is the implementation of that idea in the vocabulary layer. Calling the implementation the concept itself is the source of most of the confusion.
4. **Placement of narrative differs between samples.** In the editor-first sample, the hub narrative sits on the schema property. In the three-layer sample, it sits on the hub concept. The rule for where narrative goes is not yet written.
5. **Scheme placement is open.** Integral Theory is one author's tradition, closer to a PerspectiveType, but it is stored as a discipline-style scheme (`int:scheme`). Whether `psy:moralStages` should sit in `psy:` or be linked through the Integral reading is undecided.

## Open questions
- Should a scheme be keyed to a discipline (`law:`, `psy:`) or to a tradition (`int:`, linked to a PerspectiveType)?
- Should the grouping of hubs be renamed (for example `hov:conceptHubs`), or should each idea become its own scheme with the hub at the top?
- Where should the narrative for a hub live: on the schema property, on the hub concept, or split?

## Summary
- A hub is a shared English idea. A spoke is one discipline's version of it. The `skos:Concept` is how the vocabulary layer records the hub, and the schema property is the thing an assessment is about. Keep these three apart and the pattern holds.

## Original wording
- Author (2026-11-20, asking for a clear explanation): "i am still confused. perhaps we can jump up a level. can you explain the rationale? what function and intent is the 'hub' intended to capture? similarly, the spoke?"
- Author (2026-11-20): "we need to learn how to work better together" and "concepts are not usually thought of as organizing conceptschemes."
- Source: Obsidian Copilot chat, 2026-11-20 (review of the editor-first and three-layer mini samples). Transcript: `copilot/copilot-conversations/` (chat titled "have any of our logged discussions...").
- External references: W3C SKOS Reference (inScheme, topConceptOf, notation uniqueness); OBO Foundry principle 12 (label uniqueness). Both checked by search on 2026-11-20.
