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

### Run 4 update (same day): Chain toy test (HO-006), test only
Script and `toy_status.py` extended: `assessmentHorizon` (years) joins the claim key **only when given**, so existing keys are unchanged. Data: a thin `toy:Ch1` (Chain: identifier and label only) with four assessments of `netOutcome` (H1–H4). 48 of 48 checks pass (42 old + 6 new); the old results did not change.
- Horizon 2: P2 and P6 agree (NetBeneficial); shows PartiallyAssessed because P3, who uses the same procedure, is silent. Not a conflict.
- Horizon 20: P2 NetHarmful vs P1 NetBeneficial → **Disputed** (a same-horizon conflict still shows).
- Two horizons = two separate claims (keys 2 and 20).
- **Control:** with the horizon ignored, one claim → Disputed (the false dispute the key prevents).
- P2 holds NetBeneficial at 2 and NetHarmful at 20 at once; under "latest per perspective" without horizon in the key, the 2-year verdict would be overwritten (Sai Weng flip stays visible).
- **Not tested:** `maxHorizon` as a ceiling on a Procedure or standard; what the horizon is measured from; cut by time vs link count vs probability (only years used); chain membership and `withinChain`; a future horizon forcing `chainStatus: Extrapolated`. No deliberate-breakage pass was run for these 6 checks (only the control).
- Hypothesis that survived one fictional test; **not a decision**, not logged in [[Decisions_Log]].

### Run 5 (same day): non-expert subagent test (finding 8), first pass, NOT a pass/fail verdict
**Setup.** Fresh subagents (same model family as the designer), CQ1, CQ2, CQ8 asked in plain words, no hints about joins. Files in a temp folder outside the vault: comments and "TEST:" labels stripped from the `.ttl` (labels like "TRAP" would leak the answers); `snapshot_B.txt` = the script's snapshot table only (no checks). Three conditions: A (data only), B raw (data only), B snapshot (table only, no legend).
- **Attempt 1 (invalid for the purpose):** the files were small, so all three agents read them whole and wrote no queries. Discarded as evidence about *queries*; its observations are kept below only as marked.
- **Attempt 2 (enforced):** no reading the file, no graph dump, answers only from SPARQL results; the snapshot agent got the table alone.

| | A (queries) | B raw (queries) | B snapshot (table only) |
|---|---|---|---|
| CQ1 cause of E1 | Direct `causes` link (F1) plus assessments of F1, F4, F3; "F1 best supported", medium confidence. It listed the predicates first, which is why it found the assessments (a hurried user might not). | F1 most supported, F4 (2010) and F3 as dissent, `leftOut` and `revisedBecause` noticed; also separated answerability from cause. Counted "six" F1 assessments (five). | F1, with F3 as an alternative; treated `answerable` as a separate question. Read "Corroborated({F1, F3})" correctly as two surviving causes. |
| CQ2 severe | **E2 only** (Extreme); E1 reported as Medium (one asserted value); E3 flagged "no severity". E1's dispute and E6–E9 never seen. **Silent partial answer.** | E2 (Extreme) and E1, E6–E9 (High) listed; applied band mappings itself; noticed E1's 4/10 and Low; E3 Medium; did not apply independence or settlement rules. Not silent, but expensive. | E2, E6–E9 clear; E1 "Disputed, can't call it severe"; E3 Incommensurable. Visible, nothing dropped. |
| CQ8 when / who | 2009–2014; AllOperators; high confidence. Cheapest. | Same, plus the 2009 vs 2012 start dispute found. | When: found 2012–2014 and the disputed start. **Who was directly affected: "the table doesn't say"** (the snapshot has no observed core; `affectedStanding` read NotAssessed). |

