# Proposed Class Tree and DUL Alignment

Status: **Proposed.** Revised 2026-11-26 to the working picture: harm categories are individuals held by perspectives, not classes; a perspective is a first-class object whose holders are optional relations; catalogs are concept schemes; claims are separate from curation. Each class carries a definition (`skos:definition` or `rdfs:comment`) and a description (`skos:scopeNote`). The DUL links are IRI references only, permitted for testing by [[Decisions_Log]] (2026-11-25). Nothing is imported or copied from DUL. Index: [[_Harm Ontology v0.03.1 Master Index]]. Licence: ledger T1. Decisions behind this revision: [[Decisions_Log]] (2026-11-17 PerspectiveType entry, revised; 2026-11-22 entry, reopened). Discipline and tradition are out of scope for now (ledger S21).

Provisional markers: **(P)** = the DUL definition still needs checking against the published file. **(Proposed)** = not yet logged.

## Tree

```text
ENTITY (dul:Entity)
│
├── OBJECT (dul:Object)
│   ├── Agent (dul:Agent)
│   │   ├── PhysicalAgent (dul:PhysicalAgent)
│   │   └── SocialAgent (dul:SocialAgent)
│   │       ├── Corporation (subclass, kind)                     (P)
│   │       │   └── instances: Boeing, Shell, ...
│   │       └── Institution (subclass, kind)                     (P)
│   │           └── RegulatoryInstitution (subclass, kind)       (P)
│   │               └── instances: FAA, NRC, OSHA, ...
│   ├── AffectedEntity (object side: an Object with the capacity to bear effects;
│   │     affectability is a property; kinds are Person, Organism, PhysicalArtifact, Place ...)
│   │     may also be an Agent (self-regarding harm)
│   └── Source (physical) (dul:Object)
│
├── EVENT (dul:Event)
│   ├── Act (agentive) (dul:Action)
│   │     requires an agent participant and an executed task
│   ├── Process (dul:Process)
│   ├── Effect (a change) (dul:Event)
│   └── Omission (OUR CLASS; no DUL home)
│
├── QUALITY (dul:Quality)
│   ├── State (OPEN: dul:Quality with a TimeInterval region, or a Situation)
│   └── Capability (dul:Quality, wrapped in an assessment)
│
├── SITUATION (dul:Situation)
│   ├── CausalChain (thin container) (dul:Situation)
│   └── ExposureSituation (PROPOSED; tension with DUL's social-object placement)
│
├── REGION (dul:Region)
│   └── TimeInterval (dul:TimeInterval)
│
├── ABSTRACT (dul:Abstract)
│   └── Divergence, Missingness, Valence (OUR CLASSES; deliberately not in DUL)
│
├── ROLE (dul:Role; a Concept)
│   ├── Regulator (role, not a kind of agent)
│   ├── Control role: barrier, safeguard, restraint, feedback
│   ├── ImpactedRole (role: classifies an AffectedEntity, scoped to a consequence;
│   │     impact is known only relative to a consequence, hence the name)
│   └── Source, Trigger, Predisposition (causal roles, scoped to a consequence)
│
└── SOCIAL OBJECTS (dul:SocialObject)
    ├── Concept (dul:Concept)
    │   └── PerspectiveHarmCategory (Proposed; class of harm categories held by a perspective;
    │         instances are named individuals, see the categories table below; not harm classes)
    ├── Description (dul:Description)
    │   ├── SituationDescription (satisfied by CausalChain)
    │   ├── PerspectiveType (frame and standard; a first-class object whatever holds it)
    │   │   └── PerspectiveSpecification (the snapshot used in one assessment;
    │   │         holders and use attach here, with dates)
    │   └── MechanismModel (held by an Agent)
    ├── Collection (dul:Collection) (P)
    │   └── Council (Proposed; a collection of founders or key thinkers whose views
    │         define a version of a perspective; declares its kind and scope)
    ├── Norm (dul:Norm) (P)
    ├── InformationObject (dul:InformationObject)
    │   ├── Determination (expresses a Description)
    │   │   ├── HarmDetermination (a bearer's harm; declares bearer, judged state, horizon)
    │   │   │   ├── SubstrateHarm (somatic, psychological, pecuniary, normative status)
    │   │   │   └── FunctionalHarmDetermination (impairment of an assigned function)
    │   │   └── ClassificationClaim (Proposed; claims that a PerspectiveHarmCategory
    │   │         applies to a HarmDetermination; carries assessor, perspective, horizon, basis)
    │   └── Record, report, testimony
    └── Assessment (act of judging; dul:Action with an agent)

Not in the tree (out of scope for now, ledger S21):
- Discipline and tradition as classes. Their holder relations are recorded only as optional
  relations on a perspective (see Relations below).

Not a DUL class (SKOS, vocabulary layer):
- Catalog: a skos:ConceptScheme, one per source perspective (see Catalogs below).
```

