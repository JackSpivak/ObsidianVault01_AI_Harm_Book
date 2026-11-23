---
epoch: 1795462111513
mode: agent
backendId: opencode
sessionId: "ses_df61f9f2fffeD6adTgW0OQwjbj"
model: '{"baseModelId":"google/gemini-3.5-flash-lite","effort":"low"}'
tags:
  - copilot-conversation
usage: '{"usedTokens":35907,"contextWindow":1048576,"updatedAt":1795462491345}'
topic: "Harm representation key entities"
---

**user**: Discussion about Harm Representation - Key First Class Entities
[Timestamp: 2026/11/23 12:28:31]

**ai**: In the **Harm Ontology (v3 architecture)** developed across this vault, harm is not treated as an intrinsic property of things, but as a **perspective-relative assessment** ([[HO-000 Harm as Perspective-Relative Assessment|HO-000]], [[HO-premise No Intrinsic Harmfulness|HO-premise]]). 

To operationalize this without baking normative verdicts into physical reality, the architecture establishes a precise set of **Key First-Class Entities** across the neutral core, the judging/perspectival layer, and the meta-analytical layer.

---

### 1. The Neutral Core: Mechanisms & Conditions
* **`Factor`** (`CausalCandidate`): Neutral constituent elements contributing to situations—such as acts, processes, omissions, structures, risks, or conditions. Factors do not carry intrinsic valence; whether a factor is harmful is entirely a matter of assessment.
* **`Effect`** (`CausalCandidate`): Neutral downstream consequences or changes that ramify through time. Effects carry attributes like temporal status, reversibility, severity, and experienceability, but remain valence-neutral until judged.
* **`FactorAssembly`** (`CausalCandidate`): A thin container (identifier and label only) representing a constellation or "perfect storm" of factors (e.g., [[HO-003 Causal Assembly - the Perfect Storm|HO-003]]). Its members, sufficiency, and causal origin (*Emergent*, *Exploited*, *Engineered*) are supplied dynamically through [[CausalAssessment]], not pre-asserted.
* **`AffectedEntity`** (formerly *Patient* / *Moral Patient*): The inclusive category for anything capable of being impacted or holding interests—subdivided into `SentientIndividual`, `CollectiveArtificialPerson`, `NonSentientSystem` (natural or engineered ecosystems), `FutureGeneration`, `AISystem`, and `Relationship` ([[Decisions_Log]]). Under v3 rules, moral or legal *standing* is itself assessed rather than hardcoded.

