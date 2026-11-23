---
epoch: 1795374459934
mode: agent
backendId: opencode
sessionId: "ses_dfb585194ffe7nYryStUFiC3xm"
model: '{"baseModelId":"anthropic/claude-haiku-5-5","effort":"low"}'
tags:
  - copilot-conversation
topic: "Assessment Structure Proposal Draft 3.1 and Harm Ontology Feature and Change Ledger Implementaion"
usage: '{"usedTokens":181801,"contextWindow":1000000,"updatedAt":1795414661701}'
lastAccessedAt: 1795413557471
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

**ai**: That makes complete sense. Using **`Settled`** as the milestone where a feature has passed its design and testing gates and is officially "ready for implementation" (targeted at v3.1) keeps the workflow extremely clear:
1. **Draft / Stress-Test:** Proposal is being evaluated, and blockers are worked out.
2. **Settled:** Consensus reached, design validated, ready to be coded into the `.ttl` and logged in [[Decisions_Log]].
3. **Implemented / Completed:** Coded into the schema and verified.

Let's update [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] using the `edit` tool to reflect this precise distinction between *Settled (ready for implementation)* and *Completed (realized in code)*.I have updated [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] to explicitly separate **Settled** (proposals fully specified and ready for implementation in v3.1) from **Completed** (realized in code and logged in [[Decisions_Log]]), maintaining a clean, prospective design pipeline.
<!-- copilot-message {"tools":["edit (edit): 02_Ideas Topics Concepts/Harm Ontology/Harm Ontology v3.1 — Feature Roadmap and Change Ledger.md"]} -->
[Timestamp: 2026/11/22 22:28:00]

**user**: i also want to be clear that we keep "complete" as a status and retain the complete features/changes in the ledger perhaps sorted to the bottom. so that we can just easily see what we have accomplished. i think tracking date proposed and date implemente or rejected would be valuable.  The idea is also that we would copy this document into Harm Ontology 3.xx — Feature Roadmap and Change Ledger to continue after v3.1 implementation is complete.  and then continue this as a standard management/governance practice
[Timestamp: 2026/11/22 22:32:05]

**ai**: 
<!-- copilot-message {"tools":["edit (edit): 02_Ideas Topics Concepts/Harm Ontology/Harm Ontology v3.1 — Feature Roadmap and Change Ledger.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/Harm Ontology v3.1 — Feature Roadmap and Change Ledger.md"]} -->
[Timestamp: 2026/11/22 22:32:05]

**user**: please continue with last prompt
[Timestamp: 2026/11/22 22:32:55]

**ai**: I've updated [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] to match your requirements:

- **Status set:** `Seed Idea` · `Draft Proposal` · `Under Stress-Test` · `Settled` · `Complete` · `Rejected`. I used "Complete" as you wrote it, rather than "Completed".
- **Date fields added to the template:** Date Proposed, Date Settled, and Date Implemented / Rejected.
- **Bottom section renamed** to "Complete and Rejected Changes (Retained for the Record)". Finished and rejected items sit at the bottom and are never deleted.
- **Rollover note** remains at the end: when v3.1 is complete, the document is copied to `Harm Ontology v3.2 — Feature Roadmap and Change Ledger` (or v4.0) and the cycle continues.

Two things I have not done yet:
- **CP-01 has no dates.** It was proposed on 2026-11-22, so I can add that date when you confirm.
- **The `Settled` section is still empty.** CP-01 is a `Draft Proposal`, so it stays in the active section until it is settled.
<!-- copilot-message {"tools":["edit (edit): 02_Ideas Topics Concepts/Harm Ontology/Harm Ontology v3.1 — Feature Roadmap and Change Ledger.md"]} -->
[Timestamp: 2026/11/22 22:32:55]

**user**: yes add that date.  and i think it should say date settled/rejected.  not implemented/rejected.
also, i believe that the ledger should be in reverse chronological order.  newest at top oldest at bottom
can you also review and collect all currently open proposals or decisions here for review. i am thinking that a decision is really a type of proposal - a proposed item that needs resolution
[Timestamp: 2026/11/22 22:39:32]

**ai**: I've updated the ledger. Changes:

- **CP-01 now has a date:** Date Proposed 2026-11-22.
- **Date field renamed** to "Date Settled / Rejected" in the template and all entries.
- **Ordering:** active items run newest first, oldest last. Note that IDs follow collection order, not dates.
- **Type field added:** `Proposal`, `Decision`, `Open Issue` or `Task`. Decisions are a kind of proposal that needs resolution, as you suggested.

**Open items collected (19 entries, CP-01 to CP-19):**

| Date | Item | Type |
|---|---|---|
| 2026-11-22 | Discipline-enabled assessments and functional subclasses | Proposal |
| 2026-11-21 | Narrative generation (searchlight pilot) | Task |
| 2026-11-19 | Agents, participation and assessing organisations (HO-007) | Decision |
| 2026-11-18 | Assessment-everywhere (variant B) | Decision |
| 2026-11-18 | Strict settlement rule | Open Issue |
| 2026-11-18 | Narrative placement and editor usability | Open Issue |
| 2026-11-18 | AffectedEntity subtype names | Decision |
| 2026-11-18 | affectedStanding as exclusive | Decision |
| 2026-11-16 | Capability approach (Sen and Nussbaum) | Decision |
| 2026-11-16 | Map v3 to AIRO, VAIR and DPV | Task |
| 2026-11-15 | Split Assessment (Causal, Valence, Responsibility) | Decision |
| 2026-11-15 | Causal standards | Proposal |
| 2026-11-15 | Reify `participatesIn` as a claim | Decision |
| 2026-11-15 | "Sufficient as assessed" (revises HO-003) | Decision |
| 2026-11-15 | Condition split and role types | Open Issue |
| 2026-11-14 | Worldviews as standards | Decision |
| 2026-11-14 | Classical Council ideas as standards | Decision |
| Undated | HO-006 causal chain class (v4) | Proposal |
| Undated | Other open items from the v3 draft | Open Issue |

**Caveats:**
- This list comes from the notes I read: the v3 draft (rev 2026-11-20), the migration plan, the bookmark index and the HO-II.a note. It is not exhaustive. Several notes I did not open, such as HO-005, HO-007 and the handoffs, may hold more.
- Dates marked "2026-11-15 (draft structure)" are the draft's creation date, not the date each item was actually raised. Please correct any you know.
- Two items are shown as undated: HO-006 and the grouped carry-forward item. I didn't find dates for them.

Would you like me to go through the notes I didn't open, so I can confirm or add items?
<!-- copilot-message {"tools":["write (edit): 02_Ideas Topics Concepts/Harm Ontology/Harm Ontology v3.1 — Feature Roadmap and Change Ledger.md"]} -->
[Timestamp: 2026/11/22 22:39:32]

**user**: yes.  this list should be complete so make your search exhaustive
[Timestamp: 2026/11/22 22:41:03]

**ai**: I searched the Harm Ontology folder, the Decisions Log, the admin and task notes, the handoffs, and the session notes in the Writer's Room. I found about 80 open items, far more than the 19 in the ledger. Most are not yet entered in the ledger. Several are the same item seen from different notes, so I've merged them. Dates are given where the vault records them. Blank means no date is recorded.

**Not yet searched:** the `copilot/copilot-conversations/` transcripts. They may hold more open points, and I can sweep them next if you want full coverage.

## 1. Schema and structure (v3.1 candidates)

