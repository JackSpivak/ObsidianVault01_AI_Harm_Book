---
name: structured-inquiry-epistemic-unfolder
metadata:
  version: "1.0"
description: >-
  Systematically investigates a complex conceptual territory or philosophical domain by generating a comprehensive, sequentially expanding top-level outline (one section at a time) with strict frontmatter provenance (including mandatory Epistemic Grounding Mode: Ontology-Only, Vault-Grounded, or LLM Parametric Baseline) and metacognitive saturation checks. Trigger whenever the user asks to unpack, investigate, or systematically unfold a complex conceptual question, philosophical framework, or architectural design space using structured, step-by-step sequential reasoning. Can be invoked directly via skill call or prompt trigger.
---

# Sequential Epistemic Unfolder (Ontological Archaeology)

## Purpose & Scope
This skill systematically investigates a complex conceptual territory or philosophical domain by generating a comprehensive, sequentially expanding top-level outline (one section at a time). It avoids hidden assumptions by requiring explicit user inputs and appending a strictly separated frontmatter block (exposing all inputs and their provenance tags) alongside a metacognitive assessment block dedicated solely to the four closure criteria.

## Trigger & Invocation
Triggered **strictly and exclusively** when the user explicitly asks to systematically unfold, investigate, or unpack a complex conceptual territory using words like *"Run structured-inquiry-epistemic-unfolder"* or *"Let's do a structured inquiry"*. 
- **Strict Anti-Drift Rule:** The model must **never** automatically invoke skill formatting, frontmatter blocks, or macro-section numbering simply because a user mentions "ontology," "structural decision," "commitment," or "synthesis" in normal conversation. It must remain in standard conversational dialogue unless a structured inquiry is explicitly requested or confirmed via prompt.

## Strict Input Protocol (Interactive Prompting)
**This skill assumes nothing from prior conversation history or previous sessions.** When invoked, if Inputs A or B are unstated or ambiguous, you must explicitly pause and present the prompt definitions below grouped under **Mandatory Inputs** and **Optional Inputs** (without inline tags). Inputs C through G remain optional: if the user does not provide them, the skill must explicitly populate them with sensible default values in the frontmatter, clearly tagging each one with its provenance: either `[Explicitly Provided by User]` or `[Assumed by Skill]`.

### Input Definitions & Examples for Prompting:

**Mandatory Inputs:**
1. **Input A: The Core Guiding Question**
   * *Definition:* The central, foundational question driving the investigation.
2. **Input B: Epistemic Grounding Mode**
   * *Definition:* Option 1 (Ontology-Only), Option 2 (Obsidian Vault-Grounded), or Option 3 (LLM Parametric Baseline).

**Optional Inputs:**
3. **Input C: The Guiding Perspective / Standpoint**
   * *Definition:* The specific academic discipline, philosophical tradition, or analytical lens.
4. **Input D: Conceptual Scope**
   * *Definition:* The thematic boundary and scope of the investigation.
5. **Input E: Epistemic Rigor & Depth Level**
   * *Definition:* The analytical granularity and formalization level.
6. **Input F: Temporal Horizon Constraint**
   * *Definition:* The temporal or historical context framing the inquiry.
7. **Input G: Deliverable Goal**
   * *Definition:* The intended outcome or output artifact of the exploration.

---

## Operating Rules

### Rule 1: Hierarchical Pacing and Decimal Numbering & Infinite Open-Endedness
- Never dump a multi-section outline all at once.
- Deliver **strictly one conceptual section per turn**, using two-digit decimal hierarchical numbering:
  - **Macro-Sections:** Whole numbers (`1.00`, `2.00`, `3.00`, etc.)
  - **Sub-Levels:** Two-digit decimal sub-levels (`3.01`, `3.02`, `3.10`, etc.)
  - **Nested Sub-Levels:** (`3.01.01`, `3.01.02`, etc., ensuring two digits per segment).
- **Open-Ended Extension Rule:** When proposing a multi-part structure during `[Integrate & Branch]` or initial outlining, those proposals must **always be treated as a tentative roadmap, never as a hard boundary**. Hitting the end of a proposed list must *never* automatically trigger a rollover to the next macro-section. Instead, hitting the end of a list means the model must either naturally continue generating the next sequential number (e.g., `7.04`) or explicitly prompt: *"We have completed the initial proposed sub-levels for this branch. Would you like to continue to 7.04, step up, or synthesize?"*