## Definitions and descriptions

**Agent** (dul:Agent)
- Definition: an agentive Object, either physical or social.
- Description: agency is classified as a status of an entity. Where agency is contested (autonomous systems, algorithms), the classification is an assessed claim with an assessor and a basis.

**SocialAgent** (dul:SocialAgent)
- Definition: an individual whose existence comes from its social communicability and capacity to act, acting through at least one PhysicalAgent.
- Description: a SocialAgent with no identifiable PhysicalAgent through which it acts has a missingness status on its acting relation. The agent is not dropped.

**Corporation** (subclass of SocialAgent) (P)
- Definition: a SocialAgent established as a corporate body, under a corporate-law statute.
- Description: a kind, fixed by incorporation. Dissolution ends the entity; a change of purpose does not change its kind. Legal personhood as a determination (with jurisdiction and norm) is recorded separately.

**Institution** (subclass of SocialAgent) (P)
- Definition: a SocialAgent constituted by norms and practices that persist beyond its members.
- Description: a broad kind used to group regulatory, educational and other institutions.

**RegulatoryInstitution** (subclass of Institution) (P)
- Definition: an institution established by charter or statute to regulate a domain.
- Description: a kind, fixed by its founding instrument. Membership is recorded with its source and jurisdiction. The class does not say what the institution does in any given situation; that is the Regulator role.

**Regulator** (role, dul:Role)
- Definition: a Concept that classifies an agent in a Situation as exercising regulatory authority.
- Description: a role, not a kind. Any agent can hold it, including a RegulatoryInstitution, a professional body, a self-regulating association or a court. Assignment is time-indexed, scoped to a jurisdiction, and grounded in a Norm.

**Act** (dul:Action)
- Definition: an Event with at least one agent participant that executes a task.
- Description: an act with no agent is an Event, not an Act. Where the agent is unknown, the event stays an Event with a missingness status, and is not forced into an Act.

**Process** (dul:Process), **Effect** (dul:Event)
- Definition: a Process is continuous and agentless; an Effect is a change in an entity, recorded neutrally.
- Description: neither carries valence. Valence belongs to determinations.

**Omission** (our class; no DUL home)
- Definition: the absence of an expected act or event, relative to a stated expectation.
- Description: an absence is not an Event or Object. The expectation that makes it an omission is itself a Description, so omissions are assessed.

**State** (open) (P)
- Definition: a time-indexed condition of an entity.
- Description: DUL has no State class. Choose between a Quality with a TimeInterval region, or a Situation. Decision pending.

**Capability** (dul:Quality, wrapped in an assessment)
- Definition: a Quality of a source that enables it to produce an effect of a kind.
- Description: the Quality is neutral; the assessment of it carries the basis and standard. Harmfulness is a separate, later assessment.

**CausalChain** (dul:Situation)
- Definition: a Situation that satisfies a SituationDescription, selecting entities and links.
- Description: a thin container. Membership, boundary and horizon come from the description and from assessments, not from the container. DUL classes Situation as a social object, which we accept for chains.

**ExposureSituation** (proposed; dul:Situation)
- Definition: a Situation describing an entity's exposure to a hazard.
- Description: a physical exposure is a social object under DUL. This is a tension to resolve before adoption.

**SituationDescription** (dul:Description)
- Definition: a Description that a Situation can satisfy, stating the condition for membership.
- Description: the content of a ChainDetermination. Many situations can satisfy one description, and one situation can satisfy several, one per perspective.