| # | Open item | Type | Date | Source |
|---|---|---|---|---|
| S1 | Discipline-enabled assessments and functional subclasses (CP-01) | Proposal | 2026-11-22 | Session |
| S2 | Agents, Event, participation and assessing organisations (HO-007). Bookmark shape not decided, not in the index, and the author has not confirmed it | Decision | 2026-11-19 | Handoff |
| S3 | What counts as an agent (a lion, flood water, an AI system); what `Agent (?)` covers | Open | 2026-11-15 | v3 draft |
| S4 | Narrative placement: on the property or the concept. Reopened after the Protégé review | Open | 2026-11-18 | Provisional brief |
| S5 | Domains, ranges and property groups for every class. Instances show no fields to fill in. Data-entry route not chosen | Task | 2026-11-19 | Handoff |
| S6 | How the 12 display groups are represented (super-properties plus annotation, or other) | Open | 2026-11-18 | Handoff |
| S7 | Layer-1 rename from "ontology" to "schema" is adopted but not logged | Decision | 2026-11-18 | Handoff |
| S8 | `nameByDomain` / `definitionByDomain` renamed to `…ByDiscipline`? | Decision | 2026-11-21 | Skeleton |
| S9 | `fieldOfApplication` gets a target class, not free text | Decision | 2026-11-21 | Skeleton |
| S10 | `observabilityLimit` (0.01) has no 0.02 match. Confirm whether Box A covers it | Open | 2026-11-21 | Skeleton |
| S11 | Group numbering: "twelve display groups" but numbered 0–12 | Open | 2026-11-21 | Skeleton |
| S12 | `CorePrinciples`: class, or one individual whose members are principles? | Open | 2026-11-21 | Skeleton, Decisions Log |
| S13 | Attachment for core principles: new property (`hasCorePrinciples`) or `foundationalCommitments` | Open | 2026-11-21 | Decisions Log |
| S14 | `foundationalCommitments` needs a range | Open | 2026-11-21 | Skeleton |
| S15 | `heldBy → Discipline` or `CollectiveAgent`; overlaps `bearerRole` and `lineage` | Open | 2026-11-21 | Skeleton |
| S16 | `usedBy → Agent`: one relation with `practisedIn`, or two? | Open | 2026-11-21 | Skeleton |
| S17 | `informedBy → Theory`, with status as an Assessment or a fixed value | Open | 2026-11-21 | Skeleton |
| S18 | Proposed new classes: Discipline, Theory, ConceptualTerritory, FieldOfApplication | Proposal | 2026-11-21 | Skeleton |
| S19 | `hasVocabulary`, `anchoredIn`, `statedPurpose / use → Purpose` | Proposal | 2026-11-21 | Skeleton |
| S20 | Element-typing rule: an element that is both participant and term (ConceptualTerritory); the rule itself is logged as a working rule | Open | 2026-11-21 | Decisions Log |
| S21 | Is a discipline's perspective the same kind as a tradition's? Working answer: yes | Open | 2026-11-21 | Skeleton |
| S22 | Do disciplines hold perspectives, or do communities of practitioners? | Open | 2026-11-21 | Skeleton |
| S23 | Can a PerspectiveSpecification instantiate more than one tradition (mixed lenses)? | Open | 2026-11-20 | 0.02, Handoff |
| S24 | Physics and Integral coverage test: not run, waiting for the author's go-ahead | Task | 2026-11-21 | Skeleton |
| S25 | Overlap test (0.02 table) and naming test in Protégé | Task | 2026-11-21 | Skeleton |
| S26 | Harm-assessment gap schema: attach to PerspectiveType, a procedural layer, or `HarmAssessment`? Attachment is provisional | Decision | 2026-11-21 | Handoff |
| S27 | Four candidate gap attribute groups (Mandate, Valuation, Procedural Lifecycle, Remedial Closure) are not logged or tested | Proposal | 2026-11-21 | Handoff |
| S28 | Placement test for proposed elements: is it a tradition, an assessment, the thing assessed, or an output? Recorded as proposed | Decision | 2026-11-21 | Handoff |
| S29 | Which of the 20 searchlight questions become attributes and which stay narrative | Open | 2026-11-21 | Session |
| S30 | Statement-level provenance (RDF-star or named graphs) | Open | 2026-11-17 | 0.01, 0.02 |
| S31 | Attribute-space or embedding model for comparing traditions | Open | 2026-11-17 | 0.02 |
| S32 | Record the ontology itself as an instance of its own PerspectiveType | Open | 2026-11-17 | 0.02, Council reviews |
| S33 | Two-level split: PerspectiveType vs Perspective (0.01) | Open | 2026-11-15 | 0.01 |
| S34 | Keep `developmentalAltitude` given it is contested | Open | 2026-11-15 | 0.01 |
| S35 | Assessment `CausalAssessment` profile: does it need its own perspective profile? | Open | 2026-11-17 | HO-005 |
| S36 | Mandatory core SHACL properties for every Assessment (horizon, scope, AffectedEntity?) | Open | 2026-11-14 | HO-II.e |

## 2. Council proposals awaiting decision (PerspectiveStructure 0.01 reviews)

Each of these is open. Some are partly absorbed in 0.02, so their status needs checking.

- **Classical:** Stance group; treat groups as display facets only, not classes; split status.
- **Ethics:** Normative core group; `moralCircle` as a third scope axis.
- **Legal:** Institutional group; Hart's description/evaluation split across the structure; `validFrom` / `validTo` everywhere.
- **Logic:** minimal core plus pragmatic test as the consolidation method; hybrid OWL + SKOS for "harm"; corroboration and calibration in place of `verificationStatus` for lenses.
- **Physics:** frames in an attribute space; dynamics group; invariants and transformations as the test for perspectival vs factual divergence.
- **Sci-Fi:** Subject's side group; Power and Infrastructure facets; `acceptedHarm` as a first-class sibling of `blindSpot`.
- **Cognitive:** AI systems as recordable PerspectiveTypes; four-way blind-spot typing (partly resolved 2026-11-17); a "verdict convergence, rationale divergence" Divergence subtype; `explorationMode`.

## 3. Vocabulary and crosswalk (layer 3)

- Hub `hov:hubs` renamed, or each hub its own scheme (2026-11-20)
- Integral: discipline scheme or tradition scheme (`int:` keying) (2026-11-20)
- `psy:moralStages`: which scheme (2026-11-20)
- Where hub narrative lives (2026-11-20)
- Two `developmentalAltitude` elements plus an untyped `rdf:Description`: which carries the label (2026-11-20)
- Congruence grades: Kant changed to closeMatch; review the other four (2026-11-17)
- Blind-spot grades (eight spokes): review
- Developmental-altitude grades: review; verify the 12-colour sequence, teal/turquoise names and the third tier against primary text
- Is the third tier kosmocentric or beyond the band scheme?
- Check Gilligan's wording; check Hierocles before using his circles as a scale
- Which hubs come next: accountability locus, consent to be seen; interior/exterior hubs from AQAL
- Should discipline scheme index notes exist now or later?
- Is "congruence" plain enough as a hub name?
- Meta-Category V crosswalk: review targets, decide VB-0, load AIRO/DPV, run on Meta-Category II, open V-2e (Akerlof/Stiglitz)

## 4. Ontology body (HO notes)

- **HO-001:** how is dispositional harm measured; is consent a defence or part of the mechanism; assent/judgment as an object of harm.
- **HO-002:** who runs the tests (self-evaluation problem); one note per test case; a case for each verdict value (Mixed, Neutral, Contested).
- **HO-002.a:** agreement rules behind Settled and Disputed; `modality` definition (resolved for the test, not yet logged); the three author decisions.
- **HO-003:** role within an assembly; nested assemblies; "jointly sufficient" when members are Unknown; revision still pending.
- **HO-004:** how criticality is assessed without a full model; does `predictabilityHorizon` belong to the perspective or the system; provisional verdicts becoming final outside law.
- **HO-005:** what anchors assessments against the regress (evidence anchor); Valence/Responsibility split; causal standards; reifying `participatesIn`; "sufficient as assessed".
- **HO-006 (v4):** is a Chain a class or a view; what the horizon is measured from; whether it cuts by time, link count or probability; where `maxHorizon` lives; chain-level net assessment; status calculation change; Chain under `CausalCandidate`; `withinChain` untested.
- **HO-I.a:** role types complete; causal share measurable; can a structure cause harm; the Condition split.
- **HO-I.b:** net results across a chain.
- **HO-I.c:** posthumous harm as ConditionallyPhenomenal: a value or a Divergence.
- **HO-II.a:** worldviews as standards; Classical Council ideas as standards.
- **HO-II.b:** block the "who knows?" excuse, e.g. require confidence on extrapolated links.
- **HO-II.c:** who encodes the ratio; the TransUnion test case.
- **HO-II.d:** does `fitness` belong to the perspective or the standard-intent pair.
- **HO-II.d.3:** should a scheme be keyed to a discipline or tradition; rename hub grouping.
- **HO-III.a:** can coverage be measured; is "Contested" redundant once Divergences exist.
- **HO-III.b:** versions and licences (SNOMED CT); how loose the BFO alignment should be.
- **HO-premise:** is "Contested" a verdict or a sign of a Divergence; does the rights-based standard break the premise.

## 5. Assessment-everywhere (variant B)

- Adoption gated by the non-expert test. Options: re-run with a fixed snapshot, with a human, or with larger data. Then score.
- SHACL validation (no assessment, shortcuts without status) — not run.
- Horizon test R01: needs sourced research first (new chat).
- Does the strict settlement rule leave almost anything Settled in real data?
- CQ7 still partly met; CQ8's "directly affected" wording (core `affects` or `affectedStanding = Direct`) awaiting author answer.
- `affectedStanding` treated as exclusive: test choice to revisit.
- `occurredDuring` (interval): proposed, untested.
- AffectedEntity subtypes: `NonSentientSystem` vs `NaturalSystem` / `EngineeredSystem`; `CollectiveNaturalGroup`; `Household`; `Unclassified`; AffectedEntity type as an assessment.
- Re-read author decisions 5–21 before building further (flagged as a caution in the handoff).

## 6. Tasks and migration

- **Licence check for DOLCE+DnS Ultralite (DUL):** blocking. Sources conflict. Ask the ODP maintainers in writing; evaluate CC BY 4.0 DOLCE as an alternative; record the outcome.
- **Capability approach (Sen and Nussbaum):** HIGH PRIORITY, before Phase 3.
- **Map v3 to AIRO, VAIR, DPV-RISK, LKIF-Core:** check negative valence before choosing `closeMatch` or `equivalentClass`.
- **Narrative generation (searchlight pilot):** one PerspectiveType; proposed, not started.
- **Methodology rules 1–7:** the one-page draft is referenced in the 2026-11-20 session note as `Handoff - Harm Ontology Methodology Re-evaluation`, but that note does not exist in the vault.
- **Migration Phase 0:** open the `# Master Formal Ontology of Harm` source and compare v1 and v2.
- **Root files:** archive decision on `Interdisciplinary_Harm_Ontology_Compendium.md` and the root `.ttl`. Awaiting your decision.
- **Scripts:** delete the `~/harm-ontology-scripts/` duplicate once the vault copy is trusted.
- **Bookmarks:** HO-II.d.3 and the HO-007 bookmark are not yet in the index; the placement of HO-II.d.4 is awaiting confirmation.
- **Three open questions on the 2026-11-19 explanations:** one bookmark with tiers or separate; add the HO-002 test cases now; is "participation" the right word.

