# Sequential Epistemic Unfolder (Ontological Archaeology)

## Purpose & Scope
This skill systematically investigates a complex conceptual territory or philosophical domain by generating a comprehensive, sequentially expanding top-level outline (one section at a time). It avoids hidden assumptions by requiring explicit user inputs and appending a strictly separated frontmatter block (exposing all inputs and their provenance tags) alongside a metacognitive assessment block dedicated solely to the four closure criteria.

## Strict Input Protocol (Interactive Prompting)
**This skill assumes nothing from prior conversation history or previous sessions.** When invoked, if any inputs are unstated or ambiguous, you must explicitly pause, present the prompt definitions below, and require the user to provide both **Input A (Core Question)** and **Input B (Epistemic Grounding Mode)** as mandatory inputs, while Inputs C through G remain optional.

### Input Definitions & Examples for Prompting:
1. **Input A: The Core Guiding Question (MANDATORY)**
   * *Definition:* The central, foundational question driving the investigation.
   * *Example:* *"How would we know a harm if we saw one?"*
2. **Input B: Epistemic Grounding Mode (MANDATORY)**
   * *Definition:* The precise source boundary of the investigation. Must be explicitly specified as one of three options:
     * **Option 1: Ontology-Only** (Strictly bounded to the formal RDF/OWL/SKOS schema definitions and core classes without discursive speculation).
     * **Option 2: Obsidian Vault-Grounded** (Draws upon the rich ecosystem of vault notes, design discussions, unfiled ideas, and draft files—recognizing that this includes exploratory, unverified, and speculative design thought that appears mature).
     * **Option 3: LLM Parametric Baseline** (Relies exclusively on pre-trained LLM weights, academic consensus, and standard philosophical traditions, with zero vault access).
3. **Input C: The Guiding Perspective / Standpoint (Optional)**
   * *Definition:* The role, posture, or paradigm you are operating from.
   * *Example:* *"Universal Epistemologist"* or *"System Architect"*.
4. **Input D: Conceptual Scope & Deliverable Goal (Optional)**
   * *Definition:* The intended scope and final output target of the inquiry.
   * *Example:* *"Comparative Baseline Investigation"*.
5. **Input E: Epistemic Rigor & Depth Level (Optional)**
   * *Definition:* The balance between broad interdisciplinary synthesis and microscopic analytical precision.
   * *Example:* *"Analytical Philosophy Synthesis"*.
6. **Input F: Temporal Horizon Constraint (Optional)**
   * *Definition:* The time scale the investigation should account for.
   * *Example:* *"Civilizational / Universal Scale"*.
7. **Input G: Output Format & Staging Preference (Optional)**
   * *Definition:* The stylistic register of the generated output.
   * *Example:* *"Academic Philosophical Critique"*.

---

## Operating Rules

### Rule 1: One Section at a Time (Sequential Pacing)
- Never dump a multi-section outline all at once.
- Deliver **strictly one conceptual section per turn**, numbered sequentially (Section I, II, III, etc.).

### Rule 2: Frontmatter & Metacognitive Separation
At the beginning of every delivered section, append two distinct blocks in order:
1. **Inputs & Provenance Frontmatter (Explicitly exposing all inputs and their origin tags, including the mandatory Epistemic Grounding Mode):**
   * *Input A (Core Guiding Question):* `[Exact Text]` (`[Explicitly Provided]`)
   * *Input B (Epistemic Grounding Mode):* `[Ontology-Only / Obsidian Vault-Grounded / LLM Parametric Baseline]` (`[Explicitly Provided]`)
   * *Input C (Guiding Perspective):* `[Exact Text]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)
   * *Input D (Conceptual Scope):* `[Exact Text]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)
   * *Input E (Epistemic Rigor):* `[Exact Text]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)
   * *Input F (Temporal Horizon):* `[Exact Text]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)
   * *Input G (Output Format):* `[Exact Text]` (`[Explicitly Provided]` / `[Inferred/Assumed]`)
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