**PerspectiveHarmCategory** (Proposed; dul:Concept, SKOS narrative)
- Definition: a concept that a perspective uses to describe harm: a category of harm as conceptualised by that perspective.
- Description: a category is held by a perspective, not a property of harm. Its instances are curated from a source entry, with provenance. Being an instance is a fact about the catalogue, not a claim that any case falls under the category. Applying a category to a case is a ClassificationClaim. The name says that a perspective can hold categories of many kinds.

**PerspectiveType** (dul:Description)
- Definition: a frame of standards, scope and defaults, used to make assessments.
- Description: a first-class Description. It exists whether or not any agent, discipline, tradition, profession, institution, culture or other holder holds it. Holders are optional relations on it (see Relations).

**PerspectiveSpecification** (dul:Description)
- Definition: the snapshot of a PerspectiveType used in one assessment.
- Description: holders and use attach here, with dates, because they are facts about a particular use.

**Council** (Proposed; dul:Collection) (P)
- Definition: a collection of founders or key thinkers whose views define a version of a perspective.
- Description: a council is a version-defining set. Different councils for one perspective give different versions (for example classical and revisionist readings of Freud). Each council declares its kind (tradition, discipline, method, institution, value, voice) and its scope (what it can see, what it cannot). Overlapping councils are mapped, not merged.

**MechanismModel** (dul:Description, conceptualised by an Agent)
- Definition: a Description of how a mechanism works, held by an agent.
- Description: a person-held model can be wrong in a specific, traceable way. The conceptualisation link (dul:conceptualizes) records who holds it.

**Determination** (dul:InformationObject that expresses a Description)
- Definition: the output of an Assessment: a versioned InformationObject that expresses a Description.
- Description: determinations persist and can be relied on later. They are inputs to Acts, never causes in themselves.

**HarmDetermination**
- Definition: a determination that a bearer is harmed in a judged state, from an assessment.
- Description: declares `hasBearer` (Entity), `judgesState`, `atHorizon`, with `assessedBy`, `perspective` and `standard`. Harm attaches to a state of the bearer, not to the bearer as such.

**ClassificationClaim** (Proposed; dul:InformationObject)
- Definition: a claim that a PerspectiveHarmCategory applies to a HarmDetermination, made by an assessor using a perspective.
- Description: carries `assessedBy`, `usedPerspective` and `citesBasis` (citations that support the claim), and `atHorizon`. Names are provisional: `hasClassificationClaim` on the determination, `claimsCategory` from the claim to the category. A perspective uses a frame; it does not make the claim. The assessor does.

**Assessment** (dul:Action with an agent)
- Definition: the act of judging, made by an agent from a perspective under a standard.
- Description: distinct from its determination. The act/output rule applies.

**Norm** (dul:Norm) (P)
- Definition: a social object that prescribes or permits conduct.
- Description: legal personhood, regulatory mandates and corporate charters are expressed as Norms, and their application is a determination.

## Catalogs

A catalog is a `skos:ConceptScheme`, one per source perspective. It is a vocabulary-layer object, not a DUL class.

- Each category is `skos:inScheme` of the catalog it comes from.
- Hierarchy among categories is recorded with `skos:broader` within a catalog. It is not `rdfs:subClassOf`, and the reasoner does not follow it.
- Shared ideas across catalogs are hubs, with categories as spokes mapped by `skos:closeMatch`, `skos:narrowMatch`, `skos:broadMatch` or `skos:relatedMatch`, each with a one-line reason (the hub-and-spoke pattern, HO-II.d.3).
- Listing, counting and cross-catalog comparison are SPARQL queries, not reasoner results.

**Working catalog for the v1 import:** a single catalog, `ex:V1HarmCatalog`, holds all 31 categories below. Its source perspective is not recorded in the v1 file, so the catalog is split into per-source catalogs once that is decided. Until then the import makes no claim about which perspective each category belongs to.

## Relations (working picture)

- `originatedBy`: founder or originator to a perspective.
- `heldBy`, `transmittedBy`, `usedBy`: holders and users of a perspective, each optional, repeatable and time-indexed. Holder kinds are not yet settled (ledger S15, S22).
- `usesCategory` (or `hasCategory`): a perspective to the categories it uses. Several perspectives may use one category.
- `hasClassificationClaim`, `claimsCategory`, `assessedBy`, `usedPerspective`, `citesBasis`, `atHorizon`: the claim pattern above.
- `hasBearer`, `judgesState`, `atHorizon`, `assessedBy`, `perspective`, `standard`: on HarmDetermination (already logged 2026-11-25).

