---
epoch: 1795852553754
mode: agent
backendId: opencode
sessionId: "ses_dded98ad0ffe5fgyt2SeFStO7k"
model: '{"baseModelId":"google/gemini-3.5-flash-lite","effort":"low"}'
tags:
  - copilot-conversation
topic: "Blockers and open questions"
usage: '{"usedTokens":33403,"contextWindow":1048576,"updatedAt":1795852685063}'
---

**user**: Blockers and Open Questions
[Timestamp: 2026/11/28 00:55:53]

**ai**: The vault's active feature roadmap and change ledger—specifically [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] and recent sessions—tracks approximately 110 open items, proposals, and decisions. 

The primary **blockers and open questions** dividing the design right now cluster into four main areas:

---

### 1. Assessment Architecture & Scope Blockers (`S` Series)
* **S21 (Discipline vs. Tradition Scope):** Whether disciplines and traditions are represented as entities in the model. (Rescoped: deferred as non-essential to core competency questions, but impacts how discipline/tradition perspectives link).
* **S26 & S28 (Gap Schema Attachment & Placement Test):** Where gap attribute groups (*mandate, valuation, lifecycle, remedy*) attach—whether on `PerspectiveType`, a procedural layer, or `HarmAssessment`. This is directly blocked by the **Placement Test (`S28`)**.
* **S37 (Status of Harmfulness):** A fundamental choice between two ontological options:
  1. Reifying `Harmfulness` as a class with an assessor, standard, and criterion (`AssessedHarmfulness` as a subclass).
  2. Having only first-class `AssessedHarmfulness` with **no ontic harmfulness** (aligning with the core premise that harm is always an assessment, never an intrinsic property).
* **S3 / S2 (Agent Scope & Participation):** Defining what counts as an `Agent` (including AI systems, floodwaters, and lions) and reifying `participatesIn` as a claim.

---

### 2. DUL Alignment & Core Ontological Definitions (`HD` Series)
* **HD3 / HD9 (Judged States for Situations & Events):** How a Situation satisfies its description or an Event pursues its course when bearing harm.
* **HD21 (State definition):** Defining a State as a `Quality` with a `TimeInterval` region vs. a `Situation` (since DUL lacks a native `State` class).
* **HD25 & HD26 (Entity vs. Object & DUL Verification):** Whether `AffectedEntity` has superclass `Entity` or `Object`, requiring verification against DUL classes (*Community, Group, Collection, CollectiveAgent, Norm, Quality, Region, TimeInterval*).

---

### 3. Causal, Valence & Responsibility Split (`K` & `H` Series)
* **K1 (The Causal/Valence/Responsibility Split):** Currently, harm, fault, and cause are mixed, making answerability hard to read from cause alone (blocking CQ9 and S35). Resolving K1 splits `HarmAssessment` subclasses to handle fault, cause, and harm separately.
* **K2 (Causal Standards):** Reconciling legal vs. philosophical standards (*but-for, NESS, INUS, probability-raising*).
* **H2–H6 (Horizon Boundaries & Net Chain Assessment):** Determining how `maxHorizon` is measured (from factor, effect, or `assessedAt`), who overrides it, and how status calculations propagate across causal cascades.

---

### 4. Testing, Validation & Evidence Gating (`A` Series)
* **A4 & K5 (Strict Settlement & Evidence Anchors):** Requiring 2+ independent sources using the same procedure to reach `Settled` status, and anchoring evidence against infinite regress.
* **A1 / A2 / A5 (Gating & Horizon Tests):** Passing non-expert subagent tests and real-world horizon tests (R01) before Variant B architecture can be fully adopted.

---

### Where to look in the vault:
* **The Master Ledger:** [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]]
* **Latest Handoff Summary:** [[Handoff - Harm Ontology]]
* **Session Records:** [[2026-11-22 Harm Ontology Ledger and Assessment Session]]
<!-- copilot-message {"tools":["obsidian-copilot_miyo_search (other)","grep (search): 04_Ideas Topics Concepts/Harm Ontology/Harm Ontology v0.03.1/Harm Ontology v3.1 — Feature Roadmap and Change Ledger.md"]} -->
[Timestamp: 2026/11/28 00:55:53]

**user**: s26 and s28 seem to represent the most significant and consequential blocker currently.  is that correcrt
[Timestamp: 2026/11/28 00:58:01]

**ai**: **Yes, absolutely.** S26 and S28 represent a foundational architectural pivot for the entire ontology, and identifying them as the most consequential blocker is spot on.

### Why S26 and S28 are so critical:

1. **The Core Ontological Trap (S26):** 
   In earlier drafts, metadata like *mandate, valuation, lifecycle, and remedy* (the gap groups and procedural attributes) were mistakenly attached directly to the `PerspectiveType` (e.g., the historical school of thought or philosophical tradition). 
   * **The mistake:** A philosophical tradition or disciplinary lens (like "Classical Council" or "Microeconomics") does not have a statutory deadline, a courtroom mandate, or an active legal remedy of its own. Conflating the *lens* with the *act of assessment* breaks the model's logic.

2. **The Test (S28):** 
   **S28** enforces the **Placement Test** (formalized across vault notes like [[Design Decision - Vocabulary Placement - Narrative, OWL Classes or Mixed]] and `PLACEMENT_TEST.md`), which forces every proposed element to answer:
   * Does it describe a **tradition/lens** (`PerspectiveType`)?
   * Does it describe a **particular act of assessment** (`HarmAssessment`)?
   * Does it describe the **thing assessed** (`Factor`, `Effect`, `AffectedEntity`)?
   * Does it describe an **output or remedy** (`RemedialObligation`)?

### Why unblocking S26/S28 unblocks the rest:
Until S26 is definitively resolved (attaching procedural/gap groups to `HarmAssessment` or a procedural layer rather than the static `PerspectiveType`), building out the OWL schema, running SHACL validation, and populating discipline modules (`S1`) remains structurally unstable. It prevents the model from mixing static worldviews with dynamic, real-world judgments.
<!-- copilot-message {"tools":["obsidian-copilot_miyo_search (other)"]} -->
[Timestamp: 2026/11/28 00:58:01]