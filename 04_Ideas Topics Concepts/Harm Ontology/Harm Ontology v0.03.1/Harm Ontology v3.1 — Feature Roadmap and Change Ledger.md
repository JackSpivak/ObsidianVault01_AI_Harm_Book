---
fileClass: Roadmap
type: roadmap
status: developing
tags: [ontology/harm, roadmap]
aliases: [Harm Ontology v3.1 Roadmap, Schema Change Ledger, Feature Roadmap]
created: 2026-11-22
updated: 2026-11-22
---

# Harm Ontology v3.1 — Feature Roadmap and Change Ledger

*The staging ground for proposed schema additions, structural changes, open decisions, rationale, priority, target version, dependencies and blockers, before anything is written into the `.ttl` files. Named for v3.1 so the direction is visible. Items may target v4 or later. Content migration is tracked separately in [[Harm Ontology Migration Plan]].*

**Conventions**
- **Type:** `Proposal` (new feature or change) · `Decision` (proposed item that needs resolution) · `Open Issue` (problem to resolve first) · `Task` (work that blocks other items) · `Defect` (error found in an existing file).
- **Status:** `Seed Idea` · `Draft Proposal` · `Under Stress-Test` · `Settled` · `Complete` · `Rejected`. *Settled* means tested or not needing testing, and ready for implementation in its target version. *Complete* means implemented and logged in [[Decisions_Log]].
- **Date:** Date Proposed is the date the item was first recorded. Date Settled / Rejected is filled when it changes status. Undated items stay undated until someone can confirm a date.
- **Order:** active items newest first, oldest last. IDs follow the order items were collected, not their dates.
- **Blocks / Blocked by:** item IDs. "(inferred)" marks a dependency I worked out from the notes, not one a note states.
- **Complete and Rejected** items stay in this ledger, at the bottom, and are never deleted.

---

## Active Ledger

### 0. Determinations, bearers and wholes (session 2026-11-24 to 2026-11-25)

Source for every row: [[2026-11-24 Harm Ontology Common Schema and DUL Alignment Session]] unless a different source is given. Items marked Settled were logged in [[Decisions_Log]] on 2026-11-25; items marked Proposed, Draft, Open or Deferred were not.

