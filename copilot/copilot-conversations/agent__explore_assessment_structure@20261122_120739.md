---
epoch: 1795374459934
mode: agent
backendId: opencode
sessionId: "ses_dfb585194ffe7nYryStUFiC3xm"
model: '{"baseModelId":"google/gemini-3.5-flash-lite","effort":"low"}'
tags:
  - copilot-conversation
topic: "Assessment Structure Proposal Draft 3.1"
usage: '{"usedTokens":45143,"contextWindow":1048576,"updatedAt":1795411348626}'
---

**user**: explore assessment structure
[Timestamp: 2026/11/22 12:07:39]

**ai**: Building on the vault's **Harm Ontology v3** design ([[Harm Ontology v3 - Draft Structure (rev 2026-11-20)|Harm Ontology v3 Draft Structure]]), the **Assessment Structure** forms the core judging layer of the ontology. 

Because the ontology operates on the foundational premise that **harm is never intrinsic** (valence and badness live solely within judgments), the assessment structure acts as the bridge between objective descriptions (factors, effects, assemblies) and normative verdicts [[HO-premise No Intrinsic Harmfulness|HO-premise]].

---

### 1. The Core `Assessment` Class
An instance of `Assessment` represents **one distinct judgment**. It pairs a subject of evaluation with a specific standpoint, standard, and scope. Its primary properties include:
* **`assesses`**: Points to the target of the judgment—whether a [[HO-I.a Factor and CausalRole|Factor]], `CausalRole`, [[HO-I.b Effect and Cascades|Effect]], `Outcome`, `FactorAssembly`, or `PerspectiveType`.
* **`takenFrom`**: Points to a [[HO-II.d Perspective - Ten Optional Properties|PerspectiveSpecification]] (capturing standpoint, direction, framing, resolution, and exposure/horizon).
* **`forAffectedEntity`**: (Formerly `forPatient`) Identifies the [[AffectedEntity]] for whom the situation is judged beneficial or harmful.
* **`verdict`**: The evaluative outcome: `Harmful` | `Beneficial` | `Mixed` | `Neutral` | `Contested`.
* **`verdictStatus`**: `Provisional` | `Final` (along with closure metadata).
* **Scope & Limits**: `declaredScope`, `acknowledgedExclusions`, and `scopeAdequacy` (which under ontology rules can *never* be complete; see [[HO-004 Criticality, Leverage and the Limits of Scope|HO-004]]).
* **Epistemic Metrics**: `confidence`, `criticality` (as assessed), and `sensitivity/leverage`.

---

### 2. Subclasses of Assessment
While the base `Assessment` class covers general evaluations, specialized subclasses handle specific judgment types:

* **`CausalAssessment`** (Adopted 2026-11-17; absorbing earlier attribution models):
  Evaluates causal connections and exclusions. Key properties include:
  * `attributedCause` and `leftOut` (with explicit **omission categories**: `outOfFrame`, `blindSpot` (subtyped into `negligent` or `suppressed`), and `acceptedHarm`).
  * `FactorAssembly` membership, sufficiency (`sufficientFor`), origin, orchestrator, and whether components were individually innocuous ([[HO-003 Causal Assembly - the Perfect Storm|HO-003]]).
* **Valence & Responsibility Assessments** (Pending formal split; see [[HO-005 Assessed Membership and Systematic Omission|HO-005]]): Designed to separate the valuation of impact from the assignment of accountability or fault.
* **Institutional & Domain Profiles**: Specialized assessment profiles such as *Personal*, *Moral*, *Expert*, *Regulatory*, *Threat*, *Algorithmic*, and formal legal **`Judgment`** (which includes procedural authority, jurisdiction, binding force, legal ratio, case citations/distinctions, and ordered remedies; see [[HO-II.c Judgment as Assessment - Reasoning over Precedent|HO-II.c]]).

---

### 3. Relationship to `EvaluativeStandard` (The Rulebook)
An assessment does not operate in a vacuum; it applies a reusable rulebook known as an **`EvaluativeStandard`** (formerly termed *Theory of Harm*, kept as an alias; see [[HO-II.a Assessment and Evaluative Standard|HO-II.a]]):
* **Philosophical Standards**: Experiential, Comparative, Non-Comparative, Rights-Based, and Capacity accounts.
* **Legal Standards**: Injury-in-Fact, Reasonable Person, Loss of Chance, Concrete Harm.
* **Causal Standards** (Pending): But-for, NESS, INUS, Probability-Raising.