## Next step

I can write the full set into the ledger as entries with IDs, types, dates and status. CP-19 would then be split out. Two questions before I do:

1. **Granularity:** one entry per item (about 80), or group by topic as above (about 15 entries)?
2. **Dates:** I'd leave undated items as undated rather than guess. Do you want to fill any in?
<!-- copilot-message {"tools":["grep (search): 02_Ideas Topics Concepts/Harm Ontology","grep (search): 00_Claude_Admin","grep (search): 01_The Writer's Room","read (read): 01_The Writer's Room/Handoff - Harm Ontology.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3.1 - Skeleton Schema (proposed).md","read (read): 00_Claude_Admin/Canon_and_Continuity.md","Get-ChildItem -Recurse -Filter *.md \"02_Ideas Topics Concepts/Harm Ontology\" | ForEach-Object { $f=$_; $lines=Get-Content -LiteralPath $f.FullName -Encoding UTF8; $start=-1; for($i=0;$i -lt $lines.Count;$i++){ if($lines[$i] -match '^#+ .*(Open question|Open issue|Pending|Open and pending|Open decisions)'){ $start=$i; \"== $($f.Name) L$($i+1)\"; continue }; if($start -ge 0){ if($lines[$i] -match '^#+ ' ){ $start=-1 } elseif($lines[$i].Trim() -ne ''){ $lines[$i] } } } } (execute)","cd \"ObsidianVault01_AI_Harm_Book\"; Select-String -Path \"00_Claude_Admin\\Decisions_Log.md\" -Pattern 'pending|proposed|open|not decided|awaiting|untested' -CaseSensitive:$false | ForEach-Object { $_.Line.Substring(0,[Math]::Min(260,$_.Line.Length)) }; \"----\"; Get-ChildItem -Recurse -Filter \"*Methodology*\" | Select-Object -ExpandProperty FullName; Get-ChildItem -Recurse -Filter \"*Follow-ups*\" | Select-Object -ExpandProperty FullName; \"----\"; Get-Content -LiteralPath \"02_Ideas Topics Concepts\\Harm Ontology\\ontology\\Harm Ontology v3 Provisional Release Brief.md\" -Encoding UTF8 | Select-Object -First 60 | ForEach-Object { $_.Substring(0,[Math]::Min(220,$_.Length)) } (execute)","cd \"ObsidianVault01_AI_Harm_Book\"; foreach($f in @(\"01_The Writer's Room\\Handoff - Perspective Vocabulary and v3 Follow-ups.md\",\"01_The Writer's Room\\2026-11-21 Harm Ontology Searchlight and Gap Session.md\",\"01_The Writer's Room\\2026-11-20 Harm Ontology Sample Review and Methodology.md\",\"02_Ideas Topics Concepts\\Harm Ontology\\ontology\\Harm Ontology v3 Harm Assessment Schema Extensions (Proposed).md\",\"00_Claude_Admin\\Tasks\\Perspective Narrative Generation - Searchlight Task.md\")) { \"=== $f\"; Select-String -LiteralPath $f -Pattern 'pending|open|not decided|to decide|awaiting|untested|\\?\\s*$|next' -CaseSensitive:$false | ForEach-Object { $_.Line.Substring(0,[Math]::Min(200,$_.Line.Length)) } } (execute)"]} -->
[Timestamp: 2026/11/22 22:41:03]

**user**: great. Let's do this with one major addition.  you seem to have lost the rationale somewhere along the way.  if this is to be meaningful we need to retain why we proposed it in the first place.  also, if any of the items are blockers, why and what feature/change they block.  dont know if this is best accomplished with additional columns

please redisplay the previous work with additions discussed.

pause and wait for confirmation then:

then lets close this conversation. lets harvest any ideas with appropriate bookmarking and generate session note (there is a lot of good detail here) . and update handoff especially to include what's needed to continue with finalizing a draft proposal for assessment
[Timestamp: 2026/11/22 23:08:02]

**ai**: Here is the full ledger with rationale and dependencies added. I have not written anything to the vault yet.

**Proposed format.** I suggest two additions:
- **Why proposed:** a short rationale with its source. Where the vault gives no reason, the cell says "not recorded" rather than guessing.
- **Blocks / Blocked by:** typed IDs, for example "Blocks: S5, S26". Keeping them as fields rather than only columns lets a Bases view filter on them later.

Priority is H/M/L where the vault indicates it, otherwise "–". Target is v3.1 unless marked v4. Blockers marked (inferred) are my reading of how items relate, not something a note states.

---

## 1. Schema and structure

| ID | Item | Type | Status | Date | Pri | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|---|
| S1 | Discipline-enabled assessments and functional subclasses (CP-01) | Proposal | Draft | 2026-11-22 | H | Perspectives should enable assessments, not just tag them. Assessments serve different purposes (regulatory, forensic, diagnostic, normative) | Blocked by S21, S26. Interacts with K1 |
| S2 | Agents, Event, participation, assessing organisations (HO-007) | Decision | Draft | 2026-11-19 | H | Robbery case (robbers take part in an event that is part of an assembly); lion, storm and audit-firm cases raised by the author | Blocks S3, K3, A9. Blocked by T10 |
| S3 | What counts as an agent; `Agent (?)` scope, incl. AI systems | Open | Open | 2026-11-15 | M | Lion, flood water and AI system cases; the draft marks Agent "(?)" | Blocked by S2 |
| S4 | Narrative placement: on the property or the concept | Open | Reopened | 2026-11-18 | H | Mini example judged "awful" in Protégé; sample placements differ | Blocks D1 build, S5 |
| S5 | Domains, ranges and property groups for every class; data-entry route | Task | Open | 2026-11-19 | H | Instances show no fields to fill in; OWL attaches properties to classes poorly | Blocks D1 build. Blocked by S4, S6 |
| S6 | How the 12 display groups are represented | Open | Open | 2026-11-18 | H | Author: "this subgrouping was essential to understanding"; 0.02 says display facets, not classes | Blocks S5 (groups) |
| S7 | Layer-1 name "schema" (replaces "ontology") | Decision | Adopted, unlogged | 2026-11-18 | L | Naming clarity; author's choice | Blocks logging only |
| S8 | Rename `nameByDomain` / `definitionByDomain` to `…ByDiscipline` | Decision | Draft | 2026-11-21 | M | "Domain" is overloaded with rdfs:domain | Blocked by T9, coverage and overlap tests (S24, S25) |
| S9 | `fieldOfApplication` gets a target class, not free text | Decision | Draft | 2026-11-21 | M | Free text cannot be queried; 0.02 group 5 | Blocks S16. Blocked by S25 |
| S10 | `observabilityLimit` (0.01) has no 0.02 match | Open | Open | 2026-11-21 | L | Attribute dropped between versions; not recorded why | Blocked by Box A decision |
| S11 | Group numbering: "twelve groups" but numbered 0–12 | Open | Open | 2026-11-21 | L | Inconsistent count | Blocks S6 ordering |
| S12 | `CorePrinciples`: class or single individual? | Open | Open | 2026-11-21 | H | Generative rules that produce verdicts (physics example) | Blocks S13. Blocked by S24 |
| S13 | Attachment for core principles | Open | Open | 2026-11-21 | H | Foundational commitments (identity) and core principles (generative) are different relations (logged 2026-11-21) | Blocked by S12, S14. Separate conversation planned |
| S14 | `foundationalCommitments` needs a range | Open | Open | 2026-11-21 | M | Logged property has no range | Blocks S13 |
| S15 | `heldBy` → Discipline or CollectiveAgent | Open | Open | 2026-11-21 | M | Who holds a perspective; overlaps `bearerRole`, `lineage` | Blocked by S22, S25 |
| S16 | `usedBy` vs `practisedIn`: one relation or two | Open | Open | 2026-11-21 | M | Separate settings from agents that use a perspective | Blocked by S9 |
| S17 | `informedBy` → Theory, with assessed status | Proposal | Draft | 2026-11-21 | M | Traditions draw on theories with differing support; status may be an assessment | Blocked by S25; open whether status is an Assessment |
| S18 | New classes: Discipline, Theory, ConceptualTerritory, FieldOfApplication | Proposal | Draft | 2026-11-21 | M | "Physics" has at least five senses; each needs its own class | Blocked by S20, S25 |
| S19 | `hasVocabulary`, `anchoredIn`, `statedPurpose` / `use → Purpose` | Proposal | Draft | 2026-11-21 | L | Traditions keyed to disciplines; uses need a purpose node | Blocked by S21, S22 |
| S20 | Element-typing rule for elements that are both participant and term | Open | Working rule | 2026-11-21 | M | Overloaded words (ConceptualTerritory) | Blocks S18 (inferred) |
| S21 | Is a discipline's perspective the same kind as a tradition's? | Open | Working answer: yes | 2026-11-21 | H | CP-01 depends on DisciplinePerspective being a PerspectiveType | Blocks S1 |
| S22 | Do disciplines or communities of practitioners hold perspectives? | Open | Open | 2026-11-21 | M | Decides `heldBy` | Blocks S15 |
| S23 | Can one specification combine more than one tradition (mixed lenses)? | Open | Open | 2026-11-20 | L | Real assessments may draw on several lenses | Blocks nothing recorded |
| S24 | Physics and Integral coverage test | Task | Not run | 2026-11-21 | H | Test 0.02 structure against two different perspectives before logging | Blocks logging of S8–S20. Awaiting author go-ahead |
| S25 | Overlap test (0.02 table) and naming test in Protégé | Task | Not run | 2026-11-21 | H | Check each new name against neighbours and methodology rules | Blocks logging of S8–S20 |
| S26 | Gap schema attachment: PerspectiveType, procedural layer or HarmAssessment | Decision | Provisional | 2026-11-21 | H | Gap groups (mandate, valuation, lifecycle, remedy) describe assessment acts, not traditions | Blocks S27, S1 subclass placement. Blocked by S28 |
| S27 | Four gap attribute groups | Proposal | Draft | 2026-11-21 | M | Real institutions (e.g. EIA) need mandate, metric, trigger and remedy, which HO lacks | Blocked by S26, S28 |
| S28 | Placement test for new elements | Decision | Proposed method | 2026-11-21 | H | Stops elements landing in the wrong class; applies to all future proposals | Blocks S26, S27 |
| S29 | Which of the 20 searchlight questions become attributes | Open | Open | 2026-11-21 | M | Some questions may be better as narrative | Blocked by T4 |
| S30 | Statement-level provenance (RDF-star or named graphs) | Open | Open | 2026-11-17 | M | Claims need their own source | None recorded |
| S31 | Attribute-space model for comparing traditions | Open | Open | 2026-11-17 | L | Physics council: frames as points in attribute space | None recorded |
| S32 | Ontology as an instance of its own PerspectiveType | Open | Open | 2026-11-17 | L | Model should state its own lens | None recorded |
| S33 | Two-level split: PerspectiveType vs Perspective | Open | Probably absorbed | 2026-11-15 | M | 0.01 proposal; Perspective umbrella adopted 2026-11-17 | Needs status check |
| S34 | Keep `developmentalAltitude`, given it is contested | Open | Open | 2026-11-15 | M | Integral concept with contested support | Blocked by V7 |
| S35 | Does CausalAssessment need its own profile? | Open | Open | 2026-11-17 | M | Causal judgments may need different required fields | Blocked by K1 |
| S36 | Mandatory SHACL properties for every Assessment | Open | Open | 2026-11-14 | M | Missing means "not considered", so a minimum set is needed | Blocks D3 validation. Blocked by A1 |

