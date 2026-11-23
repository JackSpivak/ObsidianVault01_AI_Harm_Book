---
fileClass: Roadmap
type: roadmap
status: developing
tags: [ontology/harm, roadmap]
aliases: [Harm Ontology v3.1 Roadmap, Schema Change Ledger]
created: 2026-11-22
---

# Harm Ontology v3.1 — Feature Roadmap and Change Ledger

*The staging ground for proposed schema additions, structural updates, open decisions, rationale, priority, target version, dependencies, and blockers, before formal migration to `.ttl` files. Associating this ledger with v3.1 clarifies direction and priorities. Items may target v4 or later.*

**Conventions**
- **Type:** `Proposal` (a new feature or change) · `Decision` (a proposed item that needs resolution) · `Open Issue` (a problem to resolve before implementation) · `Task` (work that blocks other items).
- **Order:** newest at the top, oldest at the bottom, by Date Proposed. IDs are assigned in the order items were collected, so they are not chronological.
- **Complete and Rejected** items stay in the ledger at the bottom and are never deleted.

---

## Active Ledger (Newest First)

### CP-20: Test the Perspective Critical Reading Skill
- **Type:** Task
- **Status:** `Draft Proposal`
- **Date Proposed:** 2026-11-22
- **Date Settled / Rejected:** N/A
- **Priority:** High
- **Target Version:** v3.1 (process; no schema change)
- **Core Rationale:** The skill `perspective-critical-reading` (`copilot/skills/perspective-critical-reading/SKILL.md`) reads a narrative from a named perspective and reports its questions, findings and blind spots. Its value was observed in three informal runs (military strategist, public health epidemiologist, Vajrayana Buddhist) on the Reuters Crimean Bridge report, but those runs broke the skill's own ordering rule: the questions were written after the text was read. The skill has not been tested in the order it now requires.
- **Proposed Test:**
  - Re-run one perspective with the ordering rule: core questions recorded from the perspective alone, before the text is pasted.
  - Compare the perspective-only questions with the narrative-shaped ones. Count how many of the earlier questions survive.
  - Check each provenance tag ([P], [T], [I], [K]) against the text.
  - Test whether blind spots are reported as readily as findings.
- **Blockers / Open Questions:**
  - Which perspective to test first, and whether its core questions should be grounded in a retrieved source or in the vault's council reviews.
  - Whether the three earlier runs are kept as worked examples, and where.
  - Whether the skill's relation to [[HO-002 Ontology Stress-Test Suite|HO-002]] cases should be decided before or after the test.
- **Origin / Stakeholder:** Session dialogue, 2026-11-22

### CP-01: Discipline-Enabled Assessments and Functional Subclasses
- **Type:** Proposal
- **Status:** `Draft Proposal`
- **Date Proposed:** 2026-11-22
- **Date Settled / Rejected:** N/A
- **Priority:** High
- **Target Version:** v3.1
- **Core Rationale:** Perspectives must actively enable assessments rather than just tag them. Different assessment types serve distinct institutional or pragmatic functions (regulatory, forensic, diagnostic, normative critique) that should be reflected in the class hierarchy.
- **Proposed Additions:**
  - `DisciplinePerspective` (class or individual linkage)
  - `enablesAssessment` (object property: `DisciplinePerspective` → `HarmAssessment`)
  - Functional subclasses of `HarmAssessment`: `RegulatoryAssessment`, `ForensicAssessment`, `DiagnosticAssessment`, `NormativeCritiqueAssessment`
- **Three-Layer Impact:**
  - Layer 1 (Schema / OWL): `enablesAssessment` and the `HarmAssessment` subclasses
  - Layer 2 (Profiles / SHACL): validation rules for discipline-backed assessments
  - Layer 3 (Vocabulary / SKOS): hubs for assessment functions, linked to discipline schemes
