---
title: Design Note - Harm Ontology v0.03.01 Gap Assessments (Structured Inquiry Synthesis)
type: design-note
skill: structured-inquiry-epistemic-unfolder
skill_version: "1.0"
grounding_mode: LLM Parametric Baseline
status: hypotheses-to-test
input_a: "What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations?" [Explicitly Provided by User]
input_b: "Option 3 - LLM Parametric Baseline" [Explicitly Provided by User]
input_c: "General AI-harm and risk-ontology scholarship" [Assumed by Skill]
input_d: "Representational adequacy of v0.03.01 against real-world AI harm situations" [Assumed by Skill]
input_e: "Moderate rigor, narrative level" [Assumed by Skill]
input_f: "Contemporary AI deployment era" [Assumed by Skill]
input_g: "Collected set of gap assessments, each with a 2-5 sentence summary, numbered bullets of 2-5 sentences, and a single 200-250 word explanation; design note generated on Halt & Synthesize" [Explicitly Provided by User]
sections_delivered: 26
---

# Harm Ontology v0.03.01: Gap Assessments (Structured Inquiry Synthesis)

> [!warning] Epistemic caveat
> Grounding mode was LLM Parametric Baseline, so vault access was cut off during the inquiry. The v0.03.01 schema was never read. Every assessment below is a hypothesis drawn from general harm-ontology scholarship. Each ends with a practical test to run against the actual schema.

## Overview

The inquiry unfolded six macro-level gaps and then drilled into five of them. Pointer moves are noted in each section.

| Macro gap | Sub-levels delivered |
|---|---|
| 1.00 Temporal and processual structure | 1.01 to 1.04 |
| 2.00 Distributed causation and attribution | 2.01 to 2.04 |
| 3.00 Context, vulnerability and relational severity | 3.01 to 3.04 (3.05 not delivered) |
| 4.00 Non-individual and non-human bearers | 4.01 to 4.04 (4.05 not delivered) |
| 5.00 Epistemic status, uncertainty and trade-offs | 5.01 to 5.04 |
| 6.00 Granularity, abstraction and interoperability | none |

**Not delivered (open items):** 3.05 observed versus experienced harm, 4.05 the missing claimant, and sub-levels under 6.00.

**Final assessment at halt:** Saturation High. Marginal returns Low to Moderate. Convergence achieved for the initial roadmap. Utility High Leverage. Further value lies in validating against the real schema, not in more parametric unfolding.

---

## 1.00 Gap: Temporal and Processual Structure of Harm

**Summary:** Harm ontologies usually treat harm as a discrete, timestamped event. Real AI harms often build up gradually, stay latent, escalate, recur or recover over time. If v0.03.01 treats time only as an event attribute, it probably cannot represent these trajectories.

**Key points:**

1. **Accumulation.** Many harms arise from repeated low-level exposures, not one incident. Examples are a recommender slowly shifting a teenager's self-image and a hiring filter narrowing a career over years. An event-only model records each exposure as trivial or misses the pattern entirely.
2. **Latency and delay.** The damaging decision may be made at deployment while the consequence appears months later, or only when conditions change. Without an onset-delay construct, cause and effect cannot be linked across that gap. This weakens foreseeability and accountability analysis.
3. **Phases and escalation.** Harms move through exposure, onset, amplification, stabilization and residual effects. A single record flattens these phases. That hides where an intervention would have changed the course.
4. **Reversibility and recovery.** Whether a harm can be undone, and how long recovery takes, shapes its real severity. Ontologies that record only that harm occurred cannot distinguish a temporary setback from permanent damage. Remediation timeliness cannot be assessed either.
5. **Pattern linkage.** Minor incidents may belong to a larger recurring or escalating pattern. Without a process entity that groups events, each is classified in isolation. The aggregate harm stays invisible.

