---
type: outline
status: developing
tags: [ontology/harm]
aliases: [Harm Ontology v3, v3 Draft Structure]
created: 2026-11-15
source: "[[2026-11-14 Harm Ontology Redesign]]"
---

# Harm Ontology v3 — Draft Structure

The consolidated v3 model as of the end of session [[2026-11-14 Harm Ontology Redesign]]. Each element links to its decision in [[Decisions_Log]] (2026-11-14 and 2026-11-15) or to its HO note. Markers:
- **(?)** open question
- **(pending)** proposed but deliberately *not* logged; to be decided after testing

No element has been tested yet (see [[HO-002 Ontology Stress-Test Suite]]).

> [!warning] Status
> This is a design draft, not an ontology file. No v3 `.ttl` exists yet. Building one is Phase 1 of [[Harm Ontology Migration Plan]].

## Governing commitments
- Theories of harm **describe and judge**; they don't classify. → [[HO-000 Harm as Perspective-Relative Assessment]]
- **No intrinsic harmfulness**: valence lives only in assessments. → [[HO-premise No Intrinsic Harmfulness]]
- **Deliberately asymmetric in time**: causes converge into a settled past; effects ramify into an open future. The full causal past and full causal future are limit concepts, never instantiated. → [[HO-004 Criticality, Leverage and the Limits of Scope]]
- **Scope is never complete**: `scopeAdequacy` defaults to Unknown and can never be Complete. → HO-004
- **Open world, explicit missingness, domain profiles.** → [[HO-II.e Missingness Statuses and Domain Profiles]]
- **Map, don't import** (reuse expert vocabularies). → [[HO-III.b Reusing Expert Domain Vocabularies]]

## Structure

