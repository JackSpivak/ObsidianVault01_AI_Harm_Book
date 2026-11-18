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
  - **toy case run once**
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
  - Files: `ontology/tests/toy_branch_ledger_A.ttl`, `…_B.ttl`; script `~/harm-ontology-scripts/toy_status.py`.

## Next step
1. **Causal-conflict rule (toy finding 1, major).** B marked "who caused it?" as Disputed only because two perspectives named *different* causes (policy vs bug), which can both be true. That contradicts HO-003.
   - Proposal, not decided: causal values conflict only when an assessment **denies** a cause or claims a cause is the **only** one.
   - Do any other categorical attributes (answerability, type) have the same problem?
2. **Toy run 2:**
   - add a revision trigger (finding 5, e.g. `revisedBecause`)
   - add cases that test independence / `repeats`, Corroborated and Incommensurable (finding 7)
   - compare date intervals by overlap (finding 6)
3. Then the **non-expert subagent test** (CQ1, CQ2, CQ8, given the schema only). It must check whether depending on script-generated snapshots causes silent failures (finding 8).
4. Then **Horizon R01**, which needs sourced research first.
- Alternative track: Migration Phase 0, continued (open `# Master Formal Ontology of Harm (Part 1…)`, compare v1 and v2, and extract inventories by script).

## Pending (proposed, not decided; see [[HO-005 Assessed Membership and Systematic Omission]])
- Splitting Assessment into Causal / Valence / Responsibility. The toy case used a separate ResponsibilityAssessment, test only.
- Causal standards (but-for, NESS, INUS…) as a second family of standards.
- Reifying `participatesIn` as a claim.
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
- Scripts go in `~/harm-ontology-scripts/`, outside the vault. Test `.ttl` files go in `02_Ideas Topics Concepts/Harm Ontology/ontology/tests/`.

## Sub-workstreams
- **PerspectiveType consolidation (HO-II.d):** done 2026-11-17. Follow-ups: [[Handoff - Perspective Vocabulary and v3 Follow-ups]].

## Read first
- This note, then [[HO-002.a Assessment-Everywhere Test Strategy]] (Author decisions, Variant B design, Variant A baseline) and [[2026-11-18 Harm Ontology v3 Toy Case Results]].
- [[Harm Ontology v3 - Draft Structure]] and [[Harm Ontology Migration Plan]] as needed.

## Previous sessions
- 2026-11-18 "Harm Ontology v3 testing": `copilot/copilot-conversations/agent__read_harm_ontology_v3_handoff._rename_chat_to_Harm_Ontology@20261118_004932.md`
- 2026-11-17/18 "read Harm Ontology v3 handoff": `copilot/copilot-conversations/agent__read_Harm_Ontology_v3_handoff@20261117_235104.md`
- [[2026-11-14 Harm Ontology Redesign]] (transcript: `copilot/copilot-conversations/agent__philosopher_adverse_stress_test_harm_ontology@20261114_071639.md`; read selectively, don't reopen the chat)