**Explanation:**
Most harm ontologies model harm as a discrete event: an incident occurs, an affected party suffers a loss, a category is assigned. Real AI situations rarely behave this way. Harm often accumulates through repeated low-level exposures, or stays latent until conditions change. An ontology lacking first-class representation of duration, onset delay, escalation, recurrence, reversibility and recovery will flatten these trajectories into a single timestamped record. That discards what makes them hard to detect and remedy. The likely missing constructs are a harm process or trajectory entity distinct from the harm event, with phases (exposure, onset, amplification, stabilization, residual effects). Also likely missing are thresholds separating tolerable from damaging accumulation, and explicit links to intervention points where the course could have been altered. Without these, the ontology cannot answer when a harm became foreseeable, whether remediation arrived in time, or whether a minor incident belongs to a larger pattern. It also cannot support early-warning analysis, because the signals of a developing harm are only visible as a sequence. The practical test for v0.03.01 is whether time appears merely as an attribute on events, or as a structural dimension that organizes events into processes with phases, thresholds and intervention opportunities. If the former, trajectory-based harms will be systematically under-represented, and the ontology will bias toward dramatic, discrete incidents.

### 1.01 Sub-Gap: Cumulative Exposure and Threshold Effects

**Summary:** Within the temporal gap, the most concrete problem is how harm builds up from many small exposures. Individual exposures may each fall below any threshold for recording, yet together cross into real damage. If v0.03.01 records only incidents that already pass a severity bar, cumulative harms will remain invisible until late.

**Key points:**

1. **Sub-threshold exposures.** Each interaction may be harmless on its own, such as one recommendation or one minor score adjustment. An event-based schema has no reason to record it. The accumulated effect is then unrepresented.
2. **Dose and duration.** Harm often depends on how much exposure occurred and over how long. Attributes for frequency, intensity and cumulative duration are needed. A yes-or-no occurrence flag cannot carry them.
3. **Tipping points and thresholds.** Accumulation can be linear, or it can cross a point after which effects become severe or irreversible. The ontology needs a way to mark threshold crossings. Without it, the moment a harm became real cannot be identified.
4. **Exposure-to-harm linkage.** Exposure and harm are distinct things, and the same exposure leads to harm for some bearers and not others. A model that treats exposure as just a cause field loses this. Separate exposure and harm entities, with a conditional link, would capture it.
5. **Aggregation across sources.** A person may be exposed to the same type of harm through several systems at once. Each system's record looks minor when viewed alone. Cross-system aggregation requires a shared bearer-centered view.

**Explanation:**
Cumulative harm is among the hardest cases for event-based ontologies. A single recommendation, a minor score adjustment or one slightly biased response may each be unremarkable, and under a schema that records only incidents passing a severity bar, none would be logged. Yet repeated exposure over weeks or years can produce real damage, such as distorted self-perception, narrowed opportunity or entrenched belief. To represent this, an ontology needs exposure as a first-class entity separate from harm, with attributes for frequency, intensity and cumulative duration. It also needs a notion of threshold or tipping point, so that the crossing from tolerable to damaging can be marked, along with whether effects became irreversible. Because the same exposure harms some bearers and not others, the link from exposure to harm must be conditional on bearer characteristics rather than assumed. A further complication is aggregation across sources: a person may be exposed to the same type of harm through several systems at once, each of which appears minor in isolation. Seeing the total requires a bearer-centered view that pools exposures across systems and operators. Without these elements, the ontology will favor dramatic single incidents, underestimate slow harms, and give no basis for early warning. The practical test for v0.03.01 is whether it can record an exposure that caused no recordable harm at the time, and later link it to a threshold crossing.

### 1.02 Sub-Gap: Latency and Delayed Onset

**Summary:** Some harms appear long after the decision or event that caused them. The damaging choice may be made at design or deployment, and the consequence surfaces months or years later, or only when conditions shift. If v0.03.01 ties a harm to the time it was observed, it cannot link cause and effect across that gap.

**Key points:**