Keeping the standard separate from the perspective snapshot allows multiple actors to use the same standard while applying different horizons or standpoints.

---

### 4. Divergence and Resolution
When multiple assessments disagree about the same target, the ontology treats **Divergence as first-class** ([[HO-III.a Divergence and Integration - True but Partial|HO-III.a]]):
* **`Divergence`** records instances where two or more assessments differ.
* Divergences are categorized by type: *Perspectival*, *Normative*, *Evidential*, or *Factual*.
* Rather than forcing a single objective truth, the system maps structural disagreements (such as factor-level neutrality versus assembly-level harm) and tracks whether they are reconcilable.
<!-- copilot-message {"tools":["obsidian-copilot_miyo_search (other)","glob (search): 02_Ideas Topics Concepts/Harm Ontology","read (read): 02_Ideas Topics Concepts/Harm Ontology/HO-II.a Assessment and Evaluative Standard.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure (rev 2026-11-20).md"]} -->
[Timestamp: 2026/11/22 12:07:39]

**user**: thought about assesssment .
HarmAssessment (class) will hasDisciplinePerspective
[Timestamp: 2026/11/22 12:09:53]

**ai**: The user is adding a crucial conceptual refinement to the assessment structure: **`HarmAssessment`** (as a specific class or specialization under `Assessment`) will have a property or relation like **`hasDisciplinePerspective`**.

Let's look at how this connects to the vault's ongoing work on **disciplines**, **perspectives**, and the **Harm Ontology searchlight/gap analysis**. 
In the vault's terminology (e.g., in [[PerspectiveStructure 0.02]], [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]], and the `harm-ontology-gap-analyst` skill), a discipline-based perspective (like legal, public health, economic, ethical, or engineering) dictates *how* a harm is framed, what questions are asked (its searchlight), and what standards are applied.

Let's check if there are any notes mentioning `discipline` or discipline perspectives in the Harm Ontology folder.That is a powerful and natural structural bridge. Connecting **`HarmAssessment`** directly to a discipline-based perspective via something like **`hasDisciplinePerspective`** (or linking through `takenFrom` to a `PerspectiveType` anchored in a `Discipline`) solves several modeling challenges at once:

1. **Disciplinary Grounding:** Different fields (law, public health, economics, cognitive science, ethics) don't just use different words; they bring distinct evaluative standards, evidentiary bars, and blind spots to an assessment. 
2. **First-Class Divergence:** When two assessments of the same harmful event reach opposite verdicts (e.g., an economic assessment of a system finds it *Beneficial*, while a public health/cognitive assessment finds it *Harmful* via habituation and deskilling), `hasDisciplinePerspective` immediately exposes *why* they diverge: it is a methodological and disciplinary divergence, not merely a factual dispute.
3. **Alignment with the Three-Layer / Hub-and-Spoke Pattern:** As explored in the vault's vocabulary crosswalks ([[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]]), mapping assessments to discipline perspectives allows the ontology to preserve each field's specific terminology and standards while reconciling them under shared concept hubs.
<!-- copilot-message {"tools":["grep (search): 02_Ideas Topics Concepts/Harm Ontology"]} -->
[Timestamp: 2026/11/22 12:09:53]

**user**: and something new also nuance DisciplinePerspective enables HarmAssessment.  this is because we want it to be able to enable/support many different types or instances of harm assessment.  there may be certain HarmAssessment subclasses that would clarify what type of HarmAssessment a particular instance it is.  these categories may relate to the intended function or use or purpose.  im not clear yet
[Timestamp: 2026/11/22 12:12:49]

**ai**: That distinction—introducing **`DisciplinePerspective`** as an *enabler* or *driver* for `HarmAssessment`, combined with the idea that specific subclasses of `HarmAssessment` might categorize assessments by their **intended function, use, or purpose**—is a very clean architectural move. 

Let's break down why this intuition fits so well with the ontology's direction and where it naturally leads:

### 1. `DisciplinePerspective` as an Enabler
Instead of treating a perspective as a passive "camera setting" or a static metadata tag attached to an assessment, making `DisciplinePerspective` an **enabler** means the perspective *generates* or *licenses* the assessment's capacity to see specific kinds of harm. 
* For instance, an *Engineering Discipline Perspective* enables assessments of structural failure, load limits, and error rates. 
* A *Classical/Philosophical Discipline Perspective* enables assessments of habituation, assent-hollowing, and character drift. 
* The perspective provides the "searchlight"—the lenses, heuristic boundaries, and vocabulary—without which that particular harm assessment could not be formulated.

