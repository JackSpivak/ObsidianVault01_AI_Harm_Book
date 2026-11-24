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

*Record of the realizations from the 2026-11-23 session. Each entry gives the wording from the session (quoted, with cuts marked "…"), then the same four framings used in [[Harm Ontology v3 Design Notes - Assessment Architecture and Core Realizations]]: what it **extended**, what it **accomplished**, what it **enabled the model to represent**, and what was **distinctive**. A **Discussion** follows each entry. Items still awaiting your confirmation are listed in [[Pending Design Decision - Harmfulness as Reified Class]], not here. Nothing here is logged in [[Decisions_Log]] yet.*

---

## 1. Temporal split: AssessedHarm is past or present only

**Session wording (author):** "i think that assessed harm probably needs to be tied to harm that actually occurred in the past and/or one that is concurrently occurring. i think it is disingenuous and conflating to label assessedharm when it is an assessment of future harm. that would really require a crystal ball. we need other language."

- **Extended:** the earlier `AssessedHarm` class, which had been used for both actualized and projected harm.
- **Accomplished:** `AssessedHarm` is restricted to harm that has occurred or is occurring. Projection of future harm gets its own family of terms.
- **Enabled the model to represent:** the difference between an empirical record and a forecast, so a forecast can never be mistaken for a record.
- **Distinctive:** the line is drawn on the timeline, not on the quality of the evidence. Even a well-grounded forecast is still a forecast.

**Discussion.** Risk writing routinely says "the storm will cause $4bn in harm" or "this model will cause catastrophic harm." Both sentences use the language of records for claims that cannot yet be checked. Restricting `AssessedHarm` to past and present makes that slippage visible. Candidate names for future-oriented projection were AssessedPotentialHarm, AssessedPostulatedHarm and AssessedImaginedHarm.

## 2. AssessedImaginedHarm as the name for projection

**Session wording (author):** "personally i like AssessedImaginedHarm - which can still take all the severity and scale weight that an active imagination can project."

- **Extended:** the temporal split in Section 1 into a named class for future projection.
- **Accomplished:** the term admits that projection is imaginative construction while leaving room for its severity and scale to be taken seriously.
- **Enabled the model to represent:** a projection that is large and serious but openly modeled, so it can be graded instead of dismissed or accepted at face value.
- **Distinctive:** it is the most candid of the candidate names, and the one that makes the grounding requirement in Section 3 necessary.

**Discussion.** Critics of climate models and of AI existential-risk forecasts often object to the imaginative leap from present proxies to catastrophic futures, not to the arithmetic. Calling the output "imagined" concedes the point the critic cares about and then asks what grounds the imagination. The name also avoids the opposite error of dismissing projections as merely "arbitrary."

## 3. Grounding the imagination: evidentiary basis and vetting

**Session wording (author):** "we already have some properties related to vetting and evidence that could be attached to require that imagination is grounded in some kind of objective observable data"

**Session wording (author, on scientific responsibility):** "scientists should be able to (and are able to unless they have been irresponsible or deceitful) provide the evidentiary basis for the model, its structure, testing, independent vetting and match between prediction and reality. they don't have to do this each time someone claims it is arbitrary or imaginative. the individual basis artifacts (or maybe the whole perspective (if its core principles have been sufficiently verified?) could be deemed reliable (at least with respect to its core principles)"

- **Extended:** `AssessedImaginedHarm` from a name into a graded claim with provenance.
- **Accomplished:** a projection can be audited for its evidentiary basis, its vetting, and how well past predictions matched outcomes, without rerunning the whole argument each time.
- **Enabled the model to represent:** the grounding chain (`hasEvidentiaryBasis`, `hasVettingCriterion`, a grounding score, an `AssessmentHorizon`) and the inheritance of reliability from a vetted perspective or pipeline to the projections it produces.
- **Distinctive:** trust is placed in the generative pipeline and its verified core principles, so each individual output does not have to be re-justified from raw data.