**What the snapshot agent could not interpret or found misleading (its own words, paraphrased):**
- No legend: columns, `-`, P1–P6, `answerable`, `standing`, `@2015`; the table gives no Effect labels.
- **"Corroborated" does not read as agreement:** E1 cause is Corroborated with two different values; E2 duration is Corroborated though the sources' ranges differ (narrowed to the intersection, so 2009–2011 vanishes from the headline).
- **"SingleSource" on E6 and E7 reads wrong** when two sources agree (it means one independent organisation).
- 64 of 86 rows are NotAssessed, all shown as **Open**: a reader could take gaps for findings, and Open also holds SingleSource and Corroborated. (Decision 20 asked for exactly this check; here the bracketed detailed status was visible, so the agent separated them. With the two-layer view only, it would not.)
- E2 severity shown as "Extreme" while the source says "critical" (harmless, but a translation it did not announce).

**Reading (Claude's, not a decision):**
- B raw and the snapshot showed **no silent omission of a disputed or unassessed item**; A did (CQ2). That is the same direction as run 2.
- B's costs appeared elsewhere: **CQ8 through the snapshot alone fails** (the observed core is missing), and the status vocabulary needs a legend and plainer labels. Whether that counts as a "fail" under the pre-written rule ("a silent partial answer in B is a fail") is the author's call: it is partial but not silent (NotAssessed is shown), though it could mislead.
- **Limits:** one run per condition; subagents are the same model family as the designer; the data is small enough to read whole (attempt 1), so larger data may behave differently; "A" was helped by agents listing predicates first; the agent's row count (87) was wrong (86), so even careful readers err; no human non-expert. Not yet scored against the criteria.
- Files: `C:\Users\conta\AppData\Local\Temp\naive_test\` (outside the vault; regenerate with `prep.py` and the script's snapshot section).

### Scoring against the criteria written in advance (Claude's scoring; the author confirms)
Criteria: [[HO-002.a Assessment-Everywhere Test Strategy]] (CQ table, Scoring section). Evidence is **toy case runs 2–5 only** (fictional data, same-family subagents). Scale: Yes / Partly / No; "silent" or "visible" for a naive query's failure. Join counts were **not measured**; complexity below is qualitative from the subagent runs.

| CQ | A | B | Why for B |
|---|---|---|---|
| CQ1 cause | Partly, **silent** (naive `causes` returns F1 as fact; assessments found only if the user lists predicates) | **Yes** (toy) | Corroborated {F1, F3}, all perspectives listed, none picked. Caveat: the standard shows only via CQ5; the snapshot keeps the latest view per perspective, so P1's 2010 F4 is not in it (history needs as-of queries) |
| CQ2 severe | **No, silent** (E2 only; E1 dispute, E3 gap dropped) | **Yes** | Settled, Disputed and Open all shown with status and counts, in the snapshot and in raw queries |
| CQ3 agreement | No (cannot be written) | **Yes** (toy) | Settled only for E8, with evidence required. Caveat: E8 is built to settle; no real data has reached Settled |
| CQ4 over time | Partly (dated assessments; no history for asserted attributes) | **Yes** (toy) | As-of 2016 Settled, 2020 Disputed; each change shows its trigger, P4's missing one flagged |
| CQ5 basis | No | **Partly** | Stated/Inherited/Unstandardized derived for every assessment; "Inherited points to the default standard" was not checked by the script |
| CQ6 omission | Partly | **Yes** (toy) | `leftOut` with omission type on causal and severity assessments. Systematic omission (HO-005) not tested |
| CQ7 AffectedEntity | No, silent (forced into a type) | **Partly** | (a)–(e) all ran as expected, but on made-up stand-ins with no procedure or evidence, and `affectedStanding` treated as exclusive (a test choice the AI-system dispute depends on) |
| CQ9 answerability | No | **Yes** (toy) | Disputed, kept apart from cause |
| CQ8 control | **Yes**, cheapest | **No, as built** (Yes via a raw core query) | The rule allows "A plus use of a named view". The named view (snapshot) lacks the observed core, so "who was directly affected" cannot be answered from it |
| Subagent run: silent failure? | A: **yes** (CQ2) | **None found**, but **misleading** labels | No disputed or unassessed item dropped. "Corroborated" and "SingleSource" mislead lay readers; "Open" lumps 64 NotAssessed with SingleSource and Corroborated |

**Adoption rule** (B only if it passes CQ1–CQ7 and CQ9, shows no silent failure in the subagent run, and on CQ8 costs no more than A plus a named view):
- CQ1, 2, 3, 4, 6, 9: met in the toy case. CQ5 and CQ7: **partly**. Subagent run: **literally met**, with the label caveat. CQ8: **not met as built**.
- **Result: B is not adoptable on this evidence.** Gaps are fixable in the *view* rather than the model: add the observed core to the snapshot; add a legend and Effect labels; plainer status labels; do not let "Open" merge NotAssessed with the rest (decision 20's fallback: show all seven). Then re-run CQ8.
- **Not yet scored:** the Horizon (R01) slice, SHACL validation, whether anything reaches Settled in real data, human non-experts, the chain extension.
- Score by an interested party (the designer's assistant): treat as a draft for the author to challenge. A re-run with fixed views, a human or larger data is the check on it.

### Run 6 (same day): snapshot view fixed, CQ8 re-run
**View changes in `toy_status.py`** (the model and data did not change; 48 of 48 checks still pass): a legend at the top; an Effect label on each block; the **observed core** (`affects`, recorded dates) shown beside the assessed readings; plain status words (SETTLED, DISPUTED, AGREE-BUT-NOT-SETTLED, ONE-INDEPENDENT-SOURCE, PARTLY-ASSESSED, NOT-COMPARABLE, NOT-ASSESSED), so NotAssessed is no longer merged into Open (a quick-scan layer Settled / Disputed / Open is kept); NOT-ASSESSED attributes listed in one line per Effect; "+n earlier" marks older views that the "latest per perspective" rule hides.

**Re-run:** two fresh subagents (a non-technical operator, a busy manager), each given only the new snapshot (`snapshot_B2.txt`, "TEST:" labels stripped), same three questions.
- **CQ1:** both: F1 main, F3 possible second cause, not a conflict; kept `answerable` apart from cause.
- **CQ2:** both: E8 firmly severe (only SETTLED), E2/E6/E7/E9 probably, E1 unclear (disputed), E3 not comparable, the rest not assessed. No Effect dropped.
- **CQ8 (was the failure):** both now state **AllOperators** from the core and the dates (recorded 2009–2014; start disputed 2009 vs 2012; end agreed 2014). Both **hedged on "directly"**, because `affectedStanding` is NOT-ASSESSED for E2.
- **Still found confusing or risky (their words, paraphrased):** AGREE-BUT-NOT-SETTLED "sounds reassuring"; ONE-INDEPENDENT-SOURCE can look strong when two assessors agree; why E9 is not settled while E8 is, is not shown (missing evidence is not displayed); the "+2 earlier" views are hidden; E1 cause lists two values a skimmer might read as both confirmed; core and assessed dates differ and the table does not say which to trust; F1/F3/P1–P6 and the severity band translation are unexplained; most Effects unlabelled; E15's Couple1 line under a household Effect looked odd.
- **No wrong conclusion was drawn by either agent.** n = 2, same model family as the designer, legend given, no human.
- **Open wording question for the author:** does "directly affected" in CQ8 mean the core `affects`, or `affectedStanding = Direct`? The hedge is correct under the second reading; under the first, B now answers as A does.

**Re-score (draft):** CQ8 moves from *No as built* to **Yes, with the wording caveat above**. Subagent run: no silent failure, label risks reduced but not gone. **CQ5 and CQ7 remain Partly** (toy limits), so the adoption rule is still **not fully met**, but the remaining blockers are no longer the snapshot. Suggested next: have the script check that Inherited points to the default standard (CQ5); show *why* a claim is not settled (missing evidence, different methods, silent perspective); then Horizon.

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
