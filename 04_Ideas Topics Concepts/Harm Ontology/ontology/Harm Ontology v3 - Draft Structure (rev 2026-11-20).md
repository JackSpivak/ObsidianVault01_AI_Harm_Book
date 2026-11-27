---
type: outline
status: developing
tags: [ontology/harm]
aliases: [Harm Ontology v3 rev 2026-11-20, v3 Draft Structure rev]
created: 2026-11-15
revised: 2026-11-20
source: "[[Harm Ontology v3 - Draft Structure]]"
---
The **Classical Council** (featuring thinkers like Socrates, Aristotle, Marcus Aurelius, Laozi, Confucius, and Epicurus) offers a distinct competency that sets it apart from the other councils: **examining systems through the lens of character formation, foundational human nature, and the internal harmony of the agent rather than external rules or mechanics.**

While other councils focus on different angles—such as Legal on institutional validity, Physics on detection thresholds, Logic on formal validation, or Ethics on modern normative rules (deontology, utilitarianism)—the Classical Council uniquely brings:

1. **Habituation and Character Formation:** Drawing on Aristotle, it focuses on how repeated actions and structures slowly train a person's underlying dispositions and self-governing capacities (e.g., how gentle dependencies reshape the "chooser" rather than just breaking a rule).
2. **Assent and Internal Sovereignty:** Drawing on Stoics like Marcus Aurelius, it scrutinizes what happens to an agent's faculty of judgment and assent when external systems automate decision-making.
3. **Cosmic and Natural Alignment:** Incorporating Eastern and classical views (Laozi, Confucius), it assesses whether an intervention respects natural proportions, relational harmony, and the proper functioning or excellence (*arete*) of a human life, rather than just optimizing utility or complying with statutes.
# Harm Ontology v3 — Draft Structure (rev 2026-11-20)

Revision of [[Harm Ontology v3 - Draft Structure]] after a line-by-line review on 2026-11-20. It places every decision logged in [[Decisions_Log]] from 2026-11-14 to 2026-11-18, and the 2026-11-19 proposal in [[Handoff - Harm Ontology]], into one tree. The original note is kept unchanged as the 2026-11-17/18 record. Markers:
- **(?)** open question
- **(pending)** proposed but deliberately *not* logged; to be decided after testing
- **(proposed)** raised in a session, not logged

Nothing here is adopted yet. The toy-case test of the "assessment everywhere" variant (B) is partly done; the sourced Horizon test and the non-expert test are still to do. See [[HO-002 Ontology Stress-Test Suite]] and [[HO-002.a Assessment-Everywhere Test Strategy]].

> [!warning] Status
> This is a design draft, not an ontology file. No v3 `.ttl` exists yet. Building one is Phase 1 of [[Harm Ontology Migration Plan]].

## Governing commitments
- Theories of harm **describe and judge**; they don't classify. → [[HO-000 Harm as Perspective-Relative Assessment]]
- **No intrinsic harmfulness**: valence lives only in assessments. → [[HO-premise No Intrinsic Harmfulness]]
- **Deliberately asymmetric in time**: causes converge into a settled past; effects ramify into an open future. The full causal past and full causal future are limit concepts, never instantiated. → [[HO-004 Criticality, Leverage and the Limits of Scope]]
- **Scope is never complete**: `scopeAdequacy` defaults to Unknown and can never be Complete. → HO-004
- **Open world, explicit missingness, domain profiles.** → [[HO-II.e Missingness Statuses and Domain Profiles]]
- **Map, don't import** (reuse expert vocabularies). → [[HO-III.b Reusing Expert Domain Vocabularies]]
- **Three layers** (2026-11-17): ontology (OWL, `ho:`) for structure; profiles (SHACL, `hosh:`) for requiredness; vocabulary (SKOS, `hov:`) for words and meaning. → [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]]
- **Single source of truth** (2026-11-15): the `.ttl` is the source; the readable Compendium is generated from it. → [[Harm Ontology Migration Plan]]

## Structure