| ID | Item | Source | Type | Status | Date | Pri | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|---|---|
| HD29 | SHACL check for dual typing: `hosh:ConceptIsIndividualShape` (targets `skos:Concept`, requires `rdf:type owl:NamedIndividual`) and `hosh:CausalModelValueShape` (checks values of `ho:causalModel`). Run with pyshacl. Recorded in [[Decisions_Log]] 2026-11-28 | [[Decisions_Log]] 2026-11-28 (dual typing); session 2026-11-28 | Task | Open | 2026-11-28 | M | The dual-typing rule is only enforced if a shape checks it. OWL reasoners do not report a missing declaration | Blocked by the profiles layer build. Relates to HD28 |
| HD28 | Vocabulary placement: strictly narrative (SKOS only), OWL classes and subclasses, or mixed (reasoning axes as classes, narrative in SKOS, facets linking them). Option C recommended in session; not decided | [[Design Decision - Vocabulary Placement - Narrative, OWL Classes or Mixed]]; session 2026-11-24 (00:26 to 00:37) | Decision | Pending (author has not chosen) | 2026-11-25 | H | Author: "dont they need to b things in order to reason about them?" and the reasoning-over-richness concern. Governs every harm-type term | Blocks HD18 final form, HD19 test, and the placement test (S28). Blocked by HD19 (inferred) |
| HD1 | Determination branch: every harm output is a HarmDetermination under one Determination root (also Capability, Harmfulness, Chain, Responsibility, Condition, Investigative, Exposure, Relevance, Consent, Remedy) | Session, 00:51 and 02:30 tree | Proposal | Draft | 2026-11-25 | H | Holds every verdict without making harm an ontic class; the surgeon case needs several determinations of one class | Blocks HD2, HD11, HD17. Blocked by HD21 (inferred) |
| HD2 | Determination subclasses split by the question answered, not the kind of harm (council categories stay in the vocabulary) | Session, 00:51 | Decision | Settled (principle); class list Draft | 2026-11-25 | H | Author: "this is helpful" in response to the rule | Blocked by HD1 |
| HD3 | Every HarmDetermination declares `hasBearer` (range Entity), `judgesState`, `atHorizon`, with `assessedBy`, `perspective`, `standard` | Session, 02:16 to 02:25 | Decision | Settled (declaration and Entity range); Situation and Event state rules Open | 2026-11-25 | H | Author wants harm easy to declare, not inferred from roles | Blocks HD4, HD9 |
| HD4 | Harm attaches to a time-indexed state of its bearer; the same bearer can carry several harms | Session, 02:16 | Proposal | Draft | 2026-11-25 | H | Keeps bearer identity separate from each harm | Blocked by HD3, HD21 |
| HD5 | FunctionalHarmDetermination is a subclass of HarmDetermination; functions are assigned by a perspective (FunctionDescription) | Session, 02:28 to 02:29; [[Decisions_Log]] 2026-11-25 | Decision | Settled (subclass) | 2026-11-25 | H | Impairment of function is a harm; cyber harm depends on it | Blocks HD6 |
| HD6 | Impairment subclasses for functional harm: availability, integrity, confidentiality (provisional; CIA convention from memory, not checked against a standard) | Session, 02:29 | Proposal | Draft (provisional) | 2026-11-25 | M | Cyber harm expressed as impaired function | Blocked by HD5; first cyber case not yet run |
| HD7 | Harm to an emergent whole must be capturable; wholes are bearers; harm can target capability, unity or persistence; members' states remain separate targets | Session, 02:18 to 02:24; [[Decisions_Log]] 2026-11-25 | Decision | Settled (requirement); structure Draft | 2026-11-25 | H | Author: "harm to an emergent whole is essential to be able to capture" | Blocks HD8 |
| HD8 | EmergentWhole class, constituted by members via `hasConstituent` (not `hasMember`); own qualities; `unitySource` and `unityLocus`; `unityState` (intact, degraded, broken) time-indexed; persistence condition in the definition | Session, 02:18 to 02:24 | Proposal | Draft | 2026-11-25 | H | Formation example: harm by breaking unity, not by casualties | Blocked by HD7, HD21, HD26 (hasConstituent unverified) |
| HD9 | Judged state for Situation and Event bearers: a Situation's satisfaction of its description; an Event's course or outcome. Such harms are often contested | Session, 02:25 | Open | Open | 2026-11-25 | M | Ecosystems, markets, negotiations and rescues can bear harm | Blocked by HD3; relates to HD27 |
| HD10 | Causal boundary and temporal horizon are declared, justified parameters of an assessment; no HorizonDetermination; divergence over boundary or horizon is recorded | Session, 00:51; [[Decisions_Log]] 2026-11-25 | Decision | Settled (acceptance inferred from "this is helpful"; author to confirm) | 2026-11-25 | H | Author asked whether the boundary and horizon are identifiable or open-ended | Relates to A5 (horizon test), H3 (maxHorizon) |
| HD11 | Trigger and predisposition are weights on a RelevanceDetermination, not separate classes | Session, 00:51 | Proposal | Draft | 2026-11-25 | M | Dinner-party and dealer cases; avoids class bloat | Blocked by HD1 |
| HD12 | Sentience and experienceability are properties of Objects, not subclasses | Session, 01:46 | Proposal | Draft | 2026-11-25 | M | Avoids doubling the tree for every combination | Relates to HO-I.c |
| HD13 | Act and event: an agentive act is `dul:Action` (agent and task required); a non-agentive change is `dul:Event` or `dul:Process`; an unknown agent stays an Event with a missingness status | Session, 01:25; tree rules | Proposal | Draft | 2026-11-25 | H | Agency is contested in cases such as AI, autonomous systems and corporations | Blocked by HD21 (for the State rule), S2 (inferred) |
| HD14 | Competency-question sufficiency: four checks (answerable, attributable, traceable to a stakeholder, testable on a case); coverage tested in both directions | Session, 00:55; [[Decisions_Log]] 2026-11-25 | Decision | Settled (method); matrix results Draft | 2026-11-25 | H | Author: "lets go ahead with the matrix you suggested" | Blocks HD19 |
| HD15 | Competency questions and coverage matrix live in [[Model Structure Test Note - Competency Questions and Coverage]] | Session, 00:59; [[Decisions_Log]] 2026-11-25 | Decision | Settled (location); contents Draft | 2026-11-25 | M | Author asked for a test note | Blocks HD14 runs |
| HD16 | Regulator is a role; RegulatoryInstitution is a class fixed by charter or statute; named bodies are instances; corporations are a class with instances; legal personhood is a determination | Session, 01:30 to 01:34; [[Decisions_Log]] 2026-11-25 | Decision | Settled (provisional marks remain on Corporation, Institution, RegulatoryInstitution, Norm, Organization) | 2026-11-25 | H | Author asked whether bodies are subclasses or instances | Provisional marks blocked by HD26 |
| HD17 | Compliance and legal verdicts (compliant, liable) form a separate branch, not harm, unless harm is a premise | Session, 00:51 | Proposal | Draft | 2026-11-25 | M | Keeps normative status out of harm | Blocked by HD1; see HD23 |
| HD18 | Narrative in SKOS; reasoning richness carried by structural facets (`manifestsAs`, `hasModality`, `isSubstrateOf`) that point to SKOS concepts; divergence at a horizon is a facet comparison across assessments | Session, 00:26 to 00:37; [[Decisions_Log]] 2026-11-25 | Decision | Proposed (under stress test) | 2026-11-25 | H | Author's concern that the split loses reasoning over richness | Blocks HD19. Blocked by S4 (inferred) |
| HD19 | Stress test: surgeon case (one psychological effect, three perspectives) and surgeon-sued case, run through the coverage matrix | Session, 00:42 and 01:00 | Task | Not run | 2026-11-25 | H | Tests whether the Answered rows hold on a real case | Blocked by HD14, HD1 to HD3 |
| HD20 | Identification rules for instances (sortal plus persistence condition) and provisional natural-system classes | Session, 01:41 to 01:46; [[Decisions_Log]] 2026-11-25 | Decision | Deferred (author: "not yet") | 2026-11-25 | L | Would multiply classes before a case needs them | Revisit with HD27 |
| HD21 | State: a Quality with a TimeInterval region, or a Situation (no State class in DUL) | Session, tree (OPEN) and 01:xx gap list | Open | Open | 2026-11-25 | H | Used by HD4, HD8, HD13 and the wedge case; DUL gap 1 | Blocks HD4, HD8, HD13 |
| HD22 | ExposureSituation is a physical situation, but DUL treats Situation as a SocialObject | Session, tree | Open | Open | 2026-11-25 | M | Physical exposure and the fire room | Blocks ExposureDetermination naming |
| HD23 | Is ComplianceDetermination core or a discipline module? Is ConditionDetermination a subclass of Determination in its own right? | Session, 00:51 open points | Open | Open | 2026-11-25 | M | Scope of the core | Blocks HD17 |
| HD24 | Naming: `HarmDetermination` vs `HarmfulEffectDetermination` (both used in the chat); `ChainDetermination` vs `CausalChainDetermination` (both in the tree) | Session, 02:08 and 02:16 | Defect | Open | 2026-11-25 | M | Two names for one class | Blocks HD1 final list |
| HD25 | Is Entity the superclass of AffectedEntity (kinds across Object and SocialObject), or Object? | Session, 02:08 to 02:10 | Open | Open | 2026-11-25 | M | DUL: Entity is the top class; Situations are not Objects | Blocked by HD26 |
| HD26 | Check against the DUL file: Community, Group, Collection, CollectiveAgent, Organization, Norm, Quality, Event subclasses, InformationObject, Description, Region, TimeInterval, hasConstituent; confirm version (3.22 read; 3.32 and 4.2 reported) | Session, 01:23 to 01:26 | Task | Open | 2026-11-25 | H | Several classes marked provisional; tree not yet verified | Blocks HD8, HD16, HD25; extends S41 |
| HD27 | Natural individuals and systems: a river as `dul:PhysicalObject` or NaturalIndividual; an ecosystem as a Situation or a Collective; a watershed as a Place | Session, 01:41 to 01:46 | Open | Open | 2026-11-25 | L | Needed for ecosystem harm | Blocked by HD20 (deferred); relates to HD9 |

