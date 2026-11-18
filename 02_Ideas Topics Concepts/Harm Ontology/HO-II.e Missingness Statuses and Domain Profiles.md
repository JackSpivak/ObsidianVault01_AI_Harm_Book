---
fileClass: Idea
type: idea
status: developing
bookmark: HO-II.e
canonical_id: ho-missingness-domain-profiles
territory: new
tags: [ontology/harm]
aliases: [HO-II.e, Missingness Statuses, Domain Profiles]
created: 2026-11-14
filed: 2026-11-14
---

# HO-II.e — Missingness Statuses and Domain Profiles

Index: [[_Harm Ontology Bookmark Index]] · Parent: [[HO-000 Harm as Perspective-Relative Assessment|HO-000]] · Tier HO-II (judging layer)

## Why this is distinct
- Real assessments are sparse, and information is often missing. The model treats **why** a value is missing as information in itself, and lets each domain add the properties it needs, without making anything mandatory everywhere.

## Anticipated direction
- **Open world:** an absent property means "not considered".
- **Explicit statuses:** Unknown (considered but undeterminable), NotApplicable, Undisclosed (known but withheld), Disputed, Pending (will become knowable).
- **Domain profiles** (`ThreatAssessment`, `ClinicalAssessment`, `Judgment`, `RegulatoryImpactAssessment`…) add properties. SHACL requires key properties to be **addressed** (given a value or a status), never to be **known**.
- `confidence` and `suppliedBy` (provenance) on values.

## Conceptual territory
- New for this vault. It uses standard RDF/OWL open-world semantics with SHACL closed-world validation, and resembles source-reliability ratings in threat intelligence.

## Summary
- Absent vs. Unknown matters: the Sai Weng neighbours never asked about horizon, while the old man asked and answered "unknown". Undisclosed is typical of AI harm: the information exists, but it's held by the party with most to lose. Recording who holds a missing value turns gaps into evidence.

## Original wording
> "ten properties is a lot. however, i am wondering that perhaps this is part of the nature of the real world.  not all of these may be applicable to all circumstances or instances of a perspective (when it is not so literal as a camera). and some circumstances may require more for an assessment to valuably serve the intent.  think of a cybersecurity threat assessment for example.  another aspect of the real world is that regardless of how many actual properties are needed there will inevetably be missing information in many or most cases.  in real world instances these properties might be left blank (null) or better \"unknown\" especially by default"
- **Attribution:** Author

> "The key phrase is **\"must be addressed,\" not \"must be known.\"**"
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references (from memory, unverified):** SHACL (W3C); CVSS, STRIDE, MITRE ATT&CK for the cybersecurity profile.

## Real-world examples
- A company's internal risk data: Undisclosed, held by the assessed party.
- A latent harm still unfolding: Pending.

## Why it matters to the book
- Opacity is not a neutral gap. Who withholds what is part of the harm.

## Open questions
- Which properties should the core SHACL shape require to be addressed for *every* Assessment (at minimum horizon, scope and AffectedEntity?)

## Related
- [[HO-II.d Perspective - Ten Optional Properties]]
- [[HO-III.b Reusing Expert Domain Vocabularies]]
- [[HO-I.c Phenomenality - Observability and Experienceability]]
