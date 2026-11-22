---
epoch: 1795357696068
mode: agent
backendId: opencode
sessionId: "ses_dfc5ae101ffeAFfkQ6sFGJfTrY"
model: '{"baseModelId":"anthropic/claude-sonnet-5-5","effort":"low"}'
tags:
  - copilot-conversation
topic: "Harm ontology harm types catalog"
usage: '{"usedTokens":186849,"contextWindow":1000000,"updatedAt":1795362547506}'
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

**user**: i am thinking that the notion of a harm type might be capture in a distinction. the word harm, itself may be overloaded. if we can agree on an assessment that evaluates an event to be harmful and it does so from a perspective i believe it would be using that disciplines perspective on a type of "Harmfullness" rather than harm.  Harmfulness might have subcategories carrying types of harmfulness as well as many of the attributes - discipline and perspective specific identifiers of characteristics that make an event or situation potentially harmful...  like clues that a perspectives "searchlight" might be scanning for metaphorically
<!-- copilot-message {"notes":["02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md"]} -->
[Timestamp: 2026/11/22 07:40:28]

**ai**: This distinction fits the snapshot well, and it fixes a problem I had. "Harm" is currently used for three different things:

1. **The judged outcome.** This is the Assessment `verdict: Harmful`.
2. **The affected thing.** This is `ObjectOfHarm` and `HarmfulEffect`.
3. **The signs that make a judgment likely.** Nothing in the snapshot holds this yet.

Your "harmfulness" is the third sense. It is the cues a perspective looks for, not the verdict and not the effect.

## How it fits what exists

- **The premise.** The name of HO-premise "No Intrinsic Harmfulness" already uses the word. Harmfulness stays safe only if it is always *harmfulness-as-seen-from a perspective*. A cue is not a property of the event. It is something a perspective treats as significant.
- **The searchlight already has parts.** `PerspectiveSpecification` has framing, resolution and sensitivity (threshold), plus `inclusionCriteria`. A `PerspectiveType` has `moralCircle` and `defaultEvaluativeStandard`. v3.1 mentions `objectOfAttention` (0.02 core). Together these say where the light points and how bright it is. What's missing is a list of the cues it picks up.
- **Dispositional and potential harm.** `isDispositional`, `isStatistical` and the `Risk` factor kind already point at "potentially harmful" as something distinct from "harmed".

## A possible shape (a proposal, not in the notes)

- **HarmfulnessIndicator** is a cue: a characteristic a perspective scans for. It has subcategories by type of harmfulness, such as bodily integrity, loss of agency, irreversibility, vulnerability of the affected entity, and breach of a duty. Disciplines and traditions supply their own.
- **A perspective scans for indicators.** A PerspectiveType would carry `scansFor → HarmfulnessIndicator`, with sensitivity attached per indicator. This is the "searchlight".
- **An Assessment records which indicators it observed**, as evidence for a verdict. That is the link back to the harm: the indicator supports the verdict and never entails it.
- **Divergence gets sharper.** Two perspectives can see the same event and light up different indicators. That is a Perspectival divergence at the level of cues, before any verdict differs.
- **Mapping.** Indicators fit the vocabulary layer (Box D): the discipline's own term, mapped to hub concepts at graded levels. This also answers my earlier question about a shared catalog. It would be a catalog of cues by discipline, not of harms.

## Questions for you

- Is harmfulness a **class** (indicators as individuals that take part in relations), or a **concept scheme** (word-senses to define and map)? Under the 2026-11-21 rule in v3.1, an indicator that is linked to perspectives and assessments should be an individual, and the discipline's word for it should be a concept.
- Do you want "harm" kept for the verdict only, with "harmfulness" for the cues?
- Is an indicator ever **absent-but-expected**? This would be a cue a perspective scans for that wasn't found, which connects to omission handling in HO-005.

I can draft this as a short proposal note, structure only, in the style of v3.1.
[Timestamp: 2026/11/22 07:40:28]

**user**: what unique dimensions or attributes of harmfulness can be inferred or gleaned from the 7 notes in which capture the individual discipline council reviews of perspective structure looking for gaps
<!-- copilot-message {"notes":["02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md"]} -->
[Timestamp: 2026/11/22 08:39:14]