- **Test Case Dependencies:** [[HO-002 Ontology Stress-Test Suite|HO-002]] cases involving multi-institutional reporting (regulatory audit vs. academic critique)
- **External Alignment:** DPV / AIRO assessment and accountability roles
- **Origin / Stakeholder:** Session dialogue, 2026-11-22
- **Blockers / Open Questions:**
  - Are the subclasses mutually exclusive, or can one assessment be both forensic and regulatory?
  - How do they interact with the pending split of Assessment into Causal, Valence and Responsibility ([[HO-005 Assessed Membership and Systematic Omission]])?
  - Does Protégé show multi-level assessment subclasses cleanly?

### CP-02: Perspective Narrative Generation (Searchlight Pilot)
- **Type:** Task
- **Status:** `Draft Proposal`
- **Date Proposed:** 2026-11-21
- **Date Settled / Rejected:** N/A
- **Priority:** High (blocks content migration)
- **Target Version:** v3.1
- **Core Rationale:** Test whether prompts can generate a PerspectiveType's questions, blind spots and findings-and-remedies narrative.
- **Blockers:** Needs one PerspectiveType chosen for the pilot. See [[Perspective Narrative Generation - Searchlight Task]].
- **Origin:** [[Harm Ontology Migration Plan]] to-do list

### CP-03: Agents, Participation and Assessing Organisations (HO-007)
- **Type:** Decision
- **Status:** `Draft Proposal`
- **Date Proposed:** 2026-11-19
- **Date Settled / Rejected:** N/A
- **Priority:** High
- **Target Version:** v3.1
- **Core Rationale:** Agents, events and organisational assessors are not yet modelled. Needed for the robbery case and for audit firms, testing agencies and regulators as `assessor`.
- **Proposed Additions:** Event class; Agent participation in an Event that participates in a FactorAssembly; roles in participation; organisations as `assessor`. Participation is not responsibility.
- **Blockers / Open Questions:**
  - Author confirmation of HO-007 is still pending.
  - What counts as an agent (a lion, floodwater, an AI system)?
  - Add test cases to [[HO-002 Ontology Stress-Test Suite|HO-002]].
- **Related:** [[Handoff - Harm Ontology]]

### CP-04: Assessment-Everywhere (Variant B)
- **Type:** Decision
- **Status:** `Under Stress-Test`
- **Date Proposed:** 2026-11-18
- **Date Settled / Rejected:** N/A
- **Priority:** High
- **Target Version:** v3.1 or v4 (undecided)
- **Core Rationale:** Move Factor, CausalRole, Effect and AffectedEntity attributes into assessments, so that "fact" becomes a status.
- **Blockers / Open Questions:**
  - Non-expert subagent test still to run. It gates adopting variant B.
  - Sourced Horizon test (R01) not yet run.
  - SHACL validation not yet run.
- **Related:** [[HO-002.a Assessment-Everywhere Test Strategy]]; toy-case results in [[2026-11-18 Harm Ontology v3 Toy Case Results]]

### CP-05: Strict Settlement Rule
- **Type:** Open Issue
- **Status:** `Under Stress-Test`
- **Date Proposed:** 2026-11-18
- **Date Settled / Rejected:** N/A
- **Priority:** High
- **Core Rationale:** The strict rule (at least 2 independent assessments, same procedure and version, evidence, no silent in-scope perspective) may leave almost nothing Settled in real data.
- **Blockers:** Needs testing against real cases, not only toy data.

### CP-06: Narrative Placement and Editor Usability
- **Type:** Open Issue
- **Status:** `Draft Proposal`
- **Date Proposed:** 2026-11-18 (reopened 2026-11-19)
- **Date Settled / Rejected:** N/A
- **Priority:** High (blocks Phase 1)
- **Core Rationale:** The mini example was hard to read in Protégé. Properties show no domains or ranges, and narrative placement is unsettled.
- **Blockers / Open Questions:**
  - Choose narrative placement (separate files by layer, as the leaning suggests, or a single file).
  - Give every class its properties, with domain and range.
  - Settle how property groups appear in an editor.