1. **Separation of cause time and effect time.** A training-data choice or a deployment decision may precede visible harm by a long interval. A single timestamp on the incident cannot hold both moments. Two distinct temporal anchors are needed, one for the originating decision and one for the onset of harm.
2. **Condition-dependent activation.** A latent defect may stay dormant until an input distribution, user population or environment changes. The harm then appears abruptly, though its origin is old. The ontology needs a way to represent a dormant hazard and the trigger that activated it.
3. **Discovery lag.** Harm may exist for a long time before anyone detects it. Observation date and onset date are different facts. Conflating them distorts duration and misdates responsibility.
4. **Foreseeability over time.** Whether a harm was foreseeable depends on what was known when the decision was made. Later knowledge should not be projected backward. The ontology needs time-indexed knowledge states to support fair assessment.
5. **Retrospective linkage.** Connecting a late harm to its distant origin requires traceable links to design, data and deployment records. Without such provenance, the link is lost once the system is updated or retired. Persistent identifiers for system versions would help.

**Explanation:**
Many significant AI harms are separated from their origin by a long interval. A choice about training data, a threshold setting or a deployment context may be made at one moment, while the resulting damage surfaces months or years later, or only when conditions change, such as a new user population or a shift in input distribution. An ontology that attaches a single timestamp to the incident cannot hold both moments, and so cannot connect cause and effect across the gap. It needs at least three distinct temporal anchors: when the originating decision or hazard was introduced, when harm actually began, and when it was discovered or reported. Conflating these distorts duration, misdates responsibility and hides discovery lag. It also needs a representation of a dormant hazard and the trigger condition that activated it, since latent defects behave differently from active ones. Assessing foreseeability fairly requires time-indexed knowledge states, so that what was known at decision time is not confused with what is known now. Finally, retrospective linkage depends on persistent identifiers for system versions, data sources and deployment records, otherwise the trail disappears when a system is updated or retired. The practical test for v0.03.01 is whether an incident record can carry separate origin, onset and discovery times, and a link to the specific system version that was responsible.

### 1.03 Sub-Gap: Phases, Escalation and Intervention Points

**Summary:** Harms often move through recognizable stages, and they can speed up, slow down, stabilize or recur. Each stage offers a different chance to intervene. If v0.03.01 records a harm as a single state, it cannot show where the course could have been changed.

**Key points:**

1. **Phase structure.** A harm can pass through exposure, onset, amplification, stabilization and residual effects. A single record collapses these into one label. A process entity with ordered phases would preserve the sequence.
2. **Escalation dynamics.** Harm can accelerate through feedback loops, such as a recommender reinforcing a vulnerability it detected. Rate and direction of change matter as much as current severity. The ontology needs attributes for escalation, plateau and decline.
3. **Recurrence.** The same harm may return after apparent resolution, for example after a model update. Treating each recurrence as a new unrelated incident hides the pattern. A link between recurring events and their shared process is needed.
4. **Intervention points.** At each phase there are actions that could have stopped or reduced the harm, such as monitoring, rollback or user notice. Recording these opportunities supports analysis of missed and effective responses. Without them, the model cannot support prevention learning.
5. **Response as part of the process.** Interventions change the course of a harm, sometimes causing new harms of their own. They should be modeled as events inside the process, not as external annotations. This also links to trade-off representation.

**Explanation:**
Real harms usually have shape. They begin with exposure, reach onset, may amplify, then stabilize and leave residual effects, and some recur after apparent resolution. A schema that records a harm as a single state with a single severity cannot show this shape, and so cannot show where the course could have been changed. The missing construct is a process entity with ordered phases and transitions between them, to which individual events attach. Within it, escalation dynamics deserve explicit treatment, because feedback loops, such as a system reinforcing a vulnerability it has detected, mean that the rate and direction of change can matter more than current severity. Recurrence needs a link between repeated events and the process they belong to, otherwise a harm that returns after a model update is logged as a new, unrelated incident. Most importantly, each phase offers intervention points, such as monitoring, rollback, user notice or access restriction, and the ontology should record both opportunities available and responses actually taken. Responses belong inside the process as events, because they alter its course and sometimes produce secondary harms. Without these elements, the ontology can describe what happened but not support learning about prevention, early detection or the timing of remediation. The practical test for v0.03.01 is whether it can represent one harm with ordered phases, a recurrence, and two interventions, one effective and one that caused a new harm.