### 2. The Perspectival & Judging Layer
* **`Perspective`** (Abstract Umbrella): The parent concept dividing into two concrete entities:
  * **`PerspectiveType`** (The *Tradition* / *Lens*): A reusable conceptual framework or discipline tradition (e.g., Utilitarianism, Tort Law, Public Health, or a trained AI model's learned representation) containing default evaluative standards and normative parameters ([[PerspectiveStructure Proposal Draft 3.1|PerspectiveStructure]]).
  * **`PerspectiveSpecification`** (The *Viewpoint* / *Snapshot*): A concrete instantiation of a perspective defined by its spatial/temporal position, optics (framing, resolution, sensitivity), purpose, and operator (`assessor` $\rightarrow$ `Agent`) ([[HO-II.d Perspective - Ten Optional Properties|HO-II.d]]).
* **`Assessment`** (The Fundamental Unit of Judgment): A first-class record of a single judgment made from a `PerspectiveSpecification` regarding a target (`assesses` $\rightarrow$ Factor, Effect, Outcome, FactorAssembly, etc.). 
  * It assigns a **`verdict`** (`Harmful`, `Beneficial`, `Mixed`, `Neutral`, `Contested`) and records scope adequacy, confidence, and acknowledged exclusions.
  * Specialized subtypes include **`CausalAssessment`** (which unifies attribution, factor assemblies, and left-out omissions), **`ValenceAssessment`**, and legal **`Judgment`** (carrying authority, procedure, jurisdiction, and finality) ([[HO-II.c Judgment as Assessment - Reasoning over Precedent|HO-II.c]]).
* **`EvaluativeStandard`** (Formerly *Theory of Harm*): The benchmark standard or principle under which an assessment is rendered (e.g., philosophical accounts like experiential or rights-based accounts, legal standards like *injury-in-fact* or *loss of chance*, and causal criteria like *But-For* or *NESS*) ([[HO-II.a Assessment and Evaluative Standard|HO-II.a]]).

### 3. The Meta Layer: Disagreement & Integration
* **`Divergence`**: A core ontological innovation representing typed disagreements between two or more assessments ([[HO-III.a Divergence and Integration - True but Partial|HO-III.a]]). Divergences are classified as **Perspectival** (different parts of the elephant), **Normative** (competing standards), **Evidential** (differing data), or **Factual** (contradictory empirical claims).
* **`Integration`** (Optional): A record combining partial or divergent assessments while explicitly tracking what was kept in frame and what was left out.
<!-- copilot-message {"tools":["obsidian-copilot_miyo_search (other)","glob (search): 02_Ideas Topics Concepts/Harm Ontology","read (read): 02_Ideas Topics Concepts/Harm Ontology/_Harm Ontology Bookmark Index.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md"]} -->
[Timestamp: 2026/11/23 12:28:31]

**user**: Critical Question:  How would I or we (as a relationship, a family, a community, a neighborhood, pollitical entities, cultures, philosophies, etc) or It (systems, networks, ecosystems, etc) know a "harm:" if we saw one?
[Timestamp: 2026/11/23 12:34:18]

**ai**: Building on the vault’s premise that **circumstances are neutral and harm is never intrinsic** (valence lives solely within judgments; see [[HO-premise No Intrinsic Harmfulness|HO-premise]]), knowing a "harm" when we see one requires looking past the raw events, objects, or behaviors and examining **how different entities occupy, observe, and evaluate reality**.

The question of *how we would know* unfolds differently depending on the scale and nature of the entity doing the perceiving:

---

### 1. For Individuals, Relationships, and Families
At the human scale, knowing a harm relies on the duality of **phenomenality** ([[HO-I.c Phenomenality - Observability and Experienceability|HO-I.c]])—splitting what can be *observed* from what can be *felt or experienced*:
* **In a Relationship / Family:** Harm is rarely a sudden, isolated physical act; it is apprehended through patterns of **habituation, captured assent, or slow erosion of capability** (e.g., [[HO-001 Harm by Habituation and Captured Assent|HO-001]]). You know a harm because an affected party experiences a constraint on their agency, emotional safety, or flourishing, even if the surrounding environment looks calm or "neutral" on paper.
* **The Epistemic Check:** To validate whether it is a harm, the family or relationship must apply an **EvaluativeStandard** (e.g., an experiential account of suffering or a relational ethics account) from a distinct standpoint, making sure to trace consequences beyond immediate reactions to see how capabilities degrade over time.

### 2. For Communities, Neighborhoods, and Cultures
At collective scales, harm is detected through structural shifts, institutional omissions, and competing frameworks of legitimacy:
* **The "Searchlight" of a Tradition:** Different communities and councils (Legal, Classical, Ethical, Ecological) cast different searchlights. A neighborhood knows a harm notthrough a single universal meter, but when structural factors (such as zoning decisions, economic extraction, or environmental neglect) accumulate into visible disruptions of community well-being or cultural continuity.
* **The Role of Divergence:** Because different groups occupy different standpoints, one neighborhood's necessary development is another's "sacrifice zone." A community knows it has encountered a true divergence rather than mere noise when multiple distinct assessments clash—revealing that the disagreement is **normative** (conflicting standards), **evidential** (different data sets), or **perspectival** (different parts of the elephant) rather than simply factual ([[HO-III.a Divergence and Integration - True but Partial|HO-III.a]]).

### 3. For Political Entities and Philosophical Traditions
For states, legal bodies, and formal philosophies, knowing harm requires institutionalized procedures of judgment:
* **The Legal / Regulatory Apparatus:** Political entities operationalize harm through formal **Assessments** and **Judgments** (following procedural integrity, jurisdiction, and binding force). They know a harm has occurred when an act, omission, or structural risk breaches an established standard of *injury-in-fact* or rights violation.
* **The Horizon Trap (The Sai Weng Principle):** Political and philosophical frameworks are notoriously prone to the **Sai Weng trap**—where an apparent harm turns into a benefit, or vice versa, depending on where the observer stops looking ([[HO-II.b Assessment Horizon - the Sai Weng Trap|HO-II.b]]). A sophisticated political entity or philosophy knows a harm only when it explicitly declares its **assessment horizon** and time scale (e.g., short-term electoral cycle vs. multi-generational civilizational decay), acknowledging that whoever sets the horizon sets the verdict.

### 4. For Non-Human Systems, Networks, and Ecosystems ("It")
For complex systems, technical networks, and natural or engineered ecosystems, harm cannot be felt or experienced directly in the human sense. Instead, knowing a harm requires tracking structural stress, feedback loops, and systemic degradation:
* **Ecosystems & Networks:** An ecosystem or digital network doesn't "complain" of harm; rather, harm is known through **criticality, leverage, and systemic resilience**. When an assemblage of individually innocuous factors (an engineered "perfect storm" as in [[HO-003 Causal Assembly - the Perfect Storm|HO-003]]) crosses a threshold, the system exhibits loss of diversity, cascading failures, or systemic collapse.
* **The Role of the Assessor:** Because "It" cannot self-assess, an external or embedded operator (an ecologist, system architect, or automated monitoring agent) must take a perspective, set a boundary or horizon, and apply a systemic evaluative standard (such as homeostatic stability or functional capacity) to declare that a part of the network or ecosystem has been harmed.

---

### Summary: The Unified Epistemology of Harm
Across every scale—from an intimate family dynamic to a planetary ecosystem—we know a harm not by searching for an invisible chemical called "harmfulness" attached to an object, but by asking four anchoring questions of our assessment framework:
1. **What neutral factors and assemblies are at work?** (The objective substrate: [[HO-I.a Factor and CausalRole|HO-I.a]])
2. **Who or what is affected, and what is their standing?** (The affected entity: [[HO-002.a Assessment-Everywhere Test Strategy]])
3. **What standard, standpoint, and time horizon are we judging from?** (The camera settings: [[HO-II.d Perspective - Ten Optional Properties|HO-II.d]])
4. **How do competing perspectives view this same reality?** (The meta-layer of Divergence: [[HO-III.a Divergence and Integration - True but Partial|HO-III.a]])
<!-- copilot-message {"tools":["obsidian-copilot_miyo_search (other)"]} -->
[Timestamp: 2026/11/23 12:34:18]