```text
HARM ONTOLOGY v3 (draft, 2026-11-15; revised 2026-11-17)
│
├── CausalCandidate (2026-11-17) ................... parent of Factor and FactorAssembly; anything a
│                                                    CausalAssessment may select or leave out
│
├── Factor ⊑ CausalCandidate ....................... neutral; one contributor among many  → HO-I.a
│   ├── Act · Process · Omission · Structure · Risk
│   └── Condition (?) → PhysicalState (?) · Status (?) · Disposition (?)
│   props: causes → Factor|Effect · isContinuous · observability (box A) · hasAgent → Agent (?)
│          (membership in a FactorAssembly is now supplied by assessments; see below)          → HO-003
│
├── CausalRole ..................................... part a factor plays in one chain     → HO-I.a
│   roleType: Trigger · Enabler · Amplifier · Conduit · ProximateCause · DistalCause · ContributingCause (?)
│   props: borneBy → Factor|Effect · contributesTo → Effect · causalNecessity · proximity ·
│          causalShare (?) · isDistributed · isForeseeable · answerableAgent (?) · withinAssembly (?)
│
├── FactorAssembly ⊑ CausalCandidate ............... (formerly CausalAssembly; altLabel "causal assembly") → HO-003
│   THIN CONTAINER: identifier + label only, the shared referent rival assessments point to.
│   Supplied by CausalAssessment, not asserted here: members · hasUnknownMembers · individuallyInnocuous ·
│          origin: Emergent | Exploited | Engineered · orchestrator → Agent (?) · sufficientFor → Effect|Outcome
│   (derived shortcuts allowed where assessments agree; Disputed where they don't)
│
├── (Attribution — merged into CausalAssessment, 2026-11-17; see Assessment kinds) → HO-004
│
├── Effect ......................................... neutral; one consequence among many  → HO-I.b
│   kinds: SleepLoss · ReputationalDamage · Deskilling · CapturedAssent (?) · Death · …
│   HarmfulEffect — optional, inferred from ≥1 Harmful assessment
│   props: leadsTo → Effect (cascades; open-ended) · affects → AffectedEntity · hasObjectOfHarm ·
│          experienceability (box A) · isPosthumous · isStatistical · isDispositional ·
│          severity · reversibility · temporalTrajectory · modality · temporalStatus: Actual|Extrapolated|Pending
│   (Effect and Factor are not disjoint)
│
├── Outcome ........................................ a cut across the ramification at a horizon → Decisions 2026-11-14
│   props: hasEffect → Effect · selectedBy → PerspectiveSpecification (framing, resolution)
│
├── AffectedEntity ................................. SentientIndividual · CollectiveArtificialPerson · NonSentientSystem ·
│   (formerly Patient; altLabels "patient",          FutureGeneration · AISystem · Relationship
│    "moral patient"; renamed 2026-11-18)
│   types are inclusive; standing is assessed (decided 2026-11-18)
│   proposed 2026-11-18, untested (→ HO-002.a): AffectedEntity type as assessed · Unclassified ·
│          NonSentientSystem → NaturalSystem | EngineeredSystem · affectedStanding: Direct|Derivative ·
│          CollectiveNaturalGroup (communities, cultures, tribes) · Household · Factor and AffectedEntity not disjoint
├── ObjectOfHarm (values) .......................... Somatic · PsychologicalCognitive · Assent/Judgment (?) · MaterialPecuniary ·
│                                                    DignitaryRelational · NormativeStatus · OpportunityCapability · SystemicEnvironmental
│
├── EvaluativeStandard (individuals) ............... altLabel "theory of harm"             → HO-II.a
│   ├── Philosophical: ExperientialAccount · ComparativeAccount · NonComparativeAccount · RightsBasedAccount · CapacityAccount
│   ├── Legal: InjuryInFact · ReasonablePerson · LossOfChance · ConcreteHarm · …
│   ├── Causal (pending): ButFor · NESS · INUS · ProbabilityRaising · Mechanistic · Proximate   → HO-005
│   └── Worldview (?)
│
├── Perspective (ABSTRACT; no direct members; definition + Explanation only) (2026-11-17)
│   │   disjoint subclasses:
│   │
│   ├── PerspectiveType ............................ prefLabel "tradition" · altLabel "lens"     → [[PerspectiveStructure 0.02]]
│   │   e.g. Utilitarianism · Tort Law · Public Health · a trained AI model
│   │   groups 0–12 + profiles (LegalInstitutional · LearnedModel); key links:
│   │   defaultEvaluativeStandard → EvaluativeStandard · moralCircle ↔ AffectedEntity ·
│   │   accountabilityLocus / lineage → Agent · remedy → LegalResponse ·
│   │   group 11 = Assessments of the tradition (congruence · omission · developmentalAltitude …)
│   │
│   └── PerspectiveSpecification (reusable; all props optional) ... prefLabel "perspective specification" ·
│       │                                            altLabels "viewpoint", "perspective snapshot"  → HO-II.d
│       ├── instantiates → PerspectiveType (inherits its defaults; may override)
│       ├── Position: standpoint · direction
│       ├── Time: timestamp (assessedAt) · exposure (horizon) · predictabilityHorizon (?)
│       ├── Optics: framing · resolution · sensitivity (threshold)
│       ├── Purpose: intent · appliedEvaluativeStandard (inherits defaultEvaluativeStandard if absent) ·
│       │            fitness · inclusionCriteria · aggregationRule
│       └── Operator: assessor → Agent
│
├── Assessment (one judgment = one instance) ....... → HO-II.a
│   props: assesses → Factor|CausalRole|Effect|Outcome|FactorAssembly|PerspectiveType · takenFrom → PerspectiveSpecification ·
│          forAffectedEntity · chainScope · chainStatus: Actual|Extrapolated ·
│          verdict: Harmful|Beneficial|Mixed|Neutral|Contested · verdictStatus: Provisional|Final (+ closedBy) ·
│          declaredScope · acknowledgedExclusions · scopeAdequacy (never Complete) ·
│          sensitivity/leverage · criticality (as assessed) · confidence · suppliedBy
│   kinds: CausalAssessment (adopted 2026-11-17; absorbs Attribution):
│            attributedCause → CausalCandidate · leftOut → CausalCandidate (+ omission assessment) ·
│            FactorAssembly members · sufficientFor · origin · orchestrator · individuallyInnocuous
│          ValenceAssessment · ResponsibilityAssessment (split still pending)               → HO-005
│   profiles: Personal · Moral · Expert · Regulatory · Threat · Algorithmic ·
│             Judgment (+ authority · jurisdiction · bindingForce · procedure · ratio ·
│             cites/distinguishes/overrules · remedyOrdered · finality)                       → HO-II.c
│
├── Divergence ..................................... → HO-III.a
│   props: between → Assessment (2+) · divergesOn → PerspectiveSpecification or PerspectiveType property ·
│          divergenceType: Perspectival | Normative | Evidential | Factual ·
│          (pattern) FactorLevel vs AssemblyLevel · reconcilable
├── Integration (optional) ......................... integrates · resolves/leavesOpen · keptInFrame/leftOut
│
├── Agent (?) ...................................... UnitaryIntentionalAgent · CollectiveAgent · AutonomousSystem (?)
│   beneficiaryRole (from v2): Perpetrator | PrincipalInstitutional | DownstreamMarket | None
│
└── LegalResponse (later) .......................... CauseOfAction · Doctrine · Remedy

BOX A — Phenomenality (property): Phenomenal | NonPhenomenal | ConditionallyPhenomenal
        observability (+ observableBy · revealedBy · hiddenFrom) · experienceability (relative to the affected entity)
BOX B — Missingness: (absent)=not considered · Unknown · NotApplicable · Undisclosed · Disputed · Pending
BOX C — Reuse: own namespace; map (skos:closeMatch); candidates BFO · PROV-O · OWL-Time · SHACL · OBO RO ·
        legal (LKIF, Akoma Ntoso) · cyber (STIX, ATT&CK, CVSS) · AI incidents (AIID, CSET, MIT) — all unverified
BOX D — Vocabulary layer (2026-11-17) → [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]]
        three layers: ontology (ho:) · profiles (hosh:) · vocabulary (hov: hubs + discipline schemes)
        graded mappings: exact · close · narrow · broad · related; value scales, e.g. [[Integral Altitude Scale]]
```

