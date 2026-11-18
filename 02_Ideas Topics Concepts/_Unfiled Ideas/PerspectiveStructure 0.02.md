---
fileClass: Idea
type: idea
status: developing
bookmark: draft
canonical_id: ho-perspective-structure-0-02
territory: revisited
revisits: "[[PerspectiveStructure 0.01]]"
tags: [ontology/harm]
aliases: [PerspectiveStructure 0.02, PerspectiveType Structure v-0.02]
created: 2026-11-17
---

# PerspectiveStructure 0.02

> [!info] Version
> Consolidates [[PerspectiveStructure 0.01]] and its seven council reviews (HO-II.d.1.a–g). 0.01 stays frozen. Words and meanings for each attribute live in the vocabulary layer, [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes|HO-II.d.2]]; this note holds the structure.

## Why this is distinct
- 0.01 was a first list of eight groups. 0.02 prunes and reorganises 120+ proposed attributes into a minimal core, twelve display groups and two profiles, separates description from evaluation, and places PerspectiveType inside [[Harm Ontology v3 - Draft Structure|Harm Ontology v3]].

## Anticipated direction
- Write a concept hub, with discipline spokes, for each ★ attribute (congruence, omission and developmentalAltitude are done).
- Resolve the three v3 integration issues below.
- Then express the structure in the v3 `.ttl` (Migration Plan, Phase 1).

## Conceptual territory
- Revisits 0.01. Uses OWL for structure, SHACL for profiles and SKOS for vocabulary (the three layers, HO-II.d.2).

## Summary

### Decisions this version applies (all in [[Decisions_Log]], 2026-11-17)
- **PerspectiveType / Perspective split:** both are classes; each tradition and each shot is an individual; a shot `instantiates` a tradition and may override its defaults; subclasses only for kinds of tradition.
- **Terminology:** PerspectiveType has prefLabel "tradition", altLabel "lens"; Perspective is a "shot"; `fieldOfApplication` replaces `domainOfApplicability`; "profiles" replaces "domain profiles"; "domain" keeps only its OWL meaning.
- **Three layers:** ontology (`ho:`), profiles (`hosh:`), vocabulary (`hov:` hubs plus discipline schemes), with graded mappings.
- **Integral position confirmed** as group 3 (author, 2026-11-17).

### Consolidation rules used
- **Minimal core** (Descartes): only four attributes are required; every other attribute may take a missingness status ([[HO-II.e Missingness Statuses and Domain Profiles|HO-II.e]]).
- **Pragmatic test** (Peirce; the HO-II.d keep-test): an attribute stays only if some query, decision or Divergence changes when its value changes.
- **Rank by impact** (Fermi): ★ marks the leading tier.
- **Description vs evaluation** (Hart): evaluative attributes sit in group 11, each an Assessment with `assessedBy`.
- **Date-stamped meanings** (Scalia): `meaningAsOf`, `validFrom` / `validTo`.
- Groups are display facets, not OWL classes (Laozi).

