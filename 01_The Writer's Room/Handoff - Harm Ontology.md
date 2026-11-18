---
type: session
status: developing
tags: [handoff, ontology/harm]
aliases: [Harm Ontology Handoff]
created: 2026-11-15
updated: 2026-11-18
workstream: Harm Ontology
latest_session: "[[2026-11-18 Harm Ontology v3 Toy Case Results]]"
---

# Handoff — Harm Ontology

*Rolling, forward-facing note. Overwrite it at each session close; history lives in the session notes and in git. Attach this note to start a new chat.*

## Status
- The v3 **design** is drafted in [[Harm Ontology v3 - Draft Structure]]. No production v3 `.ttl` exists yet.
- **Assessment-everywhere test** ([[HO-002.a Assessment-Everywhere Test Strategy]]):
  - agreement rule v1 complete
  - variant B designed
  - variant A baseline written
  - **toy case run three times** (run 3: 42 of 42 checks pass; findings 1, 5, 6, 7 addressed in the test)
- **Migration Phase 0** is partly done: the v1 `.ttl` is repaired and validated, and the tooling is ready.
- **Nothing is adopted.** Variant B can't be adopted until the non-expert test passes.

## Done 2026-11-18 (session "Harm Ontology v3 testing")
- **Logged in [[Decisions_Log]]:** Patient renamed **AffectedEntity**, with:
  - altLabels "patient" and "moral patient"
  - `patientStanding` → `affectedStanding`
  - `forPatient` → `forAffectedEntity`
  - `standingOfSubjects {agent · affected · datum}`
- **Where the rename has been applied:** the draft structure, [[PerspectiveStructure 0.02]] and HO-002.a. The other ~17 notes and the v1 `.ttl` are deferred to migration (memory list item 10). Propose those edits as a list first, and never change verbatim quotes.
- **Test-only decisions in HO-002.a (Author decisions 5–21):**
  - `assessmentBasis: Stated | Inherited | Unstandardized`, derived by script
  - Procedure as a separate class
  - **asymmetric rule** for every attribute: settling needs the same Procedure and version; disputing needs only a conflict, under any procedure
  - unstandardized dissent counts
  - same-claim test is target + attribute + scope, and overlapping scopes count as the same claim
  - graded values compared through shared bands
  - scope is declared and shown
  - silence blocks settlement
  - settling needs ≥2 strictly independent assessments
  - latest assessment per perspective, with an as-of date
  - evidence required
  - statuses shown in two layers (Settled / Disputed / Open)
  - Effect `occurredDuring`
- **Toy case "Branch ledger"** (fictional): [[2026-11-18 Harm Ontology v3 Toy Case Results]].
  - B passed every question where A failed silently (CQ1 naive, CQ2, CQ7) and cost no more on the CQ8 control.
  - Files: `ontology/tests/toy_branch_ledger_A.ttl`, `…_B.ttl`; script `ontology/scripts/toy_status.py`.

