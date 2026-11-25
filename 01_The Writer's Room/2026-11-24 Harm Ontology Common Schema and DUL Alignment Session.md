---
type: session
status: archived
tags: [ontology/harm, schema, dul, determinations, bearer]
aliases: [2026-11-24 Harm Ontology Schema Session, Common Schema and DUL Session]
created: 2026-11-24
session_date: 2026-11-24
participants: [Author, "Copilot assistant (model not recorded in transcript)"]
source: "copilot/copilot-conversations/agent__i_want_to_develop_a_common_schema_that_will_organize@20261124_213159.md (ran 2026-11-24 21:31 to 2026-11-25 02:30)"
workstream: "[[Handoff - Harm Ontology]]"
harvested_through: "2026/11/25 02:30:54"
continued_in:
topics: [HarmDetermination, determination-subclasses, DUL, IRI-reference, AffectedEntity, ImpactedRole, bearer, EmergentWhole, unitySource, FunctionalHarm, competency-questions, actor-taxonomy]
---

# 2026-11-24 Harm Ontology: Common Schema and DUL Alignment Session

## Summary
- Started from the author's wish for a common schema, and from the question whether vocabulary should be narrative only, OWL classes, or a mix. Compared a schema-heavy approach with a split approach (reasoning in OWL, narrative in SKOS). Recommended the split, then tested it on the surgeon case and the surgeon-sued case.
- Settled that every harm is a **HarmDetermination**, with subclasses by the question answered. Proposed determination classes for identification, exposure, relevance, chains, responsibility, consent and remedy, alongside harm.
- Set up competency-question testing: a test note and a coverage matrix in both directions (questions to classes, classes to questions).
- Aligned the proposed schema to DOLCE+DnS Ultralite (DUL) by IRI reference, and logged the decision. Mapped acts, events, agents, situations, roles and information objects, and recorded where DUL has no home for our classes.
- Worked through actors and affected entities: physical versus social, the kinds of organised and emergent collective, and the bearer of a harm. Settled that harm attaches to a bearer's state, and that functional harm is a subclass of HarmDetermination.
- The shared-tree document was not replaced in the vault. The tree in the chat (02:30) is the current version. The saved note still predates it.

## Decisions made
- Shallow actor/object tree: subclass only on physical versus social. Collectiveness is the open `unitySource` property, and `unityLocus` holds who holds unity. Finer distinctions wait for a failing case. → [[Decisions_Log]] (2026-11-25)
- AffectedEntity replaces Receptor. The object side is AffectedEntity (affectability is a property); the role is ImpactedRole, scoped to a consequence. → [[Decisions_Log]] (2026-11-25, amended the same day)
- DUL is used by IRI reference only, for testing. Import or copy waits for the licence (T1). → [[Decisions_Log]] (2026-11-25); ledger T1 narrowed.
- Named bodies (FAA, OSHA, NRC, Boeing) are instances. RegulatoryInstitution and Corporation are the classes. Regulator is a role. Legal personhood is a determination. → proposed tree only, **not logged**
- Harm attaches to a bearer's state, and `hasBearer` ranges over Entity (Object, Situation or Event). → proposed, **not logged**
- Functional harm is a subclass of HarmDetermination (`FunctionalHarmDetermination`), with impairment subclasses (availability, integrity, confidentiality) marked provisional. The author asked to include it "right now". → in the tree, **not logged**
- Emergent wholes (flock, formation, herd, tribe) are bearers, with capability, unity and persistence as their own harm targets. → proposed, **not logged**