## Imported harm categories (v1)

Each v1 harm class becomes one individual of `PerspectiveHarmCategory`, in the working `ex:V1HarmCatalog`. The name is the v1 local name plus "Category". The v1 `rdfs:subClassOf` links are dropped, and the v1 `skos:broader` links are kept as the hierarchy within the catalog. Definitions, scope notes, examples, history notes and citations are carried over unchanged, as SKOS annotations, with provenance back to the v1 IRI. The v1 root `harm:Harm` becomes the root category `ex:HarmCategory`, which has no broader category.

| v1 class | Individual | Broader (within catalog) |
|---|---|---|
| harm:Harm (root) | ex:HarmCategory | none |
| ExperientialHarm | ex:ExperientialCategory | HarmCategory |
| HedonicHarm | ex:HedonicCategory | ExperientialCategory |
| DignitaryRelationalHarm | ex:DignitaryRelationalCategory | ExperientialCategory |
| PsychologicalEmotionalTrauma | ex:PsychologicalEmotionalTraumaCategory | ExperientialCategory |
| NuisanceSensoryOffense | ex:NuisanceSensoryOffenseCategory | ExperientialCategory |
| VicariousMoralInjury | ex:VicariousMoralInjuryCategory | ExperientialCategory |
| WelfareInterestHarm | ex:WelfareInterestCategory | HarmCategory |
| InterestSetbackHarm | ex:InterestSetbackCategory | WelfareInterestCategory |
| PublicCriminalHarm | ex:PublicCriminalCategory | WelfareInterestCategory |
| PrivateTortiousHarm | ex:PrivateTortiousCategory | WelfareInterestCategory |
| ExpectationRelianceHarm | ex:ExpectationRelianceCategory | WelfareInterestCategory |
| ProbabilisticRiskHarm | ex:ProbabilisticRiskCategory | WelfareInterestCategory |
| CollectiveEnvironmentalHarm | ex:CollectiveEnvironmentalCategory | WelfareInterestCategory |
| OpportunityCostChoiceHarm | ex:OpportunityCostChoiceCategory | WelfareInterestCategory |
| DeontologicalRightsHarm | ex:DeontologicalRightsCategory | HarmCategory |
| KantianDeontologicalHarm | ex:KantianDeontologicalCategory | DeontologicalRightsCategory |
| InjuriaSineDamnoHarm | ex:InjuriaSineDamnoCategory | DeontologicalRightsCategory |
| EpistemicTestimonialHarm | ex:EpistemicTestimonialCategory | DeontologicalRightsCategory |
| FiduciaryBetrayalHarm | ex:FiduciaryBetrayalCategory | DeontologicalRightsCategory |
| TeleologicalDeprivationHarm | ex:TeleologicalDeprivationCategory | HarmCategory |
| PerfectionistTeleologicalHarm | ex:PerfectionistTeleologicalCategory | TeleologicalDeprivationCategory |
| DeprivationHarm | ex:DeprivationCategory | TeleologicalDeprivationCategory |
| CapabilityStructuralHarm | ex:CapabilityStructuralCategory | TeleologicalDeprivationCategory |
| WrongfulDeathConsortiumHarm | ex:WrongfulDeathConsortiumCategory | TeleologicalDeprivationCategory |
| ParensPatriaePaternalisticHarm | ex:ParensPatriaePaternalisticCategory | TeleologicalDeprivationCategory |
| AttachmentDevelopmentalHarm | ex:AttachmentDevelopmentalCategory | TeleologicalDeprivationCategory |
| SystemicCyberneticHarm | ex:SystemicCyberneticCategory | HarmCategory |
| ExternalityCoordinationHarm | ex:ExternalityCoordinationCategory | SystemicCyberneticCategory |
| InformationAsymmetryHarm | ex:InformationAsymmetryCategory | SystemicCyberneticCategory |
| AlgorithmicAlignmentHarm | ex:AlgorithmicAlignmentCategory | SystemicCyberneticCategory |
| EpistemicPollutionHarm | ex:EpistemicPollutionCategory | SystemicCyberneticCategory |

