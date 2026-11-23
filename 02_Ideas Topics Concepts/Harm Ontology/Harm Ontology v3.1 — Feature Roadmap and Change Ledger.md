---
fileClass: Roadmap
type: roadmap
status: developing
tags: [ontology/harm, roadmap]
aliases: [Harm Ontology v3.1 Roadmap, Schema Change Ledger]
created: 2026-11-22
---

# Harm Ontology v3.1 — Feature Roadmap and Change Ledger

*The staging ground for proposed schema additions, structural updates, rationale, priority, target implementation version, dependencies, and unresolved design blockers before formal migration to `.ttl` files. Associating this roadmap with v3.1 clarifies our direction and priorities, explicitly distinguishing immediate v3.1 targets from v4 and beyond.*

---

## Active Change Proposals (Staging Area)

### CP-01: Discipline-Enabled Assessments and Functional Subclasses
- **Status:** `Draft Proposal`
- **Priority:** `High`
- **Target Version:** `v3.1`
- **Core Rationale:** Perspectives must actively enable assessments rather than just tag them. Different assessment types serve distinct institutional/pragmatic functions (regulatory, forensic, diagnostic, normative critique) that should be reflected in their class hierarchy.
- **Proposed Additions:**
  - `DisciplinePerspective` (class/individual linkage)
  - `enablesAssessment` (object property: `DisciplinePerspective` → `HarmAssessment`)
  - Functional Subclasses of `HarmAssessment`: `RegulatoryAssessment`, `ForensicAssessment`, `DiagnosticAssessment`, `NormativeCritiqueAssessment`.
- **Three-Layer Impact:**
  - **Layer 1 (Schema / OWL):** Add `enablesAssessment` property and `HarmAssessment` functional subclasses.
  - **Layer 2 (Profiles / SHACL):** Add validation rules for discipline-backed assessments.
  - **Layer 3 (Vocabulary / SKOS):** Define hubs for assessment functions and link discipline schemes.
- **Test Case Dependencies:** Needs integration into [[HO-002 Ontology Stress-Test Suite|HO-002]] test cases involving multi-institutional reporting (e.g., regulatory audits vs. academic critiques).
- **External Alignment:** Cross-reference with DPV/AIRO assessment and accountability roles.
- **Origin / Stakeholder:** Co-developed from session dialogue (2026-11-22).
- **Blockers / Open Questions / Problems to Resolve:**
  - Are these subclasses mutually exclusive, or can an assessment be both forensic and regulatory?
  - How do these subclasses interact with the pending split of Assessment into Causal, Valence, and Responsibility ([[HO-005 Assessed Membership and Systematic Omission]])?
  - Does Protégé's editor view handle multi-level assessment subclasses cleanly without cluttering the property tree?

---

## Template for Future Proposals

### CP-XX: [Feature Title]
- **Status:** `Seed Idea` | `Draft Proposal` | `Under Stress-Test` | `Settled` | `Rejected`
- **Priority:** `Low` | `Medium` | `High` | `Critical`
- **Target Version:** `v3.1` | `v4` | `v5+`
- **Core Rationale:** [Why is this needed? What real-world or theoretical gap does it close?]
- **Proposed Additions:** [Classes, properties, individuals, or SKOS hubs involved]
- **Three-Layer Impact:** [Notes on Layer 1 OWL Schema, Layer 2 SHACL Profiles, and Layer 3 SKOS Vocabulary]
- **Test Case Dependencies:** [Which HO-002 test cases or toy runs validate this?]
- **External Alignment:** [Alignment with AIRO, DPV, LKIF-Core, or other external ontologies]
- **Origin / Stakeholder:** [Source session, council review, or author directive]
- **Blockers / Open Questions / Problems to Resolve:** [Unsolved tensions, edge cases, or dependencies]
- **Related Notes:** [Links to relevant HO notes, decisions, or council reviews]

---

## Completed / Settled Changes
*(Items moved here once codified into the `.ttl` schema and logged in [[Decisions_Log]].)*