**Discussion.** Radical skepticism treats every model as imagination. Naive realism treats every model as a map of reality. The author's position sits between them: a model is disciplined imagination, and its discipline can be shown through its structure, testing and track record. The inheritance idea means a projection can say "this is generated by a perspective whose back-testing fidelity is X over a window of Y years." The author's own summary was: "Validating the Generative Pipeline (Perspectives & Baselines) rather than just the isolated output."

**Caution:** the grounding score and the inheritance rule are proposals, not settled design. Whether a score can be meaningful across domains is open.

## 4. Harmfulness is not an ontic property; it is an assessment

**Session wording (author):** "someone or some organization may believe because of the triad of object capability that someone or something is harmful. but inevitably that is an assessment. weather predictions are famously fallible and speaking of the storm as harmful may depend on the attributedMechanism being flawed. maybe sea and atmospheric temperatures are believed to be critically moving a normal storm into a severely harmful one. but sensor data is flawed and skews the required mechanism"

- **Extended:** the earlier triad in which Harmfulness was treated as a physical, objective disposition of an object or actor.
- **Accomplished:** it corrects a drift in the earlier framing. Calling a storm or a gun "harmful" is always a judgment that depends on a mechanism model, so Harmfulness cannot sit outside an assessment.
- **Enabled the model to represent:** failure modes. A storm can be wrongly classed as harmful because a sensor is skewed, and that is a fault in the assessment, not in the storm.
- **Distinctive:** it removes the "view from nowhere." Physical objects keep their capabilities, and everything about harm is an assessment of them.

**Discussion.** The gun-rights argument ("the gun is neutral; it becomes dangerous only in certain hands") is the same debate. Capability is a fact about the object. Harm is an evaluation of that capability within a causal context, and the evaluation depends on the actor, the mechanism and the criteria. The author's suggestion that AssessedHarmfulness might be a subclass of Harmfulness is one option. The alternative, that Harmfulness is dropped and AssessedHarmfulness becomes first-class, is recorded in the pending decision note.

## 5. Harmfulness as a reified class with its own properties

**Session wording (author):** "I am thinking of it rather as a thing 'class' that can have all of its own properties to be reasoned over - like assessor, hasobjectivestandard or hasharmfulnessCriterion (or maybe harmfulness criterion is a subclass of ObjectiveStandard and is in the domain of hasHarmfulnessCriterion"

- **Extended:** the earlier treatment of Harmfulness as a property or scalar.
- **Accomplished:** Harmfulness becomes a class that can be reasoned over, with properties for the assessor, the objective standard and the criteria.
- **Enabled the model to represent:** candidate properties `hasAssessor`, `hasObjectiveStandard`, `hasHarmfulnessCriterion`, with `HarmfulnessCriterion` as a subclass of `ObjectiveStandard`.
- **Distinctive:** the class is the reasoning object. Its properties say who judged, against what, and by which criterion.

**Discussion.** This is open. It fits the Principles-and-Standards pattern in [[Harm Ontology v3 Design Notes - Assessment Architecture and Core Realizations]] (Section 6), where a `[Domain]Standard` class sits between principles and assessments. The open question is whether a harmfulness criterion is a standard in the technical sense (an IEEE-type code) or a principle in the moral sense. See the pending decision note.

## 6. Causal chains are occurrent structures with participants, not subclass trees

**Session wording (author):** "so it sounds like the notion of membership in the chain can be represented structurally through the use of classes and object properties however the assessment of completeness or flawedness must be layered on through shacl rules (most likely)"

- **Extended:** the causal chain from a flat list of components into a structure built from DUL-style occurrents and participants.
- **Accomplished:** membership in a chain (Actor, Event, Capability, Mechanism, ObjectOfHarm, HarmfulOutcome) is expressed through object properties. Completeness is checked by a separate constraint layer.
- **Enabled the model to represent:** that only objects and agents participate in events. A process is not a participant. An impaired memory is a quality of a person, and the faulty recall is a part of that person's cognitive life.
- **Distinctive:** structure says what can be linked. SHACL says what must be present for the chain to count as complete.