**ai**: The seven reviews are about what a *perspective* records, not about harm. The cues below are my inference from their gap lists, and I note the source council for each. They fit your "searchlight" idea well. Each proposed lens attribute implies something the lens looks for, or something it cannot see.

## Dimensions of harmfulness the reviews imply

**1. Who and what is affected**
- **Standing of the subject** (Ethics): treated as an agent, a patient, or mere data. Reduction to "mere means" is itself a cue.
- **Moral circle** (Ethics): whether the affected being counts at all, including non-users, future generations, ecosystems and AI systems.
- **Legal personhood and standing** (Legal): harms the law recognises in principle but nobody can bring.
- **Differential burden** (Legal): a neutral-looking rule that falls unequally.
- **Cost bearer vs. beneficiary** (Ethics): benefits and burdens land on different people.
- **Distributive concern** (Ethics): how outcomes are spread, and whether the worst-off carry them.
- **Vulnerability and dependency** (Ethics): asymmetric care relationships, exploited dependence.

**2. Power, consent and voice**
- **Power asymmetry** (Sci-Fi): the imbalance between the holder of the lens and its subject.
- **Consent, and consent under asymmetry** (Ethics and Sci-Fi): consent given or absent, and whether refusal was a real option.
- **Voice, and discounting of voice** (Ethics and Cognitive): whose account of their own situation is heard. This includes testimonial injustice and low precision weighting.
- **Legibility** (Sci-Fi): whether the subject can understand what is done to them.
- **Public justifiability and procedural integrity** (Ethics and Legal): secret rules, retroactivity, and mismatch between declared rule and official action.

**3. Accountability**
- **Accountability locus** (Logic): the "rule of Nobody", with no one who must answer.
- **Accountability laundering and moral crumple zones** (Sci-Fi): "the algorithm decided", or blame landing on the nearest human.
- **Remedy** (Legal): a harm that can be named but not repaired.
- **Intent attribution** (Cognitive): harm where no intent can be located, such as AI-caused harm.

**4. Visibility and detection**
- **Observability and latency** (Legal, Physics): limitation periods, harms that time out before discovery, and harms below the noise floor.
- **Instrument dependence** (Physics): complaint counts miss people who don't complain.
- **Anomalies set aside** (Physics): reports that fit no recognised category.
- **Emergence at scale** (Physics): harms that exist only in aggregate.
- **Compression and category loss** (Physics and Sci-Fi): harm lost in translation, or forced into a category that doesn't fit.
- **Fabrication and the liar's dividend** (Sci-Fi): real evidence dismissed as fake.

**5. Dynamics (how harm evolves)**
- **Performativity and feedback loops** (Physics): a lens that creates the evidence for itself.
- **Resonance** (Physics): mutual amplification between lenses or between a system and its community.
- **Adaptive response** (Sci-Fi): subjects game, hide or resist, which changes the harm.
- **Normalization of deviance** (Physics): gradual acceptance of anomalies until failure.
- **Specification gaming** (Sci-Fi): the letter of the objective is met and the intent defeated.

**6. Harm to the holder and to the observer**
- **Effect on holder** (Classical): lenses that produce the harm they measure, such as fear or suspicion.
- **Character formation and cognitive alteration** (Ethics and Sci-Fi): habituation, deskilling, changes to memory and judgment.
- **Observer cost** (Physics): moderators harmed by looking.
- **Observer effect** (Physics): chilling effects from being watched.

**7. Knowledge and truth**
- **Fact handling** (Logic): facts dissolved into opinion.
- **Immunizing moves and misnaming** (Logic, Classical and others): names such as "safety" claimed without being earned.
- **Prior and base-rate assumptions** (Logic): for example, assumed fraud rates.
- **Order-of-magnitude error** (Physics): such as the Challenger 1-in-100 vs 1-in-100,000 gap.

**8. Time and scale**
- **Discounting the future** (Ethics): a moral choice disguised as arithmetic.
- **Scale validity** (Physics): a lens used outside the range where it works.
- **Slow violence** (Sci-Fi): harm told in a way that hides accumulation.
- **Future robustness** (Sci-Fi): a lens that fails as technology advances.

**9. How the exclusion is held (the "searchlight" itself)**
- This is the four-way split of blind-spot types: **out of frame** (constitutive), **negligent**, **accepted** (Omelas) and **suppressed**.
- It is about why a cue is not seen, so it doubles as a diagnostic on the searchlight.