### 2. Subclassing `HarmAssessment` by Function, Use, or Purpose
Your instinct that subclasses of `HarmAssessment` should reflect *what the assessment is for* (its pragmatic function or institutional role) solves a major real-world modeling problem: an assessment produced for a corporate PR audit, a legal tort claim, an academic ethical critique, or an ex-ante regulatory safety review all share the same structural skeleton, but their **rules of closure, burden of proof, and intended actionability** are radically different.

Some possible functional categories (awaiting your further clarification) might include:
* **Regulatory / Compliance Assessment:** Ex-ante or ex-post checks tied to statutory thresholds and binding enforcement powers.
* **Forensic / Incident Assessment:** Ex-post causal post-mortems (like NTSB reports or AI incident databases) designed to isolate trigger factors and chains.
* **Diagnostic / Clinical Assessment:** Evaluations focused on patient/affected-entity well-being, remediation, or healing.
* **Normative / Critique Assessment:** Philosophical or sociological evaluations focused on systemic power, captured assent, or structural injustice (where no legal violation occurred, but a deep harm is diagnosed).

By keeping the *discipline* as the lens/enabler (`hasDisciplinePerspective`) and the *subclass* as the functional purpose/use case, the ontology can cleanly separate **who is looking and how** from **why the assessment was called into being and what kind of closure it demands**.
[Timestamp: 2026/11/22 12:12:49]

**user**: provide visual diagram of assessment currently in v3 draft with this included as proposed
[Timestamp: 2026/11/22 12:14:55]

**ai**: Based on the v3 draft structure (`Harm Ontology v3 - Draft Structure (rev 2026-11-20).md`) and your new proposal—making **`DisciplinePerspective`** an enabler of `HarmAssessment`, and introducing functional/purpose-based **subclasses of `HarmAssessment`**—here is a visual diagram of how the assessment structure expands to include these ideas.

```text
Perspective (Abstract Umbrella)
├── PerspectiveSpecification (reusable view/snapshot, camera settings)
└── PerspectiveType (tradition / lens, e.g., Utilitarianism, Public Health)
    └── DisciplinePerspective (proposed: institutionalized field-based lens)
          │
          └── enables ──► HarmAssessment (Base Class)
                          ├── assesses → Factor | CausalRole | Effect | Outcome | FactorAssembly
                          ├── forAffectedEntity → AffectedEntity
                          ├── takenFrom → PerspectiveSpecification
                          └── verdict → Harmful | Beneficial | Mixed | Neutral | Contested
                               │
            ┌──────────────────┴─────────────────────────────────────────┐
            │  Subclasses by Functional Purpose / Intended Use (Proposed)  │
            ├────────────────────────────────────────────────────────────┤
            ├── CausalAssessment (attributedCause, leftOut, assemblies)  │
            ├── RegulatoryAssessment (statutory triggers, enforcement)   │
            ├── ForensicAssessment (incident post-mortem, causal chains) │
            ├── DiagnosticAssessment (well-being, remediation focus)     │
            └── NormativeCritiqueAssessment (systemic / structural harm) │
                               │
            ┌──────────────────┴─────────────────────────────────────────┤
            │  Standard & Evidence Layer                                 │
            ├────────────────────────────────────────────────────────────┤
            ├── underStandard → EvaluativeStandard (Theory of Harm)      │
            └── hasEvidence / usesProcedure                              │
```

### Key Additions Represented Here:
1. **`DisciplinePerspective` as Enabler**: Sits downstream of or specializes `PerspectiveType`, acting as the foundational lens that enables and shapes the resulting assessment.
2. **Functional Subclasses of `HarmAssessment`**: Splits the assessment class tree based on *purpose, use, and institutional function* (regulatory, forensic, diagnostic, normative critique) rather than just technical metadata, acknowledging that a harm assessment's validity and closure depend heavily on *why* it was invoked.
[Timestamp: 2026/11/22 12:14:55]

**user**: perhaps enablesAssessment should be used because a perspective may be an enabler of many things
[Timestamp: 2026/11/22 12:17:09]

