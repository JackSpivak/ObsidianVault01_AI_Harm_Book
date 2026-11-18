---
type: admin
status: developing
tags: [admin, continuity]
---

# Canon & Continuity

The single list of established facts. If it's here, it's true for the book.
Link to the detailed note for each entry.

## Timeline
| When | Event | Source note |
|---|---|---|
| | | |

## Characters (quick facts)
| Character | Key fixed facts | Note |
|---|---|---|
| | | |

## World rules / technology
-

## Places
-

## Glossary (harm ontology terms)
| Term | Meaning | Source note |
|---|---|---|
| **Discipline** | A field of knowledge and its vocabulary (law, ethics, cognitive science…). In the ontology, a discipline scheme in the vocabulary layer. | [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes\|HO-II.d.2]] |
| **Perspective** | Abstract umbrella class with no direct members: either a tradition (PerspectiveType) or a perspective specification (PerspectiveSpecification). Carries only a definition and Explanation. | [[Decisions_Log]] 2026-11-17 |
| **Tradition** (PerspectiveType) | A reusable way of seeing and judging, with a lineage: Utilitarianism, Tort Law, Public Health, a trained AI model. Subclass of Perspective; prefLabel "tradition"; altLabel "lens". Holds `defaultEvaluativeStandard`. | [[PerspectiveStructure 0.02]] |
| **Lens** | Informal synonym for tradition (altLabel of PerspectiveType). Not used for a single viewpoint. | [[Decisions_Log]] 2026-11-17 |
| **Perspective specification** (PerspectiveSpecification) | The specifications under which one assessment is made: standpoint, time, horizon, framing, sensitivity, purpose, assessor. Subclass of Perspective; altLabels "viewpoint", "perspective snapshot". Instantiates a tradition, may override its defaults, and holds `appliedEvaluativeStandard`. Formerly called "shot" (retired). | [[HO-II.d Perspective - Ten Optional Properties\|HO-II.d]] |
| **Field of application** | Where a tradition is applied (medicine, credit scoring). Property `fieldOfApplication` (formerly `domainOfApplicability`). | [[Decisions_Log]] 2026-11-17 |
| **Profile** | A rule set saying which properties a kind of record must address (e.g. LegalInstitutional, LearnedModel). Formerly "domain profile". | [[HO-II.e Missingness Statuses and Domain Profiles\|HO-II.e]] |
| **Domain** | Reserved for its OWL meaning only: the class a property applies to. | [[Decisions_Log]] 2026-11-17 |

## Open continuity questions
- 