## 2. Council proposals (PerspectiveStructure 0.01 reviews)

| ID | Item | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|
| C1 | Classical: Stance group; treat groups as display facets only | Open | 2026-11-17 | Character and orientation not captured; facets vs classes | Blocked by S6 |
| C2 | Ethics: Normative core group; `moralCircle` as third scope axis | Open | 2026-11-17 | Normative commitments not separated from identity | Blocked by S6 |
| C3 | Legal: Institutional group; description/evaluation split; `validFrom`/`validTo` | Open | 2026-11-17 | Law separates describing a rule from evaluating it; versioning needed | Blocks S6. Overlaps S33 |
| C4 | Logic: minimal core plus pragmatic test; corroboration in place of `verificationStatus` for lenses | Open | 2026-11-17 | Popper/Mayo: "verified" overstates what is known about a lens | Blocked by S30 (inferred) |
| C5 | Physics: dynamics group; invariants as test for perspectival vs factual divergence | Open | 2026-11-17 | Feedback and invariance give a test for divergence | Blocked by S31 |
| C6 | Sci-Fi: Subject's side group; Power and Infrastructure facets | Open | 2026-11-17 | Subject perspective and power were missing | Blocked by S6 |
| C7 | Sci-Fi: `acceptedHarm` as sibling of `blindSpot` | Partly absorbed | 2026-11-17 | Accepted harm differs from a blind spot | Absorbed in omission categories (2026-11-17); confirm |
| C8 | Cognitive: AI systems as recordable PerspectiveTypes | Open | 2026-11-17 | AI systems carry trained-in lenses | Blocks V13 (inferred) |
| C9 | Cognitive: "verdict convergence, rationale divergence" as Divergence subtype | Open | 2026-11-17 | Agreement on verdict can hide different reasons | Blocks HO-III.a subtypes |
| C10 | Cognitive: `explorationMode` (explore vs exploit) | Open | 2026-11-17 | Explorers find new harms | None recorded |

## 3. Vocabulary and crosswalk (layer 3)

| ID | Item | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|
| V1 | Rename `hov:hubs`, or make each hub its own scheme | Open | 2026-11-20 | Plural name reads like a concept | Blocked by T5 |
| V2 | Integral scheme keyed to discipline or tradition | Open | 2026-11-20 | Integral is one author's tradition, closer to a PerspectiveType | Blocks V3, V9 |
| V3 | Scheme for `psy:moralStages` | Open | 2026-11-20 | Placement unchecked | Blocked by V2 |
| V4 | Where hub narrative lives | Open | 2026-11-20 | Samples differ | Blocked by T5 |
| V5 | Two `developmentalAltitude` elements plus untyped `rdf:Description` | Defect | 2026-11-20 | Sample error found in review | Blocked by T5 |
| V6 | Congruence and blind-spot grades review | Partly done | 2026-11-17 | Mapping grades need checking; Kant changed to closeMatch | None |
| V7 | Developmental altitude: verify 12-colour sequence, Gilligan wording, Hierocles | Open | 2026-11-17 | Citations unverified | Blocks V8, S34 |
| V8 | Is the third tier kosmocentric? | Open | 2026-11-17 | Source does not say | Blocked by V7 |
| V9 | AQAL interior/exterior hubs | Proposal | 2026-11-17 | Vocabulary coverage | Blocked by V2 |
| V10 | Next hubs: accountability locus, consent to be seen | Proposal | 2026-11-17 | Hub set incomplete for `?` attributes | None |
| V11 | Create discipline scheme index notes now or later | Open | 2026-11-17 | Scale question | None |
| V12 | Is "congruence" a plain enough name | Open | 2026-11-17 | Reads legal | None |
| V13 | Meta-Category V crosswalk: review targets, decide VB-0, load AIRO/DPV, run Meta-Category II | Task | 2026-11-17 | Tests the migration method on a real category | Blocked by K6, K7, S3, K5 (named as blocked rows in crosswalk) |

## 4. Assessment-everywhere (variant B) and tests

| ID | Item | Type | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|
| A1 | Adopt variant B (attributes move into assessments) | Decision | Under test | 2026-11-18 | Assertions about Factors and Effects hide disputes; a fact becomes a settled status | Blocks S36, final Assessment shape. Blocked by A2, A4, A5 |
| A2 | Non-expert subagent test | Task | First pass, unscored | 2026-11-18 | Checks whether a reader is misled by the snapshot (silent omission) | Blocks A1. Blocked by T-decision on fixed snapshot |
| A3 | SHACL validation of assessment-everywhere snapshot | Task | Not run | 2026-11-18 | Nodes without an assessment; shortcuts without status | Blocks D3 |
| A4 | Strict settlement rule (2+ independent, same procedure, evidence) | Open | Open | 2026-11-18 | Prevents false consensus | Blocks A1. Blocked by A5 |
| A5 | Horizon test R01 | Task | Needs sourced research | 2026-11-18 | Horizon as part of the claim key, tested on real cases | Blocks A4, H5 |
| A6 | CQ8 "directly affected": core `affects` or `affectedStanding = Direct` | Open | Awaiting author | 2026-11-18 | Wording gap in test | Blocks scoring confirmation |
| A7 | `affectedStanding` as exclusive | Decision | Test choice | 2026-11-18 | Simplifies toy test | Blocked by A5 |
| A8 | `occurredDuring` as interval | Proposal | Untested | 2026-11-18 | Effects happen over periods | Blocked by A2 (inferred) |
| A9 | AffectedEntity subtypes: NonSentientSystem vs NaturalSystem/EngineeredSystem; Household; CollectiveNaturalGroup; CollectiveArtificialPerson; Unclassified; type as assessment | Decision | Untested | 2026-11-18 | Standing for communities, systems and future generations | Blocked by A1, S2 |
| A10 | Re-read author decisions 5–21 | Task | Not done | 2026-11-18 | Acceptance of recommendations in one sitting; risk of momentum | Blocks A1 |

## 5. Causal assessment (HO-003, HO-005, HO-I.a)

| ID | Item | Type | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|
| K1 | Split Assessment into Causal, Valence, Responsibility | Decision | Pending | 2026-11-15 | Harm, fault and cause are currently mixed; answerability read from cause (CQ9 silent) | Blocks CQ9, S35 |
| K2 | Causal standards: but-for, NESS, INUS, probability-raising | Proposal | Pending | 2026-11-15 | Law and philosophy give different causal answers | Blocks T28, T29 tests |
| K3 | Reify `participatesIn` as a claim | Decision | Pending | 2026-11-15 | Participation is asserted by someone | Blocked by S2 |
| K4 | "Sufficient as assessed" (revises HO-003 "jointly sufficient") | Decision | Pending | 2026-11-15 | "Jointly sufficient" assumes a fact about members | Blocked by K1 tests |
| K5 | Evidence anchor against the regress | Open | Open | 2026-11-15 | Assessments of evidence need evidence | Blocks A4, V13 |
| K6 | Condition split (state, status, disposition) | Open | Open | 2026-11-15 | Condition is ambiguous | Blocks V13 |
| K7 | Role types complete; causal share measurable | Open | Open | 2026-11-15 | Role list may be incomplete | Blocks V13 |
| K8 | Does a structure cause harm, or only set the scene? | Open | Open | 2026-11-14 | Structures as causes | None recorded |

