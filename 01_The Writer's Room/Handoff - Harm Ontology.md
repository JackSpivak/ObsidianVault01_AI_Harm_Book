---
type: session
status: developing
tags: [handoff, ontology/harm]
aliases: [Harm Ontology Handoff]
created: 2026-11-15
updated: 2026-11-19
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
- **Where the rename has been applied:** the draft structure, [[PerspectiveStructure 0.02]], HO-002.a, and (2026-11-18, author-approved list "A") 21 lines in 12 notes: HO-I.b, HO-I.c, HO-II.a, HO-II.b, HO-II.e, HO-premise, HO-002 Stress-Test Suite, the Bookmark Index, the Migration Plan, the Crosswalk (Meta-Category V), and two _Unfiled Ideas notes. **Left on purpose:** verbatim quotes, older Decisions_Log entries, the 2026-11-14 session note, PerspectiveStructure 0.01, the council reviews, real medical "patient", chat transcripts. **Still deferred to migration:** `hasPatientOntology`, `PatientOntologyValue`, "Moral Patient (`hasMoralPatient`)" in the v1 `.ttl` (and the root copy), the v1/v2/v2a compendia and Master Formal Ontology Part 1 (deprecate and map, don't edit in place). Never change verbatim quotes.
- **Paused (author, 2026-11-18):** formal v3 testing is on hold; the author will use v3 informally against real-world data and collect v4 updates and improvements first. No production `.ttl` or compendium yet.
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
0. **Chain toy test: done** (run 4, 48 of 48 pass; see [[2026-11-18 Harm Ontology v3 Toy Case Results]]). Horizon in the claim key worked in the test. `maxHorizon`, horizon origin and `withinChain` untested. Test only, not logged.
1. **Non-expert subagent test: first pass done (run 5), not scored.** No silent omission in B (A had one, CQ2). Findings: the snapshot alone cannot answer CQ8 "who was directly affected" (no observed core); "Corroborated" and "SingleSource" read misleadingly; "Open" lumps 64 NotAssessed with the others; no legend. Limits: n=1 per condition, same model family, small data. Decide whether to re-run with a fixed snapshot (core columns, legend, plainer labels), with a human, or with larger data; then score. B still can't be adopted until the author calls it. See [[2026-11-18 Harm Ontology v3 Toy Case Results]].
2. **SHACL validation:** nodes with no assessment, shortcuts with no status.
3. **Scored (draft, toy evidence only)** against HO-002.a: CQ1, 2, 3, 4, 6, 9 met; CQ5 and CQ7 partly. **Run 6: snapshot view fixed** (legend, core, plain labels, NotAssessed separate, "+n earlier") and CQ8 re-run with 2 fresh subagents: CQ8 now **Yes, with a wording caveat** (author: does "directly affected" mean core `affects` or `affectedStanding = Direct`?). B still not fully met (CQ5, CQ7 partly). **Run 7 done:** CQ5 pointer check added (basis → its standard; passes; 58 of 58 checks, breakage run made 5 fail) and the snapshot now says *why* a claim is or isn't settled; one wording bug fixed (UNDER-TWO-INDEPENDENT-SOURCES, not re-tested with a reader). CQ5 now **Yes (toy)**; CQ7 still **Partly** (no procedure or evidence in the CQ7 cases). Remaining view confusion: "AGREE-BUT-NOT-SETTLED" sounds nearly settled, severity band translation unexplained, codes undefined. Author to answer the CQ8 "directly" wording question, then confirm or challenge the scoring, then Horizon. See [[2026-11-18 Harm Ontology v3 Toy Case Results]].
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

## Which files to use for the property-attachment question (added 2026-11-19)
**There is no full v3 `.ttl`.** The design lives in [[Harm Ontology v3 - Draft Structure]] (a markdown outline, the source for each class's properties). For how instances get their properties in Protégé, work with **only** this file:
- **Use:** `02_Ideas Topics Concepts/Harm Ontology/ontology/tests/editor_first_mini/ho-editor-mini.ttl` (an identical RDF/XML copy, `ho-editor-mini.owl`, is beside it; README there). It models only PerspectiveType and PerspectiveSpecification attributes; Assessment, CausalAssessment, Person, Agent and the other classes are stubs, so it is **incomplete on purpose** for this question.
- **Superseded, do not use for this question:** `ontology/tests/three_layer_mini/` (four files plus catalog; the first mini example; judged "awful" by the author; no domains, ranges or groups).
- **Not the schema:** `ontology/tests/toy_branch_ledger_A.ttl` and `…_B.ttl` are test data for the assessment-everywhere test (fictional; the `hoa:` attribute vocabulary, Procedure, Evidence and the status script are test-only).
- **Not v3:** `ontology/Interdisciplinary Harm Ontology v1.ttl` and the root `Interdisciplinary Harm Ontology.ttl` (v1; do not edit; the root one awaits an archive decision).
- Both minis are **test artefacts with placeholder IRIs**, not the v3 release. The mini's builder scripts are one-off migration tools, not part of day-to-day work.

## Open issues and to-dos added 2026-11-19 (unresolved; track until closed)
- **Agents, participation and assessing organizations (proposed bookmark HO-007; awaiting author confirmation; no page or index entry yet).**
  - Raised by the author: a Person (or any Agent) as an agent of harm by participating in an Event that participates in a FactorAssembly (foundational case: robbers in a robbery that causes loss of a pecuniary interest); a lion in a zoo that maims someone who falls into the enclosure; flood water and windblown debris in a storm; whether agency requires sentience; PerspectiveSpecification `assessor` as organizations of all kinds (contracted audit firms, UL-type testing agencies, regulators assessing safety, competence or compliance).
  - Proposed shape (not decided): one root HO-007 with tiers: **I** what counts as an agent (separate axes: causal capacity, purposive action, capacity to answer); **II** participation in events and roles in it (`Agent → Event → FactorAssembly`; participation is not responsibility, which stays with the pending ResponsibilityAssessment); **III** assessing organizations (independence, authority, capture). Candidate `HO-007-premise`: "agency is a role in an assessed participation, not an intrinsic kind" (a hypothesis, not a decision). Inanimate things (flood water, debris, a grid) are Factors with a CausalRole (Conduit / ProximateCause), not agents.
  - **To resolve:** bookmark shape (one with tiers, or separate); an Event class (v3 has Factor kinds Act and Process but no Event; 0.02 has `originatingCircumstance → Event` as a stub); a participation relation for Agents and roles in it; what `Agent (?)` covers (Person, organization, animal, AI system); link to the Causal / Valence / Responsibility split.
  - **Tests to add to HO-002 (pending approval; add and run when implemented):** the robbery; the lion in the zoo; the storm with flood and debris; assessor independence and capture. Unverified from memory: legal participation doctrines (principal, accessory, conspiracy, vicarious liability), linguistic agent / force / instrument roles, the OBO Relation Ontology and BFO "participates in".
- **Editor-first requirement (author, 2026-11-18): "i am not interested in the script approach at all."** Generated pages are rejected as the way to read or maintain the model; everything must be visible and editable in Protégé. See [[Harm Ontology v3 Three-Layer Mini Example Brief]]. Still open:
  - The first mini example was judged "awful" and had no domain, range or groups. The **editor-first mini** (`ontology/tests/editor_first_mini/`) was built to fix that. The author then reported not seeing domain, range or the super-property groups; my diagnostic questions (which file is open, which tab) are unanswered.
  - **Instances show no properties to fill in** (author, 2026-11-19). Cause: the sample gave only PerspectiveType and PerspectiveSpecification their attributes, and OWL attaches no properties to classes anyway. **To resolve:** give every class its properties with domain and range from the draft structure's `props:` lines (Assessment, CausalAssessment, Effect, Factor, Agent…); decide how data entry is guided (template individuals, SHACL profile shapes, or a spreadsheet route such as the Cellfie plugin; none verified).
  - **Property groups** (the 12 display groups): abstract super-properties plus an annotation is proposed (not approved; 0.02 said groups are "display facets, not OWL classes").
  - **Narrative placement is open again** (not logged); the three-layers decision (2026-11-17) is being re-judged against the editor-first requirement.
- **Layer-1 name "schema"** (author, 2026-11-18, replaces "ontology"/"core"): adopted but **not logged in [[Decisions_Log]]**; the log entry of 2026-11-17 still says "ontology (OWL)". Propose a new entry when the author asks.
- **Full-build briefs:** [[Harm Ontology v3 Provisional Release Brief]] carries the requirements above; it should not be acted on until narrative placement and the schema's domains, ranges and groups are settled.

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
- [[Harm Ontology v3 Test Summary]] for why and how the v3 tests were run, and which files they used.
- [[Harm Ontology - Explanations from 2026-11-19 (Agents and Instance Properties)]]: the reasoning behind the agent, participation and instance-property questions (reference note; nothing decided).
- **If the task is producing the first v3 `.ttl` and a generated Compendium (new chat): attach this handoff and [[Harm Ontology v3 Provisional Release Brief]] together.** The brief lists every file the build needs, including [[Decisions_Log]] and [[PerspectiveStructure 0.02]]. A three-layer worked example (schema, profiles, vocabulary, loader) is described in [[Harm Ontology v3 Three-Layer Mini Example Brief]]. **Author's Protégé check, 2026-11-18: negative.** Hard to navigate; the mini schema had no domains or ranges, so properties showed no links. See "Open issues and to-dos added 2026-11-19" above. Narrative placement is open again and was not logged. The handoff alone is not enough for that task: its "Next step" list is about testing.
- [[Harm Ontology v3 - Draft Structure]] and [[Harm Ontology Migration Plan]] as needed.

## Previous sessions
- 2026-11-18 "Harm Ontology v3 testing": `copilot/copilot-conversations/agent__read_harm_ontology_v3_handoff._rename_chat_to_Harm_Ontology@20261118_004932.md`
- 2026-11-17/18 "read Harm Ontology v3 handoff": `copilot/copilot-conversations/agent__read_Harm_Ontology_v3_handoff@20261117_235104.md`
- [[2026-11-14 Harm Ontology Redesign]] (transcript: `copilot/copilot-conversations/agent__philosopher_adverse_stress_test_harm_ontology@20261114_071639.md`; read selectively, don't reopen the chat)