### 1. Schema and structure

| ID | Item | Source | Type | Status | Date | Pri | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|---|---|
| S1 | Discipline-enabled assessments and functional subclasses (CP-01) | Session 2026-11-22 ([[Task - Assessment Structure Initial Thinking]]) | Proposal | Draft | 2026-11-22 | H | Perspectives should enable assessments, not just tag them. Assessments serve different purposes (regulatory, forensic, diagnostic, normative) | Blocked by S26. Interacts with K1 |
| S2 | Agents, Event, participation, assessing organisations (HO-007) | [[Handoff - Harm Ontology#Open issues and to-dos added 2026-11-19]] | Decision | Draft | 2026-11-19 | H | Robbery case (robbers take part in an event that is part of an assembly); lion, storm and audit-firm cases raised by the author | Blocks S3, K3, A9. Blocked by T10 |
| S3 | What counts as an agent; `Agent (?)` scope, incl. AI systems | [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)#Structure]] (Agent (?) line) | Open | Open | 2026-11-15 | M | Lion, flood water and AI system cases; the draft marks Agent "(?)" | Blocked by S2 |
| S4 | Narrative placement: on the property or the concept | [[Harm Ontology v3 Provisional Release Brief#Decisions needed from the author before building]] (item 6) | Open | Reopened | 2026-11-18 | H | Mini example judged "awful" in Protégé; sample placements differ | Blocks D1 build, S5 |
| S5 | Domains, ranges and property groups for every class; data-entry route | [[Handoff - Harm Ontology#Open issues and to-dos added 2026-11-19]] | Task | Open | 2026-11-19 | H | Instances show no fields to fill in; OWL attaches properties to classes poorly | Blocks D1 build. Blocked by S4, S6 |
| S6 | How the 12 display groups are represented | [[Handoff - Harm Ontology#Open issues and to-dos added 2026-11-19]] (Property groups) | Open | Open | 2026-11-18 | H | Author: "this subgrouping was essential to understanding"; 0.02 says display facets, not classes | Blocks S5 (groups) |
| S7 | Layer-1 name "schema" (replaces "ontology") | [[Handoff - Harm Ontology#Open issues and to-dos added 2026-11-19]] (Layer-1 name) | Decision | Adopted, unlogged | 2026-11-18 | L | Naming clarity; author's choice | Blocks logging only |
| S8 | Rename `nameByDomain` / `definitionByDomain` to `…ByDiscipline` | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Structural and naming changes pending (not decided)]] | Decision | Draft | 2026-11-21 | M | "Domain" is overloaded with rdfs:domain | Blocked by T9, S24, S25 |
| S9 | `fieldOfApplication` gets a target class, not free text | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Structural and naming changes pending (not decided)]] | Decision | Draft | 2026-11-21 | M | Free text cannot be queried; 0.02 group 5 | Blocks S16. Blocked by S25 |
| S10 | `observabilityLimit` (0.01) has no 0.02 match | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Structural and naming changes pending (not decided)]] (item 6) | Open | Open | 2026-11-21 | L | Attribute dropped between versions; reason not recorded | Blocked by Box A decision |
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
| S21 | Scope: are disciplines and traditions to be represented as things in the model? (Was: is a discipline's perspective the same kind as a tradition's?) | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Open questions]] | Open | Deferred (reopened 2026-11-26, rescoped). Question is now scope only: S21 matters to the schema and vocabulary only if disciplines and traditions are represented as things in the model. The catalog design is keyed to source perspectives and does not depend on it. The 2026-11-22 answer ("same kind", tradition uses skos:altLabel) is withdrawn pending this decision, since it conflicts with the working picture that a tradition holds perspectives. Was: Settled (Yes, 2026-11-22; tradition uses skos:altLabel, not prefLabel) | 2026-11-22 | H | CP-01 depends on DisciplinePerspective being a PerspectiveType | None (S1 unblocked from S21) |
| S22 | Do disciplines or communities of practitioners hold perspectives? | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Open questions]] | Open | Open | 2026-11-21 | M | Decides `heldBy` | Blocks S15 |
| S23 | Can one specification combine more than one tradition (mixed lenses)? | [[PerspectiveStructure Proposal Draft 3.1]] (open questions) | Open | Open | 2026-11-20 | L | Real assessments may draw on several lenses | None recorded |
| S24 | Physics and Integral coverage test | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Coverage test: physicsPerspective and integralPerspective (proposed, structure only)]] | Task | Not run | 2026-11-21 | H | Test 0.02 structure against two different perspectives before logging | Blocks logging of S8–S20. Awaiting author go-ahead |
| S25 | Overlap test (0.02 table) and naming test in Protégé | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Test plan before any logging]] | Task | Not run | 2026-11-21 | H | Check each new name against neighbours and methodology rules | Blocks logging of S8–S20 |
| S26 | Gap schema attachment: PerspectiveType, procedural layer or HarmAssessment | [[Handoff - Harm Ontology#Searchlight, gap identification and method (2026-11-21; proposed, nothing logged)]] | Decision | Settled in substance (2026-11-28: all six items settled; S28 logging pending. Item 1 settled, provenance on HarmAssessment plus a procedure provenance set; see [[Decisions_Log]] 2026-11-28. Item 2 settled same day: rules on the procedure, cases on the output with `closureStatus` per RemedialObligation; see [[Decisions_Log]] 2026-11-28. Item 4 settled same day: enumerations are SKOS concepts that are also named individuals; see [[Decisions_Log]] 2026-11-28. Item 3 settled same day: issuedBy and hasEnforcementAuthority required, adoptedBy optional, no adoption records; see [[Decisions_Log]] 2026-11-28. Item 5 settled same day: object or data rule; confidenceLevel is an object property to ConfidenceLevel individuals, distinct from epistemicStatus; atHorizon is an object property to a Horizon individual (horizonKind, horizonReference, horizonEnd, horizonStart); OWL-Time reuse still to test; see [[Decisions_Log]] 2026-11-28. Item 6 settled same day: `enablesAssessment` dropped; `takenFrom` renamed `assessedFromPerspective`, on the base Assessment class, required by SHACL; see [[Decisions_Log]] 2026-11-28. S26 items 1 to 6 are settled. The placement test (S28) still needs logging before S26 is closed) | 2026-11-21 | H | Gap groups (mandate, valuation, lifecycle, remedy) describe assessment acts, not traditions | Blocks S27, S1 subclass placement. Blocked by S28 |
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
| S37 | Status of Harmfulness: reified class (Harmfulness with assessor, standard and criterion, `AssessedHarmfulness` as subclass) or first-class `AssessedHarmfulness` with no ontic Harmfulness | [[Harm Ontology v3 Design Notes - Harmfulness, Imagined Harm and Causal Chains#4. Harmfulness is not an ontic property; it is an assessment|Design notes §4–5]] | Decision | Open | 2026-11-23 | H | Harm is always judged; storm sensor and gun-rights cases | Blocks S38, S39. Author choice between the two options |
| S38 | `AssessedHarm` restricted to past or present harm; future projection named `AssessedImaginedHarm` | [[Harm Ontology v3 Design Notes - Harmfulness, Imagined Harm and Causal Chains#1. Temporal split: AssessedHarm is past or present only|Design notes §1–2]] | Decision | Proposed | 2026-11-23 | H | A forecast must not be recorded as a measured harm | Awaiting author confirmation. Blocks S39 |
| S39 | Grounding for `AssessedImaginedHarm`: evidentiary basis, vetting, grounding score, inheritance from a vetted pipeline | [[Harm Ontology v3 Design Notes - Harmfulness, Imagined Harm and Causal Chains#3. Grounding the imagination: evidentiary basis and vetting|Design notes §3]] | Proposal | Draft | 2026-11-23 | H | Projections need provenance without re-arguing the model each time | Blocked by S38. Whether a grounding score means the same across domains is open |
| S40 | Modular TBox over a shared ABox: domain modules (`psych:`, `legal:`) extend a core, instances keep one namespace | [[Harm Ontology v3 Design Notes - Harmfulness, Imagined Harm and Causal Chains#9. Modular domain properties over a shared instance graph|Design notes §9]] | Decision | Proposed | 2026-11-23 | M | One person keeps one identity across psychological and legal views | Awaiting author confirmation (chat: Ontological Commitment 01) |
| S41 | Causal-chain parent classes to be checked against the published DUL OWL file | [[Harm Ontology v3 Design Notes - Harmfulness, Imagined Harm and Causal Chains#6. Causal chains are occurrent structures with participants, not subclass trees|Design notes §6]] | Task | Partly checked (2026-11-24) | 2026-11-23 | H | The DUL-aligned table was drafted from memory and may misplace some classes. Checked 2026-11-24 against the file (version 3.22 mirror): Action, Agent, Role, Situation, Abstract, expresses, conceptualizes, classifies, hasParticipant, hasQuality. Not yet checked: InformationObject, Description, Quality, Event subclasses, Region, TimeInterval (see HD26) | Blocks any build of the causal-chain schema |

### 2. Council proposals (PerspectiveStructure 0.01 reviews)

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

### 3. Vocabulary and crosswalk (layer 3)

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
| V13 | Meta-Category V crosswalk: review targets, decide VB-0, load AIRO/DPV, run Meta-Category II | [[Harm Ontology Crosswalk - Pilot Meta-Category V]] (next steps) | Task | Open | 2026-11-17 | Tests the migration method on a real category | Blocked by K6, K7, S3, K5 (named as blocked rows in crosswalk) |

### 4. Assessment-everywhere (variant B) and tests

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

### 5. Causal assessment (HO-003, HO-005, HO-I.a)

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

### 6. Chain (HO-006, v4)

| ID | Item | Source | Type | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|---|
| H1 | Chain class (thin container, bounded by horizon) | [[HO-006 Causal Chain - an Assessed Selection with a Horizon]] | Proposal | Seed | Undated | `CausalRole` refers to a chain that has no object | Target v4. Blocked by H2–H3, A5 |
| H2 | Horizon measured from factor, effect or `assessedAt`; cuts by time, links or probability | [[HO-006 Causal Chain - an Assessed Selection with a Horizon#Open questions]] | Open | Open | Undated | Net effects need a bound | Blocks H1 |
| H3 | Where `maxHorizon` lives and who may override | [[HO-006 Causal Chain - an Assessed Selection with a Horizon#Open questions]] | Open | Open | Undated | Horizon is part of the claim key | Blocks H1 |
| H4 | Chain-level net assessment | [[HO-006 Causal Chain - an Assessed Selection with a Horizon#Open questions]] | Open | Open | Undated | Net results across a chain (HO-I.b) | Blocks H1 |
| H5 | Status calculation change beyond horizon in the key | [[HO-006 Causal Chain - an Assessed Selection with a Horizon#Open questions]] | Open | Open | Undated | Chain may change status rules | Blocked by A5 |
| H6 | Chain under `CausalCandidate` with FactorAssembly | [[HO-006 Causal Chain - an Assessed Selection with a Horizon#Open questions]] | Open | Open | Undated | Convergent causes | Blocked by H1 |

### 7. Other HO notes: open questions

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

### 8. Tasks, decisions and governance

| ID | Item | Source | Type | Status | Date | Why proposed | Blocks / Blocked by |
|---|---|---|---|---|---|---|---|
| T1 | DOLCE+DnS Ultralite licence | [[Harm Ontology v3.1 - Skeleton Schema (proposed)#Top priority: licence check (before any alignment work)]]; [[Decisions_Log]] 2026-11-25 | Task | Narrowed 2026-11-25: IRI reference permitted for testing; licence check still open for import or copy | 2026-11-21 (narrowed 2026-11-25) | Candidate upper ontology; sources conflict on licence (one hosting page states CC BY-SA 3.0). IRI reference is normal practice and is now permitted for testing. Importing, downloading or copying DUL content needs the licence confirmed | Blocks any import or copy of DUL, and O13. Subclass alignment by IRI may proceed. Written reply from ODP maintainers still needed before import |
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

Items that block the most others:
- **S24 and S25** (coverage and overlap tests) block S8–S20.
- **S28** (placement test) blocks S26 and S27.
- **A2 and A5** (non-expert and Horizon tests) block A1, the main structural choice.
- **S4, S5, S6, T11–T13, T15** (narrative placement, schema domains and ranges, build rules) block the first `.ttl`.
- **K1** (Valence/Responsibility split) blocks CQ9, S35 and several causal tests.
- **T2** (capability approach) blocks Phase 3.

Not blocked by anything, decidable now: S7, S11, T14, T17, T18.

---

## Settled (ready for implementation in v3.1)
*(No items yet. An item moves here when it has passed its tests or the author's review and is fully specified.)*

---

## Complete and Rejected (retained for the record)
*(Items with status `Complete` (implemented and logged in [[Decisions_Log]]) or `Rejected`. Newest at the top. Never deleted.)*

*No items yet.*

---

## Template for new entries

### CP-XX: [Title]
- **Type:** Proposal | Decision | Open Issue | Task | Defect
- **Status:** Seed Idea | Draft Proposal | Under Stress-Test | Settled | Complete | Rejected
- **Date Proposed:** [YYYY-MM-DD or Undated]
- **Date Settled / Rejected:** [YYYY-MM-DD or N/A]
- **Priority:** Low | Medium | High | Critical
- **Target Version:** v3.1 | v4 | v5+
- **Source:** [[link to note and heading]]
- **Why proposed:** [the gap it closes, with its source]
- **Proposed additions:** [classes, properties, individuals or SKOS hubs]
- **Three-layer impact:** [Layer 1 OWL · Layer 2 SHACL · Layer 3 SKOS]
- **Test case dependencies:** [HO-002 cases or toy runs]
- **External alignment:** [AIRO, DPV, LKIF-Core or other]
- **Blocks:** [IDs]
- **Blocked by:** [IDs, with "(inferred)" where not stated in a note]
- **Open questions:** [unresolved tensions]

---

**Version rollover:** when v3.1 implementation is complete, copy this document to `Harm Ontology v3.2 — Feature Roadmap and Change Ledger` (or v4.0). Carry active items across. Keep Complete and Rejected items at the bottom of the copy.
