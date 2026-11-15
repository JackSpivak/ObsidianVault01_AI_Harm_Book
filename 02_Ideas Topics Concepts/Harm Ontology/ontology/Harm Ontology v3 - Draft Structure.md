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
HARM ONTOLOGY v3 (draft, 2026-11-15)
│
├── Factor ......................................... neutral; one contributor among many  → HO-I.a
│   ├── Act · Process · Omission · Structure · Risk
│   └── Condition (?) → PhysicalState (?) · Status (?) · Disposition (?)
│   props: causes → Factor|Effect · isContinuous · observability (box A) · hasAgent → Agent (?)
│          participatesIn → CausalAssembly (inverse hasMember)                          → HO-003
│
├── CausalRole ..................................... part a factor plays in one chain     → HO-I.a
│   roleType: Trigger · Enabler · Amplifier · Conduit · ProximateCause · DistalCause · ContributingCause (?)
│   props: borneBy → Factor|Effect · contributesTo → Effect · causalNecessity · proximity ·
│          causalShare (?) · isDistributed · isForeseeable · answerableAgent (?) · withinAssembly (?)
│
├── CausalAssembly ................................. factors jointly sufficient (as assessed — pending) → HO-003
│   props: hasMember → Factor · hasUnknownMembers (box B) · individuallyInnocuous ·
│          origin: Emergent | Exploited | Engineered · orchestrator → Agent (?) · sufficientFor → Effect|Outcome
│
├── Attribution .................................... factors a perspective calls "the cause" (bounded selection) → HO-004
│
├── Effect ......................................... neutral; one consequence among many  → HO-I.b
│   kinds: SleepLoss · ReputationalDamage · Deskilling · CapturedAssent (?) · Death · …
│   HarmfulEffect — optional, inferred from ≥1 Harmful assessment
│   props: leadsTo → Effect (cascades; open-ended) · affects → Patient · hasObjectOfHarm ·
│          experienceability (box A) · isPosthumous · isStatistical · isDispositional ·
│          severity · reversibility · temporalTrajectory · modality · temporalStatus: Actual|Extrapolated|Pending
│   (Effect and Factor are not disjoint)
│
├── Outcome ........................................ a cut across the ramification at a horizon → Decisions 2026-11-14
│   props: hasEffect → Effect · selectedBy → Perspective (framing, resolution)
│
├── Patient ........................................ SentientIndividual · CollectiveArtificialPerson · NonSentientSystem ·
│                                                    FutureGeneration (?) · AISystem (?) · Relationship (?)
├── ObjectOfHarm (values) .......................... Somatic · PsychologicalCognitive · Assent/Judgment (?) · MaterialPecuniary ·
│                                                    DignitaryRelational · NormativeStatus · OpportunityCapability · SystemicEnvironmental
│
├── EvaluativeStandard (individuals) ............... altLabel "theory of harm"             → HO-II.a
│   ├── Philosophical: ExperientialAccount · ComparativeAccount · NonComparativeAccount · RightsBasedAccount · CapacityAccount
│   ├── Legal: InjuryInFact · ReasonablePerson · LossOfChance · ConcreteHarm · …
│   ├── Causal (pending): ButFor · NESS · INUS · ProbabilityRaising · Mechanistic · Proximate   → HO-005
│   └── Worldview (?)
│
├── Perspective (reusable; all props optional) ..... → HO-II.d
│   ├── Position: standpoint · direction
│   ├── Time: timestamp (assessedAt) · exposure (horizon) · predictabilityHorizon (?)
│   ├── Optics: framing · resolution · sensitivity (threshold)
│   ├── Purpose: intent · standard · fitness · inclusionCriteria · aggregationRule
│   └── Operator: assessor → Agent
│
├── Assessment (one judgment = one instance) ....... → HO-II.a
│   props: assesses → Factor|CausalRole|Effect|Outcome|CausalAssembly · takenFrom → Perspective ·
│          forPatient · chainScope · chainStatus: Actual|Extrapolated ·
│          verdict: Harmful|Beneficial|Mixed|Neutral|Contested · verdictStatus: Provisional|Final (+ closedBy) ·
│          declaredScope · acknowledgedExclusions · scopeAdequacy (never Complete) ·
│          sensitivity/leverage · criticality (as assessed) · confidence · suppliedBy
│   kinds (pending split): CausalAssessment · ValenceAssessment · ResponsibilityAssessment   → HO-005
│   profiles: Personal · Moral · Expert · Regulatory · Threat · Algorithmic ·
│             Judgment (+ authority · jurisdiction · bindingForce · procedure · ratio ·
│             cites/distinguishes/overrules · remedyOrdered · finality)                       → HO-II.c
│
├── Divergence ..................................... → HO-III.a
│   props: between → Assessment (2+) · divergesOn → Perspective property ·
│          divergenceType: Perspectival | Normative | Evidential | Factual ·
│          (pattern) FactorLevel vs AssemblyLevel · reconcilable
├── Integration (optional) ......................... integrates · resolves/leavesOpen · keptInFrame/leftOut
│
├── Agent (?) ...................................... UnitaryIntentionalAgent · CollectiveAgent · AutonomousSystem (?)
│   beneficiaryRole (from v2): Perpetrator | PrincipalInstitutional | DownstreamMarket | None
│
└── LegalResponse (later) .......................... CauseOfAction · Doctrine · Remedy

BOX A — Phenomenality (property): Phenomenal | NonPhenomenal | ConditionallyPhenomenal
        observability (+ observableBy · revealedBy · hiddenFrom) · experienceability (patient-relative)
BOX B — Missingness: (absent)=not considered · Unknown · NotApplicable · Undisclosed · Disputed · Pending
BOX C — Reuse: own namespace; map (skos:closeMatch); candidates BFO · PROV-O · OWL-Time · SHACL · OBO RO ·
        legal (LKIF, Akoma Ntoso) · cyber (STIX, ATT&CK, CVSS) · AI incidents (AIID, CSET, MIT) — all unverified
```

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
  - future generations, AI systems and relationships as patients
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
