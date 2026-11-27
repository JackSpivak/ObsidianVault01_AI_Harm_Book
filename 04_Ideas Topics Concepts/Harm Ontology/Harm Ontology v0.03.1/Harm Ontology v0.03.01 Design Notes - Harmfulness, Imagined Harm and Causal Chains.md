---
fileClass: Idea
type: note
status: developing
bookmark: draft
canonical_id: ho-v3-design-notes-harmfulness-imagined-harm
tags: [ontology/harm, harmfulness, assessed-imagined-harm, causal-chain, modular-ontology, design-notes]
aliases: [Harmfulness and Imagined Harm Design Notes, Causal Chain Design Notes]
created: 2026-11-23
updated: 2026-11-23
---

# Harm Ontology v3 Design Notes: Harmfulness, Imagined Harm and Causal Chains

*Record of the realizations from the 2026-11-23 session. Each entry gives the wording from the session (quoted, with cuts marked "…"), then four framings: what it **extended**, what it **accomplished**, what it **enabled the model to represent**, and what was **distinctive**. A **Discussion** follows each entry. Items still awaiting confirmation are listed in [[Pending Design Decision - Harmfulness as Reified Class]], not here. Nothing here is logged in [[Decisions_Log]] yet.*

---

## 1. Temporal split: AssessedHarm is past or present only

**Session wording (author):** "i think that assessed harm probably needs to be tied to harm that actually occurred in the past and/or one that is concurrently occurring. i think it is disingenuous and conflating to label assessedharm when it is an assessment of future harm. that would really require a crystal ball. we need other language."

- **Extended:** the earlier `AssessedHarm` class, which had been used for both actualized and projected harm.
- **Accomplished:** `AssessedHarm` is restricted to harm that has occurred or is occurring. Projection of future harm gets its own family of terms.
- **Enabled the model to represent:** the difference between an empirical record and a forecast, so a forecast cannot be mistaken for a record.
- **Distinctive:** the line is drawn on the timeline, not on the quality of the evidence. Even a well-grounded forecast is still a forecast.

**Discussion.** Risk writing routinely says "the storm will cause $4bn in harm" or "this model will cause catastrophic harm." Both sentences use the language of records for claims that cannot yet be checked. The problem is not that forecasters are dishonest. It is that the vocabulary hides the difference between what has been observed and what has been projected, and readers fill the gap with false certainty. An ontology that uses one class for both inherits the same blur. Restricting `AssessedHarm` to past and present makes the distinction a structural fact: any instance of that class must point to an observed or observing state, and any forward-looking claim must belong to a different class. The author's test was simple. You cannot assess harm that has not yet happened without a crystal ball. Candidate names for the future-oriented family were AssessedPotentialHarm, AssessedPostulatedHarm and AssessedImaginedHarm. The next entry explains why the third was preferred. The split also has a practical benefit. A query for "harms assessed as occurring" will no longer return models of what might happen, and a regulator asking which harms are already documented gets a clean answer.

## 2. AssessedImaginedHarm as the name for projection

**Session wording (author):** "personally i like AssessedImaginedHarm - which can still take all the severity and scale weight that an active imagination can project."

- **Extended:** the temporal split in Section 1 into a named class for future projection.
- **Accomplished:** the term admits that projection is imaginative construction while leaving room for its severity and scale to be taken seriously.
- **Enabled the model to represent:** a projection that is large and serious but openly modeled, so it can be graded rather than dismissed or accepted at face value.
- **Distinctive:** it is the most candid of the candidate names, and the one that makes the grounding requirement in Section 3 necessary.

**Discussion.** Critics of climate models and of AI existential-risk forecasts often object to the imaginative leap from present proxies to catastrophic futures, not to the arithmetic. Calling the output "potential" or "postulated" can quietly accept the model as a real possibility, while "imagined" concedes the point the critic cares about. It also avoids the opposite error of treating projections as merely arbitrary. The author's wording keeps the full weight of severity and scale. A projection of civilizational collapse is not made smaller by being called imagined. What changes is the burden placed on it: an imagined harm of great scale must show how its imagination is anchored. That is the reason the name is more useful than its alternatives. Potential harm invites the question "how probable?", which is often answered with a number that hides its assumptions. Imagined harm invites the question "what grounds the imagining?", which opens the evidentiary chain. The term therefore does real work in an ontology: it names the class whose instances must carry provenance, and it stops a dramatic forecast from passing as a measurement. It also supports fairness toward modelers, because the name says plainly what kind of claim is being made.

## 3. Grounding the imagination: evidentiary basis and vetting