```text
HARM ONTOLOGY v3 (draft, 2026-11-15; rev 2026-11-20 incorporating decisions to 2026-11-18)
│
├── CausalCandidate (2026-11-17) ....................... parent of Factor and FactorAssembly; anything a
│                                                        CausalAssessment may select or leave out
│                                                        SHACL: sh:or allows only Factor or FactorAssembly
│
├── Factor ⊑ CausalCandidate ........................... neutral; one contributor among many  → HO-I.a
│   ├── Act · Process · Omission · Structure · Risk
│   └── Condition (?) → PhysicalState (?) · Status (?) · Disposition (?)
│   props: causes → Factor|Effect · isContinuous · observability (box A) · hasAgent → Agent (?)
│          (membership in a FactorAssembly is supplied by assessments, not asserted here)  → HO-003
│
├── CausalRole ...................................... part a factor plays in one chain     → HO-I.a
│   roleType: Trigger · Enabler · Amplifier · Conduit · ProximateCause · DistalCause · ContributingCause (?)
│   props: borneBy → Factor|Effect · contributesTo → Effect · causalNecessity · proximity ·
│          causalShare (?) · isDistributed · isForeseeable · answerableAgent (?) · withinAssembly (?)
│   (may fold into CausalAssessment if assessment-everywhere is adopted; see warning below)
│
├── FactorAssembly ⊑ CausalCandidate ................ (formerly CausalAssembly; altLabel "causal assembly",
│   │                                                    renamed 2026-11-17)                    → HO-003
│   THIN CONTAINER: identifier + label only, the shared referent rival assessments point to,
│   like a case number.
│   Supplied by CausalAssessment, not asserted here: members · hasUnknownMembers · individuallyInnocuous ·
│          origin: Emergent | Exploited | Engineered · orchestrator → Agent (?) · sufficientFor → Effect|Outcome
│   (derived shortcuts allowed where assessments agree; Disputed where they don't)
│
├── Effect .......................................... neutral; one consequence among many  → HO-I.b
│   kinds: SleepLoss · ReputationalDamage · Deskilling · CapturedAssent (?) · Death · …
│   HarmfulEffect — optional, inferred from ≥1 Harmful assessment
│   props: leadsTo → Effect (cascades; open-ended) · affects → AffectedEntity · hasObjectOfHarm ·
│          experienceability (box A) · isPosthumous · isStatistical · isDispositional ·
│          severity · reversibility · temporalTrajectory · modality · temporalStatus: Actual|Extrapolated|Pending
│   proposed 2026-11-18, untested (→ HO-002.a): occurredDuring (time interval; observable core + assessed
│          reading; in the toy test, readings "YYYY-YYYY" are compatible if they overlap, Disputed only if disjoint)
│   (Effect and Factor are not disjoint)
│
├── Outcome ......................................... a cut across the ramification at a horizon → Decisions 2026-11-14
│   props: hasEffect → Effect · selectedBy → PerspectiveSpecification (framing, resolution)
│
├── AffectedEntity (renamed from Patient, 2026-11-18; altLabels "patient", "moral patient")
│   │   types are inclusive; standing is assessed (decided 2026-11-18)
│   ├── Logged subtypes: SentientIndividual · FutureGeneration · AISystem · Relationship
│   ├── Proposed subtypes (untested → HO-002.a): Household · CollectiveNaturalGroup (communities,
│   │      cultures, tribes) · CollectiveArtificialPerson · NonSentientSystem → NaturalSystem | EngineeredSystem
│   │      (the 2026-11-18 log names NaturalSystem and EngineeredSystem; confirm NonSentientSystem)
│   ├── Proposed attributes (untested → HO-002.a): AffectedEntity type as assessed · Unclassified ·
│   │      affectedStanding: Direct|Derivative (test-only: treated as exclusive) ·
│   │      Factor and AffectedEntity not disjoint
│   └── patientStanding → affectedStanding (2026-11-18)
│
├── ObjectOfHarm (values) ........................... Somatic · PsychologicalCognitive · Assent/Judgment (?) ·
│                                                        MaterialPecuniary · DignitaryRelational · NormativeStatus ·
│                                                        OpportunityCapability · SystemicEnvironmental
│
├── EvaluativeStandard (individuals) ................ altLabel "theory of harm" (renamed 2026-11-14) → HO-II.a
│   ├── Philosophical: ExperientialAccount · ComparativeAccount · NonComparativeAccount · RightsBasedAccount · CapacityAccount
│   ├── Legal: InjuryInFact · ReasonablePerson · LossOfChance · ConcreteHarm · …
│   ├── Causal (pending): ButFor · NESS · INUS · ProbabilityRaising · Mechanistic · Proximate   → HO-005
│   └── Worldview (?)
│
├── Perspective (ABSTRACT; no direct members; definition + Explanation only) (2026-11-17)
│   │   disjoint subclasses:
│   │
│   ├── PerspectiveType ............................. prefLabel "tradition" · altLabel "lens"     → [[PerspectiveStructure 0.02]]
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
│       ├── Purpose: intent · appliedEvaluativeStandard (inherits defaultEvaluativeStandard if absent;
│       │            a differing value is a queryable departure, possibly a Divergence) ·
│       │            fitness · inclusionCriteria · aggregationRule
│       └── Operator: assessor → Agent (organizations as assessors: proposed, see HO-007)
│
├── Assessment (one judgment = one instance) ........ → HO-II.a
│   props: assesses → Factor|CausalRole|Effect|Outcome|FactorAssembly|PerspectiveType · takenFrom → PerspectiveSpecification ·
│          forAffectedEntity (renamed from forPatient, 2026-11-18) · chainScope · chainStatus: Actual|Extrapolated ·
│          verdict: Harmful|Beneficial|Mixed|Neutral|Contested · verdictStatus: Provisional|Final (+ closedBy) ·
│          declaredScope · acknowledgedExclusions · scopeAdequacy (never Complete) ·
│          sensitivity/leverage · criticality (as assessed) · confidence · suppliedBy
│   kinds:
│     ├── CausalAssessment (adopted 2026-11-17; absorbs Attribution; the Attribution entries of 2026-11-14 are superseded):
│     │      attributedCause → CausalCandidate · leftOut → CausalCandidate (+ omission assessment) ·
│     │      FactorAssembly members · sufficientFor · origin · orchestrator · individuallyInnocuous
│     │      omission categories (2026-11-17): outOfFrame · blindSpot › negligent | suppressed · acceptedHarm
│     ├── ValenceAssessment · ResponsibilityAssessment (split still pending)             → HO-005
│     └── Profiles: Personal · Moral · Expert · Regulatory · Threat · Algorithmic ·
│              Judgment (+ authority · jurisdiction · bindingForce · procedure · ratio ·
│              cites/distinguishes/overrules · remedyOrdered · finality)                   → HO-II.c
│
├── Divergence ...................................... → HO-III.a
│   props: between → Assessment (2+) · divergesOn → PerspectiveSpecification or PerspectiveType property ·
│          divergenceType: Perspectival | Normative | Evidential | Factual ·
│          (pattern) FactorLevel vs AssemblyLevel · reconcilable
├── Integration (optional) .......................... integrates · resolves/leavesOpen · keptInFrame/leftOut
│
├── Agent (?) ....................................... UnitaryIntentionalAgent · CollectiveAgent · AutonomousSystem (?)
│   │   beneficiaryRole (from v2): Perpetrator | PrincipalInstitutional | DownstreamMarket | None
│   └── (proposed, 2026-11-19, HO-007) Event class; participation of an Agent in an Event that participates
│       in a FactorAssembly; roles in participation; participation is not responsibility
│
└── LegalResponse (later) ........................... CauseOfAction · Doctrine · Remedy

BOX A — Phenomenality (property): Phenomenal | NonPhenomenal | ConditionallyPhenomenal
        observability (+ observableBy · revealedBy · hiddenFrom) · experienceability (relative to the affected entity)
BOX B — Missingness: (absent)=not considered · Unknown · NotApplicable · Undisclosed · Disputed · Pending
BOX C — Reuse: own namespace; map (skos:closeMatch); candidates BFO · PROV-O · OWL-Time · SHACL · OBO RO ·
        legal (LKIF, Akoma Ntoso) · cyber (STIX, ATT&CK, CVSS) · AI incidents (AIID, CSET, MIT) — all unverified
BOX D — Vocabulary layer (2026-11-17) → [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]]
        three layers: ontology (ho:) · profiles (hosh:) · vocabulary (hov: hubs + discipline schemes)
        graded mappings: exact · close · narrow · broad · related; value scales, e.g. [[Integral Altitude Scale]]
```