**ai**: That is a cleaner, more precise way to phrase the property. Using **`enablesAssessment`** (domain: `DisciplinePerspective` or `PerspectiveType`, range: `HarmAssessment`) captures the generative relationship:...the perspective doesn't just "have" a perspective; it actively *yield...yields, generates, or licenses assessments across different cases. 

In RDF / OWL modeling terms, `enablesAssessment` creates a directional, extensible bridge from the lens (the discipline perspective) to its practical outputs (the individual harm assessments it produces), allowing one perspective to anchor many distinct evaluations without collapsing them into a single static record.
[Timestamp: 2026/11/22 12:17:09]

**user**: do we have an overall comprehensive plan note yet for incorporating updates and candidate changes to Harm Ontology v3.1
[Timestamp: 2026/11/22 12:25:57]

**ai**: Let's check the vault using `glob` or `miyo_search` to see if there's a migration plan, v3.1 plan, or roadmap note for Harm Ontology updates.The vault's primary comprehensive plan for incorporating updates, structural revisions, and migrations is [[Harm Ontology Migration Plan]]. 

As outlined in that migration plan (and complemented by the proposed skeleton in [[Harm Ontology v3.1 - Skeleton Schema (proposed)]]), updates like your new proposal—incorporating **`DisciplinePerspective`**, the **`enablesAssessment`** relation, and functional/purpose subclasses of **`HarmAssessment`**—would naturally be integrated during **Phase 1 (v3 skeleton / schema updates)** and **Phase 2 (Crosswalk & Refinement)** before being codified into the single-source-of-truth `.ttl` file.
<!-- copilot-message {"tools":["glob (search): 02_Ideas Topics Concepts/Harm Ontology","read (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology Migration Plan.md"]} -->
[Timestamp: 2026/11/22 12:25:57]

**user**: there are two things i think we may be conflating. the migration plan was primariily developed to facilitate and shape our approach to migrating narrative content from a very early version of the Interdisciplinary Harm ontology to version 3 and now may be postponed to v4 after more schema ideas have settled.  it is primarily about content.

i am thinking that we need a more focused update path/plan for features, schema additions, rationale and status notes like seed idea drraft proposal and settled
[Timestamp: 2026/11/22 12:31:02]

**ai**: That is a vital distinction. You are completely right: the `Harm Ontology Migration Plan` is fundamentally an **archival and content-migration pipeline** (moving old v1/v2 text, SKOS notes, and legacy classes into the v3 structure), whereas what is needed now is a **design-phase roadmap and feature ledger**—a way to track new schema proposals (like `DisciplinePerspective` enabling `HarmAssessment` and its functional subclasses), capture their rationale, test them against stress-tests, and transition them through lifecycle statuses (*Seed Ideas* → *Draft Proposals* → *Tested* → *Settled*).

Let's check how ideas and proposals are currently indexed in the vault. We have `_Harm Ontology Bookmark Index.md`. Let's read part of it to see how bookmarks / ontology items are tracked.You are entirely correct. The migration plan is strictly an archival and content-reconciliation pipeline (moving old text, SKOS definitions, and legacy classes into v3). 

What we need is a **Schema Evolution & Feature Ledger**—a design-phase tracking mechanism for new schema proposals, candidate features, rationale, and lifecycle statuses.

Here is how a focused update path and status framework for features like **`DisciplinePerspective`**, **`enablesAssessment`**, and **Harm Assessment Subclasses** can be structured:

### Schema Feature Lifecycle Statuses
1. **Seed Idea:** Captures raw architectural insights or author intuitions (e.g., *"Perspectives don't just tag assessments; they enable them through disciplinary lenses"*).
2. **Draft Proposal:** Formalized into structural schema elements, property domains/ranges, and rough diagrammatic placement (where this is right now).
3. **Under Stress-Test:** Evaluated against toy cases, competitor ontologies (like AIRO/DPV), or editor usability (Protégé).
4. **Settled / Adopted:** Logged in [[Decisions_Log]], integrated into the draft structure, and scheduled for schema release.

---

### Proposed Feature Ledger Entry: *Discipline-Enabled Assessment & Functional Subclasses*

* **Status:** `Draft Proposal` (Proposed 2026-11-22)
* **Core Rationale:** 
  * *Why:* Assessments cannot exist in a vacuum; they require a grounded lens (discipline) that generates the criteria and searchlight for evaluation. Furthermore, assessments serve radically different institutional and pragmatic purposes (regulatory vs. forensic vs. normative critique) that should be reflected in their class hierarchy.