> [!note] Revision 2026-11-17
> Applied decisions from [[Decisions_Log]] (2026-11-17): Perspective as abstract umbrella over PerspectiveType and PerspectiveSpecification; default and applied evaluative standards; CausalCandidate; CausalAssembly renamed FactorAssembly (thin container); Attribution merged into CausalAssessment; vocabulary layer (Box D). The 2026-11-15 structure is in the note's git history.

> [!note] Revision 2026-11-18
> Applied decision from [[Decisions_Log]] (2026-11-18): Patient renamed **AffectedEntity** (altLabels "patient", "moral patient"); `patientStanding` → `affectedStanding`; `forPatient` → `forAffectedEntity`; `moralCircle` and `affects` now point to AffectedEntity. Subtype names unchanged. The rename in other notes and the v1 `.ttl` is deferred to migration.

> [!warning] Proposed 2026-11-18, untested
> **Assessment everywhere:** the attributes still asserted on Factor, CausalRole, Effect and AffectedEntity above would move into assessments, extending the FactorAssembly thin container. "Fact" becomes a status (settled Observation), not a kind; `assessmentBasis: Stated | Inherited | Unstandardized` (formerly `standardBasis`; test-only, see HO-002.a); CausalRole may fold into CausalAssessment; shortcuts always carry `Settled | Disputed | NotAssessed`. The tree above is **not yet changed** for this. Test plan: [[HO-002.a Assessment-Everywhere Test Strategy]]. Decided on 2026-11-18: AffectedEntity (then Patient) types inclusive, standing assessed ([[Decisions_Log]]).

## Open and pending (summary)
- **Pending, deliberately not logged:**
  - splitting Assessment into Causal / Valence / Responsibility
  - causal standards
  - reifying `participatesIn` as a claim
  - "sufficient as assessed" (all → [[HO-005 Assessed Membership and Systematic Omission]])
- **Open:**
  - the Condition split
  - role types and causal share
  - Agent and AI systems
  - future generations, AI systems and relationships as affected entities
  - Assent/Judgment as an object of harm
  - worldviews as standards
  - consent
  - the legal layer
  - the evidence anchor against the regress

## Summary
- This note puts in one place the structure that was otherwise spread across the Decisions Log and the HO notes, so that it survives the end of the session.

## Original wording
> "we have created the structure for a new ontology this  would be version 3 I don't believe that we have produced a copy of it yet in any format. is that true.
> so if we restarted wouldnt this work actually be lost?"
- **Attribution:** Author
- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-15 (`copilot/copilot-conversations/agent__philosopher_adverse_stress_test_harm_ontology@20261114_071639.md`).