## How the thinking moved
- **Pros and cons of the split.** The assistant set out the split (reasoning in the schema, narrative in SKOS) and its costs: the reasoner can't infer across the SKOS narrative, bridges need maintenance, and queries get more complex. The author pressed on how to reason over the richness, asking which two perspectives differ on a harm at a given horizon. The answer was to put richness into structural properties on determinations (`manifestsAs`, `hasModality`, `isSubstrateOf`) and link them to SKOS concepts, not to add OWL classes.
- **Surgeon case, then the surgeon sued.** The surgeon case gave three perspectives on one psychological effect. The surgeon's view was low severity; the patient's legal view was high severity; the expert's view was moderate and partly avoidable. Three determinations of one class, with a divergence between them. The assistant proposed that the perspectives differ in determinations, not in classes.
- **Shared subclass.** Confirmed HarmDetermination as the parent of substrate kinds (somatic, psychological, pecuniary, normative status). The assistant then proposed a wider Determination root with the other determination kinds.
- **Determination subclasses by question answered.** The author asked for diagnostic and investigative determinations, plus situational, circumstantial, predisposing-cause and relevant-state determinations. Proposed: Condition, Investigative, Exposure, Relevance, Chain, Responsibility, Consent, Remedy, plus a separate Compliance branch. Trigger and predisposition are weights on a Relevance determination, not classes. A causal boundary and a horizon are declared parameters, not computed outputs.
- **Question sufficiency.** The author asked how to know the question set is good enough. Four sources (use cases, external standards, the layers themselves, failure cases) and four checks per question (answerable from the schema, attributable, traceable to a stakeholder, testable on a case). The assistant suggested a coverage matrix. The author agreed and asked for a note. The test note was created and the matrix added (section 4a).
- **DUL licence.** The assistant first treated DUL as needing a licence for subclass links, then reversed: IRI references are normal semantic-web practice, and the earlier caution applied to importing or copying. The author then decided on IRI reference for testing.
- **Alignment table.** Acts, processes, effects, agents, objects, roles, information objects, descriptions and the thin container all have DUL homes. Gaps: no State class (Quality with a TimeInterval, or a Situation); omission; an Action needs an agent, so structural acts become Events; physical situations are social objects in DUL; consent and remedy partial; divergence, missingness, valence and omission type are ours by design.
- **Act, event and agent rule.** An agentive act is a `dul:Action`; a non-agentive change is a `dul:Event`; an unknown agent stays an Event with a missingness status. The author accepted this in principle.
- **Corporations and regulators.** Initially "social agents", then the author asked whether they should be subclasses with instances. The assistant agreed. Regulator is a role, so the class is RegulatoryInstitution, defined by its founding charter.
- **AffectedEntity name conflict.** The name covered both the object that can be harmed and the role played for a consequence. The assistant offered two options; the author chose keeping the entity and renaming the role to ImpactedRole, because impact is known only relative to a consequence.
- **Pushback on over-specification.** The assistant kept proposing distinctions (unity sources, procedure versus coupling, four sources of unity). The author said this was "a lot of overthinking" and asked for a model robust enough to add distinctions as cyber and ecosystem cases arrive. The rule chosen: a shallow tree, an open property, extend only when a competency question fails.
- **Object vs entity.** The assistant first described Entity as a subclass of Object, which was wrong. In DUL Entity is the top class; Object, Event and Abstract sit under it. The author noted the distinction was still unclear, and the assistant corrected the direction.
- **Harm to wholes.** The author pressed that harm to an emergent whole (a flock, a formation) must be capturable. Harm can fall on capability, on unity, or on persistence. Unity is a time-indexed state. The author's formation example is the test case.
- **Bearer of a harm.** The assistant proposed three declared fields: bearer, judged state, horizon. The author asked "dont' we have an object (in dul sense) or an event or a situation that can be the bearer?" The answer: `hasBearer` ranges over Entity.
- **Functional harm.** The author asked whether impairment of function is an injury. Yes, and it suits cyber harm (loss of availability, corruption, disclosure). Functions are assigned by a perspective, so impairment is always relative to a function someone has assigned. The author asked for FunctionalHarmDetermination in the tree.