### Structure
```text
PerspectiveType  (prefLabel "tradition" · altLabel "lens")
│   ◄── instantiates ──  Perspective  (shot; HO-II.d; overrides frame defaults)
│
├── 0  CORE (required) ──────────────────────────────────────────────────────
│   ├── name ★
│   ├── canonicalSource ★ ............ absorbs foundationalWork, canonicalText
│   ├── objectOfAttention ★
│   └── foundationalCommitments ★ .... absorbs assumption, principles, priors/baseRates
│
├── 1  RELATIONS (relations before attributes) ──────────────────────────────
│   ├── divergesFrom / convergesWith ★ → PerspectiveType (reified; HO-III.a)
│   ├── specializes / generalizes .... absorbs formalCause
│   ├── partOf / hasSublens
│   ├── complements · complementaryWith · definedAgainst
│   ├── coupledWith .................. resonance and feedback between traditions
│   └── correctedBy → Community ...... community of inquiry
│
├── 2  IDENTITY & LINEAGE ───────────────────────────────────────────────────
│   ├── nameByDomain · definitionByDomain (+ meaningAsOf)   [rename pending: "domain" → "discipline"]
│   ├── conceptStructure {definitional · family resemblance · prototype · interpretive} + exemplars
│   ├── lensKind {designed · tacit · learned · cultural technology}
│   ├── lineage → Person · originatingCircumstance → Event
│   ├── transmissionMode {text · apprenticeship · ritual · institution · narrative · trained model}
│   └── historicalNote
│
├── 3  INTEGRAL POSITION (confirmed 2026-11-17) ─────────────────────────────
│   ├── 3.1 quadrant axes (Wilber, AQAL)
│   │   ├── interiority ★ {interior · exterior · both}
│   │   ├── collectivity ★ {individual · collective · both}
│   │   └── quadrant (derived) {UL interior–individual · LL interior–collective ·
│   │                           UR exterior–individual · LR exterior–collective}
│   └── 3.2 scope axes (kept separate)
│       ├── socialScope (size) {individual · family · community · tribe · nation · species …}
│       ├── moralCircle ★ (which beings count) {… · humanity · sentient · future · AI systems · ecosystems}
│       └── developmentalAltitude (Assessment; scale + assessedBy required)
│             e.g. Integral: bands ▸ Gebser stages ▸ colours → [[Integral Altitude Scale]]
│                  Gilligan care stages · Kohlberg levels · Confucian / Stoic → hub in HO-II.d.2
│
├── 4  EXTENT ───────────────────────────────────────────────────────────────
│   ├── spatialScope · systemicScope
│   ├── temporalScope (+ discountRate)
│   └── scaleValidity
│
├── 5  AIM & NORMATIVE CORE ─────────────────────────────────────────────────
│   ├── statedPurpose ★ .............. operative side is assessed under congruence (11)
│   ├── normativeForm ★ {deontic · consequentialist · aretaic · relational · contractualist} (plural)
│   ├── valueTheory · embedsStandard → EvaluativeStandard (HO-II.a)
│   ├── unitOfMeasure ★ + commensurability
│   ├── intentWeighting ★ {intent · outcome · mixed}
│   ├── distributiveConcern · conflictResolution {lexical · weighing · deadlock}
│   └── fieldOfApplication ........... (formerly domainOfApplicability; jurisdiction in Legal profile)
│
├── 6  EPISTEMICS ───────────────────────────────────────────────────────────
│   ├── method + instrumentResponse ★ (threshold · false alarm · miss)
│   ├── criterionOfTruth + inferenceModes
│   ├── causalModel → CausalGraph (HO-I.a)
│   ├── errorHandling {update · act on world · suppress · immunize}
│   ├── explorationMode {explore · exploit}
│   ├── factHandling {preserves · blurs · dissolves}
│   └── manipulability (+ authenticityAssumption)
│
├── 7  STANCE (holder's side) ───────────────────────────────────────────────
│   ├── bearerRole · controlLocus
│   ├── stanceTowardObject {physical · design · intentional}
│   ├── governingAnalogies
│   └── effectOnHolder ★ {affective · dispositional · cognitive · physical/observer cost}
│
├── 8  SUBJECT'S SIDE ───────────────────────────────────────────────────────
│   ├── standingOfSubjects ★ {agent · patient · datum}
│   ├── modelOfSubject · legibility (+ interfaceAbstraction)
│   ├── consentToBeSeen ★ (qualified by powerAsymmetry)
│   ├── adaptiveResponse
│   └── livedExperience
│
├── 9  POWER ────────────────────────────────────────────────────────────────
│   ├── authority → bound parties + authorityBasis {coercive · legal · expert · moral · customary}
│   ├── whoseInterests ★ · costBearer ★ (+ differentialBurden) · whoseVoice ★ (+ precisionWeighting)
│   ├── powerAsymmetry {low · high · total}
│   ├── accountabilityLocus ★ {named agent · role · institution · Nobody} (+ laundering)
│   └── remedy
│
├── 10 DYNAMICS & MATERIALITY ───────────────────────────────────────────────
│   ├── performativity ★ {none · self-confirming · self-defeating}
│   ├── infrastructureDependence
│   ├── validFrom / validTo · changeMode
│   └── prevalence {dominant · contested · marginal · emerging}
│
├── 11 ASSESSMENTS (each an Assessment with assessedBy → PerspectiveType) ───
│   ├── congruence ★★ (stated vs operative) .... hub drafted, HO-II.d.2
│   ├── omission ★ ............................. hub drafted, HO-II.d.2
│   │   ├── outOfFrame (constitutive)
│   │   ├── blindSpot (visible but missed) {negligent · suppressed}
│   │   └── acceptedHarm (seen and tolerated)
│   ├── failureMode {excess · deficiency}
│   ├── epistemicStanding: corroboration · calibration + uncertainty · anomalies · orderOfMagnitude
│   ├── proceduralIntegrity (Fuller's eight) · publicJustifiability
│   └── knownCritique → critiquedBy
│   (developmentalAltitude is also an Assessment; displayed in group 3)
│
├── 12 PROVENANCE & TRUST (about the record) ────────────────────────────────
│   ├── 12a Sources: keyReference · citation · Source class
│   ├── 12b PROV: wasAttributedTo · wasGeneratedBy · wasDerivedFrom · created/modified · originalWording
│   └── 12c verificationStatus (citations only) · evidenceLabel · confidence · canonStatus
│
└── PROFILES (HO-II.e) ──────────────────────────────────────────────────────
    ├── LegalInstitutional: validity · efficacy · recognitionStatus · internalAcceptance · standing ·
    │     precedentialWeight · standardOfProof · causationTest · jurisdiction · limitationPeriod ·
    │     discoveryRule · legalPersonhood (twin of moralCircle)
    └── LearnedModel: trainingProvenance · objectiveFunction · comprehensionClaim (lensKind = learned)

★ leading tier · ★★ first-class · everything outside group 0 is optional (missingness statuses apply)
```