> [!note] Revision history
> - **2026-11-15:** original draft structure.
> - **2026-11-17:** Perspective umbrella (PerspectiveType and PerspectiveSpecification); default and applied evaluative standards; CausalCandidate; CausalAssembly renamed FactorAssembly (thin container); Attribution merged into CausalAssessment; vocabulary layer (Box D).
> - **2026-11-18:** Patient renamed AffectedEntity; `patientStanding` → `affectedStanding`; `forPatient` → `forAffectedEntity`; patient types inclusive, standing assessed.
> - **2026-11-19:** HO-007 proposal (agents, participation, assessing organizations) added as proposed, not logged.
> - **2026-11-20:** this revision. Places all logged decisions in one tree; see the review below.

> [!warning] Proposed 2026-11-18, untested
> **Assessment everywhere:** the attributes still asserted on Factor, CausalRole, Effect and AffectedEntity above would move into assessments, extending the FactorAssembly thin container. "Fact" becomes a status (settled Observation), not a kind; `assessmentBasis: Stated | Inherited | Unstandardized` (formerly `standardBasis`; test-only, see HO-002.a); CausalRole may fold into CausalAssessment; shortcuts always carry `Settled | Disputed | NotAssessed`. The tree above is **not yet changed** for this. Test plan: [[HO-002.a Assessment-Everywhere Test Strategy]].