## 6. Chain (HO-006, v4)

| ID | Item | Type | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|
| H1 | Chain class (thin container, bounded by horizon) | Proposal | Seed | Undated | `CausalRole` refers to a chain that has no object | Target v4. Blocked by H2–H3, A5 |
| H2 | Horizon measured from factor, effect or `assessedAt`; cuts by time, links or probability | Open | Open | Undated | Net effects need a bound | Blocks H1 |
| H3 | Where `maxHorizon` lives and who may override | Open | Open | Undated | Horizon is part of the claim key | Blocks H1 |
| H4 | Chain-level net assessment | Open | Open | Undated | Net results across a chain (HO-I.b) | Blocks H1 |
| H5 | Status calculation change beyond horizon in the key | Open | Open | Undated | Chain may change status rules | Blocked by A5 |
| H6 | Chain under `CausalCandidate` with FactorAssembly | Open | Open | Undated | Convergent causes | Blocked by H1 |

## 7. Other HO notes: open questions

| ID | Note | Open item | Why it matters | Blocks / Blocked by |
|---|---|---|---|---|
| O1 | HO-001 | How is dispositional harm measured; is consent a defence | Measuring habituation | None recorded |
| O2 | HO-001 | Assent/judgment as object of harm | Captured assent | Blocks S-group (inferred) |
| O3 | HO-002 | Who runs the tests (self-evaluation) | Designer testing own model | Blocks test credibility |
| O4 | HO-002 | One note per test case; a case for each verdict value | Coverage | None |
| O5 | HO-II.a | Worldviews as standards | Afterlife and ancestor traditions | Blocks Standard family |
| O6 | HO-II.a | Classical Council ideas as standards | Harm to wrongdoer, manufactured desire | None |
| O7 | HO-II.b | Block "who knows?" by requiring confidence on extrapolated links | Sai Weng trap | Blocked by A5 (inferred) |
| O8 | HO-II.c | Who encodes the ratio; TransUnion test case | Judgment profile | None |
| O9 | HO-II.d | Does `fitness` belong to the perspective or the standard-intent pair | Purpose attributes | None |
| O10 | HO-II.d.3 | Keying of schemes; where hub narrative lives | Vocabulary | Blocked by V2 |
| O11 | HO-II.e | Mandatory SHACL core properties | Minimum data | Blocks S36 |
| O12 | HO-III.a | Can coverage be measured; is "Contested" redundant | Verdict set | None |
| O13 | HO-III.b | Versions and licences (SNOMED CT); BFO alignment looseness | Reuse | Blocked by T1 (licence) |
| O14 | HO-premise | Is "Contested" a verdict or a sign of Divergence; does rights-based standard break the premise | Core premise | Blocks O12 |
| O15 | HO-I.c | Posthumous harm as value or Divergence | Phenomenality | None |
| O16 | HO-I.b | Net results across a chain | Cascades | Blocked by H4 |
| O17 | HO-premise | Not logged: "sufficient as assessed" (see K4) | | |

## 8. Tasks, decisions and governance

| ID | Item | Type | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|
| T1 | DOLCE+DnS Ultralite licence | Task | Open, sources conflict | 2026-11-21 | Candidate upper ontology; licence unclear, so no copy or import | Blocks any DUL subclass mapping, O13. Blocked by written reply from ODP maintainers |
| T2 | Sen/Nussbaum capability approach | Task | Open | 2026-11-16 | Functionings and capabilities need a home | Blocks Phase 3 (HIGH). Blocked by S-group decisions (inferred) |
| T3 | Map v3 to AIRO, VAIR, DPV-RISK | Task | Open | 2026-11-16 | Reuse IRIs; avoid rival definitions | Blocks Phase 2 crosswalk. Blocked by check of negative valence |
| T4 | Searchlight narrative pilot (CP-02) | Task | Not started | 2026-11-21 | Can prompts generate questions, blind spots and findings | Blocks Phase 3–4 content. Blocked by choosing one PerspectiveType |
| T5 | Methodology rules 1–7 (referenced note missing from vault) | Task | Proposed | 2026-11-20 | Sample inconsistencies need a rule set | Blocks V1, V4, V5 |
| T6 | Migration Phase 0: open `# Master Formal Ontology of Harm` | Task | Not started | 2026-11-15 | Remaining source content | Blocks Phase 2 |
| T7 | Archive decision for root files (Compendium, v1 `.ttl`) | Decision | Awaiting author | 2026-11-18 | Old files untouched | Blocked by author |
| T8 | Delete `~/harm-ontology-scripts/` duplicate | Task | Waiting | 2026-11-18 | One copy only | Blocked by trust in vault copy |
| T9 | Bookmark placements: HO-II.d.3, HO-II.d.4, HO-007 | Decision | Awaiting author | 2026-11-20 | Index should match notes | Blocks S8–S20 logging (inferred) |
| T10 | Bookmark shape for HO-007; add HO-002 tests now; wording of "participation" | Decision | Awaiting author | 2026-11-19 | Open choices before a page is written | Blocks S2, S3 |
| T11 | Build inclusion rules: include pending and proposed elements (flagged)? | Decision | Awaiting author | 2026-11-18 | Decides what enters the schema | Blocks D1 build |
| T12 | Test-only machinery: omit or separate module | Decision | Awaiting author | 2026-11-18 | Procedure, Evidence, Band etc. are test-only | Blocks D1 build |
| T13 | Namespace IRI and `owl:versionIRI` | Decision | Open | 2026-11-18 | Plan requires a versioned namespace; test IRI must not be reused | Blocks D1 build |
| T14 | Declare `airo:`, `dpv:`, `vair:` prefixes now | Decision | Awaiting author | 2026-11-18 | Avoids later churn | None |
| T15 | Build method: hand-written Turtle or script | Decision | Awaiting author | 2026-11-18 | v4 will change the table | Blocks D1 build |
| T16 | Transcript sweep for explanations not in notes | Decision | Awaiting author | 2026-11-18 | Explanations may be lost | Not in first release |
| T17 | Log "schema" layer name (S7) | Decision | Not logged | 2026-11-18 | Record in Decisions Log | Blocks nothing |
| T18 | Decision: whether test-only decisions and pending items are logged | Decision | Standing rule | 2026-11-18 | Log only after testing | None |

---

## Dependency summary

The items that block the most others:
- **S24 and S25** (coverage and overlap tests) block S8–S20.
- **S28** (placement test) blocks S26 and S27.
- **A2 and A5** (non-expert and Horizon tests) block A1, which is the main structural choice.
- **S4, S5, S6, T11–T13, T15** (narrative placement, schema domains and ranges, build rules) block the first `.ttl`.
- **K1** (Valence/Responsibility split) blocks CQ9, S35 and several causal tests.
- **T2** (capability approach) blocks Phase 3.

Several items are not blocked by anything. These are ready to decide now: S7, S11, T14, T17, T18.

---

## Before I write this into the ledger

1. Should I use the Blocks / Blocked by fields as shown, or add them as table columns in the ledger?
2. Leave undated items undated, as now?
3. Do the (inferred) dependencies look right? I can mark them as confirmed only after you check them.

I'll wait for your confirmation. After that I'll write the ledger, then the session note and the handoff update, with the assessment finalisation steps set out in the handoff.
[Timestamp: 2026/11/22 23:08:02]