### Dropped or folded in
- `formalCause` → `specializes` + definition · `reflexiveApplication` → selfInstance (open question) · `dominantFactors` → shot level · `translationLoss` / `compressionLoss` → notes on a transformation mapping, if adopted · `limitBehavior`, `futureRobustness` → notes under epistemicStanding · `emergentEcosystems` → deferred · `narrativeForm` → a `transmissionMode` value · `importance` → Power and Dynamics · `harmPrincipleRespected` → publicJustifiability · `degeneracy`, `reentrantIntegration` → [[HO-III.a Divergence and Integration - True but Partial|HO-III.a]] · `status` → split into prevalence (10) and epistemicStanding (11) · `blindSpot` → omission with three branches.

### Place in Harm Ontology v3
- New class **PerspectiveType** beside the existing **Perspective**; `Perspective instantiates PerspectiveType`.
- Links: `embedsStandard` → EvaluativeStandard · `moralCircle` ↔ Patient · omission ↔ CausalAssessment.`leftOut` (formerly Attribution) and HO-005 · `accountabilityLocus`, `lineage` → Agent · `remedy` → LegalResponse · LegalInstitutional profile ↔ Judgment profile (HO-II.c) · LearnedModel ↔ Agent.AutonomousSystem (?).
- New use of Assessment: assessments *of* traditions. New box: the vocabulary layer (HO-II.d.2).

## Original wording
> "Read Handoff - PerspectiveStructure 0.02 and the notes it lists, then propose the 0.02 structure."
- **Attribution:** Author

> "Eleven groups is too many for a reader."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5), in the first proposal (which then had eleven groups plus Core)

> "lets use these recommendations except list tradition as skos:prefLabel and lens as skos:altLabel"
- **Attribution:** Author

> "integral group confirmed. altitude  note then write perspective structure"
- **Attribution:** Author

> "sorry,  i meant semantically woud Attribution be the same as AttributedCause.  i am wondering about a less ambiguous formal name"
- **Attribution:** Author

> "lets decide c."
- **Attribution:** Author (choosing to merge v3 Attribution into CausalAssessment)

- **Source:** Obsidian Copilot agent session "Read Handoff - PerspectiveStructure 0.02 and the notes it lists", 2026-11-17 (`copilot/copilot-conversations/agent__Read_Handoff_-_PerspectiveStructure_0.02_and_the_notes_it_lists,@20261117_170442.md`); earlier session "Name this chatWhat is Perspective", 2026-11-17.
- **External references:** the seven council reviews ([[v-0.01 ClassicalCouncil Review of - PerspectiveStructure 0.01|Classical]], [[v-0.01 EthicsCouncil Review of - PerspectiveStructure 0.01|Ethics]], [[v-0.01 LegalCouncil Review of - PerspectiveStructure 0.01|Legal]], [[v-0.01 LogicCouncil Review of - PerspectiveStructure 0.01|Logic]], [[v-0.01 PhysicsCouncil Review of - PerspectiveStructure 0.01|Physics]], [[v-0.01 SciFiCouncil Review of - PerspectiveStructure 0.01|Sci-Fi]], [[v-0.01 CognitiveCouncil Review of - PerspectiveStructure 0.01|Cognitive]]) and their verified citation tables; Wilber primary texts as listed in [[Integral Altitude Scale]].

## Real-world examples
- Traditions to record first: Public Health, Utilitarianism, Tort Law, Integral Theory, and one trained AI model (LearnedModel profile).

## Why it matters to the book
- A harm dispute is often a dispute between traditions that don't know they are traditions. 0.02 makes a tradition's commitments, omissions, power and congruence explicit, and lets a trained model be recorded as one.

## Open questions
- **v3 integration:**
  - Standard overlap: make PerspectiveType's `embedsStandard` the default and the shot's `standard` the override?
  - Omission and causal selection: **decided 2026-11-17.** v3 `Attribution` merges into `CausalAssessment`, with `attributedCause` and `leftOut` → `CausalCandidate` (Factor or FactorAssembly, formerly CausalAssembly, now a thin container whose membership and origin are assessed); each left-out item may carry an omission assessment. Tradition-level omission patterns act as defaults that cases confirm or contradict.
- Can a shot instantiate more than one tradition (mixed lenses)?
- Rename `nameByDomain` / `definitionByDomain` to `…ByDiscipline`?
- Still open from the handoff: statement-level provenance (RDF-star or named graphs) · attribute-space / embedding model for comparing traditions · the ontology as an instance of its own PerspectiveType · new Divergence subtypes for HO-III.a.
- The council reviews are not independent evidence: all seven were voiced by one model.

## Related
- [[PerspectiveStructure 0.01]]
- [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]]
- [[Integral Altitude Scale]]
- [[Harm Ontology v3 - Draft Structure]]
- [[HO-II.d Perspective - Ten Optional Properties]]
- [[Handoff - PerspectiveStructure 0.02]]
