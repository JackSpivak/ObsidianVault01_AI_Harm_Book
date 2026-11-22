---
epoch: 1795330643176
mode: agent
backendId: opencode
sessionId: "ses_dfdf540fcffeY5zOt8pIfQcKZ0"
model: '{"baseModelId":"google/gemini-3.5-flash-lite","effort":"low"}'
tags:
  - copilot-conversation
topic: "Harm Ontology handoff note"
usage: '{"usedTokens":15438,"contextWindow":1048576,"updatedAt":1795330651642}'
---

**user**: read harm ontology
<!-- copilot-message {"notes":["01_The Writer's Room/Handoff - Harm Ontology.md"]} -->
[Timestamp: 2026/11/21 23:57:23]

**ai**: The **Harm Ontology** project is currently in an active prototyping, testing, and methodology-refinement phase (v3 draft design). Here is a summary of the current status, recent work, open questions, and next steps as outlined in the handoff note:

### 1. Current Status & Design State
* **v3 Design:** Drafted in [[Harm Ontology v3 - Draft Structure]], but no production v3 `.ttl` file has been created yet.
* **Core Rename:** "Patient" has been officially renamed to **`AffectedEntity`** (with altLabels `patient` and `moral patient`), along with related properties (`affectedStanding`, `forAffectedEntity`, and `standingOfSubjects {agent · affected · datum}`).
* **Assessment-Everywhere Test (HO-Everywhere Test (HO-002.a)**:
  - Variant B design has been implemented and tested via toy cases (e.g., the fictional "Branch ledger" toy case in [[2026-11-18 Harm Ontology v3 Toy Case Results]]), passing 42 to 58 checks across various runs.
  - Formal v3 testing is currently paused by the author for informal real-world data application and collection of v4 updates.

### 2. Key Recent Findings & Open Discussions
* **Methodology & Protégé Usability:** Working through editor-first requirements, property groups, domain/range settings, and three-layer mapping rules (`ho-editor-mini.ttl`).
* **Agents, Participation, and Organizations:** Proposed under bookmark HO-007 (Person/Agent participation in events, assessing organizations, inanimate factors vs. agents).
* **Proposed v4 / Extensions:** 
  * A `Chain` class bounded by a horizon (`maxHorizon`).
  * Splitting `Assessment` into Causal / Valence / Responsibility.
  * Causal standards (but-for, NESS, INUS, etc.).

### 3. Next Steps & Horizon
* Reviewing test decisions (Author decisions 5–21) and deciding on pending items like the Causal Chain / Horizon R01 workstream.
* Continuing Migration Phase 0 if returning to v1/v2 extraction scripts and compendia.

Let me know which specific part of the ontology, drafts, test results, or next steps you would like to dive into!
<!-- copilot-message {"tools":["read (read): 01_The Writer's Room/Handoff - Harm Ontology.md"]} -->
[Timestamp: 2026/11/21 23:57:23]