## Catalog view: membership and hierarchy (shown separately)

Part 1 is membership: every item is an individual of `PerspectiveHarmCategory`, with no subclassing. Part 2 is the `skos:broader` hierarchy within `ex:V1HarmCatalog`. Part 2 is a relation between individuals, not a class tree; it is shown as a tree for reading only.

Part 1, membership (32 individuals, all in `ex:V1HarmCatalog`):

```text
PerspectiveHarmCategory (class)
  members:
    HarmCategory (root)
    ExperientialCategory, HedonicCategory, DignitaryRelationalCategory,
    PsychologicalEmotionalTraumaCategory, NuisanceSensoryOffenseCategory,
    VicariousMoralInjuryCategory
    WelfareInterestCategory, InterestSetbackCategory, PublicCriminalCategory,
    PrivateTortiousCategory, ExpectationRelianceCategory, ProbabilisticRiskCategory,
    CollectiveEnvironmentalCategory, OpportunityCostChoiceCategory
    DeontologicalRightsCategory, KantianDeontologicalCategory,
    InjuriaSineDamnoCategory, EpistemicTestimonialCategory, FiduciaryBetrayalCategory
    TeleologicalDeprivationCategory, PerfectionistTeleologicalCategory,
    DeprivationCategory, CapabilityStructuralCategory, WrongfulDeathConsortiumCategory,
    ParensPatriaePaternalisticCategory, AttachmentDevelopmentalCategory
    SystemicCyberneticCategory, ExternalityCoordinationCategory,
    InformationAsymmetryCategory, AlgorithmicAlignmentCategory, EpistemicPollutionCategory
```

Part 2, `skos:broader` within the catalog (a reading aid, not a class tree):

```text
HarmCategory                                  (root, no broader)
├─ ExperientialCategory
│   ├─ HedonicCategory
│   ├─ DignitaryRelationalCategory
│   ├─ PsychologicalEmotionalTraumaCategory
│   ├─ NuisanceSensoryOffenseCategory
│   └─ VicariousMoralInjuryCategory
├─ WelfareInterestCategory
│   ├─ InterestSetbackCategory
│   ├─ PublicCriminalCategory
│   ├─ PrivateTortiousCategory
│   ├─ ExpectationRelianceCategory
│   ├─ ProbabilisticRiskCategory
│   ├─ CollectiveEnvironmentalCategory
│   └─ OpportunityCostChoiceCategory
├─ DeontologicalRightsCategory
│   ├─ KantianDeontologicalCategory
│   ├─ InjuriaSineDamnoCategory
│   ├─ EpistemicTestimonialCategory
│   └─ FiduciaryBetrayalCategory
├─ TeleologicalDeprivationCategory
│   ├─ PerfectionistTeleologicalCategory
│   ├─ DeprivationCategory
│   ├─ CapabilityStructuralCategory
│   ├─ WrongfulDeathConsortiumCategory
│   ├─ ParensPatriaePaternalisticCategory
│   └─ AttachmentDevelopmentalCategory
└─ SystemicCyberneticCategory
    ├─ ExternalityCoordinationCategory
    ├─ InformationAsymmetryCategory
    ├─ AlgorithmicAlignmentCategory
    └─ EpistemicPollutionCategory
```

Counts: 31 categories under the root, plus the root itself. The v1 value classes (`ComparativeBaselineValue`, `CausationMechanismValue`, `PhenomenologicalTransparencyValue`, `SystemOpacityValue`, `TemporalTrajectoryValue`, `DistributionAggregationValue`) are vocabularies of values, not harm categories. They are not imported here and need their own decision.

Example (three exemplars, in Turtle):

