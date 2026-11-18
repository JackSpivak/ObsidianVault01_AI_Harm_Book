---
type: session
status: developing
tags: [ontology/harm]
aliases: [Toy Case Results, Branch Ledger Toy Case]
created: 2026-11-18
workstream: Harm Ontology
---

# Harm Ontology v3 — Toy Case Results ("Branch ledger")

> [!warning] Fictional data
> The "Branch ledger" scenario is invented. It resembles the Horizon case on purpose, as a rehearsal for [[HO-002 Ontology Stress-Test Suite]] R01, but none of it is a claim about any real case.

## Summary
- Toy case for [[HO-002.a Assessment-Everywhere Test Strategy]] (pre-test step 5), comparing variant A (attributes asserted) and variant B (assessment everywhere) on the same fictional scenario.
- **Files:** `02_Ideas Topics Concepts/Harm Ontology/ontology/tests/toy_branch_ledger_A.ttl`, `…/toy_branch_ledger_B.ttl`; script `02_Ideas Topics Concepts/Harm Ontology/ontology/scripts/toy_status.py` (moved into the vault 2026-11-18; see `README.md.txt` there). Run with the `harm-ontology` conda env, `python -I`.
- **Scenario:** Factors F1 software sync bug, F2 slow reconciliation, F3 liability policy, F4 operator error. Effects E1 financial loss, E2 reputational damage (dates disputed), E3 stress illness (no assessments). Perspectives P1 internal review, P2/P3 forensic auditors from the same firm, P6 auditor from another firm, P4 operators' association (opinion), P5 appeal court. Timeline 2010–2021.
- **Two runs.** Run 1 exposed script bugs and design gaps (see below); run 2 is the result reported here.

### Results by competency question (run 2)
| CQ | Variant A | Variant B | Verdict for B |
|---|---|---|---|
| CQ1 cause of E1 | Naive query returns **F1 only**, as fact (silent) | Run 2: **Disputed**, all five perspectives shown. **Superseded in run 3:** Corroborated {F1, F3}, all perspectives still shown (see Run 3 update) | Run 2: Pass, **but the dispute was false** (finding 1). Run 3: Pass, finding 1 fixed in the test |
| CQ2 severe Effects | Returns **E2 only**; E1 (disputed) and E3 (unassessed) silently missing | Snapshot shows E1 Disputed, E2 Open (SingleSource, Extreme), E3 Open (NotAssessed); counts shown | Pass |
| CQ3 agreement | Can't be written | Severity of E1: **Disputed** (all) → **PartiallyAssessed** (P2, P3, P6) → **Settled High** (P2, P6) | Pass; shows that scope picks the result |
| CQ4 change over time | Dated causal assessments listed; asserted attributes have no history | As-of queries trace SingleSource (2011) → Disputed (2013 on) | Partly: **no revision trigger** (finding 5) |
| CQ5 basis | Not modelled | Stated / Inherited / Unstandardized derived for all 17 assessments | Pass |
| CQ6 omission | `leftOut` for causes | Same: `leftOut` for causes only | Partly (same as A) |
| CQ7 type of unlisted kind | Forced into CollectiveArtificialPerson (silent) | Unclassified, visible (SingleSource) | Pass for (c), (d); (a), (b), (e) not tested |
| CQ9 answerability | Not answerable separately | Disputed (Manager vs CompanyX), separate from cause | Pass |
| CQ8 control | 1 query: 2009–2014, AllOperators | Core equally simple; disputed start (2009 vs 2012) also visible | Pass (after finding 4) |

### Design findings
1. **False causal disputes (major).** P4 names F3 (policy) while others name F1 (bug). Both can be causes at once, so this is not a conflict. Treating different causal values as conflicting contradicts HO-003 (causal assembly). Needs a rule: causal values conflict only when an assessment denies a cause or claims it is the sole cause.
2. **Bands must be per attribute.** Run 1 banded causes and years, making them all Incommensurable. Fixed by marking graded attributes (`ho:GradedAttribute`); a Procedure may measure several attributes.
3. **Attributes need a domain** (`ho:appliesTo`). Run 1 snapshots listed "entity type of an Effect". Fixed in the test data.
4. **`affects` must be in the observable core** in B, or CQ8 needs assessments. Fixed, in line with the triage.
5. **CQ4 revision trigger missing.** Neither variant records *why* a perspective changed its view. Needs a property (e.g. `revisedBecause → Evidence | Assessment`).
6. **Dates compared as exact values.** "2009" vs "2012" is Disputed; interval overlap isn't handled.
7. **Untested paths.** Independence (`repeats`, same firm) and Corroborated never decided an outcome, because Disputed came first; Incommensurable didn't occur after the fixes. The next toy run needs cases for these.
8. **The status logic lives in a Python script, not in queries.** Non-experts depend on the generated snapshots; the non-expert test (step 6) must check that.