### 1.04 Sub-Gap: Reversibility, Recovery and Residual Effects

**Summary:** How long a harm lasts and whether it can be undone largely determines how serious it really is. Two harms of the same type can differ greatly if one is quickly remedied and the other is permanent. If v0.03.01 records only that harm occurred, it cannot separate temporary setbacks from lasting damage.

**Key points:**

1. **Reversibility.** Some harms can be fully undone, such as a wrongly denied service that is later restored. Others are permanent, such as a leaked secret or a lost opportunity. A reversibility attribute, ideally graded and not binary, is needed to tell them apart.
2. **Recovery time and cost.** Even reversible harms impose burdens in time, money and effort to repair. The affected party often bears these costs. Recording recovery duration and who paid captures a share of the harm that is otherwise omitted.
3. **Residual and secondary effects.** After the primary harm ends, lasting effects may remain, such as reputational damage or lost trust. These can persist well beyond the original event. The ontology needs a residual-effects construct linked to the original process.
4. **Remedy and redress.** Whether a remedy was offered, accepted and effective is part of the harm's story. An apology, correction or compensation can change the outcome without erasing it. Remedy events should be recorded alongside harm events.
5. **Unequal recovery capacity.** Bearers differ in resources and support, so the same harm is recovered from at different speeds. Recovery should be treated as bearer-dependent. This connects to relational severity in 3.00.

**Explanation:**
The seriousness of a harm depends heavily on whether it can be undone and how long recovery takes. A wrongly flagged account restored within an hour and a wrongly flagged account that costs someone a job are the same incident type, yet very different harms. Ontologies that record only that harm occurred cannot tell them apart. A useful treatment starts with a graded reversibility attribute, from fully reversible through partially reversible to permanent, rather than a yes-or-no flag. It should also record recovery time and recovery cost, including who bore them, since affected parties often pay in time, money and effort to repair damage that someone else caused. Beyond the primary harm, residual effects such as reputational damage, lost trust, or changed life trajectories may persist long after the original event ends, and they need their own construct tied to the originating process. Remedy and redress belong in the same picture: whether a correction, apology, reversal or compensation was offered, accepted and effective changes the outcome without erasing the harm. Finally, recovery capacity varies across bearers according to resources, support and institutional access, so recovery should be modeled as bearer-dependent. Without these elements, severity measures overstate transient incidents and understate permanent or slowly recovering ones, and the ontology cannot assess whether remediation was timely or adequate. The practical test for v0.03.01 is whether it can record one harm with a graded reversibility value, a recovery cost borne by the bearer, a lasting residual effect, and a remedy event with an effectiveness status.

---

## 2.00 Gap: Distributed Causation and Attribution

**Summary:** Real AI harms rarely have one author, because many parties contribute across the development and deployment chain. Ontologies that assume one cause, one responsible agent and one victim cannot express this. If v0.03.01 follows that pattern, accountability analysis will default to the most visible actor.

**Key points:**

1. **Supply-chain roles.** A model passes through data providers, developers, fine-tuners, integrators, deployers, operators and users. A flat "responsible agent" field cannot tell them apart. Without separate roles, contributions cannot be assigned to the right party.
2. **Types of causal contribution.** Causes can be necessary, sufficient, enabling, facilitating or merely background. A single "cause" link treats them all the same. Degrees of contribution are lost, and so are partial responsibilities.
3. **Kinds of responsibility.** Causal, moral and legal responsibility, and the capacity to prevent, are different things. They often point at different actors. An ontology that merges them cannot support fair attribution or targeted remediation.
4. **Emergent and multi-system effects.** Some harms arise only from interactions among components or systems, such as automated pipelines feeding one another. No single component exhibits the harm alone. Component-level causation cannot represent this.
5. **Diffusion of responsibility.** Each actor may reasonably assume another is guarding against the risk. The ontology needs a way to record such gaps in oversight. Otherwise a collective failure looks like no failure.