**Discussion.** OWL is monotonic and works under the open-world assumption, so a missing actor is unknown, not invalid. Completeness is a non-monotonic judgment, so SHACL `sh:minCount` shapes are the right layer. The schema was checked against DOLCE+DnS Ultralite (DUL), where `dul:Event` and `dul:Object` are the main top-level division and `dul:hasParticipant` relates objects to events. **Caution:** the DUL-aligned table and tree produced during the session were drafted from memory of DUL and have not been checked against the published OWL file. Some parent-class assignments may be wrong.

## 7. Storms, causal cascades and non-agents

**Session wording (author):** "if a storm causes harm, who would be the required ex:Actor? the storm? the kinetic impact of waves? floodwater due to surge? windblown debris?"

- **Extended:** `Actor` from "whoever does it" to "whatever initiates or drives the sequence."
- **Accomplished:** a storm is not a `dul:Agent`. It is a physical participant or origin, and the cascade (surge, debris, structural collapse) is a chain of events and mechanisms.
- **Enabled the model to represent:** cascades as nested events and mechanisms, with the root source linked as a participant, not an actor.
- **Distinctive:** it separates agency from causal origin, which is what makes natural hazards and institutional failures comparable in one schema.

**Discussion.** Natural forces have no intention, but they still start harm. Keeping "actor" for agents and using participant or source for physical origins avoids the category error of calling a hurricane responsible.

## 8. Witness error as a causal chain: act, data and institutional mechanism

**Session wording (author):** "a witness who was impaired remembers details of looting activity that is incorrect and gets the wrong person arrested who then incurs hundreds of thousands of dollars in legal defence and private investigative fees."

**Session wording (author):** "so a false testimony might be an event where false testimony data might be the actual data that arose from that event"

- **Extended:** the causal chain to include epistemic error, not only physical force.
- **Accomplished:** the testimony event (`FalseTestimonyEvent`) is separated from the information it produces (`FalseTestimonyData`, a `dul:InformationObject`). The data persists and travels, and an institution can take it as input.
- **Enabled the model to represent:** cognitive impairment → communicative act → persistent data → institutional mechanism → wrongful arrest → downstream financial and somatic harm.
- **Distinctive:** it links an internal state of a person to an external harm without treating the person as a malicious agent.

**Discussion.** This is the case that showed a complete chain can be built with no villain and still produce large, real harm. It also showed that legal harm and psychological harm need separate property paths.

## 9. Modular domain properties over a shared instance graph

**Session wording (author):** "if you implement the modular approach with appropriate namespaces, would the instances that carry the domain-specific values for these domain-specific properties have to be modular and have their own respective namespaces as well?"

- **Extended:** the single causal chain schema into modules, such as psych: and legal:, that extend a shared core.
- **Accomplished:** schema (TBox) is modular. Instances (ABox) live in one shared namespace, so one individual can carry psychological and legal assertions at once.
- **Enabled the model to represent:** analytic isolation. A query can load only the psychological module and ignore legal assertions about the same person.
- **Distinctive:** one entity, many lenses. Slicing happens in the schema, not in the data.

**Discussion.** The answer was that instances do not need their own namespaces. Namespaces mark where a term is defined, not what a thing is. This decision was recorded as Ontological Commitment 01 in the chat, but it is not yet in the vault. See the pending decision note.

---

## Open items arising from these notes
- Whether `Harmfulness` is kept as a reified class (Section 5) or replaced by first-class `AssessedHarmfulness` (see pending decision note).
- The grounding score and inheritance rule for `AssessedImaginedHarm` (Section 3): are they meaningful across domains?
- Verify the DUL-aligned parent classes against the published DUL OWL file (Section 6).
- Whether harmfulness criteria belong to technical standards or moral principles (Section 5).
- Whether Ontological Commitment 01 (Section 9) and the temporal split (Section 1) become governing commitments once the author confirms them.
