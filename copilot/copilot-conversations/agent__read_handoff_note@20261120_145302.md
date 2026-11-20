---
epoch: 1795211582174
mode: agent
backendId: opencode
sessionId: "ses_e050dacbcffes5LtWuiLfYHG0c"
model: '{"baseModelId":"google/gemini-4-hydrogen","effort":"low"}'
tags:
  - copilot-conversation
topic: "Handoff - Harm Ontology note"
usage: '{"usedTokens":14209,"contextWindow":1048576,"updatedAt":1795211589167}'
---

**user**: read handoff note
<!-- copilot-message {"notes":["01_The Writer's Room/Handoff - Harm Ontology.md"]} -->
[Timestamp: 2026/11/20 14:53:02]

**ai**: I've read [[Handoff - Harm Ontology]]. Here's where things stand:

- **Status:** The v3 design is drafted in [[Harm Ontology v3 - Draft Structure]] (no production v3 `.ttl` yet). Formal v3 testing is paused while you use v3 informally against real-world data and collect v4 updates. Nothing is adopted until the non-expert test passes.
- **Recent work:** `Patient` was renamed to `AffectedEntity` in [[Decisions_Log]] and across the draft/test notes. The "Branch ledger" toy case ran through 7 runs (58/58 checks passing), addressing causal disputes, intervals, revision triggers, independence, chains/horizons, and snapshot readability.
- **Open issues (2026-11-19):**
  - **Editor-first / Protégé:** Instances show no properties to fill in (`ho-editor-mini.ttl` only models `PerspectiveType` and `PerspectiveSpecification` attributes), property display groups and narrative placement are open, and the Layer-1 name `"schema"` isn't logged in [[Decisions_Log]] yet.
  - **Agents, participation & assessing organizations (proposed `HO-007`):** Awaiting confirmation on bookmark shape, `Event` class, participation relations, and what `Agent` covers.
- **Next steps listed:** Answer the CQ8 `"directly affected"` wording question, confirm/challenge the toy-case scoring, run **Horizon R01** (needs sourced research first), and resolve the open Protégé / `HO-007` / pending items.

What would you like to work on?
<!-- copilot-message {"tools":["read (read): 01_The Writer's Room/Handoff - Harm Ontology.md"]} -->
[Timestamp: 2026/11/20 14:53:02]