---
fileClass: Idea
type: idea
status: seed
bookmark: HO-III.b
canonical_id: ho-reuse-domain-vocabularies
territory: new
tags: [ontology/harm]
aliases: [HO-III.b, Vocabulary Reuse]
created: 2026-11-14
filed: 2026-11-14
---

# HO-III.b — Reusing Expert Domain Vocabularies

Index: [[_Harm Ontology Bookmark Index]] · Parent: [[HO-000 Harm as Perspective-Relative Assessment|HO-000]] · Tier HO-III (meta layer)

## Why this is distinct
- The model reuses terms from well-maintained ontologies through domain namespaces, so it gains expert knowledge the project can't reconstruct. It keeps its own theory-relative commitment by **mapping** (`skos:closeMatch`) rather than adopting outside classes that label things "harms" outright.

## Anticipated direction
- Map by default, reference established identifiers directly, and import only small, stable core ontologies.
- Candidates (all from memory, unverified):
  - BFO
  - PROV-O
  - OWL-Time
  - SHACL
  - LKIF-Core / Akoma Ntoso / LegalRuleML / ECLI
  - STIX / MITRE ATT&CK / CVSS / CWE / CAPEC
  - AI Incident Database, CSET AI Harm Taxonomy, MIT AI Risk Repository, OECD AI Incidents Monitor, NIST AI RMF, EU AI Act risk tiers
  - SNOMED CT / ICD-11
  - HURIDOCS
- First research task: a sourced note on the AI-harm vocabularies.

## Conceptual territory
- This is standard semantic-web practice. What's specific here is the policy of mapping by default, to protect the rule that valence lives only in assessments.

## Summary
- The author already knows the namespace approach and confirmed it as the implementation path. Mapping the model onto AI-incident taxonomies would test it against hundreds of documented cases, and might show where *their* taxonomies make the category errors found in v1.

## Original wording
> "this is great.  this also has me very committed to using pre-existing domain vocabularies into which a  great deal of work has been contributed by experts with domain knowledge we oonly guess at"
- **Attribution:** Author

> "typically this will be implemented via domain namespaces and using terms from well maintained ontologies.  I am aware of this approach.  are you proposing anything fundamentally different from a practical implementation standpoint?"
- **Attribution:** Author

> "No. What I described is the standard practice you already know"
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references:** see the candidate list above (all unverified).

## Real-world examples
-

## Why it matters to the book
- It grounds the book's harm model in vocabularies regulators and researchers already use.

## Open questions
- Versions and licences (SNOMED CT is licensed).
- How loose should alignment with BFO be?

## Related
- [[HO-II.e Missingness Statuses and Domain Profiles]]
- [[003 Harm Ontology from Outlines]]