```turtle
@prefix ex: <http://example.org/harm#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

ex:V1HarmCatalog a skos:ConceptScheme, owl:NamedIndividual ;
    skos:prefLabel "v1 harm categories (source perspective not yet recorded)"@en .

ex:HedonicCategory a ex:PerspectiveHarmCategory, owl:NamedIndividual ;
    skos:inScheme ex:V1HarmCatalog ;
    skos:prefLabel "Experiential Harm (Hedonic / Phenomenological Harm)"@en ;
    skos:definition "An action harms a subject if and only if it causes negative mental states—such as physical pain, emotional distress, anguish, or grief—or deprives the subject of positive states like pleasure and contentment."@en ;
    skos:scopeNote "Applies strictly to conscious mental states; excludes unperceived betrayals, posthumous events, or painless death."@en ;
    skos:broader ex:ExperientialCategory ;
    dcterms:bibliographicCitation "Bentham, Jeremy. An Introduction to the Principles of Morals and Legislation (1789)."@en .

ex:InterestSetbackCategory a ex:PerspectiveHarmCategory, owl:NamedIndividual ;
    skos:inScheme ex:V1HarmCatalog ;
    skos:prefLabel "Interest-Based Harm (The Counterfactual Comparative Account)"@en ;
    skos:definition "Harm occurs when an action sets back a person's vital, ongoing stakes in their well-being (such as health, property, privacy, or liberty), leaving them worse off than they otherwise would have been."@en ;
    skos:scopeNote "Requires a setback to vital ongoing welfare interests relative to a counterfactual baseline; excludes mere emotional offense."@en ;
    skos:broader ex:WelfareInterestCategory ;
    dcterms:bibliographicCitation "Mill, John Stuart. On Liberty (1859)."@en , "Feinberg, Joel. Harm to Others (1984)."@en .

ex:DeprivationCategory a ex:PerspectiveHarmCategory, owl:NamedIndividual ;
    skos:inScheme ex:V1HarmCatalog ;
    skos:prefLabel "Harm by Deprivation (Comparative Non-Existence / Omission)"@en ;
    skos:definition "Blocking access to a good state a subject would otherwise have enjoyed—most notably death, which harms a person by depriving them of future experiences and projects."@en ;
    skos:scopeNote "Measured counterfactually by comparing actual non-existence or omission against the future goods the subject would otherwise have experienced."@en ;
    skos:broader ex:TeleologicalDeprivationCategory ;
    dcterms:bibliographicCitation "Nagel, Thomas. 'Death,' Noûs (1970)."@en .
```

The other 28 follow the same pattern. The broader targets must exist as individuals too, so the parent categories are created with the same pattern.

## Rules to carry with the tree

1. Kinds are classes, roles are roles. Test: can the entity stop being this kind without ceasing to exist? If yes, it is a role.
2. Named bodies are instances, kinds are classes. OSHA is an instance of RegulatoryInstitution, not a subclass.
3. Legal status is a determination. Legal personhood and regulatory authority are recorded with jurisdiction and norm.
4. No agent, no act. An event with no identified agent stays an Event with a missingness status.
5. Valence stays out of the schema. Harm and harmfulness appear only in determinations.
6. Harm categories are individuals, not classes. A category is a concept a perspective uses. Membership of a category class is a curation fact; applying a category to a case is a ClassificationClaim.
7. Perspectives are first-class. A PerspectiveType exists whether or not anything holds it. Holders are optional, repeatable, time-indexed relations.
8. Hierarchy among categories is recorded (`skos:broader`) within a catalog, never as subclassing.
9. Partiality is declared. Each catalog and council states what it can see and what it cannot.

## Open items

- State: Quality or Situation (decision needed).
- ExposureSituation: physical situations as social objects (tension with DUL).
- Verify (P) classes against the published file: Corporation, Institution, RegulatoryInstitution, Norm, Organization, Collection.
- Confirm the DUL version before alignment is final (the mirror read is 3.22; other hosts report later versions).
- Source perspective for each v1 category (V1HarmCatalog is a placeholder until decided). Ledger V2 and O10: whether catalogs are keyed to perspectives.
- Holder kinds for `heldBy`, `transmittedBy`, `usedBy` (ledger S15, S22).
- Scope of disciplines and traditions as things in the model (ledger S21). Not in the tree until decided.
- Names of the claim properties (`hasClassificationClaim`, `claimsCategory`, `usedPerspective`, `citesBasis`): provisional.
- The v1 value classes (`ComparativeBaselineValue` and the other five): where they go.
- Metaperspective: whether the model is an instance of its own perspective type (ledger S32).
- Licence: IRI reference only until T1 is closed.