### Run 3 update (same day): findings 1, 5, 6 and 7 addressed in the test
Script `toy_status.py` and `toy_branch_ledger_B.ttl` were extended; 42 checks, all pass. A deliberate-breakage run (deny, sole and subtype links removed from a temp copy) made 4 fail, so the checks can fail.

| Finding | What was done in the test | Result |
|---|---|---|
| 1 False causal disputes | `cause` and `answerable` typed `ho:NonExclusiveAttribute`: values are additive; conflict only on `deniesValue` or `soleValue` | E1 cause is now Corroborated {F1, F3}; deny (E4, E5) and sole (E4, E5) cases give Disputed; E11 Grid (Conduit) plus F1 is additive |
| 5 Revision trigger | `revisedBecause` read and reported per changed value | P1's change has a trigger (Ev3); P4's is flagged "NO TRIGGER RECORDED" |
| 6 Dates | `ho:IntervalAttribute` (`occurredDuring`): overlap compatible, value = intersection; disjoint = Disputed | 2009–2014 vs 2012–2014 → Corroborated(2012–2014); 2009–2010 vs 2012–2014 → Disputed. `occurredStart` as a point still conflicts |
| 7 Untested paths | Cases E6–E9 | Same firm without `repeats` → SingleSource; `repeats` across firms → SingleSource; missing evidence → Corroborated; all agree with evidence → **Settled(High)** (first time); E1 severity among P2,P3,P6 → PartiallyAssessed; E3 → Incommensurable |
| CQ4 reopening | as-of 2016 vs 2020, scope P2,P6,P1,P4 | Settled(High) → Disputed |
| Other attributes (type) | subtype collapses into the more specific; `Unclassified` ignored when a specific type exists | Person1, Collective2 not disputed; Tribe1 and Partnership1 Disputed |
| CQ6 non-causal | `leftOut` on a severity assessment (N6a, AcceptedHarm) | Returned with its omission type |
| CQ7 cases | tribe, grid (also a Conduit factor), AI system (standing Disputed), animal and herd, therapy couple (Relationship primary, partners separate Effects), tax household (Household primary, Relationship derivative), partnership, LLC, boundary, moral circle with observed core untouched | All as expected (made-up stand-ins) |

- **Limits:** CQ7 cases carry no procedure or evidence, so most read SingleSource (they test conflict vs no conflict). `affectedStanding` is treated as exclusive, a test choice that the AI-system dispute depends on. Variant A was not extended. Legal and anthropological content is unverified.
- **Still open:** finding 8 (non-expert test of the generated snapshots); SHACL validation; Horizon R01; whether strict settlement leaves almost nothing Settled in real data (E8 settles only because it is built to).

### Interim reading (Claude's interpretation, not a decision)
- B passed every question where A failed silently (CQ1 naive, CQ2, CQ7), and cost no more on the CQ8 control.
- But B's first visible answer to "who caused it?" was **wrong in kind** (finding 1). Visible but false disputes are a different failure from silent omission, and could be as misleading. Fix before Horizon.
- Nothing is decided by this run. Per the adoption rule, B can't be adopted until the non-expert test.

## Original wording
> "approve"
- **Attribution:** Author (approving the toy-case scenario)
- **Source:** Obsidian Copilot agent session "Harm Ontology v3 testing", 2026-11-18 (`copilot/copilot-conversations/agent__read_harm_ontology_v3_handoff._rename_chat_to_Harm_Ontology@20261118_004932.md`)

> "The scenario is deliberately *like* Horizon, so the toy case rehearses R01. Its facts are invented and won't be read as claims about the real case."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)
- **Source:** same session

- **External references:** [[HO-002.a Assessment-Everywhere Test Strategy]] (Author decisions 3, 5–21; Variant A baseline; Variant B design); [[Harm Ontology v3 - Draft Structure]]; [[HO-003 Causal Assembly - the Perfect Storm]].

## Related
- [[Handoff - Harm Ontology]]
- [[HO-002.a Assessment-Everywhere Test Strategy]]