> [!note] Toy-case test of variant B, 2026-11-18 (test only; nothing decided)
> Results in [[2026-11-18 Harm Ontology v3 Toy Case Results]]; design in [[HO-002.a Assessment-Everywhere Test Strategy]]. What the test model currently contains, beyond the tree above:
> - **Test-only classes:** Procedure (id, version, `implementsStandard`), Evidence, Observation (an Assessment with a Procedure and Evidence), Claim (script-generated: target + attribute + scope), ScopeDeclaration, Band (Low/Medium/High/Extreme), BandMapping.
> - **Assessment properties added for the test:** `aboutAttribute` (attribute concepts in a separate `hoa:` vocabulary), `value`, `usesProcedure`, `hasEvidence`, `assessedAt`, `assessorOrganisation`, `repeats`, derived `assessmentBasis: Stated | Inherited | Unstandardized`.
> - **Status is derived, never stored:** NotAssessed · SingleSource · Corroborated · PartiallyAssessed · Settled · Disputed · Incommensurable; naive views show Settled / Disputed / Open. Settling is slow (≥2 independent assessments, same Procedure and version, evidence, no silent in-scope perspective); disputing is quick.
> - **Three attribute kinds (added in toy run 2):**
>   1. *Graded* (e.g. severity): compared through shared bands.
>   2. *Non-exclusive* (`cause`, `answerable`): different values are additive, not a conflict (per [[HO-003 Causal Assembly - the Perfect Storm]]). Conflict only if an assessment **denies** a value (`deniesValue`) or claims it is the **sole** one (`soleValue`).
>   3. *Interval* (`occurredDuring`): conflict only if intervals are disjoint; agreed value is the intersection.
>   Everything else is single-valued and mutually exclusive; `Unclassified` is not a competing value.
> - **Passed in the toy runs (58 of 58 checks in run 7; fictional data):** deny and sole-cause (on `cause` and `answerable`) → Disputed; differing causes with neither → Corroborated; interval overlap compatible, disjoint Disputed; subtype/supertype and `Unclassified` not conflicts; independence (`repeats`, same firm) → SingleSource; missing evidence → Corroborated; Settled reached; Incommensurable; `revisedBecause` reported (and a missing trigger flagged); Settled → reopened as Disputed over time; CQ5 pointer check; CQ6 omission on a non-causal attribute; CQ7 cases on made-up stand-ins; CQ8 passes with a wording caveat ("directly affected").
> - **Still untested or unbuilt:** the non-expert subagent test (gates adopting B), SHACL validation, the Horizon (R01) slice, and whether strict settlement leaves almost nothing Settled in real data. CQ7 is still partly met. Test-only choice to revisit: `affectedStanding` treated as exclusive. Variant A was not extended for run 3.

