# Model Structure Test Note: Competency Questions and Coverage

Status: **Proposed.** Working test record for the v0.03.01 structure. Nothing here is settled or logged in the decisions log. Index: [[_Harm Ontology v0.03.1 Master Index]].

## 1. Purpose
Test whether the candidate structure can answer the questions it must answer, and whether each part of it earns its place. The test has three parts: (a) competency questions (CQs), (b) case tests, and (c) a coverage matrix that checks every class answers a question and every question maps to a class.

## 2. Competency questions

### 2.1 Inherited from HO-002.a (v3, draft)
Full wording and pass criteria are in [[HO-002.a Assessment-Everywhere Test Strategy]].
- **CQ1:** Who or what caused Effect X? Causes are returned per perspective; conflicts appear side by side.
- **CQ2:** Which Effects are severe? Disputed and unassessed Effects must appear with their status, never drop out silently.
- **CQ3:** What do all perspectives agree on? Settled only under a shared procedure, with an evidence pointer.
- **CQ4:** How did a verdict change over time, and what changed it? Dated assessments; reopened claims show both states.
- **CQ5:** Which judgements rest on a stated, inherited or no standard?
- **CQ6:** What did a perspective leave out, and why (out of frame, blind spot, accepted harm)?
- **CQ7:** Does this entity count as an AffectedEntity, of what kind, and according to whom? Unlisted kinds appear as `Unclassified`.
- **CQ8:** When did Effect X occur, and who was directly affected?
- **CQ9:** Who is answerable for Effect X, and according to whom? Kept apart from CQ1 and from valence.

### 2.2 Added in the 2026-11-24 to 2026-11-25 sessions
- **CQ10:** Which two perspectives differ on the assessment of a given harm, on which dimension (valence, severity, role, horizon, standard), and at which temporal horizon?
- **CQ11:** Which harm was realised and which is projected, and what grounds the projection?
- **CQ12:** Which states and factors were relevant to this consequence, and with what weight (trigger versus predisposition)?
- **CQ13:** What was the exposure: was the entity in a hazardous situation, and for how long?
- **CQ14:** What condition did the entity have, and under which criteria was it identified?
- **CQ15:** What was the causal boundary of this assessment, and why did tracing stop there?
- **CQ16:** Was the risk accepted, by whom, and for which recipient (consent)?
- **CQ17:** Does a remedy or obligation follow, and has closure occurred?
- **CQ18:** Which information objects carried this determination forward, and did they carry an error?

## 3. Sufficiency test for any question
A question stays in the set only if it passes all four:
1. **Answerable from the schema.** Some combination of classes and properties yields an answer.
2. **Attributable.** The answer carries an assessor, a perspective and a horizon.
3. **Traceable to a use.** A named stakeholder would ask it (regulator, clinician, litigator, historian, analyst).
4. **Testable on a case.** We can say what a good answer looks like for at least one case.

## 4. Coverage matrix (to build)
- Rows: CQ1 to CQ18. Columns: every class and relation in the candidate structure.
- **Every class** appears in at least one CQ. A class that answers nothing is decoration and should be removed or justified.
- **Every CQ** maps to at least one class or relation. A CQ with no home signals a missing layer.
- **Every CQ family** is run on at least two cases with different perspectives.
- Sources for further questions: stakeholder use cases; NIST SP 800-30, ISO 14971 and STPA question sets; failure cases the model must flag (for example, "is this harm objective?" should be refused and answered "no, it is a determination").

## 4a. Coverage matrix (first pass, 2026-11-25)

Status key: **Answered** = the current candidate structure yields the answer by design (not yet built or run) · **Partly** = answer depends on a class, property or rule not yet defined · **Gap** = no class or rule supports it.

### Direction 1: each CQ mapped to classes