## Concepts introduced
- **HarmDetermination**: the shared parent of harm outputs, a versioned InformationObject expressing a Description, with bearer, judged state, horizon and assessor. → promote to idea note? (y)
- **Determination branch**: Determination as the output root (Capability, Harmfulness, Chain, Responsibility, Harm, and others). → promote? (y, with the question-answered rule)
- **ImpactedRole**: a Role that classifies an AffectedEntity, scoped to a consequence. → promote? (y)
- **hasBearer / judgesState / atHorizon**: the three declared fields of a harm determination. → promote? (n, record in the tree)
- **EmergentWhole**: a bearer whose capabilities, unity and persistence are its own, constituted by members through `dul:hasConstituent`. → promote? (y)
- **unitySource / unityLocus / unityState**: how a group acts as one (procedure, commandAndControl, coupling, norms), who holds that unity, and its intact/degraded/broken state over time. → promote? (y)
- **FunctionalHarmDetermination**: a HarmDetermination whose state judged is a function, assigned by a perspective. → promote? (y)
- **RegulatoryInstitution**: a SocialAgent kind fixed by a founding charter or statute; regulator is a role. → promote? (n)
- **Competency-question coverage matrix**: questions against classes, in both directions. → test note only (n)

## Open questions
- **State**: is it a Quality with a TimeInterval, or a Situation? Still open.
- **ExposureSituation**: a physical situation is a social object in DUL. Is that a real tension, or can it be settled by naming?
- **Natural individuals and systems**: is a river a `dul:PhysicalObject` or our own NaturalIndividual? Is an ecosystem a Situation or a Collective? Watersheds as Places?
- **Community, Group, Collection, CollectiveAgent**: do they match DUL's definitions? Unverified.
- **Event or Situation as bearer**: how often is the judged state a function, not an injury, and does that need its own determination class?
- **Determination classes**: is ConditionDetermination a subclass of Determination in its own right? Is ComplianceDetermination core or a discipline module?
- **Declared bearer**: should a bearer be declared, or inferred from roles? The author's preference leaned to declared.
- **Cyber impairment subclasses**: are availability, integrity and confidentiality the right starting set? To be tested on the first cyber case.
- **DUL version**: the mirror read was 3.22. Other hosts report 3.32 and 4.2. The version must be confirmed before alignment is final.

## Original wording
> "i want to make sure our model is robust enough to add them as needed"
- **Attribution:** Author (from: "this seems like a lot of overthinking. which i do. if we begin to consider cyber harm which i hope to do and ecosystem harm these distincctions will become relevant. i want to make sure our model is robust enough to add them as needed")

> "lets have a decision for now to clean up receptor vs AffectedEntity. use AffectedEntity"
- **Attribution:** Author

> "i think you are being to proscriptive. being affected is a role but being an Entity is an object, thats the problem - the name conflates them. either perspective is reasonable"
- **Attribution:** Author

> "I like a. and i like impactedRole for exactly the reason you named needing to know the consequence to see if someone/thing is impacted seems like an epistemic problem"
- **Attribution:** Author

> "for now lets have a decision to use dul by iri reference for the purpose of testing the integrateablity and also whether all the base classes we believe are necessary are in fact subclasses of a well designed upper ontology"
- **Attribution:** Author

> "harm to an emergent whole is essential to be able to capture. wholes have properties, behaviors and capabilities that exceed the "sum of the parts"."
- **Attribution:** Author

> "so i am still back to the original problem. dont' we have an object (in dul sense) or an event or a situation that can be the bearer of an effect"
- **Attribution:** Author

> "wait a minute. isnt an impairment or undesirable modification of function an injury/harm. i am thinking that this would apply well to cyber harms that damage function"
- **Attribution:** Author

> "lets include functional harm right now. would that be FunctionalHarmDetermination? show this in the tree"
- **Attribution:** Author

> "i am still concerned as you point out in the cons that we lose the ability to reason over the richness unless we address it somehow in a different way. if i want to know which two perspectives differ on the assessment of harm and why at a given temporalhorizon how can we create an affordance for that?"
- **Attribution:** Author

