---
epoch: 1795357696068
mode: agent
backendId: opencode
sessionId: "ses_dfc5ae101ffeAFfkQ6sFGJfTrY"
model: '{"baseModelId":"anthropic/claude-sonnet-5-5","effort":"low"}'
tags:
  - copilot-conversation
topic: "Harm ontology harm types catalog"
usage: '{"usedTokens":29053,"contextWindow":1000000,"updatedAt":1795357841991}'
---

**user**: from the current snapshot only of the harm ontology, please list types of harm that might be discovered in an assessment of harm that identified a harmful event.  i don't see a catalog or container of harm types that each discipline has identified and shared.  do we hae
<!-- copilot-message {"notes":["02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md","02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3.1 - Skeleton Schema (proposed).md"]} -->
[Timestamp: 2026/11/22 07:28:16]

**ai**: Your message cut off after "do we hae", so I've answered the part I could read. Tell me if you meant something else. I used only the two attached notes.

## Harm types the snapshot supports

The snapshot has no catalog of harm types. It deliberately avoids one: harmfulness is never intrinsic, so a verdict of Harmful lives only in an Assessment. The nearest things to a list are below.

**1. `ObjectOfHarm` (v3 line 75).** This is the closest thing to a harm-type taxonomy, with eight top-level values:
- Somatic
- PsychologicalCognitive
- Assent/Judgment (?)
- MaterialPecuniary
- DignitaryRelational
- NormativeStatus
- OpportunityCapability
- SystemicEnvironmental

**2. `Effect` kinds (line 58).** These are only examples, and the list ends in "…":
- SleepLoss
- ReputationalDamage
- Deskilling
- CapturedAssent (?)
- Death

Effects are neutral. They become a `HarmfulEffect` only if at least one assessment judges them Harmful. Effect properties such as `isPosthumous`, `isStatistical` and `isDispositional` describe variants of effects. Severity, reversibility and temporal trajectory are also listed as properties.

**3. `AffectedEntity` types (line 68).** These show who or what can be harmed, which implies further harm types:
- SentientIndividual
- CollectiveArtificialPerson
- NonSentientSystem (proposed split into NaturalSystem and EngineeredSystem)
- FutureGeneration
- AISystem
- Relationship
- Proposed: CollectiveNaturalGroup and Household

**4. Discipline-specific conceptions of harm (`EvaluativeStandard`, line 78).** These are standards for judging harm, not harm types:
- Philosophical: Experiential, Comparative, NonComparative, RightsBased, Capacity
- Legal: InjuryInFact, ReasonablePerson, LossOfChance, ConcreteHarm
- Causal (pending): ButFor, NESS, INUS and others
- Worldview (?)

**5. Other things an assessment might surface.** These are not harm types, but they are findings an assessment can produce:
- Factor kinds: Act, Process, Omission, Structure, Risk
- Divergence types: Perspectival, Normative, Evidential, Factual
- Assembly origins: Emergent, Exploited, Engineered

## Is there a shared catalog of discipline-identified harm types?

**No.** The snapshot has three partial gaps:
- **Box C (line 132).** It names candidate external vocabularies: legal (LKIF, Akoma Ntoso), cyber (STIX, ATT&CK, CVSS) and AI incidents (AIID, CSET, MIT). All are marked "all unverified". None is mapped to harm types.
- **Box D (line 134).** It describes a vocabulary layer with `hov:` hubs and discipline schemes, plus graded mappings (exact, close, narrow, broad, related). The contents live in [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]], which wasn't attached, so I can't say whether harm types are populated there.
- **v3.1.** It adds Discipline, Theory, ConceptualTerritory and FieldOfApplication, but only as structure. Narrative and content migration is deferred. Nothing links a Discipline to the harm types it recognizes.

## A possible fix (not in either note)

You could add a `HarmType` concept scheme in the vocabulary layer (SKOS). Each discipline's own term would be a concept in it, such as tort "pure economic loss", public health "morbidity" or the AI-incident taxonomies. Each would map to a hub concept at a graded level, and could point to the `ObjectOfHarm` value it fits. That keeps the "describe and judge, don't classify" commitment, because harm types become vocabulary rather than ontology classes.

I can draft that as a proposal note, or check the crosswalk note for existing harm-type content. Which would you like?
<!-- copilot-message {"tools":["read (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3.1 - Skeleton Schema (proposed).md"]} -->
[Timestamp: 2026/11/22 07:28:16]

**user**: avoiding harm types does not, to me, imply that harm is intrinsic - rather that it is characterized by identifying and identifyable characteristics that can be used in an assessment
<!-- copilot-message {"notes":["02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md"]} -->
[Timestamp: 2026/11/22 07:30:34]

**ai**: You're right, and I conflated two things. My phrase "deliberately avoids" a catalog was a misreading. Nothing in the snapshot says harm types can't be catalogued, and a catalog doesn't make harm intrinsic.

- **Intrinsic harmfulness** means an event or effect is harmful in itself, with no perspective involved. HO-premise rules that out.
- **Characterized harm** means a harm is described by identifiable characteristics, such as what was affected, how, how severely, whether it can be reversed, and who bears it. An assessment can then use those characteristics. This is compatible with the premise, and it fits the snapshot's own pattern. Effects are neutral and carry observable properties (`severity`, `reversibility`, `temporalTrajectory`, `isStatistical` and others). The Assessment then supplies the verdict.

So a harm type is better treated as a **characteristic profile**, not a class of intrinsically bad things. It is a recognizable pattern of Effect characteristics, plus an `ObjectOfHarm` and an `AffectedEntity` type. A discipline names the pattern, and an assessment can invoke it.

Two cautions from the snapshot:
- **Don't make `HarmType` a subclass of Effect.** v3 says "describe and judge, they don't classify". If a type's membership depended on a verdict, it would reintroduce intrinsic harm. The type should be defined by characteristics only, with the Harmful or Beneficial judgment staying on the assessment.
- **Where the type lives is undecided.** Two options fit v3. One is a SKOS concept in the vocabulary layer (Box D), mapped to discipline terms. The other is an attribute value that an Assessment asserts (`aboutAttribute`, as in the toy-test model). The second keeps it perspective-relative: a tort lawyer and a public-health assessor can characterize the same Effect differently, and that shows up as a Divergence, not an error.

My earlier list of `ObjectOfHarm` values, Effect kinds and `AffectedEntity` types is a starting set of those characteristics. It has no discipline provenance and no mapping to the harm types each discipline names.

Do you want me to draft a note proposing a characteristic-profile model for harm types, with the fields a discipline would fill in?
[Timestamp: 2026/11/22 07:30:34]