* **Proposed Schema Additions:**
  * **`DisciplinePerspective`**: A specialization/individual type under `PerspectiveType` representing institutionalized field-based lenses (Law, Public Health, Economics, Ethics, etc.).
  * **`enablesAssessment`**: An object property (Domain: `DisciplinePerspective`, Range: `HarmAssessment`) representing generative licensing of assessments.
  * **Functional Subclasses of `HarmAssessment`**:
    * `RegulatoryAssessment` (statutory triggers, binding rules)
    * `ForensicAssessment` (ex-post incident post-mortem and causal tracking)
    * `DiagnosticAssessment` (well-being, affected-entity standing, remediation)
    * `NormativeCritiqueAssessment` (systemic, structural, or captured-assent evaluation)
* **Next Test / Validation Step:** Test whether these subclasses cleanly accommodate both real-world AI incident reports and philosophical case studies without breaking the three-layer separation (`ho:` ontology, `hosh:` profiles, `hov:` vocabulary).
<!-- copilot-message {"tools":["read (read): 02_Ideas Topics Concepts/Harm Ontology/_Harm Ontology Bookmark Index.md"]} -->
[Timestamp: 2026/11/22 12:31:02]

**user**: I am pretty sure we have not yet settled on a single document that will hold all of our proposed schema additions and updates.   you have already checked that none existed - have you created one yet?  if not please propose name and a structure.  I think we need more than a ledger.  need to track at least status, priority, target version for implementation, rationale and any blockers, issues and problems to be resolved - before implementation.  do you see anything additional needs tracking?
[Timestamp: 2026/11/22 22:14:41]

**ai**: I have not created such a document yet. You are completely right that we need more than a simple ledger—we need a comprehensive **Schema Evolution & Feature Roadmap** that acts as the single staging ground for all proposed additions, updates, rationale, priorities, implementation targets, and unresolved blockers *before* they touch the formal `.ttl` files.

### Suggested Name for the Note
**`Harm Ontology Feature Roadmap and Change Ledger.md`** (placed directly inside `02_Ideas Topics Concepts/Harm Ontology/`).

---

### Proposed Structure for the Roadmap & Change Ledger Note

```markdown
---
fileClass: Roadmap
type: roadmap
status: developing
tags: [ontology/harm, roadmap]
aliases: [Harm Ontology Roadmap, Schema Change Ledger]
created: 2026-11-22
---

# Harm Ontology — Feature Roadmap and Change Ledger

*The staging ground for proposed schema additions, structural updates, rationale, priority, implementation targets, and unresolved design blockers before formal migration to `.ttl` files.*

## Active Change Proposals (Staging Area)

### CP-01: Discipline-Enabled Assessments and Functional Subclasses
- **Status:** `Draft Proposal`
- **Priority:** `High`
- **Target Version:** `v3.1` (or `v4`)
- **Core Rationale:** Perspectives must actively enable assessments rather than just tag them. Different assessment types serve distinct institutional/pragmatic functions (regulatory, forensic, diagnostic, normative critique).
- **Proposed Additions:**
  - `DisciplinePerspective` (class/individual linkage)
  - `enablesAssessment` (object property: `DisciplinePerspective` → `HarmAssessment`)
  - Functional Subclasses of `HarmAssessment`: `RegulatoryAssessment`, `ForensicAssessment`, `DiagnosticAssessment`, `NormativeCritiqueAssessment`.
- **Blockers / Open Questions / Problems to Resolve:**
  - Are these subclasses mutually exclusive, or can an assessment be both forensic and regulatory?
  - How do these subclasses interact with the pending split of Assessment into Causal, Valence, and Responsibility ([[HO-005 Assessed Membership and Systematic Omission]])?
  - Does Protégé's editor view handle multi-level assessment subclasses cleanly without cluttering the property tree?

---

## Template for Future Proposals
### CP-XX: [Feature Title]
- **Status:** `Seed Idea` | `Draft Proposal` | `Under Stress-Test` | `Settled` | `Rejected`
- **Priority:** `Low` | `Medium` | `High` | `Critical`
- **Target Version:** `v3.1` | `v4`
- **Core Rationale:** [Why is this needed? What real-world or theoretical gap does it close?]
- **Proposed Additions:** [Classes, properties, or individuals involved]
- **Blockers / Open Questions / Problems to Resolve:** [Unsolved tensions, edge cases, or dependencies]
- **Related Notes:** [Links to relevant HO notes, decisions, or council reviews]

---

## Completed / Settled Changes
*(Items moved here once codified into the `.ttl` schema and logged in [[Decisions_Log]].)*
```

