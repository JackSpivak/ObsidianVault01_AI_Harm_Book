---
type: index
status: active
tags: [admin/skills, ontology/harm]
aliases: [Master Skill Index, Claude Skills]
created: 2026-11-23
---

# Master Skill Index

A living index of specialized skills available to Copilot in this vault. Since Obsidian's navigation tree and internal wikilinks do not index dotfolders (like `.claude/skills`), this note serves as the human-accessible catalog and reference for our operational skills.

---

## 1. Structured Inquiry Epistemic Unfolder (`structured-inquiry-epistemic-unfolder`)
* **Folder Location (System):** [[View Skill - Structured Inquiry]] *(or view system path: `.claude/skills/structured-inquiry-epistemic-unfolder/SKILL.md`)*
* **Purpose:** Systematically investigates complex conceptual territories or philosophical domains by generating a comprehensive, sequentially expanding top-level outline (one section at a time) with strict frontmatter provenance and metacognitive saturation checks.

### Mandatory & Optional Inputs (Input Protocol)
* **Input A: The Core Guiding Question (MANDATORY)** — The central question driving the inquiry (e.g., *"How would we know a harm if we saw one?"*).
* **Input B: Epistemic Grounding Mode (MANDATORY)** — Must be explicitly specified as one of three boundaries:
  1. *Ontology-Only:* Bounded strictly to formal RDF/OWL/SKOS schema definitions and core classes.
  2. *Obsidian Vault-Grounded:* Draws upon the rich vault ecosystem of design notes, unfiled ideas, and draft files (acknowledging speculative/exploratory capability).
  3. *LLM Parametric Baseline:* Relies exclusively on pre-trained LLM weights and academic consensus (zero vault access).
* **Inputs C–G (Optional):** Guiding Perspective, Conceptual Scope, Epistemic Rigor, Temporal Horizon, and Output Format.

### Core Operating Rules
1. **Sequential Pacing:** Delivers strictly one section per turn (Section I, II, III...).
2. **Frontmatter & Metacognitive Separation:** Every section appends:
   * *Inputs & Provenance Frontmatter:* Exposing all inputs and their origin tags (`[Explicitly Provided]` vs. `[Inferred/Assumed]`).
   * *Metacognitive Assessment Block:* Answering 4 closure criteria (`Saturation`, `Marginal Returns`, `Convergence`, `Utility`) with consistent short labels.
3. **User Control Options:** Offers four choices at the end of each turn: `[Expand]`, `[Drill Deeper]`, `[Continue Sequentially]`, or `[Halt & Synthesize]`.

---

## Other Registered Vault Skills
*(Reference list of standard built-in or plug-in skills available in the environment)*
* `bookmark-index-maintainer` — Maintains and extends numbered bookmark taxonomies.
* `deep_person_research` — Exhaustive background research brief on a named person.
* `harm-ontology-gap-analyst` — Focused inquiry into the adequacy of a harm ontology.
* `json-canvas` — Creates and edits JSON Canvas (`.canvas`) files.
* `obsidian-bases` — Creates and edits Obsidian Bases (`.base`) files.
* `obsidian-markdown` — Handles Obsidian-specific Markdown syntax (wikilinks, block IDs, callouts, Mermaid).
* `opencode` — Questions about OpenCode itself, SDK, and configuration.
* `perspective-critical-reading` — Reads narratives from named disciplinary perspectives.