| CQ | Question (short) | Main classes that answer it | Status | What is missing |
|---|---|---|---|---|
| CQ1 | Who or what caused X? | ChainDetermination, RoleAssignment, Factor | Answered | none beyond K2 (causal standard) |
| CQ2 | Which effects are severe (naive)? | HarmDetermination, Divergence, Effect | Partly | unassessed effects need an explicit "not assessed" status surfaced in queries |
| CQ3 | What do all perspectives agree on? | Divergence, Determination | Partly | **Procedure** and **Evidence** classes (HO-002 agreement rule) |
| CQ4 | How did a verdict change, and why? | Determination (versioned, R17) | Partly | **revision trigger** and version-chain relation |
| CQ5 | Which judgements rest on a standard? | PerspectiveSpecification, assessmentBasis | Answered | assessmentBasis must be kept on every assessment |
| CQ6 | What did a perspective leave out? | ChainDetermination (CausalBoundary), PerspectiveSpecification | Partly | omission as a determination type beyond causal boundary |
| CQ7 | Is this an AffectedEntity, of what kind? | AffectedEntity, Agent | Partly | assessed entity type and the **Unclassified** value |
| CQ8 | When did X occur, who was affected? | Effect (occurrence date, decision 21), AffectedEntity | Answered | none |
| CQ9 | Who is answerable for X? | ResponsibilityDetermination, RoleAssignment | Answered | depends on K1 split being adopted |
| CQ10 | Which two perspectives differ, why, at horizon H? | Divergence, PerspectiveSpecification, TemporalHorizon, HarmDetermination | Answered | depends on facets being queryable |
| CQ11 | Realised or projected, and what grounds it? | AssessedImaginedHarm, temporal status, grounding | Partly | grounding inheritance rule (S39) |
| CQ12 | Which states were relevant, with what weight? | RelevanceDetermination, RoleAssignment | Partly | **weight** property on relevance (proposed, not defined) |
| CQ13 | Was the entity in a hazardous situation? | ExposureDetermination, State | Answered (proposed) | ExposureDetermination still to be confirmed (open question) |
| CQ14 | What condition did it have, by what criteria? | ConditionDetermination, State | Answered (proposed) | ConditionDetermination as a class still to be confirmed |
| CQ15 | Where did tracing stop, and why? | ChainDetermination, CausalBoundary, TemporalHorizon | Answered | none |
| CQ16 | Was the risk accepted, by whom? | ConsentDetermination, AffectedEntity | Partly | consent per recipient (R22) not yet a class in the tree |
| CQ17 | Does a remedy follow; is it closed? | RemedyDetermination | Partly | closure status and link to the obligation |
| CQ18 | Which information carried an error forward? | InformationObject, MechanismModel | Partly | **error or provenance** relation on InformationObject |
| **CQ19** (new) | Which controls or barriers were in place, did they work, per whom? | (none in the tree) | **Gap** | **Control** class has no question that uses it; needs a determination of efficacy |
| **CQ20** (new) | What capability did each perspective attribute to the source? | (none explicit) | **Gap** | CapabilityAssessment and CapabilityDetermination have no question that uses them |

### Direction 2: each class mapped to CQs

| Class | CQs that use it | Orphan? |
|---|---|---|
| PerspectiveSpecification | CQ5, CQ6, CQ10 | no |
| Factor (Act, Condition, Structure) | CQ1, CQ12 | no (thin for Structure) |
| State | CQ13, CQ14 | no |
| **Control** | none | **yes: orphan** (CQ19 added to fix) |
| Effect | CQ2, CQ8 | no |
| AffectedEntity | CQ7, CQ8, CQ16 | no |
| Agent | CQ7, CQ9 | no |
| InformationObject | CQ18 | weak (one question only) |
| MechanismModel | CQ18 | weak; should also support CQ10 (why the perspectives differ) |
| ChainDetermination / CausalChain | CQ1, CQ6, CQ15 | no |
| CausalChainPattern (role kinds) | CQ1, CQ12 | weak |
| RoleAssignment | CQ1, CQ9, CQ12 | no |
| CapabilityAssessment / CapabilityDetermination | none | **yes: orphan** (CQ20 added to fix) |
| HarmfulnessAssessment | none directly | weak; reachable only through CQ20 |
| HarmDetermination | CQ2, CQ10 | no |
| AssessedImaginedHarm | CQ11 | no |
| ConditionDetermination | CQ14 | no |
| ExposureDetermination | CQ13 | no |
| RelevanceDetermination | CQ12 | no |
| ResponsibilityDetermination | CQ9 | no |
| ConsentDetermination | CQ16 | no |
| RemedyDetermination | CQ17 | no |
| Divergence | CQ2, CQ3, CQ10 | no |
| Procedure / Evidence | none (not in the tree) | needed by CQ3 |

