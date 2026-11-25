# Proposed Class Tree and DUL Alignment

Status: **Proposed.** Each class carries a definition (`skos:definition` or `rdfs:comment`) and a description (`skos:scopeNote`). The DUL links are IRI references only, permitted for testing by [[Decisions_Log]] (2026-11-25). Nothing is imported or copied from DUL. Index: [[_Harm Ontology v0.03.1 Master Index]]. Licence: ledger T1.

Provisional markers: **(P)** = the DUL definition still needs checking against the published file.

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
    ├── Description (dul:Description)
    │   ├── SituationDescription (satisfied by CausalChain)
    │   ├── PerspectiveType (frame and standard)
    │   └── MechanismModel (held by an Agent)
    ├── Norm (dul:Norm) (P)
    ├── InformationObject (dul:InformationObject)
    │   ├── Determination (expresses a Description)
    │   └── Record, report, testimony
    └── Assessment (act of judging; dul:Action with an agent)
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

**PerspectiveType** (dul:Description)
- Definition: a frame of standards, scope and defaults, used to make assessments.
- Description: a Description, not an Agent. Perspectives are held and used by agents.

**MechanismModel** (dul:Description, conceptualised by an Agent)
- Definition: a Description of how a mechanism works, held by an agent.
- Description: a person-held model can be wrong in a specific, traceable way. The conceptualisation link (dul:conceptualizes) records who holds it.

**Determination** (dul:InformationObject that expresses a Description)
- Definition: the output of an Assessment: a versioned InformationObject that expresses a Description.
- Description: determinations persist and can be relied on later. They are inputs to Acts, never causes in themselves.

**Assessment** (dul:Action with an agent)
- Definition: the act of judging, made by an agent from a perspective under a standard.
- Description: distinct from its determination. The act/output rule applies.

**Norm** (dul:Norm) (P)
- Definition: a social object that prescribes or permits conduct.
- Description: legal personhood, regulatory mandates and corporate charters are expressed as Norms, and their application is a determination.

## Rules to carry with the tree

1. Kinds are classes, roles are roles. Test: can the entity stop being this kind without ceasing to exist? If yes, it is a role.
2. Named bodies are instances, kinds are classes. OSHA is an instance of RegulatoryInstitution, not a subclass.
3. Legal status is a determination. Legal personhood and regulatory authority are recorded with jurisdiction and norm.
4. No agent, no act. An event with no identified agent stays an Event with a missingness status.
5. Valence stays out of the schema. Harm and harmfulness appear only in determinations.

## Open items

- State: Quality or Situation (decision needed).
- ExposureSituation: physical situations as social objects (tension with DUL).
- Verify (P) classes against the published file: Corporation, Institution, RegulatoryInstitution, Norm, Organization.
- Confirm the DUL version before alignment is final (the mirror read is 3.22; other hosts report later versions).
- Licence: IRI reference only until T1 is closed.