## Open and pending (summary)
- **Pending, deliberately not logged:**
  - splitting Assessment into Causal / Valence / Responsibility (HO-005)
  - causal standards
  - reifying `participatesIn` as a claim
  - "sufficient as assessed" (all → [[HO-005 Assessed Membership and Systematic Omission]])
- **Open:**
  - the Condition split
  - role types and causal share
  - Agent and AI systems
  - **Agents, participation and assessing organizations** (raised 2026-11-19; proposed bookmark HO-007, awaiting author confirmation): an Event class; participation of an Agent in an Event that participates in a FactorAssembly (the robbery case); roles in participation; what counts as an agent (a lion, a storm's flood water and debris, an AI system); organizations as `assessor` (audit firms, testing agencies, regulators). Untested; test cases to be added to HO-002. See [[Handoff - Harm Ontology]]
  - future generations, AI systems and relationships as affected entities (partly decided 2026-11-18; subtype list to confirm)
  - Assent/Judgment as an object of harm
  - worldviews as standards
  - consent
  - the legal layer
  - the evidence anchor against the regress
  - domains, ranges and property groups for the Protégé editor-first build ([[Handoff - Harm Ontology]])
  - narrative placement in the `.ttl` (Migration Plan Phase 3–4)
- **v4 proposed (not decided):** a thin Chain class bounded by a horizon, which `CausalRole` would point to. See [[HO-006 Causal Chain - an Assessed Selection with a Horizon]].
- **Open from toy runs (2026-11-18):**
  - whether the strict settlement rule leaves almost nothing Settled in real cases
  - the non-expert test (script-generated snapshots must not fail silently), which gates adopting variant B
  - sourced Horizon research (R01)

## Review of the 2026-11-15 draft (2026-11-20)
Corrections made in this revision:
1. **Stale header and dates.** The original header said "draft, 2026-11-15; revised 2026-11-17 and 2026-11-18" and listed only Decisions 2026-11-14 and 2026-11-15 as sources. Now covers 2026-11-14 to 2026-11-19.
2. **Broken tree connector.** In the original, the AffectedEntity block and its proposed lines sat outside the tree, so the subtypes and the Patient-to-AffectedEntity rename were hard to follow. Now restructured with its own branches.
3. **Missing omission categories.** The 2026-11-17 decision on `leftOut` omission assessments (outOfFrame · blindSpot › negligent | suppressed · acceptedHarm) was absent. Added under CausalAssessment.
4. **Missing SHACL rule.** The `sh:or` constraint on CausalCandidate (2026-11-17) was absent. Added.
5. **Attribution cross-reference.** The original linked the merged Attribution to HO-004 only. The 2026-11-17 decision cites HO-004 and HO-005; now noted as superseding the 2026-11-14 Attribution entry.
6. **Patient-to-AffectedEntity subtypes.** The 2026-11-18 log lists NaturalSystem and EngineeredSystem as subtype names, but the original draft lists NonSentientSystem. Kept as proposed and flagged for confirmation; the logged subtype names need to be checked against [[Decisions_Log]].
7. **Organizations as assessors.** The `assessor → Agent` property now notes that organizational assessors are proposed under HO-007, not logged.
8. **Ambiguous "Condition" entry.** Unchanged; still open.
9. **Toy-run results.** Updated to the run 7 count (58 of 58), with CQ5 and CQ8 passing and CQ7 still partly met, replacing the 42-of-42 count from the original.
10. **Outstanding.** No edits were made to the original note, to [[Decisions_Log]], or to other notes. The rename across other notes and the v1 `.ttl` is still deferred to migration.

## Summary
- This note puts in one place the structure that was otherwise spread across the Decisions Log and the HO notes, so that it survives the end of the session. This revision brings the structure up to the decisions of 2026-11-17 and 2026-11-18, and records the review of the original draft.

## Original wording
> "we have created the structure for a new ontology this  would be version 3 I don't believe that we have produced a copy of it yet in any format. is that true.
> so if we restarted wouldnt this work actually be lost?"
- **Attribution:** Author
- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-15 (`copilot/copilot-conversations/agent__philosopher_adverse_stress_test_harm_ontology@20261114_071639.md`).