**user**: not yet.  you seem to have left out source now.  can you preserve what you have and add source back in as a link (column next to the "item" and make that source a clickable link to the actual source location
[Timestamp: 2026/11/22 23:16:54]

**ai**: Here is the same ledger with a **Source** column beside each item. Each source links to the note and, where I read it, the section heading. Items from the 2026-11-22 session have no note yet, so they are marked as session sources.

---

## 1. Schema and structure

| ID | Item | Source | Type | Status | Date | Pri | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|---|---|
| S1 | Discipline-enabled assessments and functional subclasses (CP-01) | Session 2026-11-22 (no note yet) | Proposal | Draft | 2026-11-22 | H | Perspectives should enable assessments, not just tag them. Assessments serve different purposes (regulatory, forensic, diagnostic, normative) | Blocked by S21, S26. Interacts with K1 |
| S2 | Agents, Event, participation, assessing organisations (HO-007) | [[Handoff - Harm Ontology#Open issues and to-dos added 2026-11-19]] | Decision | Draft | 2026-11-19 | H | Robbery case (robbers take part in an event that is part of an assembly); lion, storm and audit-firm cases raised by the author | Blocks S3, K3, A9. Blocked by T10 |
| S3 | What counts as an agent; `Agent (?)` scope, incl. AI systems | [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)#Structure]] (Agent (?) line) | Open | Open | 2026-11-15 | M | Lion, flood water and AI system cases; the draft marks Agent "(?)" | Blocked by S2 |
| S4 | Narrative placement: on the property or the concept | [[Harm Ontology v3 Provisional Release Brief#Decisions needed from the author before building]] (item 6) | Open | Reopened | 2026-11-18 | H | Mini example judged "awful" in Protégé; sample placements differ | Blocks D1 build, S5 |
| S5 | Domains, ranges and property groups for every class; data-entry route | [[Handoff - Harm Ontology#Open issues and to-dos added 2026-11-19]] | Task | Open | 2026-11-19 | H | Instances show no fields to fill in; OWL attaches properties to classes poorly | Blocks D1 build. Blocked by S4, S6 |
| S6 | How the 12 display groups are represented | [[Handoff - Harm Ontology#Open issues and to-dos added 2026-11-19]] (Property groups) | Open | Open | 2026-11-18 | H | Author: "this subgrouping was essential to understanding"; 0.02 says display facets, not classes | Blocks S5 (groups) |
| S7 | Layer-1 name "schema" (replaces "ontology") | [[Handoff - Harm Ontology#Open issues and to-dos added 2026-11-19]] (Layer-1 name) | Decision | Adopted, unlogged | 2026-11-18 | L | Naming clarity; author's choice | Blocks logging only |
| S8 | Rename `nameByDomain` / `definitionByDomain` to `…ByDiscipline` | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Structural and naming changes pending (not decided)]] | Decision | Draft | 2026-11-21 | M | "Domain" is overloaded with rdfs:domain | Blocked by T9, S24, S25 |
| S9 | `fieldOfApplication` gets a target class, not free text | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Structural and naming changes pending (not decided)]] | Decision | Draft | 2026-11-21 | M | Free text cannot be queried; 0.02 group 5 | Blocks S16. Blocked by S25 |
| S10 | `observabilityLimit` (0.01) has no 0.02 match | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Structural and naming changes pending (not decided)]] (item 6) | Open | Open | 2026-11-21 | L | Attribute dropped between versions; not recorded why | Blocked by Box A decision |
| S11 | Group numbering: "twelve groups" but numbered 0–12 | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Structural and naming changes pending (not decided)]] (item 7) | Open | Open | 2026-11-21 | L | Inconsistent count | Blocks S6 ordering |
| S12 | `CorePrinciples`: class or single individual? | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Class or concept: how elements are typed (proposed rule, open)]] (Open 1) | Open | Open | 2026-11-21 | H | Generative rules that produce verdicts (physics example) | Blocks S13. Blocked by S24 |
| S13 | Attachment for core principles | [[Decisions_Log]] (2026-11-21 entry on foundationalCommitments) | Open | Open | 2026-11-21 | H | Foundational commitments (identity) and core principles (generative) are different relations | Blocked by S12, S14. Separate conversation planned |
| S14 | `foundationalCommitments` needs a range | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#0.02 groups that overlap the proposals (for the coverage test)]] | Open | Open | 2026-11-21 | M | Logged property has no range | Blocks S13 |
| S15 | `heldBy` → Discipline or CollectiveAgent | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Skeleton schema (proposed additions to v3)]] | Open | Open | 2026-11-21 | M | Who holds a perspective; overlaps `bearerRole`, `lineage` | Blocked by S22, S25 |
| S16 | `usedBy` vs `practisedIn`: one relation or two | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Open questions]] | Open | Open | 2026-11-21 | M | Separate settings from agents that use a perspective | Blocked by S9 |
| S17 | `informedBy` → Theory, with assessed status | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Skeleton schema (proposed additions to v3)]] | Proposal | Draft | 2026-11-21 | M | Traditions draw on theories with differing support; status may be an assessment | Blocked by S25; open whether status is an Assessment |
| S18 | New classes: Discipline, Theory, ConceptualTerritory, FieldOfApplication | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Skeleton schema (proposed additions to v3)]] | Proposal | Draft | 2026-11-21 | M | "Physics" has at least five senses; each needs its own class | Blocked by S20, S25 |
| S19 | `hasVocabulary`, `anchoredIn`, `statedPurpose` / `use → Purpose` | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Skeleton schema (proposed additions to v3)]] | Proposal | Draft | 2026-11-21 | L | Traditions keyed to disciplines; uses need a purpose node | Blocked by S21, S22 |
| S20 | Element-typing rule for elements that are both participant and term | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Class or concept: how elements are typed (proposed rule, open)]] (Open 3) | Open | Working rule | 2026-11-21 | M | Overloaded words (ConceptualTerritory) | Blocks S18 (inferred) |
| S21 | Is a discipline's perspective the same kind as a tradition's? | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Open questions]] | Open | Working answer: yes | 2026-11-21 | H | CP-01 depends on DisciplinePerspective being a PerspectiveType | Blocks S1 |
| S22 | Do disciplines or communities of practitioners hold perspectives? | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Open questions]] | Open | Open | 2026-11-21 | M | Decides `heldBy` | Blocks S15 |
| S23 | Can one specification combine more than one tradition (mixed lenses)? | [[PerspectiveStructure Proposal Draft 3.1]] (open questions) | Open | Open | 2026-11-20 | L | Real assessments may draw on several lenses | Blocks nothing recorded |
| S24 | Physics and Integral coverage test | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Coverage test: physicsPerspective and integralPerspective (proposed, structure only)]] | Task | Not run | 2026-11-21 | H | Test 0.02 structure against two different perspectives before logging | Blocks logging of S8–S20. Awaiting author go-ahead |
| S25 | Overlap test (0.02 table) and naming test in Protégé | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Test plan before any logging]] | Task | Not run | 2026-11-21 | H | Check each new name against neighbours and methodology rules | Blocks logging of S8–S20 |
| S26 | Gap schema attachment: PerspectiveType, procedural layer or HarmAssessment | [[Handoff - Harm Ontology#Searchlight, gap identification and method (2026-11-21; proposed, nothing logged)]] | Decision | Provisional | 2026-11-21 | H | Gap groups (mandate, valuation, lifecycle, remedy) describe assessment acts, not traditions | Blocks S27, S1 subclass placement. Blocked by S28 |
| S27 | Four gap attribute groups | [[Harm Ontology v3 Harm Assessment Schema Extensions (Proposed)]] | Proposal | Draft | 2026-11-21 | M | Real institutions (e.g. EIA) need mandate, metric, trigger and remedy, which HO lacks | Blocked by S26, S28 |
| S28 | Placement test for new elements | [[2026-11-21 Harm Ontology Searchlight and Gap Session]] (placement test) | Decision | Proposed method | 2026-11-21 | H | Stops elements landing in the wrong class; applies to all future proposals | Blocks S26, S27 |
| S29 | Which of the 20 searchlight questions become attributes | [[2026-11-21 Harm Ontology Searchlight and Gap Session#Open questions carried forward]] | Open | Open | 2026-11-21 | M | Some questions may be better as narrative | Blocked by T4 |
| S30 | Statement-level provenance (RDF-star or named graphs) | [[PerspectiveStructure 0.01#Open questions]] | Open | Open | 2026-11-17 | M | Claims need their own source | None recorded |
| S31 | Attribute-space model for comparing traditions | [[PerspectiveStructure Proposal Draft 3.1]] (open questions) | Open | Open | 2026-11-17 | L | Physics council: frames as points in attribute space | None recorded |
| S32 | Ontology as an instance of its own PerspectiveType | [[PerspectiveStructure Proposal Draft 3.1]] (open questions) | Open | Open | 2026-11-17 | L | Model should state its own lens | None recorded |
| S33 | Two-level split: PerspectiveType vs Perspective | [[PerspectiveStructure 0.01#Open questions]] | Open | Probably absorbed | 2026-11-15 | M | 0.01 proposal; Perspective umbrella adopted 2026-11-17 | Needs status check |
| S34 | Keep `developmentalAltitude`, given it is contested | [[PerspectiveStructure 0.01#Open questions]] | Open | Open | 2026-11-15 | M | Integral concept with contested support | Blocked by V7 |
| S35 | Does CausalAssessment need its own profile? | [[HO-005 Assessed Membership and Systematic Omission#Open questions]] | Open | Open | 2026-11-17 | M | Causal judgments may need different required fields | Blocked by K1 |
| S36 | Mandatory SHACL properties for every Assessment | [[HO-II.e Missingness Statuses and Domain Profiles#Open questions]] | Open | Open | 2026-11-14 | M | Missing means "not considered", so a minimum set is needed | Blocks D3 validation. Blocked by A1 |

## 2. Council proposals (PerspectiveStructure 0.01 reviews)

| ID | Item | Source | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|
| C1 | Classical: Stance group; treat groups as display facets only | [[v-0.01 ClassicalCouncil Review of - PerspectiveStructure 0.01#Open questions]] | Open | 2026-11-17 | Character and orientation not captured; facets vs classes | Blocked by S6 |
| C2 | Ethics: Normative core group; `moralCircle` as third scope axis | [[v-0.01 EthicsCouncil Review of - PerspectiveStructure 0.01#Open questions]] | Open | 2026-11-17 | Normative commitments not separated from identity | Blocked by S6 |
| C3 | Legal: Institutional group; description/evaluation split; `validFrom`/`validTo` | [[v-0.01 LegalCouncil Review of - PerspectiveStructure 0.01#Open questions]] | Open | 2026-11-17 | Law separates describing a rule from evaluating it; versioning needed | Blocks S6. Overlaps S33 |
| C4 | Logic: minimal core plus pragmatic test; corroboration in place of `verificationStatus` for lenses | [[v-0.01 LogicCouncil Review of - PerspectiveStructure 0.01#Open questions]] | Open | 2026-11-17 | Popper/Mayo: "verified" overstates what is known about a lens | Blocked by S30 (inferred) |
| C5 | Physics: dynamics group; invariants as test for perspectival vs factual divergence | [[v-0.01 PhysicsCouncil Review of - PerspectiveStructure 0.01#Open questions]] | Open | 2026-11-17 | Feedback and invariance give a test for divergence | Blocked by S31 |
| C6 | Sci-Fi: Subject's side group; Power and Infrastructure facets | [[v-0.01 SciFiCouncil Review of - PerspectiveStructure 0.01#Open questions]] | Open | 2026-11-17 | Subject perspective and power were missing | Blocked by S6 |
| C7 | Sci-Fi: `acceptedHarm` as sibling of `blindSpot` | [[v-0.01 SciFiCouncil Review of - PerspectiveStructure 0.01#Open questions]] | Partly absorbed | 2026-11-17 | Accepted harm differs from a blind spot | Absorbed in omission categories (2026-11-17); confirm |
| C8 | Cognitive: AI systems as recordable PerspectiveTypes | [[v-0.01 CognitiveCouncil Review of - PerspectiveStructure 0.01#Open questions]] | Open | 2026-11-17 | AI systems carry trained-in lenses | Blocks V13 (inferred) |
| C9 | Cognitive: "verdict convergence, rationale divergence" as Divergence subtype | [[v-0.01 CognitiveCouncil Review of - PerspectiveStructure 0.01#Open questions]] | Open | 2026-11-17 | Agreement on verdict can hide different reasons | Blocks HO-III.a subtypes |
| C10 | Cognitive: `explorationMode` (explore vs exploit) | [[v-0.01 CognitiveCouncil Review of - PerspectiveStructure 0.01]] (Gopnik section) | Open | 2026-11-17 | Explorers find new harms | None recorded |

## 3. Vocabulary and crosswalk (layer 3)

| ID | Item | Source | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|
| V1 | Rename `hov:hubs`, or make each hub its own scheme | [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes#Open questions]] | Open | 2026-11-20 | Plural name reads like a concept | Blocked by T5 |
| V2 | Integral scheme keyed to discipline or tradition | [[2026-11-20 Harm Ontology Sample Review and Methodology#Open questions]] | Open | 2026-11-20 | Integral is one author's tradition, closer to a PerspectiveType | Blocks V3, V9 |
| V3 | Scheme for `psy:moralStages` | [[2026-11-20 Harm Ontology Sample Review and Methodology#Open questions]] | Open | 2026-11-20 | Placement unchecked | Blocked by V2 |
| V4 | Where hub narrative lives | [[2026-11-20 Harm Ontology Sample Review and Methodology#Open questions]] | Open | 2026-11-20 | Samples differ | Blocked by T5 |
| V5 | Two `developmentalAltitude` elements plus untyped `rdf:Description` | [[Handoff - Harm Ontology#Searchlight, gap identification and method (2026-11-21; proposed, nothing logged)]] (sample review findings) | Defect | 2026-11-20 | Sample error found in review | Blocked by T5 |
| V6 | Congruence and blind-spot grades review | [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes#Open questions]] | Partly done | 2026-11-17 | Mapping grades need checking; Kant changed to closeMatch | None |
| V7 | Developmental altitude: verify 12-colour sequence, Gilligan wording, Hierocles | [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes#Open questions]] | Open | 2026-11-17 | Citations unverified | Blocks V8, S34 |
| V8 | Is the third tier kosmocentric? | [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes#Open questions]] | Open | 2026-11-17 | Source does not say | Blocked by V7 |
| V9 | AQAL interior/exterior hubs | [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes#Open questions]] | Proposal | 2026-11-17 | Vocabulary coverage | Blocked by V2 |
| V10 | Next hubs: accountability locus, consent to be seen | [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes#Open questions]] | Proposal | 2026-11-17 | Hub set incomplete for `?` attributes | None |
| V11 | Create discipline scheme index notes now or later | [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes#Open questions]] | Open | 2026-11-17 | Scale question | None |
| V12 | Is "congruence" a plain enough name | [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes#Open questions]] | Open | 2026-11-17 | Reads legal | None |
| V13 | Meta-Category V crosswalk: review targets, decide VB-0, load AIRO/DPV, run Meta-Category II | [[Harm Ontology Crosswalk - Pilot Meta-Category V]] (next steps) | Task | 2026-11-17 | Tests the migration method on a real category | Blocked by K6, K7, S3, K5 (named as blocked rows in crosswalk) |

## 4. Assessment-everywhere (variant B) and tests

| ID | Item | Source | Type | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|---|
| A1 | Adopt variant B (attributes move into assessments) | [[HO-002.a Assessment-Everywhere Test Strategy]] | Decision | Under test | 2026-11-18 | Assertions about Factors and Effects hide disputes; a fact becomes a settled status | Blocks S36, final Assessment shape. Blocked by A2, A4, A5 |
| A2 | Non-expert subagent test | [[Handoff - Harm Ontology#Next step]] (item 1) | Task | First pass, unscored | 2026-11-18 | Checks whether a reader is misled by the snapshot (silent omission) | Blocks A1. Blocked by T-decision on fixed snapshot |
| A3 | SHACL validation of assessment-everywhere snapshot | [[Handoff - Harm Ontology#Next step]] (item 2) | Task | Not run | 2026-11-18 | Nodes without an assessment; shortcuts without status | Blocks D3 |
| A4 | Strict settlement rule (2+ independent, same procedure, evidence) | [[Handoff - Harm Ontology#Cautions]] | Open | Open | 2026-11-18 | Prevents false consensus | Blocks A1. Blocked by A5 |
| A5 | Horizon test R01 | [[Handoff - Harm Ontology#Next step]] (item 4) | Task | Needs sourced research | 2026-11-18 | Horizon as part of the claim key, tested on real cases | Blocks A4, H5 |
| A6 | CQ8 "directly affected": core `affects` or `affectedStanding = Direct` | [[Harm Ontology v3 Test Summary#Open question for the author]] | Open | Awaiting author | 2026-11-18 | Wording gap in test | Blocks scoring confirmation |
| A7 | `affectedStanding` as exclusive | [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)#Toy-case test of variant B, 2026-11-18 (test only; nothing decided)]] | Decision | Test choice | 2026-11-18 | Simplifies toy test | Blocked by A5 |
| A8 | `occurredDuring` as interval | [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)#Structure]] (Effect props) | Proposal | Untested | 2026-11-18 | Effects happen over periods | Blocked by A2 (inferred) |
| A9 | AffectedEntity subtypes: NonSentientSystem vs NaturalSystem/EngineeredSystem; Household; CollectiveNaturalGroup; CollectiveArtificialPerson; Unclassified; type as assessment | [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)#Structure]] (AffectedEntity block) | Decision | Untested | 2026-11-18 | Standing for communities, systems and future generations | Blocked by A1, S2 |
| A10 | Re-read author decisions 5–21 | [[Handoff - Harm Ontology#Cautions]] | Task | Not done | 2026-11-18 | Acceptance of recommendations in one sitting; risk of momentum | Blocks A1 |

## 5. Causal assessment (HO-003, HO-005, HO-I.a)

| ID | Item | Source | Type | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|---|
| K1 | Split Assessment into Causal, Valence, Responsibility | [[HO-005 Assessed Membership and Systematic Omission#Open questions]] | Decision | Pending | 2026-11-15 | Harm, fault and cause are currently mixed; answerability read from cause (CQ9 silent) | Blocks CQ9, S35 |
| K2 | Causal standards: but-for, NESS, INUS, probability-raising | [[Handoff - Harm Ontology#Pending (proposed, not decided; see HO-005 Assessed Membership and Systematic Omission)]] | Proposal | Pending | 2026-11-15 | Law and philosophy give different causal answers | Blocks T28, T29 tests |
| K3 | Reify `participatesIn` as a claim | [[HO-005 Assessed Membership and Systematic Omission]] (pending list) | Decision | Pending | 2026-11-15 | Participation is asserted by someone | Blocked by S2 |
| K4 | "Sufficient as assessed" (revises HO-003 "jointly sufficient") | [[HO-003 Causal Assembly - the Perfect Storm#Open questions]] | Decision | Pending | 2026-11-15 | "Jointly sufficient" assumes a fact about members | Blocked by K1 tests |
| K5 | Evidence anchor against the regress | [[HO-005 Assessed Membership and Systematic Omission#Open questions]] | Open | Open | 2026-11-15 | Assessments of evidence need evidence | Blocks A4, V13 |
| K6 | Condition split (state, status, disposition) | [[HO-I.a Factor and CausalRole#Open questions]] | Open | Open | 2026-11-15 | Condition is ambiguous | Blocks V13 |
| K7 | Role types complete; causal share measurable | [[HO-I.a Factor and CausalRole#Open questions]] | Open | Open | 2026-11-15 | Role list may be incomplete | Blocks V13 |
| K8 | Does a structure cause harm, or only set the scene? | [[HO-I.a Factor and CausalRole#Open questions]] | Open | Open | 2026-11-14 | Structures as causes | None recorded |

## 6. Chain (HO-006, v4)

| ID | Item | Source | Type | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|---|
| H1 | Chain class (thin container, bounded by horizon) | [[HO-006 Causal Chain - an Assessed Selection with a Horizon]] | Proposal | Seed | Undated | `CausalRole` refers to a chain that has no object | Target v4. Blocked by H2–H3, A5 |
| H2 | Horizon measured from factor, effect or `assessedAt`; cuts by time, links or probability | [[HO-006 Causal Chain - an Assessed Selection with a Horizon#Open questions]] | Open | Open | Undated | Net effects need a bound | Blocks H1 |
| H3 | Where `maxHorizon` lives and who may override | [[HO-006 Causal Chain - an Assessed Selection with a Horizon#Open questions]] | Open | Open | Undated | Horizon is part of the claim key | Blocks H1 |
| H4 | Chain-level net assessment | [[HO-006 Causal Chain - an Assessed Selection with a Horizon#Open questions]] | Open | Open | Undated | Net results across a chain (HO-I.b) | Blocks H1 |
| H5 | Status calculation change beyond horizon in the key | [[HO-006 Causal Chain - an Assessed Selection with a Horizon#Open questions]] | Open | Open | Undated | Chain may change status rules | Blocked by A5 |
| H6 | Chain under `CausalCandidate` with FactorAssembly | [[HO-006 Causal Chain - an Assessed Selection with a Horizon#Open questions]] | Open | Open | Undated | Convergent causes | Blocked by H1 |

## 7. Other HO notes: open questions

| ID | Item | Source | Why it matters | Blocks / Blocked by |
|---|---|---|---|---|
| O1 | How is dispositional harm measured; is consent a defence | [[HO-001 Harm by Habituation and Captured Assent#Open questions]] | Measuring habituation | None recorded |
| O2 | Assent/judgment as object of harm | [[HO-001 Harm by Habituation and Captured Assent]] (candidate object of harm) | Captured assent | Blocks S-group (inferred) |
| O3 | Who runs the tests (self-evaluation) | [[HO-002 Ontology Stress-Test Suite#Open questions]] | Designer testing own model | Blocks test credibility |
| O4 | One note per test case; a case for each verdict value | [[HO-002 Ontology Stress-Test Suite#Open questions]] | Coverage | None |
| O5 | Worldviews as standards | [[HO-II.a Assessment and Evaluative Standard#Open questions]] | Afterlife and ancestor traditions | Blocks Standard family |
| O6 | Classical Council ideas as standards | [[HO-II.a Assessment and Evaluative Standard#Open questions]] | Harm to wrongdoer, manufactured desire | None |
| O7 | Block "who knows?" by requiring confidence on extrapolated links | [[HO-II.b Assessment Horizon - the Sai Weng Trap#Open questions]] | Sai Weng trap | Blocked by A5 (inferred) |
| O8 | Who encodes the ratio; TransUnion test case | [[HO-II.c Judgment as Assessment - Reasoning over Precedent#Open questions]] | Judgment profile | None |
| O9 | Does `fitness` belong to the perspective or the standard-intent pair | [[HO-II.d Perspective - Ten Optional Properties#Open questions]] | Purpose attributes | None |
| O10 | Keying of schemes; where hub narrative lives | [[HO-II.d.3 Hub and Spoke Pattern#Open questions]] | Vocabulary | Blocked by V2 |
| O11 | Mandatory SHACL core properties | [[HO-II.e Missingness Statuses and Domain Profiles#Open questions]] | Minimum data | Blocks S36 |
| O12 | Can coverage be measured; is "Contested" redundant | [[HO-III.a Divergence and Integration - True but Partial#Open questions]] | Verdict set | None |
| O13 | Versions and licences (SNOMED CT); BFO alignment looseness | [[HO-III.b Reusing Expert Domain Vocabularies#Open questions]] | Reuse | Blocked by T1 (licence) |
| O14 | Is "Contested" a verdict or a sign of Divergence; does rights-based standard break the premise | [[HO-premise No Intrinsic Harmfulness#Open questions]] | Core premise | Blocks O12 |
| O15 | Posthumous harm as value or Divergence | [[HO-I.c Phenomenality - Observability and Experienceability#Open questions]] | Phenomenality | None |
| O16 | Net results across a chain | [[HO-I.b Effect and Cascades#Open questions]] | Cascades | Blocked by H4 |

## 8. Tasks, decisions and governance

| ID | Item | Source | Type | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|---|
| T1 | DOLCE+DnS Ultralite licence | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Top priority: licence check (before any alignment work)]] | Task | Open, sources conflict | 2026-11-21 | Candidate upper ontology; licence unclear, so no copy or import | Blocks any DUL subclass mapping, O13. Blocked by written reply from ODP maintainers |
| T2 | Sen/Nussbaum capability approach | [[Harm Ontology Migration Plan#Open to-dos]] | Task | Open | 2026-11-16 | Functionings and capabilities need a home | Blocks Phase 3 (HIGH). Blocked by S-group decisions (inferred) |
| T3 | Map v3 to AIRO, VAIR, DPV-RISK | [[Harm Ontology Migration Plan#Open to-dos]] | Task | Open | 2026-11-16 | Reuse IRIs; avoid rival definitions | Blocks Phase 2 crosswalk. Blocked by check of negative valence |
| T4 | Searchlight narrative pilot (CP-02) | [[Perspective Narrative Generation - Searchlight Task]] | Task | Not started | 2026-11-21 | Can prompts generate questions, blind spots and findings | Blocks Phase 3–4 content. Blocked by choosing one PerspectiveType |
| T5 | Methodology rules 1–7 (referenced note missing from vault) | [[2026-11-20 Harm Ontology Sample Review and Methodology#Methodology rules]] | Task | Proposed | 2026-11-20 | Sample inconsistencies need a rule set | Blocks V1, V4, V5 |
| T6 | Migration Phase 0: open `# Master Formal Ontology of Harm` | [[Harm Ontology Migration Plan#Phases]] (Phase 0) | Task | Not started | 2026-11-15 | Remaining source content | Blocks Phase 2 |
| T7 | Archive decision for root files (Compendium, v1 `.ttl`) | [[Canon_and_Continuity#Open continuity questions]] | Decision | Awaiting author | 2026-11-18 | Old files untouched | Blocked by author |
| T8 | Delete `~/harm-ontology-scripts/` duplicate | [[Decisions_Log]] (2026-11-18 scripts entry) | Task | Waiting | 2026-11-18 | One copy only | Blocked by trust in vault copy |
| T9 | Bookmark placements: HO-II.d.3, HO-II.d.4, HO-007 | [[2026-11-20 Harm Ontology Sample Review and Methodology]] (next steps) | Decision | Awaiting author | 2026-11-20 | Index should match notes | Blocks S8–S20 logging (inferred) |
| T10 | Bookmark shape for HO-007; add HO-002 tests now; wording of "participation" | [[Handoff - Harm Ontology#Open issues and to-dos added 2026-11-19]] | Decision | Awaiting author | 2026-11-19 | Open choices before a page is written | Blocks S2, S3 |
| T11 | Build inclusion rules: include pending and proposed elements (flagged)? | [[Harm Ontology v3 Provisional Release Brief#Decisions needed from the author before building]] | Decision | Awaiting author | 2026-11-18 | Decides what enters the schema | Blocks D1 build |
| T12 | Test-only machinery: omit or separate module | [[Harm Ontology v3 Provisional Release Brief#Decisions needed from the author before building]] | Decision | Awaiting author | 2026-11-18 | Procedure, Evidence, Band etc. are test-only | Blocks D1 build |
| T13 | Namespace IRI and `owl:versionIRI` | [[Harm Ontology v3 Provisional Release Brief#Decisions needed from the author before building]] | Decision | Open | 2026-11-18 | Plan requires a versioned namespace; test IRI must not be reused | Blocks D1 build |
| T14 | Declare `airo:`, `dpv:`, `vair:` prefixes now | [[Harm Ontology v3 Provisional Release Brief#Decisions needed from the author before building]] | Decision | Awaiting author | 2026-11-18 | Avoids later churn | None |
| T15 | Build method: hand-written Turtle or script | [[Harm Ontology v3 Provisional Release Brief#Decisions needed from the author before building]] | Decision | Awaiting author | 2026-11-18 | v4 will change the table | Blocks D1 build |
| T16 | Transcript sweep for explanations not in notes | [[Harm Ontology v3 Provisional Release Brief#Decisions needed from the author before building]] | Decision | Awaiting author | 2026-11-18 | Explanations may be lost | Not in first release |
| T17 | Log "schema" layer name (S7) | [[Handoff - Harm Ontology]] | Decision | Not logged | 2026-11-18 | Record in Decisions Log | Blocks nothing |
| T18 | Decision: whether test-only decisions and pending items are logged | [[Handoff - Harm Ontology#Cautions]] | Decision | Standing rule | 2026-11-18 | Log only after testing | None |

---

## Dependency summary

The items that block the most others:
- **S24 and S25** (coverage and overlap tests) block S8–S20.
- **S28** (placement test) blocks S26 and S27.
- **A2 and A5** (non-expert and Horizon tests) block A1, the main structural choice.
- **S4, S5, S6, T11–T13, T15** (narrative placement, schema domains and ranges, build rules) block the first `.ttl`.
- **K1** (Valence/Responsibility split) blocks CQ9, S35 and several causal tests.
- **T2** (capability approach) blocks Phase 3.

Several items are not blocked by anything and can be decided now: S7, S11, T14, T17, T18.

---

**Source notes:**
- Links point to the note, and to a heading where I read the section. Where a heading link is not exact, the item is in that note; search the note for the item name.
- S1 comes from the 2026-11-22 session and has no note yet. Once the session note exists, I'll link it there.
- Source links for entries whose section I did not open (for example some Migration Plan and Provisional Brief references) point to the note. I'll verify each anchor when I write the ledger.

I have not written anything to the vault. Do you want this layout in the ledger as shown? After you confirm, I'll write the ledger, then the session note and the handoff.
[Timestamp: 2026/11/22 23:16:54]