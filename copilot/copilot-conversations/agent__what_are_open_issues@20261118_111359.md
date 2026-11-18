---
epoch: 1795025639324
mode: agent
backendId: opencode
sessionId: "ses_e102450acffeCtV0ZzU0LofGiM"
model: '{"baseModelId":"google/gemini-4-hydrogen","effort":"low"}'
tags:
  - copilot-conversation
topic: "Open issues in Harm Ontology"
usage: '{"usedTokens":18019,"contextWindow":1048576,"updatedAt":1795025878446}'
---

**user**: what are open issues
<!-- copilot-message {"notes":["01_The Writer's Room/Handoff - Harm Ontology.md"]} -->
[Timestamp: 2026/11/18 11:13:59]

**ai**: Based on [[Handoff - Harm Ontology]], here are the current open issues, pending decisions, and next steps:

### 1. Immediate Technical & Testing Issues (Next Steps)
* **Causal-conflict rule (Toy finding 1, major):** Variant B marked "who caused it?" as *Disputed* simply because two perspectives named different causes (policy vs. bug), even though both can be true—contradicting HO-003.
  * *Proposed fix (undecided):* Causal values should only conflict when an assessment **denies** a cause or claims a cause is the **only** one.
  * *Open question:* Do other categorical attributes (e.g., `answerability`, `type`) have the same problem?
* **Toy Run 2 gaps:**
  * Add a revision trigger (finding 5, e.g., `revisedBecause`).
  * Add test cases for independence / `repeats`, `Corroborated`, and `Incommensurable` (finding 7).
  * Compare date intervals by overlap (finding 6).
* **Non-expert subagent test:** Needs to be run (CQ1, CQ2, CQ8, schema-only) to check whether relying on script-generated snapshots causes silent failures (finding 8). Variant B cannot be adopted until this passes.
* **Horizon R01:** Needs sourced research before proceeding.

### 2. Pending Design Decisions (Proposed, Not Decided)
*(See [[HO-005 Assessed Membership and Systematic Omission]] and [[HO-002.a Assessment-Everywhere Test Strategy]])*
* Splitting `Assessment` into Causal / Valence / Responsibility (the toy case used a separate `ResponsibilityAssessment` for testing only).
* Causal standards (but-for, NESS, INUS, etc.) as a second family of standards.
* Reifying `participatesIn` as a claim.
* Changing HO-003's "jointly sufficient" to "as assessed".
* Formalizing the evidence anchor (`Evidence` + `Observation` is built into the test design, but not yet decided).
* `AffectedEntity` proposals in HO-002.a: type as an assessment, `Unclassified`, `NaturalSystem` / `EngineeredSystem`, `affectedStanding`, `CollectiveNaturalGroup`, `Household`.

### 3. Migration & Housekeeping
* **Migration Phase 0:** Needs continuation (open `# Master Formal Ontology of Harm (Part 1…)`, compare v1 and v2, and extract inventories by script).
* **AffectedEntity rename:** Still needs to be applied to ~17 other notes and the v1 `.ttl` (deferred to migration).
* **Old root files:** `Interdisciplinary_Harm_Ontology_Compendium.md` and `Interdisciplinary Harm Ontology.ttl` are untouched and awaiting an archive decision.
* **Sub-workstream follow-ups:** See [[Handoff - Perspective Vocabulary and v3 Follow-ups]].

### 4. Risks & Cautions to Watch
* **Over-strict settlement:** The current rule may be so strict that in real cases almost nothing reaches `Settled`—watch for this in Horizon.
* **Unverified references:** Legal cases, Horizon details, Wilber, NESS/INUS, vocabularies, Lorenz, Meadows, and the war ending of the Sai Weng parable are currently from memory and unverified.
* **Reviewing test decisions:** Author decisions 5–21 in HO-002.a were made quickly in one sitting and may warrant re-reading before building further on them.
<!-- copilot-message {"tools":["read (read): 01_The Writer's Room/Handoff - Harm Ontology.md"]} -->
[Timestamp: 2026/11/18 11:13:59]

**user**: lets proceed with next steps
[Timestamp: 2026/11/18 11:15:09]

**ai**: Let's start with **Step 1: The Causal-Conflict Rule** (toy finding 1) and check whether other categorical attributes share the same issue.

### 1. Why `toy_status.py` produced a false dispute
In `toy_status.py`, any non-graded attribute is treated as **single-valued and mutually exclusive**:
```python
comparable = {v for v in vals.values() if v is not None}
if len(comparable) > 1:
    return "Disputed", None, rows
```
Because `P4` named `F3` (policy) and `P1`/`P2`/`P3`/`P6` named `F1` (bug), `len(comparable) > 1` fired and marked the cause as `Disputed`—even though both can be true under [[HO-003 Causal Assembly - the Perfect Storm]].

### 2. Do other categorical attributes have the same problem?
* **Cause (`causedBy`):** **Yes (non-exclusive).** Multiple factors can jointly cause an effect. Different named causes are additive, not conflicting, unless an assessment explicitly **denies** a cause or claims a cause is the **sole** cause.
* **Answerability (`answerableEntity` / responsibility):** **Yes (non-exclusive).** In systemic or organizational harm (e.g., `Manager` vs. `CompanyX`), multiple entities can be concurrently answerable. Naming different answerable entities shouldn't trigger `Disputed` unless one denies another's answerability or claims sole answerability.
* **Entity `type`:** **Mostly exclusive, with caveats.** Disjoint types (e.g., `NaturalPerson` vs. `CollectiveArtificialPerson`) genuinely conflict. However, `Unclassified` is an *absence* of classification rather than a competing type, and subtype vs. supertype wouldn't conflict.
* **Dates / `occurredDuring`:** **Interval-based (Finding 6).** Different years (e.g., `2009` vs. `2012`) shouldn't be compared as exact strings; overlapping intervals are compatible, while disjoint intervals conflict.

---

### Proposed Next Action
If you're ready to decide on this rule for the test:
1. **Non-exclusive attributes (`cause`, `answerability`):** Treat distinct values as compatible/additive by default; mark `Disputed` only when an assessment explicitly **denies** a value or claims **sole** cause/answerability.
2. **Exclusive attributes (`type`):** Keep mutually exclusive for disjoint types, but don't let `Unclassified` trigger a dispute.

Would you like me to implement this rule in `toy_status.py` and `toy_branch_ledger_B.ttl`—and while we're in there, add the **Toy run 2** cases (revision trigger `revisedBecause`, date interval overlap, and `repeats` / `Corroborated` / `Incommensurable`)?
<!-- copilot-message {"tools":["glob (search)","read (read): 01_The Writer's Room/2026-11-18 Harm Ontology v3 Toy Case Results.md","grep (search): 02_Ideas Topics Concepts/Harm Ontology/HO-002.a Assessment-Everywhere Test Strategy.md","read (read)"]} -->
[Timestamp: 2026/11/18 11:15:09]