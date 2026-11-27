---
fileClass: Idea
type: task
status: seed
bookmark: draft
canonical_id: ho-assessment-structure-initial-thinking
territory: new
tags: [ontology/harm, assessment, task]
aliases: [Assessment Structure Initial Thinking, HarmAssessment initial thinking]
created: 2026-11-22
---

# Task - Assessment Structure: Initial Thinking

## Why this is distinct
- Captures the first pass at the assessment structure of the harm ontology, from the opening of the 2026-11-22 session to the point where `enablesAssessment` was proposed (about 12:17 in the chat). It is a record of thinking, not a decision. Nothing here is logged in [[Decisions_Log]].
- It sits between the v3 draft's existing `Assessment` class and the proposed `HarmAssessment` line. The ledger tracks the open items that come out of it.

## Anticipated direction
- Make `HarmAssessment` the judging class that everything valuable hangs from, with `DisciplinePerspective` as the thing that enables it.
- Let functional subclasses record what an assessment is for (purpose or use), separately from which discipline is doing the looking.
- Keep the three layers apart: the schema records the class and its relations, profiles set what each kind must contain, and vocabulary holds the words.
- Next step: settle the placement test and the subclass structure, then test them (see the Handoff, "Current focus").

## Conceptual territory
- Judgment as assessment (HO-II.a, HO-II.c): an assessment is one judgment, made under a standard, from a perspective, for an affected entity.
- Perspective as enabler (PerspectiveType, DisciplinePerspective): a discipline's perspective generates many assessments rather than tagging them.
- Purpose and function (not yet a bookmark): what an assessment is called into being to do (regulatory, forensic, diagnostic, normative critique). These differ in burden of proof, closure and actionability.

## Summary
The assessment structure started from the v3 draft, where `Assessment` is one judgment with these properties (as set out in the draft, rev 2026-11-20):
- `assesses` → Factor, CausalRole, Effect, Outcome, FactorAssembly or PerspectiveType
- `takenFrom` → PerspectiveSpecification
- `forAffectedEntity` (renamed from `forPatient`, 2026-11-18)
- `verdict`: Harmful, Beneficial, Mixed, Neutral or Contested; `verdictStatus`: Provisional or Final
- scope: `declaredScope`, `acknowledgedExclusions`, `scopeAdequacy` (never Complete)
- epistemic metrics: `confidence`, `criticality`, `sensitivity/leverage`

Its subclasses are `CausalAssessment` (adopted 2026-11-17), the pending `ValenceAssessment` and `ResponsibilityAssessment` (HO-005), and profiles (Personal, Moral, Expert, Regulatory, Threat, Algorithmic, Judgment).

The author then proposed:
1. `HarmAssessment` as a class that **has** a discipline perspective (`hasDisciplinePerspective`).
2. That the discipline perspective **enables** assessments, because one perspective is meant to support many kinds of assessment.
3. That specific subclasses of `HarmAssessment` may say what type of assessment an instance is, possibly according to its intended function, use or purpose. The author said at this point: "im not clear yet".

Claude's proposed response, marked as Claude's proposal and not the author's:
- `DisciplinePerspective` as a specialisation of `PerspectiveType`, acting as the lens that makes an assessment possible.
- Four functional subclasses of `HarmAssessment`:
  - `RegulatoryAssessment`: statutory triggers and binding enforcement
  - `ForensicAssessment`: ex-post incident analysis and causal chains
  - `DiagnosticAssessment`: well-being, affected-entity standing and remediation
  - `NormativeCritiqueAssessment`: systemic or captured-assent critique, where no rule was broken
- The relation renamed `enablesAssessment` (domain DisciplinePerspective or PerspectiveType, range HarmAssessment), at the author's suggestion, because one perspective enables many assessments.

The diagram drawn in this stretch shows the v3 assessment tree with these additions marked as proposed.

## Real-world examples
- An environmental impact assessment: a regulatory assessment inside a legal regime, with a veto held by the regime, not the assessor. (From the 2026-11-21 searchlight session.)
- An incident report (air crash or AI incident): a forensic assessment, which isolates trigger factors and chains.
- A tort claim and an academic ethics critique of the same system: same skeleton, but different closure rules and burdens of proof. This is the case that motivated functional subclasses.

## Why it matters to the book
- It makes "who judged this, from which discipline, and for what purpose?" a required question. That makes assessments of the same event comparable, and makes disagreement between them explicable.
- Functional subclasses explain why a regulator and a critic can reach different verdicts without either being wrong about the facts.

## Open questions
- Is a discipline's perspective the same kind of thing as a tradition's? Working answer: yes (ledger S21). CP-01 depends on it.
- Are the functional subclasses mutually exclusive, or can one assessment be both forensic and regulatory?
- Subclasses (a class hierarchy) or a controlled vocabulary of purpose values on one class?
- How do the functional subclasses sit with the pending Causal / Valence / Responsibility split (HO-005, ledger K1)?
- Where do the gap groups (mandate, valuation, procedure, remedy) go: PerspectiveType, a procedural layer, or HarmAssessment (ledger S26)?
- Does Protégé show multi-level assessment subclasses cleanly?
- Is "purpose" the right word, or should it be "function" or "use"? The author said "I'm not clear yet."

## Original wording
> "thought about assesssment . HarmAssessment (class) will hasDisciplinePerspective"
- **Attribution:** Author

> "and something new also nuance DisciplinePerspective enables HarmAssessment. this is because we want it to be able to enable/support many different types or instances of harm assessment. there may be certain HarmAssessment subclasses that would clarify what type of HarmAssessment a particular instance it is. these categories may relate to the intended function or use or purpose. im not clear yet"
- **Attribution:** Author

> "perhaps enablesAssessment should be used because a perspective may be an enabler of many things"
- **Attribution:** Author

- **Source:** Copilot chat, 2026-11-22 ("explore assessment structure"). Session note: [[2026-11-22 Harm Ontology Ledger and Assessment Session]].
- **External references:** none checked in this stretch.

## Real-world examples (not yet tested)
- See above. Each is a candidate for a toy case in [[HO-002 Ontology Stress-Test Suite]].

## Related
- [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)]]
- [[HO-II.a Assessment and Evaluative Standard]]
- [[HO-II.c Judgment as Assessment - Reasoning over Precedent]]
- [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] (items S1, S21, S26, K1)
- [[2026-11-22 Harm Ontology Ledger and Assessment Session]]
- [[Handoff - Harm Ontology]]

---
**Scope note:** the chat carries no visible timestamps to me, so "about 12:17" is matched by content, not by clock time. This note covers the assessment discussion from the start of the session to the `enablesAssessment` decision. It does not cover the ledger work that followed.