## Observations for your model

- **Some of these are cues about the lens, and some are cues about the event.** Dimensions 1, 2, 3 and 6 describe the situation. Dimensions 4, 5, 7 and 9 describe the lens's limits. A harmfulness indicator class would probably need to separate "what the light finds" from "what the light cannot find".
- **Two cue kinds appear.** Some are *present-cues*, such as a power asymmetry. Others are *absent-cues*, such as no remedy, no voice or no accountable party. Absence is itself a signal, which connects to your HO-005 omission handling.
- **The most convergent cue is the stated-versus-operative gap.** Confucius, Kant, Fuller, Arendt and Feynman reach it independently (five witnesses). But all seven councils were voiced by one model, so this is a candidate, not independent confirmation. The vault notes say this too.
- **Gaps in coverage.** The reviews are tilted toward institutional and AI harm. Direct bodily or material harm, and physical and economic harm, appear only as examples, not as dimensions. A real catalog would need discipline sources such as medicine, public health or economics. v3.1's planned coverage test (physics vs Integral) might surface these.

I can draft a structure-only proposal note that turns these nine groups into candidate `HarmfulnessIndicator` subcategories, each tagged with its council source and whether it is a present-cue or an absent-cue. Should I?
<!-- copilot-message {"tools":["glob (search)","grep (search)","execute (other)","read (read): 02_Ideas Topics Concepts/Harm Ontology/v-0.01 ClassicalCouncil Review of - PerspectiveStructure 0.01.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/v-0.01 EthicsCouncil Review of - PerspectiveStructure 0.01.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/v-0.01 LegalCouncil Review of - PerspectiveStructure 0.01.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/v-0.01 LogicCouncil Review of - PerspectiveStructure 0.01.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/v-0.01 PhysicsCouncil Review of - PerspectiveStructure 0.01.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/v-0.01 SciFiCouncil Review of - PerspectiveStructure 0.01.md","read (read): 02_Ideas Topics Concepts/Harm Ontology/v-0.01 CognitiveCouncil Review of - PerspectiveStructure 0.01.md"]} -->
[Timestamp: 2026/11/22 08:39:14]

**user**: is there nothing in these notes about the sequence - the unfolding - that considers the individual or collective assembly of events that precipitate harmfulness?  or about the consequence or assembly of consequences that follow that might  be characterized as harmful?  where do they consider horizon?   if there is, where do these attributes fit in your scheme above or are they an additional category?
<!-- copilot-message {"notes":["02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md"]} -->
[Timestamp: 2026/11/22 08:45:47]

**ai**: Yes, the notes cover this. My earlier list under-served it, and it should be an additional category. I'm drawing on the v3 snapshot and the council tables. I haven't opened the HO-003, HO-004 or HO-006 notes, so details beyond what v3 states about them are unchecked.

## Where the notes handle the unfolding

**Precipitating side (causes converge into a settled past)**
- **FactorAssembly** (HO-003, "the Perfect Storm") is a collective assembly of events or conditions. The assessments supply these properties:
  - members
  - `hasUnknownMembers`
  - `individuallyInnocuous`
  - origin: Emergent, Exploited or Engineered
  - orchestrator
  - `sufficientFor`
- **CausalRole** sets out each factor's part in a chain: Trigger, Enabler, Amplifier, Conduit, ProximateCause, DistalCause and ContributingCause (?). It also records:
  - proximity
  - necessity
  - causal share
  - `isDistributed`
  - `isForeseeable`
  - answerable agent
- **Factor kinds** include Act, Process, Omission, Structure and Risk, with `isContinuous`.
- **CausalAssessment** records what is attributed as the cause and what is left out (`leftOut`).
- Councils add:
  - causation tests (Legal): but-for, proximate, material contribution
  - dominant factors (Physics)
  - explicit causal models (Cognitive)
  - normalization of deviance
  - accountability diffusion
  - Hart's description/evaluation split

**Consequent side (effects ramify into an open future)**
- **Effect** has `leadsTo` (cascades, open-ended), plus severity, reversibility, `temporalTrajectory`, `isPosthumous`, `isStatistical`, `isDispositional` and `modality`.
- `temporalStatus` runs Actual, Extrapolated or Pending, and `occurredDuring` is proposed.
- Councils add:
  - performativity and feedback loops
  - resonance
  - adaptive response
  - emergence at scale
  - slow violence
  - failure by excess or deficiency
  - observer cost