> "Maybe we need a note for testing the model structure and pull the competency questions, key insights from this part of the conversation there as well as the work we are about to do on this matrix"
- **Attribution:** Author

> "if dul is publically served then we do not need license to create rdfs:subClassOf links do we? wouldnt that just be if we wanted to download dul and use it locally?"
- **Attribution:** Author

Note: the assistant's replies are paraphrased in this note. Quotes are copied from the transcript as the author typed them, including their spelling.

## External references
| Reference | Used for | Status (verified / from memory / unverified) |
|---|---|---|
| DOLCE+DnS Ultralite (DUL), Gangemi; ODP | Upper ontology for alignment, by IRI reference only | Mirror read at version 3.22 (per chat). Other versions reported (3.32, 4.2). Licence unresolved (T1). Class names from the file, but several classes still unchecked |
| ISO 14971 (hazardous situation); NIST SP 800-30; STPA | Question sources for the sufficiency test | From memory (per chat); not checked in this session |
| CIA triad (availability, integrity, confidentiality) | Starting subclasses for functional impairment | From memory (security convention); unverified against a standard |

## Artifacts touched
- Read: [[Handoff - Harm Ontology]], [[Decisions_Log]], the Harm Ontology v0.03.1 folder notes (ledger, proposed tree, test note).
- Created: [[Model Structure Test Note - Competency Questions and Coverage]] (test note, Proposed, not logged).
- Created: [[Proposed Class Tree and DUL Alignment]]. **Saved version is out of date**; the current tree is in the chat (02:30). Replacing it is an open follow-up.
- Edited: [[Decisions_Log]] (three 2026-11-25 entries, T1 narrowed), [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] (T1), [[_Harm Ontology v0.03.1 Master Index]] (sections 4 and 6).
- Tool or model errors: quota-limit errors interrupted replies at 00:50 and 01:23 (the answer was given after "resume"). Not a loss of content.

## Follow-ups
- [ ] Author: confirm whether to replace the saved proposed tree with the 02:30 version (bearer, FunctionalHarm, EmergentWhole, determination branch).
- [ ] Log or propose as decisions: harm attaches to a bearer's state (`hasBearer` over Entity); functional harm as a HarmDetermination subclass; emergent wholes as bearers; the determination branch. None are in [[Decisions_Log]] yet.
- [ ] Add to the ledger: the determination branch, bearer/judgesState/atHorizon, FunctionalHarm, EmergentWhole, unityState, and the open questions above.
- [ ] Run the coverage matrix (section 4a of the test note) against the surgeon-sued case.
- [ ] Verify the marked (P) classes and the DUL version against the published file (ledger S41).
- [ ] Settle State (Quality or Situation), since the matrix and tree both depend on it.
- [ ] Reconcile older v3 notes (HO-002.a, draft structure) that still use "Receptor".

## Closing checklist
A session = one Copilot chat, from its first message to this checklist. Pauses don't end it.
- [x] Harvest new ideas (incremental, from `harvested_through`): concepts listed above; ideas for filing as notes to be confirmed by the author.
- [x] Update `harvested_through` (2026/11/25 02:30:54)
- [x] Add anything after the last update to this note
- [x] Rewrite the workstream's Handoff note (forward-facing, short)
- [x] Set `status: archived`; `continued_in` set at the next session close
- [ ] Rename the chat in Copilot history: "[CLOSED] Harm Ontology common schema and DUL → see session note" (author action)
- [ ] Start a new chat with the Handoff note attached. Don't reopen this one; read its transcript selectively if needed.

## Related
- [[Handoff - Harm Ontology]]
- [[Decisions_Log]]
- [[Proposed Class Tree and DUL Alignment]]
- [[Model Structure Test Note - Competency Questions and Coverage]]
- [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]]
- [[2026-11-22 Harm Ontology Ledger and Assessment Session]]