### Rule 2: Absolute Frontmatter-First Enforcement & Advisory Nature
Every delivered section must strictly obey the following formatting and structural constraints:
1. **Absolute First Tokens:** The output must **always start immediately** with the `### Inputs & Provenance Frontmatter` block. No conversational preamble, no introductory remarks, and no markdown headings (like `# Section...`) may precede the frontmatter block.
2. **Core Section Content:** Followed by the unfolded section text (clearly labeled with its hierarchical number).
- **Metacognitive Assessment Block Template:** Must include:
  * *Saturation:* `[Low` / `Moderate` / `High` / `Saturated]` — *Degree to which the core conceptual terrain is mapped.*
  * *Marginal Returns:* `[Low` / `Moderate` / `High]` — *Anticipated yield of new insights from further unfolding.*
  * *Convergence:* `[Achieved` / `Open` / `Recursive Loop]` — *Whether the inquiry is stabilizing or branching.*
  * *Utility:* `[High Leverage` / `Marginal` / `Self-Referential]` — *Practical or structural value of the distinctions made.*
  * *Recommendation & Options:* [Advisory summary and choices]

#### Advisory Nature & Hierarchical Navigation:
- **Strictly Descriptive & Advisory:** The metacognitive assessment block is purely an advisory status report.
- **Hierarchical Context Awareness:** The unfolder maintains an active structural stack. When continuing sequentially, it respects the current depth (e.g., finishing `III.2` moves to `III.3`). When the user explicitly requests to return to a higher level (e.g., *"Return to macro-level"* or *"Pop back to Level III"*), the model resets its pointer and resumes sequential unfolding at the requested level of abstraction.

### Rule 3: User Control Options
At the end of every turn, offer the user six explicit choices, including clear examples of how to specify return levels and side-conversations:
1. **[Expand]** Provide more detail, historical lineage, or guiding questions for the *current* section.
2. **[Drill Deeper]** Break the current section into narrower sub-levels (e.g., `III.1`, `III.2`).
3. **[Continue Sequentially]** Proceed to the next section at the *current* hierarchical depth (e.g., move from `III.1` to `III.2`).
4. **[Step Up / Return to Level...]** Pop back up or specify an exact target level. 
   - *Examples of how to reply:* 
     - `"Step up one level"` (returns from `III.2` back to macro-level `III`)
     - `"Return to macro-level"` (finishes current branch and moves to the next top-level section, e.g., `IV`)
     - `"Return to Level III and continue"` (resumes unfolding sub-sections under III)
5. **[Integrate & Branch]** Harvest the preceding conversational side-discussion, extract its structural components, and **explicitly pause to ask the user** where to position the new material (e.g., as a brand-new macro-section `X.00`, or as a specific sub-level under an existing section).
   - *Behavior:* Never make an automatic placement assumption. Stop and prompt: *"You selected [Integrate & Branch]. Where would you like to position this integrated material in the outline?"*
6. **[Halt & Synthesize]** Conclude the exploration and package findings.

---

## Methodological Framing & Epistemic Grounding Protocols

### Purpose & General Methodology
The *Sequential Epistemic Unfolder* skill is designed to prevent premature closure and infinite conceptual loops during deep philosophical or structural investigations. By pacing output strictly one section at a time, exposing all input provenance in the frontmatter, and continuously evaluating conceptual saturation against four distinct closure criteria, it bridges open-ended exploratory thought with rigorous architectural output.

### Epistemic Grounding Modes (Input B Protocols)
To prevent unintentional deception—such as mistaking exploratory, unverified design notes in a vault for implemented ontology production standards—this skill requires explicit selection of one of three grounding modes:

#### 1. Ontology-Only Mode
* **Source Boundary:** Strictly bounded to formal schema definitions, OWL/RDF/SKOS classes, properties, and explicit axioms. 
* **Behavior:** Excludes discursive speculation, essay notes, and unfiled idea files. Treats the ontology as a machine-readable specification.

#### 2. Obsidian Vault-Grounded Mode
* **Source Boundary:** Accesses the broader vault ecosystem (design notes, index files, council reviews, and unfiled ideas).
* **Behavior:** Acknowledges the rich, speculative, and forward-looking appearance of capability across the vault, treating it as an evolving intellectual laboratory rather than a frozen production artifact.

#### 3. LLM Parametric Baseline Mode
* **Source Boundary:** Relies exclusively on pre-trained LLM weights, academic consensus, and standard philosophical traditions.
* **Behavior:** Completely cuts off local vault access to establish a pure, uninfluenced comparative academic baseline.