**Horizon**
- v3 states a deliberate asymmetry: causes converge, effects ramify. The full causal past and future are limit concepts, never instantiated.
- **Outcome** is "a cut across the ramification at a horizon", selected by a PerspectiveSpecification.
- Horizon properties on the perspective are `exposure` (horizon), `predictabilityHorizon (?)`, `timestamp` and `chainScope`.
- `scopeAdequacy` can never be Complete.
- The Classical council adds temporal scope as an instrument (the "view from above"), and the Ethics council adds discount rate. The Legal council adds limitation periods and the discovery rule, so a horizon can decide whether a harm is heard at all.
- Physics adds scale validity and `limitBehavior`, and Sci-Fi adds future robustness. HO-006 proposes a Chain bounded by a horizon (v4, not decided).

## Where this fits relative to my nine groups

It doesn't fit inside them. My groups were mostly about the *situation and the lens*. This is the *structure of the event sequence*, so I'd add it as a tenth group, **Unfolding**. Parts of my groups 4, 5 and 8 belong there, and I'd move them.

| Sub-axis | Characteristics (cues) | From my earlier groups |
|---|---|---|
| **Precipitation** (upstream assembly) | Individually innocuous parts; emergent / exploited / engineered; distributed causation; unknown members; orchestrator; foreseeability; role in chain; omissions as causes | Group 3 (accountability) overlaps |
| **Consequence** (downstream assembly) | Cascade or ramification; severity; reversibility; trajectory; latency; statistical or dispositional; posthumous; feedback to cause | Group 5 (dynamics) moves here |
| **Horizon** (the cut) | Timestamp, exposure horizon, predictability horizon, discount rate, limitation and discovery rule, actual vs extrapolated | Group 8 (time and scale) moves here |
| **Coupling** | Performativity, resonance, normalization of deviance, adaptive response: the consequence feeds the precipitating side | Group 5 |

## Two points about the model

- **Horizon is a parameter, not a cue.** The same event can show different harmfulness at different horizons. Group 8 should be the perspective's setting (`exposure`) plus the observed latency of the event, not a list of cues.
- **Sequence may be the strongest case for a perspective-relative cue.** Where one perspective starts and stops the chain (`chainScope`) decides which factors it sees as precipitating, so the Divergence between perspectives can be about the chain itself. HO-005 covers this as systematic omission.

I can fold this into the structure-only proposal as the tenth group, with the four sub-axes. Should I?
[Timestamp: 2026/11/22 08:45:47]

**user**: yes. but im sorry. i did not mean in all the notes.  please narrow your answer to the previous prompt to only include discoveries within the specific collection of 7 notes from the various council reviews of perspective structure.
<!-- copilot-message {"notes":["02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md"]} -->
[Timestamp: 2026/11/22 08:48:32]

**ai**: Narrowed to the seven council notes, the answer changes. Those notes mostly describe what a *perspective* records, so the unfolding of events appears only as how a lens handles sequence. The seven notes have no model of a precipitating assembly or of a cascade of consequences. They send you to HO-003, HO-004, HO-005 and HO-I.a for those, and that material is outside this collection. I've dropped everything I drew from v3 and the HO notes.

## What the seven notes say

**Precipitation (assembly of events leading to harm): thin**
- **Legal, `causationTest`.** The test is but-for, proximate or material contribution. It says causation is "a policy choice, not a fact". It also describes AI harm as "distributed causation", where no single contributor passes but-for (the "many hands" problem).
- **Logic, `accountabilityLocus`.** Responsibility is spread across data providers, developers, deployers and operators.
- **Logic, `methodicalDoubt`.** Decomposing an incident into data, model, deployment and use can hide emergent harms that exist only in the assembled whole.
- **Logic, `priors`.** A built-in base-rate assumption can create harm at scale (Robodebt).
- **Physics, `dominantFactors`.** The rate-limiting step or leading-order contributor.
- **Physics, `normalizationOfDeviance`.** Repeated small deviations become normal until failure (Challenger).
- **Cognitive, `internalSublenses`.** In a composite lens, the harm may arise in the classifier, the human review, the appeal or the hand-offs.
- **Cognitive, `causalModel`.** The lens's explicit causal hypotheses, with Pearl's correlation vs intervention distinction.
- **Sci-Fi, `conflictResolution` and `specificationGaming`.** Harm from colliding rules or from meeting the letter of an objective while defeating its intent.

