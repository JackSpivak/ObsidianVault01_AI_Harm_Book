---
type: reference
status: developing
tags: [ontology/harm, ontology/testing]
aliases: [Harm Ontology v3 Test Summary, Test Summary, Assessment-Everywhere Test Summary, Toy Case Methodology]
created: 2026-11-18
---

# Harm Ontology v3 Test Summary

> [!warning] Status of the evidence
> Everything here is from a **fictional toy case** ("Branch ledger"), run on 2026-11-18 (runs 1–7). Nothing is adopted. Nothing from these tests is logged in [[Decisions_Log]]. Scores are Claude's draft for the author to confirm or challenge. Written from the session record and the files listed at the end; where I did not re-read a file this session, the text says so.

## 1. Why we tested
- **The question:** should the v3 harm ontology be "assessment everywhere" (variant B: every contested attribute is an Assessment by a named perspective, with a derived status) instead of the current draft (variant A: attributes asserted directly, with assessments only for some)?
- **The worry behind it (author's):** silent omission. A naive query returns one tidy answer as if it were fact, and disputed or unassessed cases quietly vanish. The book is about harms that go unseen, so the model must not hide them.
- **The risk with B:** it might fix silent omission by making the model too heavy, by producing false disputes, or by depending on a script that non-experts cannot read. So the test had to measure both gain and cost.
- **Guard against momentum:** 21 test decisions were made in one sitting, mostly by accepting recommendations. So pass criteria were written **before** modelling, and nothing is logged until tested.

## 2. Strategy (seven steps, from [[HO-002.a Assessment-Everywhere Test Strategy]])
1. Competency questions and pass criteria written first.
2. Two variants side by side (A baseline, B design).
3. Toy case first, to find structural bugs cheaply.
4. Then a sourced slice of the real Horizon case (R01): **not done**, needs research first.
5. Non-expert test: fresh subagents, no hints about joins.
6. SHACL validation: **not done**.
7. Score against the criteria written in advance.

**Adoption rule (written in advance):** B is adopted only if it passes CQ1–CQ7 and CQ9, shows no silent failure in the subagent run, and on CQ8 costs no more than A plus a named view. A silent partial answer in B is a **fail**, however elegant the expert query is.

## 3. The model excerpt that was tested
A deliberately small slice of the v3 design ([[Harm Ontology v3 - Draft Structure]]), as test vocabulary in a made-up namespace (`ho:`, `hoa:` for attributes, `toy:` for data), not the production schema.
- **Thin things:** Factor, Effect, AffectedEntity (renamed from Patient), Agent, Chain (added in run 4), Evidence.
- **Assessment machinery (variant B):** Assessment, CausalAssessment, ResponsibilityAssessment; `assesses`, `aboutAttribute`, `value`, `takenFrom` (a PerspectiveSpecification), `assessorOrganisation`, `usesProcedure`, `hasEvidence`, `assessedAt`, `repeats`, `revisedBecause`, `leftOut` and `omissionType`, `deniesValue`, `soleValue`, `assessmentHorizon`.
- **Standards:** EvaluativeStandard, PerspectiveType (with a default standard), Procedure (versioned, with value-to-band mappings).
- **Derived, never stored:** `assessmentBasis` (Stated / Inherited / Unstandardized) and claim **status** (Settled, Disputed, Corroborated, SingleSource, PartiallyAssessed, Incommensurable, NotAssessed).
- **Observed core kept separate from assessed readings:** e.g. `affects` and recorded dates on an Effect vs assessments of the same things.
- **The fictional scenario:** branch operators suffer losses. Factors: F1 software sync bug, F2 slow reconciliation, F3 liability policy, F4 operator error. Effects E1 financial loss, E2 reputational damage (dates disputed), E3 stress illness (never assessed), plus test Effects E4–E9 and E11–E15 (E10 does not exist). Six perspectives P1–P6 (CompanyX review, three forensic auditors across two firms, an operators' association, an appeal court), timeline 2010–2021. Kinds of entity are made-up stand-ins (tribe, grid, AI system, animal, herd, couple, household, partnership, LLC). It resembles Horizon on purpose but makes **no claim** about it. Legal and anthropological content is unverified.

## 4. Why these competency questions
Each question targets one way the model could fail, with a pass rule fixed in advance.

| CQ | Asks | Why it is there |
|---|---|---|
| CQ1 | Who or what caused Effect X? | Causehood only as assessed; conflicting causes side by side; the A trap is the asserted `causes` link |
| CQ2 | Which Effects are severe? (naive) | Silent omission of disputed and unassessed Effects: the author's core worry |
| CQ3 | What do all perspectives agree on? | "Fact" as a status; settled only under a shared procedure with evidence |
| CQ4 | How did a verdict change over time, and why? | Dated assessments, revision triggers, reopening a settled claim |
| CQ5 | Which judgements rest on a stated, inherited or no standard? | `assessmentBasis` |
| CQ6 | What did a perspective leave out? | Omission with a type (out of frame, blind spot, accepted harm) |
| CQ7 | Does this entity count as an AffectedEntity, of what kind, per whom? | Observed core vs assessed reading; boundary; type; unlisted kinds visible as `Unclassified`; primary vs derivative standing |
| CQ9 | Who is answerable, per whom? | Responsibility kept apart from cause |
| CQ8 | When did X occur, and who was directly affected? | **Control**: the cost of B. If B makes a simple question hard, that counts against it |

## 5. Baselines and controls
- **Variant A baseline:** the current draft, queried the way a normal user would. It shows what silent failure looks like (CQ1 naive, CQ2, CQ7).
- **CQ8 as a cost control** (see above).
- **Deliberate-breakage runs:** checks are run against a temp copy with rules removed, to show they *can* fail (run 3: 4 fail; run 7: 5 fail). The chain run has only a "horizon ignored" control, no breakage run.
- **Horizon-ignored control (run 4):** the same chain data with horizon removed from the claim key returns a false Disputed, showing what the key prevents.
- **Hand-written expected values:** each check states the intended result in advance (for example "E9: agreement but one lacks evidence → Corroborated"; the CQ5 basis per perspective).
- **Traps built into the data:** an unassessed Effect (E3), an unlisted entity kind (AidCircle), same firm without a `repeats` flag (E6), different firms with `repeats` (E7), missing evidence (E9), a settled claim later reopened (E1 severity 2016 vs 2020), a revision with no trigger (P4).

## 6. Methodology
**Toy runs (`toy_status.py`):** a Python script reads the variant B `.ttl` with rdflib, groups assessments into **claims** by target + attribute + scope (+ horizon when given; overlapping scopes count as one claim), keeps the **latest assessment per perspective** as of a date, and derives a status. Conflict rules depend on the kind of attribute: graded (compared through shared bands), non-exclusive (additive unless denied or declared sole), interval (overlap compatible, disjoint conflicts), or single-valued exclusive (subtype and `Unclassified` aware). Settling needs at least two strictly independent assessments, the same procedure and version, evidence, and no silent in-scope perspective. It prints the snapshot, runs the competency questions and PASS/FAIL checks, and runs variant A's SPARQL for comparison.

**Runs (all 2026-11-18):**
| Run | What | Result |
|---|---|---|
| 1 | First toy run | Exposed script bugs and findings 1–4 (false causal disputes, bands per attribute, attribute domains, `affects` in the core) |
| 2 | Fixes | B passed where A failed silently; finding 1 (false disputes) still wrong in kind |
| 3 | Findings 1, 5, 6, 7 | Non-exclusive attributes, revision triggers, date intervals, independence paths, CQ7 cases: 42 of 42 pass; breakage run made 4 fail |
| 4 | Chain toy test (HO-006) | Horizon as part of the claim key worked: 48 of 48 pass |
| 5 | Non-expert subagent test | No silent omission in B (A had one); snapshot lacked the observed core (CQ8 failed as built) and its labels misled |
| 6 | View fixed (legend, core, plain words, NotAssessed separate, "+n earlier") | CQ8 re-run with two fresh subagents: answered; hedged on "directly" |
| 7 | CQ5 pointer check and "why (not) settled" text | 58 of 58 pass; breakage run made 5 fail; one wording bug (label) fixed, not re-tested |

**Non-expert subagent protocol (runs 5–7):**
- Fresh subagents (general agents), plain-language questions only, no hints about joins.
- The test data was **sanitised** in a temp folder outside the vault: comments and "TEST:" labels removed so they could not leak the answers.
- Attempt 1 was **invalid** (files small enough that agents read them whole and wrote no queries); it was discarded and rerun with a **strict rule**: SPARQL only, no reading the file, no dumping the graph, answers from query results only.
- Three conditions in run 5: A (data only), B raw (data only), B snapshot (generated table only, no legend). Later runs gave the snapshot alone (an "operator" and a "busy manager" persona) and added question Q4 (why E9 is not settled).
- Agents reported queries, answers, confidence and what they could not interpret.

## 7. What the results do and do not show (draft)
- **Met in the toy case:** CQ1, 2, 3, 4, 5, 6, 9; CQ8 (after the view fix, with a wording caveat). **Partly:** CQ7 (no procedure or evidence in those cases; `affectedStanding` treated as exclusive, a test choice). No silent omission found in B; A failed silently on CQ2, CQ1 (naive) and CQ7. Adoption rule: **not fully met on this evidence.**
- **Limits:** fictional data; one run per condition; subagents are the same model family as the designer; the data is small enough to read whole; no human non-expert; join counts not measured; the status logic lives in a script, not in queries (finding 8), so readers depend on generated views; the rule is strict, so real data may rarely reach Settled (E8 settles only because it was built to).
- **Still confusing to readers:** "AGREE-BUT-NOT-SETTLED" sounds nearly settled; the severity word translation is unexplained; codes and terms (P1–P6, answerable, standing) are undefined.
- **Not done:** Horizon R01 (sourced), SHACL validation, a human test, `maxHorizon` and horizon origin for chains.
- **Open question for the author:** does "directly affected" in CQ8 mean the core `affects` or `affectedStanding = Direct`?

## 8. Files
**In the vault** (`02_Ideas Topics Concepts/Harm Ontology/`):
- `HO-002.a Assessment-Everywhere Test Strategy.md`: strategy, CQs, pass criteria, Author decisions 1–21, Variant A baseline and Variant B design
- `HO-006 Causal Chain - an Assessed Selection with a Horizon.md`: the chain idea tested in run 4
- `HO-002 Ontology Stress-Test Suite` (Horizon R01 slice, not yet run) and `HO-005 Assessed Membership and Systematic Omission`: referenced
- `ontology/Harm Ontology v3 - Draft Structure.md`: the design being tested
- `ontology/tests/toy_branch_ledger_A.ttl`: variant A data (not re-read by me this session beyond what the runner queries)
- `ontology/tests/toy_branch_ledger_B.ttl`: variant B data (read in full)
- `ontology/scripts/toy_status.py`: runner and checks (58); `README.md.txt`: run commands
- `ontology/scripts/validate_ttl.py`, `inventory.py`, `inventory_v1_v2a.csv`: migration tooling, not part of this test

**Results and handoff:** `01_The Writer's Room/2026-11-18 Harm Ontology v3 Toy Case Results.md` (runs 1–7, scoring table); `01_The Writer's Room/Handoff - Harm Ontology.md`; [[Decisions_Log]] (not changed by the tests).

**Outside the vault** (`C:\Users\conta\AppData\Local\Temp\naive_test\`, temporary): `prep.py` (strips comments), `data_A.ttl`, `data_B.ttl` (sanitised), `snapshot_B.txt`, `snapshot_B2.txt`, `snapshot_B3.txt`, `snapshot_B4.txt` (successive snapshot versions), `broken_B.ttl` (breakage copy).

**Environment:** conda env `harm-ontology` (Python 3.12, rdflib, pyshacl); `python -I`, run from the vault root.

**Content examined:** only the files above and the fictional data in them. Real Horizon sources, legal cases and vocabularies were **not** examined; references to them elsewhere are from memory and unverified.

## Related
- [[HO-002.a Assessment-Everywhere Test Strategy]]
- [[2026-11-18 Harm Ontology v3 Toy Case Results]]
- [[Handoff - Harm Ontology]]
- [[HO-006 Causal Chain - an Assessed Selection with a Horizon]]
