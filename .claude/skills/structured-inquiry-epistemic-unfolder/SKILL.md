# Sequential Epistemic Unfolder (Ontological Archaeology)

## Purpose & Scope
This skill systematically investigates a complex conceptual territory or philosophical domain by generating a comprehensive, sequentially expanding top-level outline (one section at a time). It avoids hidden assumptions by requiring explicit user inputs and appending a strictly separated frontmatter block (exposing all 6 inputs and their provenance tags) alongside a metacognitive assessment block dedicated solely to the four closure criteria.

## Strict Input Protocol (Interactive Prompting)
**This skill assumes nothing from prior conversation history or previous sessions.** When invoked, if any inputs are unstated or ambiguous, you must explicitly pause, present the prompt definitions below, and require the user to provide **Input A (Core Question)** as mandatory, while Inputs B through F remain optional (with intelligent defaults applied if omitted).

### Input Definitions & Examples for Prompting:
1. **Input A: The Core Guiding Question (MANDATORY)**
   * *Definition:* The central, foundational question driving the investigation.
   * *Example:* *"How would we know a harm if we saw one?"*
2. **Input B: The Guiding Perspective / Standpoint (Optional)**
   * *Definition:* The role, posture, or paradigm you are operating from.
   * *Example:* *"Universal Epistemologist"*.
3. **Input C: Conceptual Scope & Deliverable Goal (Optional)**
   * *Definition:* The intended scope and final output target of the inquiry.
   * *Example:* *"Comparative Baseline Investigation"*.
4. **Input D: Epistemic Rigor & Depth Level (Optional)**
   * *Definition:* The balance between broad interdisciplinary synthesis and microscopic analytical precision.
   * *Example:* *"Analytical Philosophy Synthesis"*.
5. **Input E: Temporal Horizon Constraint (Optional)**
   * *Definition:* The time scale the investigation should account for.
   * *Example:* *"Civilizational / Universal Scale"*.
6. **Input F: Output Format & Staging Preference (Optional)**
   * *Definition:* The stylistic register of the generated output.
   * *Example:* *"Academic Philosophical Critique"*.

---

## Operating Rules

### Rule 1: One Section at a Time (Sequential Pacing)
- Never dump a multi-section outline all at once.
- Deliver **strictly one conceptual section per turn**, numbered sequentially (Section I, II, III, etc.).

### Rule 2: Frontmatter & Metacognitive Separation
At the beginning of every delivered section, append two distinct blocks in order:
1. **Inputs & Provenance Frontmatter (Explicitly exposing all 6 inputs and their origin tags using short labels):**
   * *Input A (Core Guiding Question):* `[Exact Text]` (`[Explicitly Provided]`)
   * *Input B (Guiding Perspective):* `[Exact Text]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)
   * *Input C (Conceptual Scope):* `[Exact Text]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)
   * *Input D (Epistemic Rigor):* `[Exact Text]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)
   * *Input E (Temporal Horizon):* `[Exact Text]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)
   * *Input F (Output Format):* `[Exact Text]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)
   * *Output Genre/Type:* `[Short Label]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)

2. **Metacognitive Assessment Block (Strictly answering the 4 closure/diminishing-returns tests with consistent short labels):**
   * *Saturation:* `[Low` / `Moderate` / `High` / `Saturated]`
   * *Marginal Returns:* `[Low` / `Moderate` / `High]`
   * *Convergence:* `[Achieved` / `Open` / `Recursive Loop]`
   * *Utility:* `[High Leverage` / `Marginal` / `Self-Referential]`
   * *Recommendation & Options:* [Brief action summary and user choices]

### Rule 3: User Control Options
At the end of every turn, offer the user four explicit choices:
1. **[Expand]** Provide more detail, historical lineage, or guiding questions for the *current* section.
2. **[Drill Deeper]** Break the current section into narrower, highly focused sub-levels.
3. **[Continue Sequentially]** Proceed to the next macro-section in the outline.
4. **[Halt & Synthesize]** Conclude the exploration and package findings.

---

## Methodological Framing & A/B Testing Protocols

### Purpose & General Methodology
The *Sequential Epistemic Unfolder* skill is designed to prevent premature closure and infinite conceptual loops during deep philosophical or structural investigations. By pacing output strictly one section at a time, exposing all input provenance in the frontmatter, and continuously evaluating conceptual saturation against four distinct closure criteria, it bridges open-ended exploratory thought with rigorous architectural output.

### Testing Subheading: Comparative Epistemic Isolation Protocols
To rigorously validate or contrast the insights generated during an inquiry, this skill supports two mutually exclusive grounding protocols:

#### 1. Pure Parametric Isolation Protocol (Excluding Obsidian Vault / Using LLM Weights Only)
* **Objective:** To establish an uninfluenced academic/philosophical baseline, testing what standard parametric training weights produce without local memory contamination.
* **Execution Rules for the Model:**
  * Strictly prohibit reading, searching, grepping, or referencing any local vault notes, markdown files, bookmark indexes, or vault-specific terminology (e.g., v3 harm ontology classes like `FactorAssembly`, `PerspectiveSpecification`, or `Divergence`).
  * Rely solely on generalized pre-trained parametric knowledge, standard philosophical lineages (utilitarianism, deontology, phenomenology), and universal academic consensus.
  * Explicitly log `[Parametric Isolation]` in the output provenance frontmatter.

#### 2. Strict Vault-Grounded Protocol (Excluding LLM General Memory / Using Obsidian Vault Only)
* **Objective:** To confine the investigation strictly to the local vault's proprietary intellectual property, design decisions, and bespoke architectural primitives.
* **Execution Rules for the Model:**
  * Strictly restrict all definitions, classes, structural hierarchies, and argumentative moves to the local vault's markdown files (e.g., `Harm Ontology v3 - Draft Structure`, `_Harm Ontology Bookmark Index`, and related `HO-` notes).
  * Suppress standard textbook philosophical tropes whenever a bespoke vault equivalent exists (e.g., replacing generic subjective welfare disputes with formal `Assessment`, `EvaluativeStandard`, and `Divergence` mechanics).
  * Explicitly log `[Vault-Strict Grounding]` in the output provenance frontmatter.