### Findings
1. **Two orphan classes**, Control and CapabilityAssessment, which means the structure has parts no question needs. Either a question is missing (CQ19 and CQ20 fix that), or the part should go. Both are needed by earlier cases (fire door, dealer), so the questions were the gap.
2. **Three gaps needing new classes or rules**: Procedure and Evidence (CQ3), revision trigger (CQ4), and efficacy for controls (CQ19).
3. **Weak classes**: InformationObject and MechanismModel each answer one question. The dispatcher and dealer cases suggest they should answer more (CQ10 and CQ18), which is a reason to keep them.
4. **Answered by design, not yet proven.** Most of the "Answered" rows depend on the candidate determination classes, which are still proposals. The matrix shows coverage on paper; only a case run can confirm the answers.

## 5. Candidate determination classes (from the 2026-11-25 discussion)
Subclass axis is the question answered, not the kind of harm. Council categories stay in the vocabulary.
- Identification: ConditionDetermination, InvestigativeDetermination, ExposureDetermination
- Relevance: RelevanceDetermination (trigger versus predisposition as a weight)
- Attribution: ChainDetermination (with CausalBoundary and horizon), ResponsibilityDetermination
- Valence and closure: HarmDetermination (substrate subclasses; severity and probability as properties; temporal status as an attribute), ConsentDetermination, RemedyDetermination
- Separate branch, not harm: ComplianceDetermination, LegalDetermination (unless harm is a premise)
- Causal boundary and time horizon are declared parameters of an assessment, with a required justification. They are not separate determination classes. Divergence over them is a recorded dimension.

## 6. Case tests run so far
| Case | What it tested | Main result |
|---|---|---|
| Fire door | Same element, several roles under three lenses; state changes role | Roles must be scoped to consequence; element state must be modelled |
| Dinner party | Loops; one person as source and receptor; mechanism model held by a person | Loops and dual roles needed; determinations versioned |
| Drug dealer | Social roles versus causal roles; structural source with no agent | Social statuses stay out of the causal layer |
| Dealer, buyer's downstream chain | Downstream projection; assessment as input, not factor | Hypothetical factors belong in AssessedImaginedHarm |
| Surgeon | Mixed valence over time; psychological harm discovered through facets | Richness via facets and SKOS links, not extra OWL classes |
| Surgeon sued | Three perspectives on one effect | Three instances of one class; divergence computed |
| Dispatcher | Information as artifact and mechanism | Information object has dual status (open) |
| 2008 crisis (sketch) | Extraction versus assessment; reports as determinations | See [[Scratch - 2008 Crisis Extraction Test Sketch.md]] (scratch, not part of the design) |

## 7. Key insights to keep
- Assessment is the act; determination is its output. Act and output are never confused in names.
- Harm (realised) and harmfulness (source-side) are different loci. Capability is assessed, not carried.
- Narrative richness belongs in the vocabulary; reasoning richness belongs in the schema; the bridge is facets and SKOS links.
- Settled past, open future. Upstream knowledge can be incomplete; the causal boundary is chosen; the horizon bounds the assessment.
- Assessments can be inputs to acts (for example, an employer's decision), but they are not factors themselves.
- Roles (source, barrier, trigger, receptor) are assessed claims, scoped to a consequence, assessor and standard.

## 8. Open questions
- Is ExposureDetermination distinct from RelevanceDetermination?
- Should ConditionDetermination be a subclass of Determination in its own right?
- Is ComplianceDetermination in the core or a discipline module?
- Does RoleAssignment have the same kind as Determination, or is it a subtype?
- Are loops a special class or repeated events?
- Which causal standard (but-for, NESS, INUS) is the default for attribution? (ledger K2)

## 9. Next steps
1. Build the coverage matrix (section 4) for CQ1 to CQ18 against the candidate classes in section 5.
2. Mark each CQ as answered, partly answered, or unanswered by the current structure.
3. Run the matrix against the surgeon-sued case and the dispatcher case.
4. Record agreed findings in the ledger, marked Proposed until the author confirms.