**Explanation:**
Real-world AI harms seldom have a single identifiable author. A model is trained by one organization on data gathered by others, fine-tuned by a second, integrated by a third, deployed by a fourth and operated by users who may adapt it in unforeseen ways. Harm emerges from interactions across this chain, and sometimes between several systems at once. An ontology that models a harm with one cause, one responsible agent and one affected party cannot express this. The probable gaps are the absence of a causal contribution structure allowing partial, necessary, enabling or merely facilitating causes. Roles separating developer, deployer, operator, user, data provider and infrastructure supplier may also be missing. So may a distinction between causal responsibility, moral responsibility, legal liability and capacity to prevent. Emergent system-level behavior that no component exhibits alone, and diffusion of responsibility, may be unrepresented too. Without such structure, accountability analysis defaults to blaming the most visible actor, and remediation targets the wrong point. Insurers, regulators and courts would then receive incident records that cannot answer who contributed what. The practical test for v0.03.01 is whether it can represent one incident with five contributing parties, each with a different type and degree of contribution, without duplicating the incident record. If it cannot, multi-actor harms will be systematically misattributed.

### 2.01 Sub-Gap: Supply-Chain Roles and Graded Causal Contribution

**Summary:** Within the distributed-causation gap, the first problem is who the parties are and how each contributed. AI systems pass through many hands, and each hand contributes differently. If v0.03.01 has one generic responsible-agent field and one cause link, it cannot say who did what.

**Key points:**

1. **Role differentiation.** Data providers, model developers, fine-tuners, integrators, deployers, operators, end users and infrastructure suppliers hold different positions. One agent class with a single "responsible" flag erases these differences. Distinct role types would allow precise assignment.
2. **Multiple roles per party.** One organization can hold several roles, such as developer and deployer, and a party's role can change across versions. The model should treat roles as relations between an agent and an incident or system, not as fixed agent types.
3. **Graded contribution types.** Contributions can be necessary, sufficient, enabling, facilitating or background. A binary cause link treats them as equal. Typed contribution links, with an optional degree, would preserve the difference.
4. **Control and knowledge.** What a party could control and what it knew shape its contribution. A deployer with no access to model internals differs from a developer who ignored a known defect. Control and knowledge attributes help interpret each contribution.
5. **One incident, many contributors.** The incident record should hold many contributor links without being duplicated per party. Duplicating records breaks aggregate counts and hides the shared event.

**Explanation:**
The first requirement for representing distributed causation is a vocabulary of who the parties are and how each contributed. AI systems pass through data providers, model developers, fine-tuners, integrators, deployers, operators, end users and infrastructure suppliers, and each stands in a different position relative to a harm. A schema with one generic agent class and a single responsible-agent field erases these differences. A stronger design treats roles as relations between an agent and a system or incident, since one organization may be both developer and deployer, and a party's role may change across system versions. Contribution itself also needs structure. Causes can be necessary, sufficient, enabling, facilitating or merely background, and a binary cause link treats a decisive contribution the same as a remote one. Typed contribution links, with an optional degree, preserve the difference. Interpreting a contribution further depends on what the party controlled and what it knew: a deployer with no access to model internals is differently placed from a developer who disregarded a known defect. Finally, the incident record should hold many contributor links without being duplicated for each party, because duplication corrupts aggregate counts and hides the fact that a single event is shared. Without these elements, accountability analysis collapses to the most visible actor. The practical test for v0.03.01 is whether one incident can carry five contributor relations with different role types, contribution types and knowledge states.