**Session wording (author):** "we already have some properties related to vetting and evidence that could be attached to require that imagination is grounded in some kind of objective observable data"

**Session wording (author, on scientific responsibility):** "scientists should be able to (and are able to unless they have been irresponsible or deceitful) provide the evidentiary basis for the model, its structure, testing, independent vetting and match between prediction and reality. they don't have to do this each time someone claims it is arbitrary or imaginative. the individual basis artifacts (or maybe the whole perspective (if its core principles have been sufficiently verified?) could be deemed reliable (at least with respect to its core principles)"

- **Extended:** `AssessedImaginedHarm` from a name into a graded claim with provenance.
- **Accomplished:** a projection can be audited for its evidentiary basis, its vetting, and how well past predictions matched outcomes, without re-arguing the whole model each time.
- **Enabled the model to represent:** the grounding chain (`hasEvidentiaryBasis`, `hasVettingCriterion`, a grounding score, an `AssessmentHorizon`) and the inheritance of reliability from a vetted perspective or pipeline to the projections it produces.
- **Distinctive:** trust is placed in the generative pipeline and its verified core principles, so each output does not have to be justified from raw data every time.

**Discussion.** Radical skepticism treats every model as imagination. Naive realism treats every model as a map of reality. The author's position sits between them: a model is disciplined imagination, and its discipline can be shown through its structure, its testing, its independent review and its track record against outcomes. The point about responsibility matters. A scientist who has done this work should not have to repeat it each time a critic calls the model arbitrary, and a critic who wants to dispute the model should engage the artifacts that already exist. The inheritance idea makes this operational. A projection can state that it was generated by a perspective whose back-testing fidelity was measured over a given window, and that the perspective's core principles have been verified, so the reliability attaches to the pipeline rather than to each output. The ontology then supports a diagnostic question for any projected harm: what is the pipeline, what is its grounding, and has it been vetted? The author's summary was "Validating the Generative Pipeline (Perspectives & Baselines) rather than just the isolated output." The caution is that a grounding score and an inheritance rule are proposals, not settled design. A single number may not mean the same thing across climate, epidemiology and AI safety, and that question is open.

## 4. Harmfulness is not an ontic property; it is an assessment

**Session wording (author):** "someone or some organization may believe because of the triad of object capability that someone or something is harmful. but inevitably that is an assessment. weather predictions are famously fallible and speaking of the storm as harmful may depend on the attributedMechanism being flawed. maybe sea and atmospheric temperatures are believed to be critically moving a normal storm into a severely harmful one. but sensor data is flawed and skews the required mechanism"

- **Extended:** the earlier triad in which Harmfulness was treated as a physical, objective disposition of an object or actor.
- **Accomplished:** it corrects a drift in the earlier framing. Calling a storm or a gun "harmful" is always a judgment that depends on a mechanism model, so Harmfulness cannot sit outside an assessment.
- **Enabled the model to represent:** failure modes. A storm can be wrongly classed as harmful because a sensor is skewed, and that is a fault in the assessment, not in the storm.
- **Distinctive:** it removes the "view from nowhere." Physical objects keep their capabilities, and everything about harm is an assessment of those capabilities.

**Discussion.** The gun-rights argument, that a gun is neutral and becomes dangerous only in certain hands, is the same problem in a different domain. Capability is a fact about the object: a firearm discharges projectiles at high velocity, and a storm releases thermodynamic energy. Harm is an evaluation of that capability within a causal context, and the evaluation depends on the actor, the mechanism and the criteria used. The author's storm example makes the point sharper. Whether sea and atmospheric temperatures are pushing a storm toward severe impact is a claim about a mechanism, and the claim can be wrong because the sensors feeding it are skewed. If the ontology lets Harmfulness sit as a physical fact, a skewed sensor produces a "true" harmfulness that nobody can check, and the error disappears into the object. If Harmfulness is always an assessment, the same error becomes visible: a judgment that rests on a faulty mechanism model. This also clarifies the gun debate without taking a side in it. Both sides can agree on the capability, and the disagreement moves to the assessment: who is holding the object, what they intend or lack, and what criteria count as dangerous. The author's suggestion that AssessedHarmfulness might be a subclass of Harmfulness, or that Harmfulness should be dropped altogether, are both live options. They are recorded in the pending decision note, because the choice affects what a query can ask.

## 5. Harmfulness as a reified class with its own properties

**Session wording (author):** "I am thinking of it rather as a thing 'class' that can have all of its own properties to be reasoned over - like assessor, hasobjectivestandard or hasharmfulnessCriterion (or maybe harmfulness criterion is a subclass of ObjectiveStandard and is in the domain of hasHarmfulnessCriterion"