- **Related:** [[Harm Ontology v3 Provisional Release Brief]]; [[Harm Ontology v3 Three-Layer Mini Example Brief]]

### CP-07: Subtype Names for AffectedEntity
- **Type:** Decision
- **Status:** `Draft Proposal`
- **Date Proposed:** 2026-11-18
- **Date Settled / Rejected:** N/A
- **Priority:** Medium
- **Core Rationale:** The 2026-11-18 log names `NaturalSystem` and `EngineeredSystem`, but the v3 draft lists `NonSentientSystem`.
- **Blockers / Open Questions:** Confirm which name is correct. Also confirm whether Household, CollectiveNaturalGroup and CollectiveArtificialPerson are logged.

### CP-08: affectedStanding as Exclusive
- **Type:** Decision
- **Status:** `Under Stress-Test`
- **Date Proposed:** 2026-11-18
- **Date Settled / Rejected:** N/A
- **Priority:** Low
- **Core Rationale:** For the toy test, `affectedStanding` (Direct / Derivative) was treated as exclusive. Whether it should be is undecided.
- **Blockers:** Decide after the Horizon test.

### CP-09: Capability Approach (Sen and Nussbaum)
- **Type:** Decision
- **Status:** `Draft Proposal`
- **Date Proposed:** 2026-11-16
- **Date Settled / Rejected:** N/A
- **Priority:** High (before Phase 3)
- **Core Rationale:** Decide where functionings, capabilities, agency, conversion factors and adaptive preferences live (EvaluativeStandard, Effect or AffectedEntity properties, Factor kinds, or a gap).
- **Blockers:** Settle Sen's open list against Nussbaum's fixed ten of capabilities.
- **Related:** [[Capability Approach - Sen and Nussbaum]]

### CP-10: Map v3 to External AI-Risk Ontologies
- **Type:** Task
- **Status:** `Draft Proposal`
- **Date Proposed:** 2026-11-16
- **Date Settled / Rejected:** N/A
- **Priority:** Medium
- **Core Rationale:** Crosswalk v3 to AIRO, VAIR and DPV-RISK, reusing their IRIs where meanings match.
- **Blockers:** Check whether `airo:Consequence` or `dpv:Harm` build in negative valence. If they do, use `skos:closeMatch`, not `owl:equivalentClass`.
- **Related:** [[External AI-Risk Ontologies - Alignment and Additions for Harm Ontology v3]]

### CP-11: Split Assessment into Causal, Valence and Responsibility
- **Type:** Decision
- **Status:** `Seed Idea`
- **Date Proposed:** 2026-11-15 (draft structure)
- **Date Settled / Rejected:** N/A
- **Priority:** Medium
- **Blockers:** Pending tests in HO-005.

### CP-12: Causal Standards (But-for, NESS, INUS, Probability-Raising)
- **Type:** Proposal
- **Status:** `Seed Idea`
- **Date Proposed:** 2026-11-15 (draft structure)
- **Date Settled / Rejected:** N/A
- **Priority:** Medium
- **Blockers:** Pending, with its own HO-005 tests.

### CP-13: Reify participatesIn as a Claim
- **Type:** Decision
- **Status:** `Seed Idea`
- **Date Proposed:** 2026-11-15 (draft structure)
- **Date Settled / Rejected:** N/A
- **Priority:** Low
- **Blockers:** Pending.

### CP-14: "Sufficient as Assessed" (revises HO-003 "jointly sufficient")
- **Type:** Decision
- **Status:** `Seed Idea`
- **Date Proposed:** 2026-11-15 (draft structure)
- **Date Settled / Rejected:** N/A
- **Priority:** Medium
- **Blockers:** Pending. See [[HO-005 Assessed Membership and Systematic Omission]].