### 2.02 Sub-Gap: Kinds of Responsibility (Causal, Moral, Legal and Preventive)

**Summary:** Being a cause of harm, being morally blameworthy, being legally liable and being able to prevent it are four different things. They often point at different parties. If v0.03.01 merges them into one responsibility notion, attribution will be unfair and remediation misdirected.

**Key points:**

1. **Causal responsibility.** This concerns who or what contributed to the outcome in fact. A party can be a cause without any fault, as when a user supplies an unusual input. The ontology should record causal contribution separately from judgments about it.
2. **Moral responsibility.** This depends on knowledge, intent, negligence and the reasonableness of conduct. It requires an assessment, which is normative and may be contested. It should be represented as an attributed judgment, not as a fact.
3. **Legal liability.** Liability depends on jurisdiction, statute and contract, and can attach to parties who were not at fault, such as under strict liability. It may also fail to attach to those who were. The ontology needs a jurisdiction-qualified liability construct.
4. **Preventive capacity.** The party best placed to prevent a harm is often not the one who caused it or who is liable. Capacity depends on access, expertise and control. Recording it supports forward-looking governance.
5. **Divergence among the four.** A single incident can show a different party at the top of each dimension. Keeping the dimensions separate allows the divergence to be seen. A merged field hides it.

**Explanation:**
Causal contribution, moral blame, legal liability and preventive capacity are four distinct ideas that are frequently conflated under the word responsibility. Causal responsibility concerns who or what contributed in fact, and a party can be a cause without fault, for example when a user supplies an unforeseeable input. Moral responsibility depends on knowledge, intent, negligence and the reasonableness of conduct. It is a normative judgment, may be contested, and is best represented as an assessment attributed to a stated assessor and not as a fact about the event. Legal liability depends on jurisdiction, statute and contract. It can attach to parties without fault, as in strict liability regimes, and fail to attach to parties who clearly contributed, so it needs a jurisdiction-qualified construct with a status such as alleged, established or dismissed. Preventive capacity concerns who was best placed to stop the harm given access, expertise and control, and it often points to a different party from the other three, such as a platform operator rather than a model developer. An ontology that holds a single responsible-party field cannot show that one incident may have different parties leading on each dimension, and so cannot support fair attribution, targeted remediation or forward-looking governance. Separating the four dimensions also keeps descriptive claims apart from normative ones. The practical test for v0.03.01 is whether one incident can name a different party as the leading one on each of the four dimensions.

### 2.03 Sub-Gap: Emergent Multi-System Effects and Diffusion of Responsibility

**Summary:** Some harms arise only from the interaction of several components or systems, and no single one of them is faulty on its own. In such cases each party may also assume another is guarding against the risk. If v0.03.01 attributes harm only to individual components or agents, these collective failures will appear to have no cause.

**Key points:**

1. **Interaction-level causes.** Automated systems that feed each other, such as trading algorithms or moderation and recommendation pipelines, can produce outcomes none would produce alone. The cause lies in the interaction. The ontology needs a way to attach a cause to a relationship or system of components, not only to one component.
2. **System boundaries.** What counts as the system differs by observer and by purpose. A harm may cross organizational and technical boundaries. The model should let the system under analysis be declared explicitly, with its components and interfaces.
3. **Emergence.** Behavior at the system level may not be predictable from component specifications. This affects foreseeability and testing. The ontology should be able to flag a harm as emergent and record that component-level testing passed.
4. **Diffusion of responsibility.** Each actor may believe another handles the risk, so no one does. This is a gap in oversight, and it is itself causally relevant. An oversight-gap construct would record who was assumed to be responsible and who in fact acted.
5. **Absence as contribution.** Failures to act, monitor or escalate contribute to harm. Event-based models record what happened and miss omissions. Omission needs representation, with the expected duty noted.