- **Extended:** the earlier treatment of Harmfulness as a property or scalar.
- **Accomplished:** Harmfulness becomes a class that can be reasoned over, with properties for the assessor, the objective standard and the criteria.
- **Enabled the model to represent:** candidate properties `hasAssessor`, `hasObjectiveStandard` and `hasHarmfulnessCriterion`, with `HarmfulnessCriterion` as a subclass of `ObjectiveStandard`.
- **Distinctive:** the class is the object of reasoning. Its properties say who judged, against what, and by which criterion.

**Discussion.** Reifying Harmfulness turns a vague scalar into something a methodologist can interrogate. A scalar such as "severity 7" says nothing about who assigned it or why. A class with an assessor, a standard and a criterion makes each of those questions answerable. This fits the Principles-and-Standards pattern in the v3 assessment note, where a `[Domain]Standard` class sits between principles and assessments. A harmfulness criterion could then be modeled as a kind of objective standard, so that two assessments using different criteria can be compared directly. The design also tests the ontology's commitments. If a criterion can be attached to a harmfulness class, the class can be queried across assessors: which criteria produced high harmfulness for the same object, and which assessors used them. That is the kind of divergence the ontology is meant to expose. The open question is what a harmfulness criterion actually is. If it is a technical threshold, such as a kinetic-energy limit or a toxicity level in parts per million, it belongs with technical standards. If it is a judgment about what counts as damaging to a person or community, it belongs with moral principles. The two cases behave differently under dispute: a threshold can be tested, while a principle can only be argued. The author's proposal leaves that choice open, and it should stay open until the pending decision is made.

## 6. Causal chains are occurrent structures with participants, not subclass trees

**Session wording (author):** "so it sounds like the notion of membership in the chain can be represented structurally through the use of classes and object properties however the assessment of completeness or flawedness must be layered on through shacl rules (most likely)"

- **Extended:** the causal chain from a flat list of components into a structure built from DUL-style occurrents and participants.
- **Accomplished:** membership in a chain (Actor, Event, Capability, Mechanism, ObjectOfHarm, HarmfulOutcome) is expressed through object properties. Completeness is checked by a separate constraint layer.
- **Enabled the model to represent:** that only objects and agents participate in events. A process is not a participant. An impaired memory is a quality of a person, and the faulty recall is part of that person's cognitive life.
- **Distinctive:** structure says what can be linked. SHACL says what must be present for the chain to count as complete.

**Discussion.** OWL is monotonic and works under the open-world assumption, so a missing actor is treated as unknown, not invalid. A causal chain that lacks an actor is not logically inconsistent; it is simply incomplete in the data. Completeness is a judgment about the data, and it can change as new information arrives, so it belongs in a non-monotonic layer. SHACL `sh:minCount` shapes provide that layer. They report which slots are empty without changing what the ontology says is possible. The split also keeps the schema honest about its own limits. Structure states what kinds of things can stand in which relations. Validation states whether a particular causal account is good enough to rely on. An analyst who sees a violation knows the risk model is flawed rather than that the world is absent a cause. The schema was drafted against DOLCE+DnS Ultralite (DUL), where `dul:Event` and `dul:Object` form the main top-level division and `dul:hasParticipant` relates objects to events. **Caution:** the DUL-aligned table and tree produced in the session were drafted from memory and have not been checked against the published OWL file. Several parent-class assignments, such as where a Mechanism sits, may be wrong. That verification is a necessary step before the schema is treated as usable.

## 7. Storms, causal cascades and non-agents

**Session wording (author):** "if a storm causes harm, who would be the required ex:Actor? the storm? the kinetic impact of waves? floodwater due to surge? windblown debris?"

- **Extended:** `Actor` from "whoever does it" to "whatever initiates or drives the sequence."
- **Accomplished:** a storm is not a `dul:Agent`. It is a physical participant or origin, and the cascade (surge, debris, structural collapse) is a chain of events and mechanisms.
- **Enabled the model to represent:** cascades as nested events and mechanisms, with the root source linked as a participant rather than an actor.
- **Distinctive:** it separates agency from causal origin, which lets natural hazards and institutional failures sit in one schema.