### CP-15: Condition Split and Role Types
- **Type:** Open Issue
- **Status:** `Seed Idea`
- **Date Proposed:** 2026-11-15 (draft structure)
- **Date Settled / Rejected:** N/A
- **Priority:** Low
- **Core Rationale:** The Condition entry is ambiguous. Role types and causal share are unresolved.

### CP-16: Worldviews as Evaluative Standards
- **Type:** Decision
- **Status:** `Seed Idea`
- **Date Proposed:** 2026-11-14
- **Date Settled / Rejected:** N/A
- **Priority:** Low
- **Core Rationale:** Should afterlife or ancestor traditions count as EvaluativeStandards? Recorded as an open question in [[HO-II.a Assessment and Evaluative Standard]].

### CP-17: Classical Council Ideas as Standards
- **Type:** Decision
- **Status:** `Seed Idea`
- **Date Proposed:** 2026-11-14
- **Date Settled / Rejected:** N/A
- **Priority:** Low
- **Core Rationale:** Should harm to the wrongdoer and manufactured desire be added as standards? Recorded in [[HO-II.a Assessment and Evaluative Standard]].

### CP-18: HO-006 Causal Chain Class (v4)
- **Type:** Proposal
- **Status:** `Seed Idea`
- **Date Proposed:** Undated (see [[HO-006 Causal Chain - an Assessed Selection with a Horizon]])
- **Date Settled / Rejected:** N/A
- **Priority:** Low
- **Target Version:** v4
- **Core Rationale:** A thin, horizon-bounded Chain class for CausalRole to point at.
- **Blockers:** First test is one chain at two horizons in the toy case.

### CP-19: Open Items Carried Forward from v3 Draft (Undated)
- **Type:** Open Issue (grouped)
- **Status:** `Seed Idea`
- **Date Proposed:** Undated
- **Date Settled / Rejected:** N/A
- **Priority:** Low
- **Items:** Assent/Judgment as an object of harm · consent · the legal layer · the evidence anchor against the regress · future generations, AI systems and relationships as affected entities (partly decided 2026-11-18) · Agent and AI systems (see CP-03) · domains and ranges for the Protégé build (see CP-06).
- **Related:** [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)]]

---

## Settled (Ready for Implementation in v3.1)
*(No items yet. An item moves here when it has passed its stress tests or author review and is fully specified.)*

---

## Complete and Rejected (Retained for the Record)
*(Items with status `Complete` (codified into the `.ttl` and logged in [[Decisions_Log]]) or `Rejected`. Newest at the top.)*

*No items yet.*

---

## Template for New Entries

### CP-XX: [Title]
- **Type:** Proposal | Decision | Open Issue | Task
- **Status:** `Seed Idea` | `Draft Proposal` | `Under Stress-Test` | `Settled` | `Complete` | `Rejected`
- **Date Proposed:** [YYYY-MM-DD]
- **Date Settled / Rejected:** [YYYY-MM-DD or N/A]
- **Priority:** Low | Medium | High | Critical
- **Target Version:** v3.1 | v4 | v5+
- **Core Rationale:** [Why is this needed? What gap does it close?]
- **Proposed Additions:** [Classes, properties, individuals or SKOS hubs]
- **Three-Layer Impact:** [Layer 1 OWL · Layer 2 SHACL · Layer 3 SKOS]
- **Test Case Dependencies:** [HO-002 cases or toy runs that validate this]
- **External Alignment:** [AIRO, DPV, LKIF-Core or other]
- **Origin / Stakeholder:** [Session, council review or author directive]
- **Blockers / Open Questions:** [Unresolved tensions, edge cases, dependencies]
- **Related Notes:** [Links]

---

**Version rollover:** when v3.1 implementation is complete, copy this document to `Harm Ontology v3.2 — Feature Roadmap and Change Ledger` (or v4.0). Carry over active items. Keep Complete and Rejected items at the bottom of the copy for the record.