**Explanation:**
Some of the most consequential AI harms arise from interaction and not from a defective part. Automated trading algorithms reacting to each other, or recommendation and moderation pipelines feeding one another, can produce outcomes that no single component would produce and that no component test would reveal. An ontology that attaches causes only to individual components or agents has nowhere to record this. It needs a way to attach a causal role to a relationship or to a declared system of components and interfaces, with the system boundary stated explicitly, because what counts as the system varies by observer and often crosses organizational lines. It should also allow a harm to be flagged as emergent, along with the fact that component-level checks passed, since this bears on foreseeability and on the adequacy of testing practice. A related pattern is diffusion of responsibility, where each actor reasonably assumes another is watching the risk and so none does. This oversight gap is causally relevant in itself, and an ontology can capture it by recording who was assumed to hold a duty and who actually acted. Closely tied to this is omission: failures to monitor, escalate or intervene contribute to harm, yet event-based schemas record what happened and not what did not. Omissions need representation, together with the expected duty and its source. The practical test for v0.03.01 is whether a harm with no faulty component, caused by an interaction and by a mutual assumption of oversight, can be recorded without forcing blame onto one party.

### 2.04 Sub-Gap: Intent, Misuse and Adversarial Actors

*Pointer note: this extended the branch beyond the three sub-levels first proposed for 2.00.*

**Summary:** Many AI harms involve a person who deliberately misuses a system, attacks it or exploits a weakness. Others involve no intent at all. If v0.03.01 does not represent intent and adversarial action, it cannot separate accidents, negligence, misuse and attacks, which call for very different responses.

**Key points:**

1. **Intent spectrum.** Harm can result from accident, negligence, reckless deployment, foreseeable misuse or deliberate malice. These need distinct values, since each leads to different remedies and duties. A single "cause" field cannot hold them.
2. **Adversarial actors.** Attackers may poison data, steal models, craft jailbreak prompts or impersonate people with generated content. They are third parties outside the supply chain. The ontology needs an actor type for them, with tactics and goals.
3. **Misuse versus intended use.** Whether an action fell within the system's intended use, a foreseeable misuse or an unforeseeable one affects how responsibility is shared. Intended-use declarations from the developer or deployer should be linkable. Without them, the line cannot be examined.
4. **Dual-use and reuse.** The same capability can serve beneficial and harmful ends, and open release lets others repurpose it. A system may be downstream of its original context. The ontology should record the chain of reuse.
5. **Safeguard failure and circumvention.** Harm may follow a defeated safeguard, whether weak or deliberately bypassed. Recording the safeguard, its purpose and the manner of failure supports prevention analysis. Without this, defenses cannot be evaluated against real incidents.

**Explanation:**
A large share of real AI harm involves someone acting with purpose: a user who misuses a system, an attacker who poisons data or steals a model, a fraudster who impersonates a person with generated media. Others involve no intent whatever, as with plain accident or negligence. These cases lead to very different obligations and remedies, yet a schema with a single cause or responsible-agent field cannot tell them apart. The ontology therefore needs an intent spectrum that distinguishes accident, negligence, reckless deployment, foreseeable misuse and deliberate malice. It also needs an adversarial actor type, covering third parties outside the development and deployment chain, with attributes for tactics, goals and capabilities. Responsibility for misuse depends on whether the action fell within the declared intended use, a foreseeable misuse or an unforeseeable one, so intended-use statements from developers and deployers should be linkable to incidents. Dual-use capability and open release add another layer, since a system may be repurposed far from its original context, and the chain of reuse should be traceable. Finally, safeguards matter: harm often follows a safeguard that was weak, absent or deliberately bypassed, and recording the safeguard, its purpose and the manner of failure lets defenses be tested against real incidents. Without these constructs, all harms look like system faults, deterrence and design lessons are confused, and genuine attacks are blamed on the very organizations they targeted. The practical test for v0.03.01 is whether it can distinguish an attack on a system from a failure of the system, and record the safeguard that was bypassed.

<!-- CHUNK-3 -->