**Discussion.** The author's question exposed a gap in the first draft. Calling "the storm" an Actor implies intention or responsibility that a weather system does not have, but ignoring the storm leaves the causal chain without its origin. The resolution is to separate two roles. An agent is something that performs goal-directed action and can be held to account. A participant or source is anything that stands in a relation to an event, including forces, objects and substances. Once that split is in place, the cascade reads naturally. The storm is a source. The surge is a process that participates in flooding. The debris is an intermediate object that transfers kinetic energy to a structure. The mechanisms are hydrostatic pressure, wave impact and debris collision. The structure is the receptor, and the harmful outcome is the recorded collapse. Each link can be assessed separately, which matters because the disputes are often about a single link: whether the surge was predicted, whether the debris came from a source that should have been secured, whether the structure met its design standard. The split also prevents a familiar rhetorical move, in which a natural event is either blamed as if it were a person or cleared of any role in the harm. Its causal role is recorded, and its moral role is left to the assessment.

## 8. Witness error as a causal chain: act, data and institutional mechanism

**Session wording (author):** "a witness who was impaired remembers details of looting activity that is incorrect and gets the wrong person arrested who then incurs hundreds of thousands of dollars in legal defence and private investigative fees."

**Session wording (author):** "so a false testimony might be an event where false testimony data might be the actual data that arose from that event"

- **Extended:** the causal chain to include epistemic error, not only physical force.
- **Accomplished:** the testimony event (`FalseTestimonyEvent`) is separated from the information it produces (`FalseTestimonyData`, a `dul:InformationObject`). The data persists and travels, and an institution can take it as input.
- **Enabled the model to represent:** cognitive impairment, then a communicative act, then persistent data, then an institutional mechanism, then a wrongful arrest, then downstream financial and somatic harm.
- **Distinctive:** it links an internal state of a person to an external harm without treating the person as a malicious agent.

**Discussion.** This case showed that a complete causal chain can be built with no villain and still produce large, real harm. The witness is not lying and is not malicious. Their impaired memory is a quality of the person, and the faulty recall is a part of their cognitive life. The author's distinction between the act and its data is the key move. The testimony event happens once, at a specific time and place, while the data it creates can be copied, filed, summarized and relied upon long afterward. A detective who reads a statement is not taking part in the witness's recall. They are consuming an information object, and their investigation is a mechanism operating on that object. This is why the chain cannot be read as a simple sequence of people. The harm passes through documents and procedures, and each of those can carry the error forward. The wrongful arrest is then an event whose assessed object is the innocent person, and whose outcome includes the fees, the reputational injury and the stress. The case also shows where the legal and psychological dimensions diverge. The fees are a legal and financial harm. The stress and cognitive injury are psychological. A single chain can carry both, which is the reason the next entry separates their property paths.

## 9. Modular domain properties over a shared instance graph

**Session wording (author):** "if you implement the modular approach with appropriate namespaces, would the instances that carry the domain-specific values for these domain-specific properties have to be modular and have their own respective namespaces as well?"

- **Extended:** the single causal chain schema into modules, such as `psych:` and `legal:`, that extend a shared core.
- **Accomplished:** schema (TBox) is modular. Instances (ABox) live in one shared namespace, so one individual can carry psychological and legal assertions at once.
- **Enabled the model to represent:** analytic isolation. A query can load only the psychological module and ignore legal assertions about the same person.
- **Distinctive:** one entity, many lenses. Slicing happens in the schema, not in the data.

**Discussion.** The author's question went to the heart of how modular ontologies stay coherent. The answer was that instances do not need their own namespaces. A namespace marks where a term is defined, not what kind of thing an individual is. If the wrongly accused person were split into a psychological individual and a legal individual, the system would have two records for one human being, and no reliable way to say they were the same. Keeping one shared instance graph preserves identity, and modularity is handled by which property vocabularies are loaded. A psychological view and a legal view of the same person then differ only in which assertions are visible. This also protects against a quiet error. If a legal module asserts that a person incurred a financial harm, and a psychological module asserts a distress response, those are two facts about one person, and a query that joins them should be able to show that. Splitting the individual would make that join impossible. The design choice links directly to the temporal and grounding entries above, since assertions about the same entity may come from different assessments with different evidentiary bases. The decision was recorded as Ontological Commitment 01 in the chat, but it is not yet in the vault. It is proposed and awaits the author's confirmation.

---

## Open items arising from these notes
- Whether `Harmfulness` is kept as a reified class (Section 5) or replaced by first-class `AssessedHarmfulness` (see pending decision note).
- The grounding score and inheritance rule for `AssessedImaginedHarm` (Section 3): are they meaningful across domains?
- Verify the DUL-aligned parent classes against the published DUL OWL file (Section 6).
- Whether harmfulness criteria belong to technical standards or moral principles (Section 5).
- Whether Ontological Commitment 01 (Section 9) and the temporal split (Section 1) become governing commitments once the author confirms them.