## Done in the toy case (2026-11-18, runs 2–3; test only, nothing logged as a decision)
- **Finding 1 (false causal disputes), fixed in the test:** attributes can be *non-exclusive* (`cause`, `answerable`). Different values are additive; conflict only if an assessment **denies** a value (`deniesValue`) or claims it is the **sole** one (`soleValue`). Also checked on `answerable`.
- **Finding 6 (dates), fixed in the test:** interval attribute `occurredDuring` ("YYYY-YYYY"): overlap is compatible (agreed value = intersection), disjoint is Disputed. `occurredStart` (a point) still conflicts on different years.
- **Finding 5 (revision trigger), in the test:** `revisedBecause`; the script reports each changed value with its trigger and flags a change with none (P4's, deliberately).
- **Finding 7 (untested paths), covered:** independence (same firm without `repeats`; `repeats` across firms), Corroborated (missing evidence; different procedures), PartiallyAssessed, Incommensurable, and Settled (E8, first time reached). CQ4: Settled (2016) reopened as Disputed (2020).
- **Exclusive attributes (entity `type`):** disjoint types conflict; a subtype with its supertype and `Unclassified` with a specific type do not.
- **CQ6 beyond causes** (omission on a severity assessment) and **CQ7 cases** (tribe, grid, AI system, animal/herd, therapy couple, tax household, partnership, LLC, boundary, moral circle, observed core vs assessed reading) run on made-up stand-ins.
- Result: 42 of 42 checks pass; a deliberate-breakage run made 4 fail, so the checks can fail. See [[2026-11-18 Harm Ontology v3 Toy Case Results]].
- **Limits:** CQ7 cases have no procedure or evidence, so they test conflict vs no conflict only (mostly SingleSource); `affectedStanding` is treated as exclusive (a test choice); variant A was not extended; legal and anthropological content is unverified.

## Next step
0. *Optional, small, do first:* the **Chain toy test** ([[HO-006 Causal Chain - an Assessed Selection with a Horizon]]): one chain assessed at two horizons; pass if the horizons are separate claims and a same-horizon conflict still shows Disputed. Keeps the schema stable before the non-expert test.
1. **Non-expert subagent test** (CQ1, CQ2, CQ8, given the schema only). It must check whether depending on script-generated snapshots causes silent failures (finding 8). B cannot be adopted until this passes.
2. **SHACL validation:** nodes with no assessment, shortcuts with no status.
3. **Score** against the pre-written criteria (HO-002.a).
4. **Horizon R01**, which needs sourced research first (new chat). Also checks whether anything reaches Settled in real data.
5. Re-read author decisions 5–21, then decide the pending items below.
- Alternative track: Migration Phase 0, continued (open `# Master Formal Ontology of Harm (Part 1…)`, compare v1 and v2, and extract inventories by script).

## Pending (proposed, not decided; see [[HO-005 Assessed Membership and Systematic Omission]])
- Splitting Assessment into Causal / Valence / Responsibility. The toy case used a separate ResponsibilityAssessment, test only.
- Causal standards (but-for, NESS, INUS…) as a second family of standards.
- Reifying `participatesIn` as a claim.
- **v4 proposed: a Chain class.** v3 has `CausalRole` "in one chain" but no Chain object. Idea: a thin Chain bounded by a horizon (finite `maxHorizon`), horizon part of the claim key; first test is one chain at two horizons in the toy case. See [[HO-006 Causal Chain - an Assessed Selection with a Horizon]].
- HO-003's "jointly sufficient" becoming "as assessed".
- The evidence anchor. It's now built into the test design as Evidence plus Observation, but not decided.
- AffectedEntity proposals listed in HO-002.a: type as an assessment, `Unclassified`, NaturalSystem / EngineeredSystem, `affectedStanding`, CollectiveNaturalGroup, Household.

## Cautions
- **Momentum:** 21 test decisions were made in one sitting, mostly by accepting Claude's recommendations. The author values reflection over quick agreement. Consider re-reading decisions 5–21 before building more on them.
- The rule is strict enough that in real cases **almost nothing may reach Settled**. That might be honest, or it might make the model useless. Watch for this in Horizon.
- Toy data is **fiction**: it resembles Horizon on purpose but makes no claims about it.
- Claims that the structure "blocks" traps are **hypotheses**. Run tests, don't assert.
- **Don't log test-only decisions or pending items** until they've been tested.
- Many references are **from memory, unverified**: legal cases, Horizon details, Wilber, NESS/INUS, the vocabularies, Lorenz, Meadows, and the war ending of the Sai Weng parable.
- Old **root files** (`Interdisciplinary_Harm_Ontology_Compendium.md`, `Interdisciplinary Harm Ontology.ttl`) are untouched and awaiting an archive decision. Ask before moving or deleting.

## Tooling
- Conda environment `harm-ontology`: `~/anaconda3/envs/harm-ontology/python.exe -I …` (rdflib, pyshacl).
- Scripts now live **in the vault** (so they reach GitHub) in `02_Ideas Topics Concepts/Harm Ontology/ontology/scripts/` (`toy_status.py`, `validate_ttl.py`, `inventory.py`, `inventory_v1_v2a.csv`, and `README.md.txt` with run commands). Test `.ttl` files go in `…/ontology/tests/`. The old `~/harm-ontology-scripts/` copy is a duplicate; edit the vault copy. Third-party `.ttl` downloads stay outside the vault.

## Sub-workstreams
- **PerspectiveType consolidation (HO-II.d):** done 2026-11-17. Follow-ups: [[Handoff - Perspective Vocabulary and v3 Follow-ups]].

## Read first
- This note, then [[HO-002.a Assessment-Everywhere Test Strategy]] (Author decisions, Variant B design, Variant A baseline) and [[2026-11-18 Harm Ontology v3 Toy Case Results]].
- [[Harm Ontology v3 - Draft Structure]] and [[Harm Ontology Migration Plan]] as needed.

## Previous sessions
- 2026-11-18 "Harm Ontology v3 testing": `copilot/copilot-conversations/agent__read_harm_ontology_v3_handoff._rename_chat_to_Harm_Ontology@20261118_004932.md`
- 2026-11-17/18 "read Harm Ontology v3 handoff": `copilot/copilot-conversations/agent__read_Harm_Ontology_v3_handoff@20261117_235104.md`
- [[2026-11-14 Harm Ontology Redesign]] (transcript: `copilot/copilot-conversations/agent__philosopher_adverse_stress_test_harm_ontology@20261114_071639.md`; read selectively, don't reopen the chat)