**Consequence (what follows): thin**
- **Classical, failure by excess or deficiency.** A lens pushed too far or too little produces harm.
- **Classical and Ethics, effect on holder and `characterFormation`.** Slow formation of dispositions. The Ethics table says these claims "will usually be extrapolated rather than actual in chain status".
- **Sci-Fi, `cognitiveAlteration`.** Memory, judgment and sense of self change.
- **Sci-Fi, `emergentEcosystems`.** Parallel economies grow up around a lens.
- **Physics and Sci-Fi, `observerCost` and `observerEffect`.** Harm to the one who looks, and chilling effects.
- **Legal, `incentiveEffects` and `enforcementReality`.** Fines become a licence fee, and enforcement falls unevenly.
- **Legal, `precedentialWeight`.** Automated decisions create de facto precedent with no overruling mechanism.
- **Legal, `remedy`.** Whether the harm can be repaired.

**Coupling (consequence feeding back into cause): the strongest material**
- **Physics, `performativity`:** none, self-confirming or self-defeating (predictive policing, credit scores).
- **Physics, `resonance`.**
- **Sci-Fi, `adaptiveResponse`.** What subjects do in return.
- **Cognitive, `predictionErrorHandling`:** update, act on the world, or suppress.
- **Cognitive, `activeSampling`.** A lens that looks only where it expects harm confirms its expectation.

**Horizon: scattered but real**
- **Classical, `temporalScope`.** The "view from above" can *reveal* slow harms or *dissolve* responsibility ("in a hundred years none of this matters"). The note proposes a revealing-vs-dissolving qualifier.
- **Ethics, `discountRate`.** "Discounting future people is a moral choice disguised as arithmetic."
- **Legal, `limitationPeriod` and `discoveryRule`.** A horizon that starts at the act, not at discovery, excludes latent harms (*Ledbetter*).
- **Physics, `scaleValidity` and `limitBehavior`.** Range of scale where the lens works, and what its verdicts do at extremes. Some harms exist only at scale ("more is different").
- **Physics, `noiseFloor`.** Harms below detection, including deliberately "low and slow" ones.
- **Sci-Fi, `futureRobustness` and `narrativeForm`.** How a lens holds as technology advances. The hero-conflict form misses slow accumulation ("slow violence"), and the carrier-bag form sees it.
- **Logic, `updateRule`.** How much evidence a lens needs before it responds, so how long harms run before institutions act.

## Not in the seven notes

- No attribute set for a **cascade or ramification** of effects.
- No **severity, reversibility or trajectory** attributes.
- No treatment of **individually innocuous factors forming a harmful whole** as a named pattern. Only the "many hands" and decomposition points come close.
- No explicit **actual vs extrapolated** chain model, apart from the single mention in the Ethics `characterFormation` row.
- No **horizon as a perspective setting** that cuts a chain. Horizon appears as temporal scope, discount rate and legal windows, as separate scattered items.

## Fit in the scheme

It is still an additional category, but a smaller one than I implied last time. Under a tenth group, **Unfolding**, the councils populate:

| Sub-axis | Strength in the seven notes |
|---|---|
| Coupling | Strong (Physics, Sci-Fi, Cognitive) |
| Horizon | Moderate, scattered (Classical, Ethics, Legal, Physics, Sci-Fi) |
| Precipitation | Thin (Legal, Logic, Physics, Cognitive) |
| Consequence | Thin (Classical, Ethics, Sci-Fi) |

For your coverage-test idea, the thin rows are a finding. The councils examined the *lens*, so the gaps they left on precipitation and consequence are expected. The unfolding model would have to come from another source, such as the HO-003, HO-004, HO-005 and HO-006 notes.

Do you want me to write the proposal note with the tenth group limited to what these seven notes support? If so, where in the vault should it go? Or should I draft it beside the v3.1 skeleton?
[Timestamp: 2026/11/22 08:48:32]