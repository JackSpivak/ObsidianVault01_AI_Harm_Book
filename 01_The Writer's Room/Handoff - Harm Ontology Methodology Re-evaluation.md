---
type: handoff
status: proposed
workstream: Harm Ontology
created: 2026-11-20
parent_handoff: "[[Handoff - Harm Ontology]]"
---

# Handoff - Harm Ontology Methodology Re-evaluation

*Task-scoped handoff, written 2026-11-20 at the end of a long chat. Nothing here is logged in [[Decisions_Log]]. Attach this note, plus [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)]], to start a new chat. The wider work is in [[Handoff - Harm Ontology]].*

## Why this exists
The editor-first and three-layer mini samples were opened and examined in Protégé. The samples exposed naming, typing and placement problems. Until an implementation methodology is agreed, the samples cannot fairly test whether the three-layer strategy (schema, profiles, vocabulary) works for both machine and human readers.

## Findings from the sample review
1. **One local name, three elements.** `developmentalAltitude` appears as:
   - `ho:developmentalAltitude`, a typed `owl:ObjectProperty` in the schema layer (`ho-schema-mini.ttl` line 102; `ho-editor-mini.ttl` line 1962). This is the recordable property.
   - `hov:developmentalAltitude`, a typed `skos:Concept` in the vocabulary layer (`ho-vocabulary-mini.ttl` line 771). This is the cross-discipline hub.
   - an untyped `rdf:Description` on the schema IRI, carrying a label and a `dcterms:source` (`ho-editor-mini.owl` around line 1181). It is not a separate individual; it adds annotations to the property's IRI, and it appears in the `.owl` file only as far as was checked.
2. **Scheme placement is undecided.** `int:scheme` (Integral) is a `skos:ConceptScheme` used like a discipline vocabulary, but Integral Theory is a single author's tradition, closer to a PerspectiveType. `int:colourAltitude` is also a scheme. `psy:moralStages` (stages of moral development) is a `skos:closeMatch` to the hub; its `skos:inScheme` was not checked.
3. **No rule for where narrative goes.** Hub narrative sits on the property in editor-first and on a concept in three-layer. Spoke explanations sit on individuals.
4. **Naming.** The scheme `hov:hubs` is named with a plural that reads like a concept, while its members are also called hubs. Whether the scheme name should change depends on the design decision below.

## Corrections made in the chat (do not carry the errors forward)
- An earlier claim that a misplaced item existed was not located. Do not rely on it.
- A claim that `.owl` and `.ttl` copies differ was not verified. Only the untyped `rdf:Description` was observed, and only in `.owl`.
- Editor-first uses `ho:` throughout. `hov:` belongs to the three-layer sample.

## External references (checked by search unless marked)
- OBO Foundry principle 12: labels unique within an ontology; one label per entity; plain English; no CamelCase or underscores in labels; automated check for duplicate labels.
- OBO Foundry ID policy: stable IRIs in a fixed namespace; not reused for a changed meaning.
- W3C SKOS Reference: by convention, unique notation per scheme; a concept may belong to more than one scheme; top concepts are declared per scheme (`skos:hasTopConcept`, `skos:topConceptOf`).
- OWL 2 punning: one IRI may be used as class, property and individual under restrictions (from memory, unverified).
- ISO 25964 and ISO 704 (from memory, unverified).

## Decisions to make (in this order)
1. **Identity rule:** one IRI, one type and one unique label per layer; how to avoid reusing a local name across layers.
2. **Scheme rule:** key a scheme to a discipline or to a tradition. Decide where a spoke belongs when its origin and its reporter differ (the Integral and `psy:moralStages` case).
3. **Layer rule:** which element type lives in which layer and prefix.
4. **Narrative rule:** which annotation goes on which element type.
5. **Mapping rule:** direction of match links and where the reason for each grade lives.
6. **Check rule:** an automated check for unique labels, one type per IRI, no untyped declarations, every hub in a scheme.
7. **Test rule:** judge samples in Protégé and VocBench against these rules, not on appearance.

## Next step for the new chat
Draft a one-page methodology note with rules 1–7 marked **proposed**. Do not change the samples until the rules are agreed. Do not log decisions until the author confirms them.

## Original wording
- Author: "we need to jump up a level and propose a ruleset or methodology specification for properly categorizing and associating vocabulary elements consistently"
- Source: Obsidian Copilot chat, 2026-11-20 (review of the editor-first and three-layer mini samples).