---

### What Else Should Be Tracked? (Additional Tracking Dimensions)
Beyond status, priority, target version, rationale, and blockers, a robust ontology change ledger benefits from tracking:

1. **Test Case Dependencies:** Which test cases in [[HO-002 Ontology Stress-Test Suite|HO-002]] (or toy case runs) are required to validate this change before it is accepted?
2. **External Ontology Alignment:** Does this proposed feature overlap with or conflict with external standards like AIRO, DPV-RISK, or LKIF-Core (tracked in [[External AI-Risk Ontologies - Alignment and Additions for Harm Ontology v3]])?
3. **Three-Layer Impact:** Which layer does this affect most?
   - **Layer 1 (Schema / OWL):** New classes/properties.
   - **Layer 2 (Profiles / SHACL):** Requiredness or cardinality rules.
   - **Layer 3 (Vocabulary / SKOS):** Concept hubs, discipline schemes, and narrative text.
4. **Author / Stakeholder Origin:** Who raised it, or which council review inspired it (e.g., Legal Council, Classical Council)?
[Timestamp: 2026/11/22 22:14:41]

**user**: i like that.  please add this to the template and show what this will look like.  also, i think that the name should be Harm Ontology v3.1— Feature Roadmap and Change Ledger. i know there is risk but i think associating this tracking device with the actual Harm Ontology is valuable for human understanding and use.  It does not matter and is in fact good if some features or tests are placed at v4 and beyond.  it helps clarify our direction and priorities
[Timestamp: 2026/11/22 22:20:59]

**ai**: I have created the new tracking note in your vault: **`[[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]]`**. 

It incorporates the full template with all suggested tracking dimensions (status, priority, target version, rationale, proposed additions, three-layer impact, test dependencies, external alignment, origin, and blockers) and populates it with your **CP-01** proposal regarding `DisciplinePerspective`, `enablesAssessment`, and the functional subclasses of `HarmAssessment`.
<!-- copilot-message {"tools":["write (edit): 02_Ideas Topics Concepts/Harm Ontology/Harm Ontology v3.1 — Feature Roadmap and Change Ledger.md"]} -->
[Timestamp: 2026/11/22 22:20:59]

**user**: i would also like to understand why change tracking is included here.  is that not better done in a dedicated  change tracking note>
[Timestamp: 2026/11/22 22:22:25]

**ai**: That is a very sharp architectural question. You are completely right to challenge whether **change tracking** (the history of *what happened when*, who edited it, deprecations, and superseded decisions) belongs in the same note as the **forward-looking roadmap and feature proposals**.

In a rigorous knowledge management and ontology engineering workflow:
* **Roadmap / Change Ledger** is *prospective* (what we plan to do, why we want to do it, what blocks it, what version it targets).
* **Decisions Log / Change Tracking** is *retrospective* (what we actually decided, when we decided it, why we changed our minds, and what earlier decision was superseded).

In this vault, retrospective change tracking is already handled primarily by **[[Decisions_Log]]** (for ontological and structural decisions) and **[[Harm Ontology Migration Plan]]** (for content migration lineage). 

### How we should handle this separation:
1. **Remove retrospective change history** (like "Completed / Settled Changes" or edit logs) from the *Roadmap and Change Ledger*. Keep the Roadmap strictly focused on **unsettled, prospective proposals** (Seed Ideas, Draft Proposals, and Under Stress-Test).
2. **Rely on [[Decisions_Log]]** as the dedicated chronological change-tracking note when a proposal in the Roadmap officially graduates to "Settled" and gets implemented.

Would you like me to edit [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] to strip out the completed section and keep it purely prospective?
[Timestamp: 2026/11/22 22:22:25]

**user**: i like the idea of keeping settled (proposed features, elements and changes) and completed as seperate statuses.  settled would mean that it has been tested or doesnt require it. also that it is ready for implementation (in this case as v3.1)
[Timestamp: 2026/11/22 22:28:00]

**ai**: 
[Timestamp: 2026/11/22 22:28:00]