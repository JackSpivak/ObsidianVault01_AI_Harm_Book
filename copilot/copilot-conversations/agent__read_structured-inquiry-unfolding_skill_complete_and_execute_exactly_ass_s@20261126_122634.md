---
epoch: 1795721194557
mode: agent
backendId: opencode
sessionId: "ses_de6ae6d52ffe0hEuIAtjW6LVXU"
model: '{"baseModelId":"anthropic/claude-sonnet-5-5","effort":"low"}'
tags:
  - copilot-conversation
topic: "Execute structured-inquiry-unfolding skill"
usage: '{"usedTokens":81302,"contextWindow":1000000,"updatedAt":1795728836927}'
---

**user**: read structured-inquiry-unfolding skill complete and execute exactly ass speecified
[Timestamp: 2026/11/26 12:26:34]

**ai**: I found the skill under a slightly different name, `structured-inquiry-epistemic-unfolder`, in `.claude/skills/`. I read all of it and took it to be the one you meant. Nothing in this conversation supplies Input A or Input B, and the skill says to assume nothing from earlier sessions. So I'm pausing here, as it specifies, and no section has been delivered yet.

## Mandatory Inputs

1. **Input A: The Core Guiding Question.** This is the central, foundational question driving the investigation.
2. **Input B: Epistemic Grounding Mode.** Choose one:
   - **Option 1, Ontology-Only.** Limited to formal schema definitions (OWL/RDF/SKOS classes, properties, axioms). Essays and unfiled notes are excluded.
   - **Option 2, Obsidian Vault-Grounded.** Draws on the whole vault: design notes, indexes, council reviews and unfiled ideas. These are treated as an evolving laboratory, not a frozen production artifact.
   - **Option 3, LLM Parametric Baseline.** Uses only pre-trained model knowledge and academic consensus. Vault access is cut off.

## Optional Inputs

If you leave these out, I will fill in defaults and tag each one `[Assumed by Skill]` in the frontmatter.

3. **Input C: Guiding Perspective / Standpoint.** The discipline, tradition or analytical lens.
4. **Input D: Conceptual Scope.** The thematic boundary of the investigation.
5. **Input E: Epistemic Rigor & Depth Level.** The analytical granularity and level of formalization.
6. **Input F: Temporal Horizon Constraint.** The temporal or historical framing.
7. **Input G: Deliverable Goal.** The intended outcome or output artifact.

Once you give me A and B, plus any optional inputs you want, I'll deliver section 1.00. It will start with the `### Inputs & Provenance Frontmatter` block and end with the metacognitive assessment and the six control options.

If you meant a different skill, tell me its path and I'll read that one instead.
<!-- copilot-message {"tools":["glob (search)","grep (search)","read (read): .claude/skills/structured-inquiry-epistemic-unfolder/SKILL.md"]} -->
[Timestamp: 2026/11/26 12:26:34]

**user**: exit
[Timestamp: 2026/11/26 13:17:49]

**ai**: Exiting the structured inquiry. I didn't deliver any sections or change any files. If you want to run it later, give me Input A (the core question) and Input B (the grounding mode).
[Timestamp: 2026/11/26 13:17:49]

**user**: structured-inquiry
[Timestamp: 2026/11/26 13:18:08]

**ai**: Starting a structured inquiry. I still need the two mandatory inputs before I can deliver section 1.00.

## Mandatory Inputs

1. **Input A: The Core Guiding Question.** This is the central, foundational question driving the investigation.
2. **Input B: Epistemic Grounding Mode.** Choose one:
   - **Option 1, Ontology-Only.** Limited to formal schema definitions (OWL/RDF/SKOS classes, properties, axioms).
   - **Option 2, Obsidian Vault-Grounded.** Draws on the whole vault: design notes, indexes, council reviews and unfiled ideas.
   - **Option 3, LLM Parametric Baseline.** Uses only pre-trained model knowledge and academic consensus. Vault access is cut off.

## Optional Inputs

Anything you leave out gets a default value, tagged `[Assumed by Skill]` in the frontmatter.

3. **Input C: Guiding Perspective / Standpoint.** The discipline, tradition or analytical lens.
4. **Input D: Conceptual Scope.** The thematic boundary of the investigation.
5. **Input E: Epistemic Rigor & Depth Level.** The analytical granularity and level of formalization.
6. **Input F: Temporal Horizon Constraint.** The temporal or historical framing.
7. **Input G: Deliverable Goal.** The intended outcome or output artifact.

You can answer in one message, for example: "A: …; B: Option 2; C: …".
[Timestamp: 2026/11/26 13:18:08]

**user**: a. what aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented tocapture real world situations b. option

b. option 3
g. set of narrative assessments regarding gaps delivered with an initial   2 to 5 sentence summary followed by a collection of numbered bullet points in 200 to 250 word explanations  for each gap and automatically generate a design note including all these
[Timestamp: 2026/11/26 13:23:18]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** Narrative gap assessments with a 2–5 sentence summary, numbered 200–250 word explanations, and an auto-generated design note `[Explicitly Provided by User]`

---

## 1.00 Gaps in Harm Ontology v0.03.01

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. Each gap below is a hypothesis drawn from general harm-ontology scholarship. Each one ends with a test you can run against the schema.

**Summary:** Harm ontologies for AI systems often model harm as a discrete event with one cause, one individual victim and a fixed severity. Real situations differ in five ways. They unfold over time, involve many contributing actors, depend on context, fall on collective or non-human bearers, and are known only with uncertainty. Version v0.03.01 is most likely under-represented on these five dimensions.

1. **Temporal and processual structure.** Most harm ontologies model harm as a discrete event: an incident occurs, an affected party suffers a loss, a category is assigned. Real AI situations rarely behave this way. Harm often accumulates slowly through repeated low-level exposures, such as a recommender system gradually shifting a teenager's self-image, or a hiring filter that quietly narrows a career over years. Other harms are latent, with the damaging decision made at deployment but the consequence surfacing months later, or only when conditions change. An ontology that lacks first-class representation of duration, onset delay, escalation, recurrence, reversibility and recovery will flatten these trajectories into a single timestamped record. That loses exactly what makes them hard to detect and remedy. The likely missing constructs are a harm process or trajectory entity distinct from the harm event, with phases (exposure, onset, amplification, stabilization, residual effects). Also likely missing are thresholds separating tolerable from damaging accumulation, and links to intervention points where the course could have been altered. Without these, the ontology cannot answer when a harm became foreseeable, whether remediation arrived in time, or whether a minor incident belongs to a larger pattern. *Test: does time appear only as an attribute on events, or as a structural dimension of the model?*

2. **Distributed causation and attribution.** Real-world AI harms seldom have a single identifiable author. A model is trained by one organization on data gathered by others, fine-tuned by a second, integrated by a third, deployed by a fourth and operated by users who may adapt it unpredictably. Harm emerges from interactions across this chain, and sometimes between several systems at once, as in automated trading or moderation pipelines feeding one another. An ontology that models one cause, one responsible agent and one affected party cannot express this. The probable gaps are the absence of a causal contribution structure allowing partial, necessary, enabling or merely facilitating causes. Roles separating developer, deployer, operator, user, data provider and infrastructure supplier may also be missing. So may a distinction between causal responsibility, moral responsibility, legal liability and capacity to prevent. Emergent system-level behavior and diffusion of responsibility may also be unrepresented. Without such structure, accountability analysis defaults to blaming the most visible actor, and remediation targets the wrong point. *Test: can v0.03.01 represent one incident with five contributing parties, each with a different type and degree of contribution, without duplicating the incident record?*

3. **Context, vulnerability and relational severity.** Harm is not a property of an output alone. It depends on who encounters it, in what circumstances, and with what resources. The same chatbot reply may be benign for one user and dangerous for someone in crisis, and the same biased score may be an inconvenience for one applicant and a life-altering barrier for another. Ontologies that classify harms by type, such as privacy, discrimination or physical safety, tend to treat severity as intrinsic. That neglects vulnerability, power asymmetry, dependency, consent and the availability of recourse. Cultural and legal context also changes whether something counts as harm at all. Another probable gap is intersectionality, where compounded identities produce harms not reducible to single-category effects. Equally important is the difference between harm as measured by an observer and harm as experienced or reported by the affected person. These can diverge sharply and carry different legitimacy in different institutions. The model likely needs a contextual layer linking harm instances to situated bearers, conditions of exposure, moderating factors and sources of perspective. Severity would then be relational and derived rather than fixed. *Test: are severity and affected-party classes context-dependent, or hard-coded?*

4. **Non-individual and non-human bearers.** Many harm ontologies implicitly assume the bearer of harm is an individual human. Yet significant AI-related harms fall on communities and demographic groups, organizations, democratic institutions, labor markets, the information environment, ecosystems affected by energy and water use, non-human animals and future generations. Harm to such bearers often cannot be decomposed into harm to identifiable individuals. Erosion of shared trust in evidence, homogenization of cultural production, or degraded representation of a language community are cases where each person's loss may be slight while the collective loss is large. Likely gaps include the lack of a typology of bearers with different standing conditions. There may also be no constructs for commons, public goods and structural conditions, and no way to represent harm that is diffuse, non-rivalrous or spread thinly across many people. Individual-centered models also assume a victim who can notice, report and claim. Collective and future harms have no natural claimant, which affects how they are recorded and prioritized. A sufficiently expressive ontology would make the bearer a polymorphic class with aggregation rules and distinct notions of loss per type. *Test: does the bearer class extend beyond persons, and how are aggregate harms expressed?*

5. **Epistemic status, uncertainty and trade-offs.** Real harm records are uncertain, disputed and incomplete, yet ontologies often store them as settled facts. Many AI harms are counterfactual or probabilistic: a model may have increased the likelihood of an outcome without determinably causing it. Others are near misses, exposures that produced no damage yet, or alleged harms contested by developers, regulators and affected parties. Evidence quality varies from rigorous audit to anecdote, and interpretations change as investigations proceed. An ontology without epistemic metadata cannot distinguish a confirmed incident from a hypothesis. It also cannot represent competing accounts of the same event, or revise a classification without erasing history. Probable missing constructs include evidence and provenance links, confidence qualifiers, and status values (alleged, substantiated, disputed, retracted). Versioned assertions attributed to the asserting party and modeling of risk and hazard as distinct from realized harm may also be missing. Related is the omission of trade-offs: an intervention that prevents one harm may cause another, or a harm may coexist with real benefits to the same party. A purely harm-centered schema cannot register this. *Test: can a single event carry multiple, conflicting, sourced characterizations with confidence levels and revision history?*

**Design note created:** `08_Resources/design-note-harm-ontology-v0.03.01-gap-assessment.md`

---

### Metacognitive Assessment
- **Saturation:** Low. This is a first pass from general knowledge, without the actual schema.
- **Marginal Returns:** High
- **Convergence:** Open
- **Utility:** High Leverage
- **Recommendation & Options:** Check each hypothesis against the real v0.03.01 schema, either by rerunning in Vault-Grounded mode or by supplying the schema. Then drill into the gaps that matter most.

### Your Options
1. **[Expand]** Add more detail, lineage or guiding questions for 1.00. Example: "Expand gap 2."
2. **[Drill Deeper]** Break a gap into sub-levels. Example: "Drill deeper into 1.02."
3. **[Continue Sequentially]** Move to the next section at the same depth. Example: "Continue to 2.00."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude and package the findings.
<!-- copilot-message {"tools":["write (edit): 08_Resources/design-note-harm-ontology-v0.03.01-gap-assessment.md"]} -->
[Timestamp: 2026/11/26 13:23:18]

**user**: exit without synthesizing
[Timestamp: 2026/11/26 13:25:16]

**ai**: Exiting the structured inquiry without synthesizing. The design note from section 1.00 is saved at `08_Resources/design-note-harm-ontology-v0.03.01-gap-assessment.md`. I haven't changed anything else.
[Timestamp: 2026/11/26 13:25:16]

**user**: structured-inquiry
[Timestamp: 2026/11/26 13:25:57]

**ai**: Starting a new structured inquiry. The skill assumes nothing from earlier sessions, so I need the two mandatory inputs again.

## Mandatory Inputs

1. **Input A: The Core Guiding Question.** This is the central, foundational question driving the investigation.
2. **Input B: Epistemic Grounding Mode.** Choose one:
   - **Option 1, Ontology-Only.** Limited to formal schema definitions (OWL/RDF/SKOS classes, properties, axioms).
   - **Option 2, Obsidian Vault-Grounded.** Draws on the whole vault: design notes, indexes, council reviews and unfiled ideas.
   - **Option 3, LLM Parametric Baseline.** Uses only pre-trained model knowledge and academic consensus. Vault access is cut off.

## Optional Inputs

Anything you leave out gets a default value, tagged `[Assumed by Skill]` in the frontmatter.

3. **Input C: Guiding Perspective / Standpoint.** The discipline, tradition or analytical lens.
4. **Input D: Conceptual Scope.** The thematic boundary of the investigation.
5. **Input E: Epistemic Rigor & Depth Level.** The analytical granularity and level of formalization.
6. **Input F: Temporal Horizon Constraint.** The temporal or historical framing.
7. **Input G: Deliverable Goal.** The intended outcome or output artifact.

You can answer in one message, for example: "A: …; B: Option 2; C: …".
[Timestamp: 2026/11/26 13:25:57]

**user**: a. what aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented tocapture real world situations b. option

b. option 3
g. on completion deliver a collected set of narrative assessments  regarding gaps each written with an initial 2 to 5 sentence summary followed by a collection of numbered bullet points in 2 to 5 sentendes in length followed by a single 200 to 250 word explanations for each gap and upon halt and synthesize prompt automatically generate a design note including all these individual assessments within the body of the design note.  do not generate a design note before the conversation is complete
[Timestamp: 2026/11/26 13:29:07]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 1.00 Gap: Temporal and Processual Structure of Harm

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Harm ontologies usually treat harm as a discrete, timestamped event. Real AI harms often build up gradually, stay latent, escalate, recur or recover over time. If v0.03.01 treats time only as an event attribute, it probably cannot represent these trajectories.

**Key points:**

1. **Accumulation.** Many harms arise from repeated low-level exposures, not one incident. Examples are a recommender slowly shifting a teenager's self-image and a hiring filter narrowing a career over years. An event-only model records each exposure as trivial or misses the pattern entirely.
2. **Latency and delay.** The damaging decision may be made at deployment while the consequence appears months later, or only when conditions change. Without an onset-delay construct, cause and effect cannot be linked across that gap. This weakens foreseeability and accountability analysis.
3. **Phases and escalation.** Harms move through exposure, onset, amplification, stabilization and residual effects. A single record flattens these phases. That hides where an intervention would have changed the course.
4. **Reversibility and recovery.** Whether a harm can be undone, and how long recovery takes, shapes its real severity. Ontologies that record only that harm occurred cannot distinguish a temporary setback from permanent damage. Remediation timeliness cannot be assessed either.
5. **Pattern linkage.** Minor incidents may belong to a larger recurring or escalating pattern. Without a process entity that groups events, each is classified in isolation. The aggregate harm stays invisible.

**Explanation:**
Most harm ontologies model harm as a discrete event: an incident occurs, an affected party suffers a loss, a category is assigned. Real AI situations rarely behave this way. Harm often accumulates through repeated low-level exposures, or stays latent until conditions change. An ontology lacking first-class representation of duration, onset delay, escalation, recurrence, reversibility and recovery will flatten these trajectories into a single timestamped record. That discards what makes them hard to detect and remedy. The likely missing constructs are a harm process or trajectory entity distinct from the harm event, with phases (exposure, onset, amplification, stabilization, residual effects). Also likely missing are thresholds separating tolerable from damaging accumulation, and explicit links to intervention points where the course could have been altered. Without these, the ontology cannot answer when a harm became foreseeable, whether remediation arrived in time, or whether a minor incident belongs to a larger pattern. It also cannot support early-warning analysis, because the signals of a developing harm are only visible as a sequence. The practical test for v0.03.01 is whether time appears merely as an attribute on events, or as a structural dimension that organizes events into processes with phases, thresholds and intervention opportunities. If the former, trajectory-based harms will be systematically under-represented, and the ontology will bias toward dramatic, discrete incidents.

---

### Metacognitive Assessment
- **Saturation:** Low. One gap of several is mapped, from general knowledge only.
- **Marginal Returns:** High
- **Convergence:** Open
- **Utility:** High Leverage
- **Recommendation & Options:** Continue sequentially to the next gap, for example distributed causation, context and vulnerability, non-individual bearers, or epistemic status. You could also check this gap against the real schema first. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 1.00. Example: "Expand 1.00."
2. **[Drill Deeper]** Break this gap into sub-levels. Example: "Drill deeper into 1.00."
3. **[Continue Sequentially]** Move to the next gap. Example: "Continue to 2.00."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:29:07]

**user**: continue sequentially
[Timestamp: 2026/11/26 13:29:34]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 2.00 Gap: Distributed Causation and Attribution

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Real AI harms rarely have one author, because many parties contribute across the development and deployment chain. Ontologies that assume one cause, one responsible agent and one victim cannot express this. If v0.03.01 follows that pattern, accountability analysis will default to the most visible actor.

**Key points:**

1. **Supply-chain roles.** A model passes through data providers, developers, fine-tuners, integrators, deployers, operators and users. A flat "responsible agent" field cannot tell them apart. Without separate roles, contributions cannot be assigned to the right party.
2. **Types of causal contribution.** Causes can be necessary, sufficient, enabling, facilitating or merely background. A single "cause" link treats them all the same. Degrees of contribution are lost, and so are partial responsibilities.
3. **Kinds of responsibility.** Causal, moral and legal responsibility, and the capacity to prevent, are different things. They often point at different actors. An ontology that merges them cannot support fair attribution or targeted remediation.
4. **Emergent and multi-system effects.** Some harms arise only from interactions among components or systems, such as automated pipelines feeding one another. No single component exhibits the harm alone. Component-level causation cannot represent this.
5. **Diffusion of responsibility.** Each actor may reasonably assume another is guarding against the risk. The ontology needs a way to record such gaps in oversight. Otherwise a collective failure looks like no failure.

**Explanation:**
Real-world AI harms seldom have a single identifiable author. A model is trained by one organization on data gathered by others, fine-tuned by a second, integrated by a third, deployed by a fourth and operated by users who may adapt it in unforeseen ways. Harm emerges from interactions across this chain, and sometimes between several systems at once. An ontology that models a harm with one cause, one responsible agent and one affected party cannot express this. The probable gaps are the absence of a causal contribution structure allowing partial, necessary, enabling or merely facilitating causes. Roles separating developer, deployer, operator, user, data provider and infrastructure supplier may also be missing. So may a distinction between causal responsibility, moral responsibility, legal liability and capacity to prevent. Emergent system-level behavior that no component exhibits alone, and diffusion of responsibility, may be unrepresented too. Without such structure, accountability analysis defaults to blaming the most visible actor, and remediation targets the wrong point. Insurers, regulators and courts would then receive incident records that cannot answer who contributed what. The practical test for v0.03.01 is whether it can represent one incident with five contributing parties, each with a different type and degree of contribution, without duplicating the incident record. If it cannot, multi-actor harms will be systematically misattributed.

---

### Metacognitive Assessment
- **Saturation:** Low. Two gaps are mapped, from general knowledge only.
- **Marginal Returns:** High
- **Convergence:** Open
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 3.00 (context, vulnerability and relational severity). Other candidates are non-individual bearers and epistemic status. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 2.00. Example: "Expand 2.00."
2. **[Drill Deeper]** Break this gap into sub-levels. Example: "Drill deeper into 2.00."
3. **[Continue Sequentially]** Move to the next gap. Example: "Continue to 3.00."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:29:34]

**user**: continue sequenrtially
[Timestamp: 2026/11/26 13:29:57]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 3.00 Gap: Context, Vulnerability and Relational Severity

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Harm depends on who encounters an output, in what circumstances and with what resources. It is not a fixed property of the output. Ontologies that classify harm by type and assign severity as an intrinsic attribute miss this. If v0.03.01 does so, it will misjudge the same event across different people and settings.

**Key points:**

1. **Vulnerability and power asymmetry.** The same reply or score affects a person in crisis, a dependent user or a marginalized applicant very differently from others. A type-based classification records only the output. Susceptibility and dependency need explicit representation.
2. **Consent and recourse.** Whether the person agreed to the exposure, and whether they can contest or reverse it, changes the harm's weight. A schema without these factors treats a chosen risk and an imposed one alike. Availability of remedy is also lost.
3. **Cultural and legal context.** Norms about speech, modesty, privacy and data sharing vary, so whether something counts as harm varies too. A single universal definition embeds one context's assumptions. The ontology needs a way to qualify harm by jurisdiction or community.
4. **Intersectionality.** Compounded identities can produce harms that are not the sum of single-category effects. Independent attribute tags for each category miss the interaction. The model needs to represent combinations.
5. **Observed versus experienced harm.** An observer's measurement and the affected person's account can diverge sharply. Each carries different legitimacy in different institutions. Recording only one erases the other perspective.

**Explanation:**
Harm is not a property of an output alone; it depends on who encounters it, in what circumstances, and with what resources. The same chatbot reply may be benign for one user and dangerous for someone in crisis, and the same biased score may be an inconvenience for one applicant and a life-altering barrier for another. Ontologies that classify harms by type, such as privacy, discrimination or physical safety, tend to treat severity as intrinsic. That neglects vulnerability, power asymmetry, dependency, consent and the availability of recourse. Cultural and legal context also changes whether something counts as harm at all. Another probable gap is intersectionality, where compounded identities produce harms not reducible to single-category effects. Equally important is the difference between harm as measured by an observer and harm as experienced or reported by the affected person, which can diverge sharply and carry different legitimacy in different institutions. The model likely needs a contextual layer linking harm instances to situated bearers, conditions of exposure, moderating factors and sources of perspective. Severity would then become relational and derived rather than fixed. Without this, prioritization based on severity scores will systematically under-rate harms to the most vulnerable, because their circumstances never enter the record. The practical test for v0.03.01 is whether severity and affected-party classes depend on context or are hard-coded.

---

### Metacognitive Assessment
- **Saturation:** Moderate. Three gaps are mapped, from general knowledge only.
- **Marginal Returns:** Moderate to High. Two more candidates remain, non-individual bearers and epistemic status.
- **Convergence:** Open
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 4.00 (non-individual and non-human bearers). You could also halt and synthesize now. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 3.00. Example: "Expand 3.00."
2. **[Drill Deeper]** Break this gap into sub-levels. Example: "Drill deeper into 3.00."
3. **[Continue Sequentially]** Move to the next gap. Example: "Continue to 4.00."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:29:57]

**user**: continue sequentially
[Timestamp: 2026/11/26 13:30:19]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 4.00 Gap: Non-Individual and Non-Human Bearers of Harm

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Many harm ontologies assume the bearer of harm is an individual human. Significant AI harms fall on groups, institutions, shared resources, the environment and future generations. If v0.03.01 has only a person-level bearer, these harms will be missing or misrecorded.

**Key points:**

1. **Collective bearers.** Communities, demographic groups, organizations and institutions can be harmed in ways that do not reduce to harm to identifiable members. Erosion of a language community's representation is one example. A person-only bearer class has no place to record this.
2. **Commons and structural conditions.** The information environment, democratic processes and labor markets are shared goods. Degrading them is diffuse and non-rivalrous. The ontology needs constructs for public goods and systemic conditions.
3. **Aggregation of small harms.** Each person's loss may be slight or invisible while the total is large, as with homogenized cultural production or lowered trust in evidence. Per-individual severity scores undercount this. Aggregation rules are needed.
4. **Non-human and future bearers.** Ecosystems affected by energy and water use, non-human animals and future generations cannot report harm themselves. They need defined standing conditions. Otherwise they are excluded by default.
5. **Missing claimant.** Individual models assume a victim who can notice, report and claim. Collective and future harms have no natural claimant, so they are rarely recorded or prioritized. The ontology should not depend on a complaint to register a harm.

**Explanation:**
Many harm ontologies implicitly assume that the bearer of harm is an individual human being. Yet significant AI-related harms fall on communities and demographic groups, organizations, democratic institutions, labor markets, the information environment, ecosystems affected by energy and water use, non-human animals and future generations. Harm to such bearers often cannot be decomposed into harm to identifiable individuals. Erosion of shared trust in evidence, homogenization of cultural production, or degraded representation of a language community are cases where each person's loss may be slight while the collective loss is large. Likely gaps include the lack of a typology of bearers with different standing conditions. There may also be no constructs for commons, public goods and structural conditions, and no way to represent harm that is diffuse, non-rivalrous or spread thinly across many people. Individual-centered models also assume a victim who can notice, report and claim, while collective and future harms have no natural claimant. That affects how they are recorded and prioritized. A sufficiently expressive ontology would make the bearer a polymorphic class, with aggregation rules and a distinct notion of loss for each type. Without this, the ontology will systematically favor harms that are individual, visible and reportable, and underweight the slow structural damage that AI deployment at scale may cause. The practical test for v0.03.01 is whether its bearer class extends beyond persons, and how aggregate harms are expressed.

---

### Metacognitive Assessment
- **Saturation:** Moderate to High. Four gaps are mapped, from general knowledge only.
- **Marginal Returns:** Moderate. One main candidate remains, epistemic status, uncertainty and trade-offs.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 5.00 (epistemic status, uncertainty and trade-offs), then consider halting and synthesizing. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 4.00. Example: "Expand 4.00."
2. **[Drill Deeper]** Break this gap into sub-levels. Example: "Drill deeper into 4.00."
3. **[Continue Sequentially]** Move to the next gap. Example: "Continue to 5.00."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:30:19]

**user**: continue sequentially
[Timestamp: 2026/11/26 13:30:44]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 5.00 Gap: Epistemic Status, Uncertainty and Trade-offs

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Real harm records are uncertain, disputed and incomplete, yet ontologies often store them as settled facts. Many harms are probabilistic, counterfactual or only alleged, and some come with offsetting benefits. If v0.03.01 has no epistemic metadata, it cannot tell a confirmed incident from a hypothesis or register competing accounts.

**Key points:**

1. **Probabilistic and counterfactual harm.** A model may raise the likelihood of an outcome without determinably causing it. Near misses and exposures with no damage yet are similar cases. A schema with only realized harm cannot hold them.
2. **Status of claims.** Harms may be alleged, substantiated, disputed or retracted. Without status values, every record looks equally established. Downstream analytics then treat anecdote and audit as the same.
3. **Evidence and provenance.** Evidence quality ranges from rigorous audit to anecdote, and interpretations shift as investigations proceed. Links to sources and confidence qualifiers are needed. Without them, no one can judge how far to rely on a record.
4. **Competing and versioned accounts.** Developers, regulators and affected parties often characterize the same event differently. The ontology should hold multiple sourced assertions and keep revision history. Otherwise a reclassification erases what was previously believed.
5. **Trade-offs and co-benefits.** An intervention that prevents one harm may cause another, and a harm may coexist with real benefits to the same party. A purely harm-centered schema cannot register this. Risk and hazard also need to be distinct from realized harm.

**Explanation:**
Real harm records are uncertain, disputed and incomplete, yet ontologies often store them as settled facts. Many AI harms are counterfactual or probabilistic: a model may have increased the likelihood of an outcome without determinably causing it. Others are near misses, exposures that produced no damage yet, or alleged harms contested by developers, regulators and affected parties. Evidence quality varies from rigorous audit to anecdote, and interpretations change as investigations proceed. An ontology without epistemic metadata cannot distinguish a confirmed incident from a hypothesis. It also cannot represent competing accounts of the same event, or revise a classification without erasing history. Probable missing constructs include evidence and provenance links, confidence qualifiers, and status values such as alleged, substantiated, disputed and retracted. Versioned assertions attributed to the asserting party, and modeling of risk and hazard as distinct from realized harm, may also be missing. Related is the omission of trade-offs: an intervention that prevents one harm may cause another, or a harm may coexist with real benefits to the same party. A purely harm-centered schema cannot register this. Without such structure, downstream analytics treat all reports as equivalent and compound reporting bias, which in turn distorts policy priorities. The practical test for v0.03.01 is whether a single event can carry multiple, conflicting, sourced characterizations with confidence levels and revision history.

---

### Metacognitive Assessment
- **Saturation:** High. All five gaps from the initial roadmap are mapped, from general knowledge only.
- **Marginal Returns:** Low to Moderate. Further yield would likely come from checking against the real schema, not from more parametric unfolding.
- **Convergence:** Achieved for the initial roadmap, though the roadmap is tentative and not a hard boundary.
- **Utility:** High Leverage
- **Recommendation & Options:** We have completed the initial proposed gaps. Would you like to continue to 6.00, step up, or synthesize? Candidates for 6.00 include granularity and level of abstraction, intersection with legal and regulatory taxonomies, and interoperability with other ontologies. Choosing Halt & Synthesize will generate the design note with all five assessments in its body.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 5.00. Example: "Expand 5.00."
2. **[Drill Deeper]** Break this gap into sub-levels. Example: "Drill deeper into 5.00."
3. **[Continue Sequentially]** Move to the next gap. Example: "Continue to 6.00."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:30:44]

**user**: continue sequentially
[Timestamp: 2026/11/26 13:31:17]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 6.00 Gap: Granularity, Abstraction Level and Interoperability

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** An ontology also has to sit at a workable level of abstraction and connect to the systems around it. Too coarse, and it cannot distinguish real situations. Too fine, and it cannot be applied consistently. If v0.03.01 is not aligned with legal, regulatory and incident-database taxonomies, its records will be hard to compare or reuse.

**Key points:**

1. **Category granularity.** Broad classes such as "discrimination" or "privacy harm" hide very different mechanisms and remedies. Overly fine classes multiply and fragment, so coders disagree on assignment. The ontology needs a hierarchy that can be read at several levels.
2. **Mechanism versus outcome.** Harm can be classified by how it arises, by what it damages, or by who bears it. A schema that mixes these axes in one flat list produces overlapping categories. Separate, orthogonal dimensions allow cleaner queries.
3. **Legal and regulatory mapping.** Statutes and regulatory frameworks define harms in their own terms, and these differ across jurisdictions. Without mappings, an incident cannot be translated into a compliance or liability question. Crosswalks to major frameworks are needed.
4. **Incident-database interoperability.** Public AI incident repositories and risk taxonomies use their own categories. A schema that cannot align with them is isolated and hard to validate against real data. Shared identifiers or alignment properties would help.
5. **Coding reliability.** Even a well-designed class set fails if different annotators assign the same case differently. The ontology should come with definitions, examples and edge-case rules. Reliability testing on real narratives would reveal weak classes.

**Explanation:**
An ontology must sit at a workable level of abstraction. If its classes are too coarse, categories such as discrimination or privacy harm conceal very different mechanisms, bearers and remedies, and real situations cannot be told apart. If they are too fine, the class set multiplies, annotators disagree on assignment, and the structure becomes impractical to apply. A common weakness is mixing several classification axes, such as mechanism, outcome, bearer and domain, in a single flat list, which produces overlapping and ambiguous categories. Separating these into orthogonal dimensions allows cleaner querying and clearer coverage analysis. Interoperability is a second concern. Statutes and regulatory frameworks define harm in their own terms and differ by jurisdiction, while public incident repositories and risk taxonomies use their own category schemes. An ontology without crosswalks or alignment properties to these cannot translate an incident into a compliance or liability question, and cannot be validated against the large body of real incident data already collected. Finally, definitions, worked examples and edge-case rules determine whether different people code the same narrative the same way. Without reliability testing on real cases, weak or overlapping classes remain hidden. The practical test for v0.03.01 is whether its classes can be applied consistently by independent coders to a sample of real incident narratives, and whether they map cleanly to at least one external taxonomy.

---

### Metacognitive Assessment
- **Saturation:** High. Six gaps are mapped, from general knowledge only.
- **Marginal Returns:** Low. Further parametric unfolding is likely to repeat earlier material or become speculative.
- **Convergence:** Achieved. The inquiry has stabilized on six gaps.
- **Utility:** Marginal to High Leverage. This gap is useful but depends on seeing the actual schema.
- **Recommendation & Options:** Marginal returns are now low, so I recommend Halt & Synthesize. If you want to keep going, the best next step is to validate these hypotheses against the real schema, not to unfold more from general knowledge. We have no further tentative candidates. Would you like to continue to 7.00, step up, or synthesize?

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 6.00. Example: "Expand 6.00."
2. **[Drill Deeper]** Break this gap into sub-levels. Example: "Drill deeper into 6.00."
3. **[Continue Sequentially]** Move to the next gap. Example: "Continue to 7.00."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:31:17]

**user**: return to level 1
[Timestamp: 2026/11/26 13:31:45]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 1.01 Sub-Gap under 1.00: Cumulative Exposure and Threshold Effects

**Pointer reset:** I returned to Level 1 and am resuming sequential unfolding beneath 1.00. The next sub-level under it is 1.01.

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Within the temporal gap, the most concrete problem is how harm builds up from many small exposures. Individual exposures may each fall below any threshold for recording, yet together cross into real damage. If v0.03.01 records only incidents that already pass a severity bar, cumulative harms will remain invisible until late.

**Key points:**

1. **Sub-threshold exposures.** Each interaction may be harmless on its own, such as one recommendation or one minor score adjustment. An event-based schema has no reason to record it. The accumulated effect is then unrepresented.
2. **Dose and duration.** Harm often depends on how much exposure occurred and over how long. Attributes for frequency, intensity and cumulative duration are needed. A yes-or-no occurrence flag cannot carry them.
3. **Tipping points and thresholds.** Accumulation can be linear, or it can cross a point after which effects become severe or irreversible. The ontology needs a way to mark threshold crossings. Without it, the moment a harm became real cannot be identified.
4. **Exposure-to-harm linkage.** Exposure and harm are distinct things, and the same exposure leads to harm for some bearers and not others. A model that treats exposure as just a cause field loses this. Separate exposure and harm entities, with a conditional link, would capture it.
5. **Aggregation across sources.** A person may be exposed to the same type of harm through several systems at once. Each system's record looks minor when viewed alone. Cross-system aggregation requires a shared bearer-centered view.

**Explanation:**
Cumulative harm is among the hardest cases for event-based ontologies. A single recommendation, a minor score adjustment or one slightly biased response may each be unremarkable, and under a schema that records only incidents passing a severity bar, none would be logged. Yet repeated exposure over weeks or years can produce real damage, such as distorted self-perception, narrowed opportunity or entrenched belief. To represent this, an ontology needs exposure as a first-class entity separate from harm, with attributes for frequency, intensity and cumulative duration. It also needs a notion of threshold or tipping point, so that the crossing from tolerable to damaging can be marked, along with whether effects became irreversible. Because the same exposure harms some bearers and not others, the link from exposure to harm must be conditional on bearer characteristics rather than assumed. A further complication is aggregation across sources: a person may be exposed to the same type of harm through several systems at once, each of which appears minor in isolation. Seeing the total requires a bearer-centered view that pools exposures across systems and operators. Without these elements, the ontology will favor dramatic single incidents, underestimate slow harms, and give no basis for early warning. The practical test for v0.03.01 is whether it can record an exposure that caused no recordable harm at the time, and later link it to a threshold crossing.

---

### Metacognitive Assessment
- **Saturation:** Moderate within Level 1. The temporal gap now has an overview and one sub-level.
- **Marginal Returns:** Moderate. Other sub-levels under 1.00 remain, for example latency and delayed onset, phases and escalation, and reversibility and recovery.
- **Convergence:** Open. Branching beneath 1.00 is still productive.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 1.02 (latency and delayed onset), or return to macro-level to resume at 7.00 or synthesize. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 1.01. Example: "Expand 1.01."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 1.01."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 1.02."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:31:45]

**user**: continue sequentially
[Timestamp: 2026/11/26 13:32:10]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 1.02 Sub-Gap under 1.00: Latency and Delayed Onset

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Some harms appear long after the decision or event that caused them. The damaging choice may be made at design or deployment, and the consequence surfaces months or years later, or only when conditions shift. If v0.03.01 ties a harm to the time it was observed, it cannot link cause and effect across that gap.

**Key points:**

1. **Separation of cause time and effect time.** A training-data choice or a deployment decision may precede visible harm by a long interval. A single timestamp on the incident cannot hold both moments. Two distinct temporal anchors are needed, one for the originating decision and one for the onset of harm.
2. **Condition-dependent activation.** A latent defect may stay dormant until an input distribution, user population or environment changes. The harm then appears abruptly, though its origin is old. The ontology needs a way to represent a dormant hazard and the trigger that activated it.
3. **Discovery lag.** Harm may exist for a long time before anyone detects it. Observation date and onset date are different facts. Conflating them distorts duration and misdates responsibility.
4. **Foreseeability over time.** Whether a harm was foreseeable depends on what was known when the decision was made. Later knowledge should not be projected backward. The ontology needs time-indexed knowledge states to support fair assessment.
5. **Retrospective linkage.** Connecting a late harm to its distant origin requires traceable links to design, data and deployment records. Without such provenance, the link is lost once the system is updated or retired. Persistent identifiers for system versions would help.

**Explanation:**
Many significant AI harms are separated from their origin by a long interval. A choice about training data, a threshold setting or a deployment context may be made at one moment, while the resulting damage surfaces months or years later, or only when conditions change, such as a new user population or a shift in input distribution. An ontology that attaches a single timestamp to the incident cannot hold both moments, and so cannot connect cause and effect across the gap. It needs at least three distinct temporal anchors: when the originating decision or hazard was introduced, when harm actually began, and when it was discovered or reported. Conflating these distorts duration, misdates responsibility and hides discovery lag. It also needs a representation of a dormant hazard and the trigger condition that activated it, since latent defects behave differently from active ones. Assessing foreseeability fairly requires time-indexed knowledge states, so that what was known at decision time is not confused with what is known now. Finally, retrospective linkage depends on persistent identifiers for system versions, data sources and deployment records, otherwise the trail disappears when a system is updated or retired. The practical test for v0.03.01 is whether an incident record can carry separate origin, onset and discovery times, and a link to the specific system version that was responsible.

---

### Metacognitive Assessment
- **Saturation:** Moderate to High within Level 1. Two sub-levels are mapped beneath the temporal gap.
- **Marginal Returns:** Moderate. Phases and escalation, and reversibility and recovery, remain.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 1.03 (phases and escalation), or return to macro-level and synthesize. We have not yet exhausted the sub-levels proposed for this branch. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 1.02. Example: "Expand 1.02."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 1.02."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 1.03."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:32:10]

**user**: continue sequentially
[Timestamp: 2026/11/26 13:32:30]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 1.03 Sub-Gap under 1.00: Phases, Escalation and Intervention Points

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Harms often move through recognizable stages, and they can speed up, slow down, stabilize or recur. Each stage offers a different chance to intervene. If v0.03.01 records a harm as a single state, it cannot show where the course could have been changed.

**Key points:**

1. **Phase structure.** A harm can pass through exposure, onset, amplification, stabilization and residual effects. A single record collapses these into one label. A process entity with ordered phases would preserve the sequence.
2. **Escalation dynamics.** Harm can accelerate through feedback loops, such as a recommender reinforcing a vulnerability it detected. Rate and direction of change matter as much as current severity. The ontology needs attributes for escalation, plateau and decline.
3. **Recurrence.** The same harm may return after apparent resolution, for example after a model update. Treating each recurrence as a new unrelated incident hides the pattern. A link between recurring events and their shared process is needed.
4. **Intervention points.** At each phase there are actions that could have stopped or reduced the harm, such as monitoring, rollback or user notice. Recording these opportunities supports analysis of missed and effective responses. Without them, the model cannot support prevention learning.
5. **Response as part of the process.** Interventions change the course of a harm, sometimes causing new harms of their own. They should be modeled as events inside the process, not as external annotations. This also links to trade-off representation.

**Explanation:**
Real harms usually have shape. They begin with exposure, reach onset, may amplify, then stabilize and leave residual effects, and some recur after apparent resolution. A schema that records a harm as a single state with a single severity cannot show this shape, and so cannot show where the course could have been changed. The missing construct is a process entity with ordered phases and transitions between them, to which individual events attach. Within it, escalation dynamics deserve explicit treatment, because feedback loops, such as a system reinforcing a vulnerability it has detected, mean that the rate and direction of change can matter more than current severity. Recurrence needs a link between repeated events and the process they belong to, otherwise a harm that returns after a model update is logged as a new, unrelated incident. Most importantly, each phase offers intervention points, such as monitoring, rollback, user notice or access restriction, and the ontology should record both opportunities available and responses actually taken. Responses belong inside the process as events, because they alter its course and sometimes produce secondary harms. Without these elements, the ontology can describe what happened but not support learning about prevention, early detection or the timing of remediation. The practical test for v0.03.01 is whether it can represent one harm with ordered phases, a recurrence, and two interventions, one effective and one that caused a new harm.

---

### Metacognitive Assessment
- **Saturation:** High within Level 1. Three sub-levels are mapped beneath the temporal gap.
- **Marginal Returns:** Low to Moderate. One planned sub-level remains, reversibility and recovery.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 1.04 (reversibility and recovery) to finish the initial sub-levels for this branch, or return to macro-level and synthesize. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 1.03. Example: "Expand 1.03."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 1.03."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 1.04."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:32:30]

**user**: continue sequentially
[Timestamp: 2026/11/26 13:32:52]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 1.04 Sub-Gap under 1.00: Reversibility, Recovery and Residual Effects

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

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

### Metacognitive Assessment
- **Saturation:** High within Level 1. All four planned sub-levels beneath the temporal gap are mapped.
- **Marginal Returns:** Low. Further sub-levels would likely overlap with 3.00 (relational severity) and 5.00 (trade-offs).
- **Convergence:** Achieved for this branch.
- **Utility:** High Leverage
- **Recommendation & Options:** We have completed the initial proposed sub-levels for this branch. Would you like to continue to 1.05, step up, or synthesize? I recommend returning to macro-level, or Halt & Synthesize. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 1.04. Example: "Expand 1.04."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 1.04."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 1.05."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 1 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:32:52]

**user**: return to level 2
[Timestamp: 2026/11/26 13:33:36]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 2.01 Sub-Gap under 2.00: Supply-Chain Roles and Graded Causal Contribution

**Pointer reset:** I returned to Level 2 and am resuming sequential unfolding beneath 2.00. The next sub-level under it is 2.01.

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Within the distributed-causation gap, the first problem is who the parties are and how each contributed. AI systems pass through many hands, and each hand contributes differently. If v0.03.01 has one generic responsible-agent field and one cause link, it cannot say who did what.

**Key points:**

1. **Role differentiation.** Data providers, model developers, fine-tuners, integrators, deployers, operators, end users and infrastructure suppliers hold different positions. One agent class with a single "responsible" flag erases these differences. Distinct role types would allow precise assignment.
2. **Multiple roles per party.** One organization can hold several roles, such as developer and deployer, and a party's role can change across versions. The model should treat roles as relations between an agent and an incident or system, not as fixed agent types.
3. **Graded contribution types.** Contributions can be necessary, sufficient, enabling, facilitating or background. A binary cause link treats them as equal. Typed contribution links, with an optional degree, would preserve the difference.
4. **Control and knowledge.** What a party could control and what it knew shape its contribution. A deployer with no access to model internals differs from a developer who ignored a known defect. Control and knowledge attributes help interpret each contribution.
5. **One incident, many contributors.** The incident record should hold many contributor links without being duplicated per party. Duplicating records breaks aggregate counts and hides the shared event.

**Explanation:**
The first requirement for representing distributed causation is a vocabulary of who the parties are and how each contributed. AI systems pass through data providers, model developers, fine-tuners, integrators, deployers, operators, end users and infrastructure suppliers, and each stands in a different position relative to a harm. A schema with one generic agent class and a single responsible-agent field erases these differences. A stronger design treats roles as relations between an agent and a system or incident, since one organization may be both developer and deployer, and a party's role may change across system versions. Contribution itself also needs structure. Causes can be necessary, sufficient, enabling, facilitating or merely background, and a binary cause link treats a decisive contribution the same as a remote one. Typed contribution links, with an optional degree, preserve the difference. Interpreting a contribution further depends on what the party controlled and what it knew: a deployer with no access to model internals is differently placed from a developer who disregarded a known defect. Finally, the incident record should hold many contributor links without being duplicated for each party, because duplication corrupts aggregate counts and hides the fact that a single event is shared. Without these elements, accountability analysis collapses to the most visible actor. The practical test for v0.03.01 is whether one incident can carry five contributor relations with different role types, contribution types and knowledge states.

---

### Metacognitive Assessment
- **Saturation:** Moderate within Level 2. The overview and one sub-level are mapped.
- **Marginal Returns:** Moderate. Sub-levels remain on kinds of responsibility, emergent multi-system effects and diffusion of responsibility.
- **Convergence:** Open
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 2.02 (kinds of responsibility: causal, moral, legal and preventive capacity). Alternatively return to macro-level. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 2.01. Example: "Expand 2.01."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 2.01."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 2.02."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 2 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:33:36]

**user**: continue sequentially
[Timestamp: 2026/11/26 13:33:58]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 2.02 Sub-Gap under 2.00: Kinds of Responsibility (Causal, Moral, Legal and Preventive)

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Being a cause of harm, being morally blameworthy, being legally liable and being able to prevent it are four different things. They often point at different parties. If v0.03.01 merges them into one responsibility notion, attribution will be unfair and remediation misdirected.

**Key points:**

1. **Causal responsibility.** This concerns who or what contributed to the outcome in fact. A party can be a cause without any fault, as when a user supplies an unusual input. The ontology should record causal contribution separately from judgments about it.
2. **Moral responsibility.** This depends on knowledge, intent, negligence and the reasonableness of conduct. It requires an assessment, which is normative and may be contested. It should be represented as an attributed judgment, not as a fact.
3. **Legal liability.** Liability depends on jurisdiction, statute and contract, and can attach to parties who were not at fault, such as under strict liability. It may also fail to attach to those who were. The ontology needs a jurisdiction-qualified liability construct.
4. **Preventive capacity.** The party best placed to prevent a harm is often not the one who caused it or who is liable. Capacity depends on access, expertise and control. Recording it supports forward-looking governance.
5. **Divergence among the four.** A single incident can show a different party at the top of each dimension. Keeping the dimensions separate allows the divergence to be seen. A merged field hides it.

**Explanation:**
Causal contribution, moral blame, legal liability and preventive capacity are four distinct ideas that are frequently conflated under the word responsibility. Causal responsibility concerns who or what contributed in fact, and a party can be a cause without fault, for example when a user supplies an unforeseeable input. Moral responsibility depends on knowledge, intent, negligence and the reasonableness of conduct. It is a normative judgment, may be contested, and is best represented as an assessment attributed to a stated assessor and not as a fact about the event. Legal liability depends on jurisdiction, statute and contract. It can attach to parties without fault, as in strict liability regimes, and fail to attach to parties who clearly contributed, so it needs a jurisdiction-qualified construct with a status such as alleged, established or dismissed. Preventive capacity concerns who was best placed to stop the harm given access, expertise and control, and it often points to a different party from the other three, such as a platform operator rather than a model developer. An ontology that holds a single responsible-party field cannot show that one incident may have different parties leading on each dimension, and so cannot support fair attribution, targeted remediation or forward-looking governance. Separating the four dimensions also keeps descriptive claims apart from normative ones. The practical test for v0.03.01 is whether one incident can name a different party as the leading one on each of the four dimensions.

---

### Metacognitive Assessment
- **Saturation:** Moderate to High within Level 2. Two sub-levels are mapped.
- **Marginal Returns:** Moderate. Emergent multi-system effects and diffusion of responsibility remain.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 2.03 (emergent multi-system effects and diffusion of responsibility), or return to macro-level. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 2.02. Example: "Expand 2.02."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 2.02."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 2.03."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 2 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:33:58]

**user**: continue sequentially
[Timestamp: 2026/11/26 13:34:17]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 2.03 Sub-Gap under 2.00: Emergent Multi-System Effects and Diffusion of Responsibility

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Some harms arise only from the interaction of several components or systems, and no single one of them is faulty on its own. In such cases each party may also assume another is guarding against the risk. If v0.03.01 attributes harm only to individual components or agents, these collective failures will appear to have no cause.

**Key points:**

1. **Interaction-level causes.** Automated systems that feed each other, such as trading algorithms or moderation and recommendation pipelines, can produce outcomes none would produce alone. The cause lies in the interaction. The ontology needs a way to attach a cause to a relationship or system of components, not only to one component.
2. **System boundaries.** What counts as the system differs by observer and by purpose. A harm may cross organizational and technical boundaries. The model should let the system under analysis be declared explicitly, with its components and interfaces.
3. **Emergence.** Behavior at the system level may not be predictable from component specifications. This affects foreseeability and testing. The ontology should be able to flag a harm as emergent and record that component-level testing passed.
4. **Diffusion of responsibility.** Each actor may believe another handles the risk, so no one does. This is a gap in oversight, and it is itself causally relevant. An oversight-gap construct would record who was assumed to be responsible and who in fact acted.
5. **Absence as contribution.** Failures to act, monitor or escalate contribute to harm. Event-based models record what happened and miss omissions. Omission needs representation, with the expected duty noted.

**Explanation:**
Some of the most consequential AI harms arise from interaction and not from a defective part. Automated trading algorithms reacting to each other, or recommendation and moderation pipelines feeding one another, can produce outcomes that no single component would produce and that no component test would reveal. An ontology that attaches causes only to individual components or agents has nowhere to record this. It needs a way to attach a causal role to a relationship or to a declared system of components and interfaces, with the system boundary stated explicitly, because what counts as the system varies by observer and often crosses organizational lines. It should also allow a harm to be flagged as emergent, along with the fact that component-level checks passed, since this bears on foreseeability and on the adequacy of testing practice. A related pattern is diffusion of responsibility, where each actor reasonably assumes another is watching the risk and so none does. This oversight gap is causally relevant in itself, and an ontology can capture it by recording who was assumed to hold a duty and who actually acted. Closely tied to this is omission: failures to monitor, escalate or intervene contribute to harm, yet event-based schemas record what happened and not what did not. Omissions need representation, together with the expected duty and its source. The practical test for v0.03.01 is whether a harm with no faulty component, caused by an interaction and by a mutual assumption of oversight, can be recorded without forcing blame onto one party.

---

### Metacognitive Assessment
- **Saturation:** High within Level 2. All three planned sub-levels beneath distributed causation are mapped.
- **Marginal Returns:** Low. Further sub-levels would likely overlap with 5.00 (uncertainty) and 6.00 (granularity).
- **Convergence:** Achieved for this branch.
- **Utility:** High Leverage
- **Recommendation & Options:** We have completed the initial proposed sub-levels for this branch. Would you like to continue to 2.04, step up, or synthesize? I recommend returning to Level 3 or Halt & Synthesize. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 2.03. Example: "Expand 2.03."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 2.03."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 2.04."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 3 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:34:17]

**user**: continue sequentially
[Timestamp: 2026/11/26 13:34:40]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 2.04 Sub-Gap under 2.00: Intent, Misuse and Adversarial Actors

**Pointer note:** This extends the branch beyond the three sub-levels first proposed for 2.00. I treated that list as a tentative roadmap, not a boundary.

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Many AI harms involve a person who deliberately misuses a system, attacks it or exploits a weakness. Others involve no intent at all. If v0.03.01 does not represent intent and adversarial action, it cannot separate accidents, negligence, misuse and attacks, which call for very different responses.

**Key points:**

1. **Intent spectrum.** Harm can result from accident, negligence, reckless deployment, foreseeable misuse or deliberate malice. These need distinct values, since each leads to different remedies and duties. A single "cause" field cannot hold them.
2. **Adversarial actors.** Attackers may poison data, steal models, craft jailbreak prompts or impersonate people with generated content. They are third parties outside the supply chain. The ontology needs an actor type for them, with tactics and goals.
3. **Misuse versus intended use.** Whether an action fell within the system's intended use, a foreseeable misuse or an unforeseeable one affects how responsibility is shared. Intended-use declarations from the developer or deployer should be linkable. Without them, the line cannot be examined.
4. **Dual-use and reuse.** The same capability can serve beneficial and harmful ends, and open release lets others repurpose it. A system may be downstream of its original context. The ontology should record the chain of reuse.
5. **Safeguard failure and circumvention.** Harm may follow a defeated safeguard, whether weak or deliberately bypassed. Recording the safeguard, its purpose and the manner of failure supports prevention analysis. Without this, defenses cannot be evaluated against real incidents.

**Explanation:**
A large share of real AI harm involves someone acting with purpose: a user who misuses a system, an attacker who poisons data or steals a model, a fraudster who impersonates a person with generated media. Others involve no intent whatever, as with plain accident or negligence. These cases lead to very different obligations and remedies, yet a schema with a single cause or responsible-agent field cannot tell them apart. The ontology therefore needs an intent spectrum that distinguishes accident, negligence, reckless deployment, foreseeable misuse and deliberate malice. It also needs an adversarial actor type, covering third parties outside the development and deployment chain, with attributes for tactics, goals and capabilities. Responsibility for misuse depends on whether the action fell within the declared intended use, a foreseeable misuse or an unforeseeable one, so intended-use statements from developers and deployers should be linkable to incidents. Dual-use capability and open release add another layer, since a system may be repurposed far from its original context, and the chain of reuse should be traceable. Finally, safeguards matter: harm often follows a safeguard that was weak, absent or deliberately bypassed, and recording the safeguard, its purpose and the manner of failure lets defenses be tested against real incidents. Without these constructs, all harms look like system faults, deterrence and design lessons are confused, and genuine attacks are blamed on the very organizations they targeted. The practical test for v0.03.01 is whether it can distinguish an attack on a system from a failure of the system, and record the safeguard that was bypassed.

---

### Metacognitive Assessment
- **Saturation:** High within Level 2. Four sub-levels are now mapped.
- **Marginal Returns:** Low. Remaining ideas would mostly repeat 2.01–2.03 or belong at other levels.
- **Convergence:** Achieved for this branch.
- **Utility:** High Leverage
- **Recommendation & Options:** We have completed the initial proposed sub-levels for this branch, plus one extension. Would you like to continue to 2.05, step up, or synthesize? I recommend returning to Level 3 or Halt & Synthesize. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 2.04. Example: "Expand 2.04."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 2.04."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 2.05."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 3 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 13:34:40]

**user**: return to level 3
[Timestamp: 2026/11/26 14:28:17]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 3.01 Sub-Gap under 3.00: Vulnerability, Power Asymmetry and Dependency

**Pointer reset:** I returned to Level 3 and am resuming sequential unfolding beneath 3.00. The next sub-level under it is 3.01.

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** The same output harms people differently depending on how susceptible, dependent or powerless they are in relation to the system and its operator. Type-based harm classes record the output and not the person's position. If v0.03.01 has no vulnerability or power-asymmetry structure, severity will be understated for those who are most at risk.

**Key points:**

1. **Sources of vulnerability.** Vulnerability can come from age, health, crisis, disability, limited literacy, economic precarity or social marginalization. It can be lasting or momentary, as when someone is in acute distress. The ontology needs a way to describe the bearer's state at the time of exposure.
2. **Power asymmetry.** Individuals facing institutions that use automated decisions have little ability to question or avoid them. The imbalance in information, resources and alternatives changes the harm's weight. A relation between bearer and operator should record this asymmetry.
3. **Dependency and lock-in.** People may rely on a system for work, care, income or companionship, with no practical substitute. Harm from a system one cannot leave differs from harm from one that is easy to leave. Dependency and switching cost are relevant attributes.
4. **Susceptibility to the mechanism.** Some people are more affected by persuasion, emotional design or personalization. A system tuned to engagement may exploit exactly these traits. Recording the mechanism and the susceptibility together shows why the harm landed where it did.
5. **Vulnerability as dynamic and relational.** A person is not vulnerable in the abstract, but in relation to a particular system and context. Treating it as a fixed label on the person risks stereotyping. The ontology should attach it to the exposure situation.

**Explanation:**
Two people can receive an identical output and be harmed to very different degrees, because their positions relative to the system differ. A type-based classification records the output and its category, but says nothing about who received it. A fuller account begins with the bearer's state at the time of exposure: age, health, acute crisis, disability, limited literacy, economic precarity or social marginalization, any of which may be lasting or momentary. It then adds the relation between bearer and operator, since individuals facing institutions that use automated decisions often cannot question, avoid or appeal them, and the imbalance in information, resources and alternatives changes how much the outcome weighs. Dependency and lock-in matter too: harm from a system relied on for work, care, income or companionship, with no practical substitute, differs from harm from one that is easy to leave, so dependency and switching cost are relevant attributes. Susceptibility to the specific mechanism is a further factor, because persuasive design, emotional mimicry and personalization affect people unevenly, and systems tuned for engagement may exploit exactly those traits. Importantly, vulnerability is relational and situational, not a fixed label on a person, and modeling it as a property of the exposure situation avoids stereotyping while capturing real differences. Without this structure, severity scores systematically understate harms to those most at risk, and prioritization follows the average case. The practical test for v0.03.01 is whether the same output can be recorded as two incidents of different severity because of the bearer's state and relation to the operator.

---

### Metacognitive Assessment
- **Saturation:** Moderate within Level 3. The overview and one sub-level are mapped.
- **Marginal Returns:** Moderate. Sub-levels remain on consent and recourse, cultural and legal context, intersectionality, and observed versus experienced harm.
- **Convergence:** Open
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 3.02 (consent, recourse and contestability). Alternatively return to macro-level. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 3.01. Example: "Expand 3.01."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 3.01."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 3.02."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 4 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:28:17]

**user**: continue sequentially
[Timestamp: 2026/11/26 14:29:12]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 3.02 Sub-Gap under 3.00: Consent, Recourse and Contestability

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Whether a person agreed to an exposure, and whether they can challenge or reverse its outcome, changes how serious a harm is. A risk freely accepted differs from one imposed without notice. If v0.03.01 does not record consent and recourse, it will treat chosen and imposed harms alike and ignore whether anyone could fix the result.

**Key points:**

1. **Awareness.** Many people do not know an automated system is involved in a decision about them. Harm from an undisclosed system differs from harm from a disclosed one. The ontology should record whether the bearer was told and whether the notice was understandable.
2. **Quality of consent.** Consent can be informed, uninformed, coerced by lack of alternatives or buried in terms of service. Clicking "accept" is not equivalent to meaningful agreement. A graded consent attribute, with basis and context, would capture this.
3. **Scope and withdrawal.** Consent to one use does not cover secondary uses such as retraining on personal data. The ability to withdraw also matters. The ontology should link consent to a defined purpose and record whether withdrawal was possible and honored.
4. **Contestability.** A person may be able to appeal, request human review or demand an explanation, or may face a closed process. The presence, accessibility and effectiveness of such channels determine whether a wrongful outcome persists. Each should be recorded.
5. **Burden of recourse.** Even where recourse exists, it may demand time, expertise or money that the bearer lacks. A nominal remedy that is practically unusable is not a real one. Recording the burden shows the gap between formal and effective recourse.

**Explanation:**
The moral and practical weight of a harm depends in part on whether the affected person agreed to the exposure and whether they can challenge its result. Many people never learn that an automated system took part in a decision about them, so a basic attribute is whether the bearer was informed, and whether the notice was comprehensible. Consent itself varies in quality: it may be informed, uninformed, effectively coerced because there is no alternative, or buried in terms of service, and a click on "accept" is not the same as meaningful agreement. A graded consent attribute with its basis and context would capture this. Consent is also bound to a purpose, since agreeing to one use does not cover secondary uses such as retraining on personal data, and the possibility and honoring of withdrawal should be recorded. On the other side, contestability determines whether a wrongful outcome persists. Channels for appeal, human review and explanation may be present or absent, accessible or obscure, effective or merely formal, and each of these should be representable. Finally, the burden of using recourse matters: a remedy that demands time, expertise or money the bearer lacks is nominal and not real, and recording the burden exposes the gap between formal and effective recourse. Without this structure, a risk freely chosen and one imposed in secret are scored identically, and systems with sham appeal processes appear acceptable. The practical test for v0.03.01 is whether an incident can record an undisclosed system, a low-quality consent and an inaccessible appeal process as separate facts.

---

### Metacognitive Assessment
- **Saturation:** Moderate to High within Level 3. Two sub-levels are mapped.
- **Marginal Returns:** Moderate. Cultural and legal context, intersectionality, and observed versus experienced harm remain.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 3.03 (cultural, legal and jurisdictional context), or return to macro-level. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 3.02. Example: "Expand 3.02."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 3.02."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 3.03."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 4 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:29:12]

**user**: continue sequentially
[Timestamp: 2026/11/26 14:29:52]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 3.03 Sub-Gap under 3.00: Cultural, Legal and Jurisdictional Context

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Whether something counts as harm, and how serious it is, differs across cultures, legal systems and communities. A single universal definition builds one context's assumptions into the ontology. If v0.03.01 has no way to qualify harm by context, it will misclassify or miss harms outside its default frame.

**Key points:**

1. **Norm variation.** Societies differ on speech, modesty, privacy, family authority, religion and data sharing. An output that is routine in one place may be offensive or dangerous in another. The ontology should let a harm be qualified by the norms of the community concerned.
2. **Legal variation.** Jurisdictions define protected categories, privacy rights, liability and prohibited content differently. An act can be unlawful in one place and lawful in another. A harm record needs jurisdiction as a qualifier, with the applicable law identified.
3. **Cross-border incidents.** AI systems operate across borders, so one incident may involve several legal regimes and cultural settings. Bearer, operator and servers may sit in different places. The ontology should accommodate multiple jurisdictions per incident.
4. **Language and representation.** Systems perform unevenly across languages and dialects, and their errors may be harmful in ways a developer's culture does not notice. Harm may be unrecognizable without local knowledge. Local language and community should be recordable attributes.
5. **Whose standard.** Choosing the standard of harm is itself a value judgment. The ontology should show which standard was applied and by whom. This avoids presenting one perspective as neutral fact.

**Explanation:**
Whether an event counts as harm, and how seriously, is not the same everywhere. Societies differ on speech, modesty, privacy, authority, religion and the sharing of data, so a reply that is routine in one setting may be offensive or dangerous in another. Legal regimes also differ: jurisdictions define protected categories, privacy rights, liability rules and prohibited content in their own ways, and the same act can be unlawful in one place and lawful in another. An ontology built on one default frame embeds that frame's assumptions as if they were universal, and then misclassifies or misses harms that arise outside it. A stronger design lets each harm record be qualified by the community norms and the jurisdiction concerned, with the applicable law identified and not assumed. Because AI systems operate across borders, one incident may involve a bearer, an operator and infrastructure in different places, so the model should allow several jurisdictions per incident. Language and representation add a further dimension: systems perform unevenly across languages and dialects, and their errors may be harmful in ways a developer's own culture does not notice, so recording the local language and community helps surface such harms. Underneath all of this is the question of whose standard defines harm. That is a value judgment, and the ontology should show which standard was applied and by whom, instead of presenting one perspective as neutral fact. Without this, harms in under-represented contexts are systematically undercounted. The practical test for v0.03.01 is whether one event can be recorded as harmful under one jurisdiction's standard and not under another's, with both stated.

---

### Metacognitive Assessment
- **Saturation:** High within Level 3. Three sub-levels are mapped.
- **Marginal Returns:** Low to Moderate. Intersectionality and observed versus experienced harm remain.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 3.04 (intersectionality), then 3.05 (observed versus experienced harm) to finish this branch. Or return to macro-level. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 3.03. Example: "Expand 3.03."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 3.03."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 3.04."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 4 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:29:52]

**user**: continue sequentially
[Timestamp: 2026/11/26 14:30:26]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 3.04 Sub-Gap under 3.00: Intersectionality and Compounded Harm

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** People hold several social positions at once, such as race, gender, disability, age and class. Harm at the intersection of these can differ in kind from the sum of harms to each group taken separately. If v0.03.01 tags affected groups as independent categories, it will miss harms that only appear for combinations.

**Key points:**

1. **Non-additive effects.** A system may perform acceptably for women and for darker-skinned people when each group is measured alone, yet fail badly for darker-skinned women. Single-category analysis hides this. The ontology needs to represent combinations as bearers in their own right.
2. **Multiple attributes per bearer.** A flat list of independent protected-category tags cannot express interaction. A bearer needs a structured profile of attributes that can be queried jointly. The profile should be recordable at the level of detail the evidence supports.
3. **Compounding across systems and over time.** Disadvantages in one domain feed into another, such as a credit score affecting housing and then employment screening. Each system's harm looks modest in isolation. Linking harms across domains for the same bearer reveals the compounding.
4. **Structural context.** Intersectional harm is produced by overlapping social structures, not by individual attributes alone. A system that mirrors existing inequality can deepen it. The ontology should allow reference to the structural pattern, not only to the individual incident.
5. **Data scarcity and invisibility.** Small intersectional groups are often too sparse in data to be measured, and so are overlooked. Absence of recorded harm is then not evidence of absence. The ontology should allow a record of "not measurable" as distinct from "no harm found".

**Explanation:**
People occupy several social positions at once, and harm at the intersection of those positions can differ in kind from the sum of harms to each group considered separately. A well-known pattern is a system that appears acceptable for women and for darker-skinned people when each is measured alone, yet performs poorly for darker-skinned women. A schema that tags affected groups with independent categories cannot express this, because it has no way to represent the combination as a bearer in its own right. The remedy is a structured bearer profile with several attributes that can be queried jointly, recorded at whatever level of detail the evidence supports. Compounding also occurs across systems and over time: a disadvantage in credit scoring can feed into housing decisions and then into employment screening, each step looking modest alone. Linking harms across domains for the same bearer exposes this accumulation. Underneath such patterns lie overlapping social structures, and a system that mirrors existing inequality can deepen it, so the ontology should be able to refer to the structural pattern and not only to the single incident. A further difficulty is data scarcity: small intersectional groups are often too sparse for measurement and so are overlooked. The ontology should distinguish "not measurable" from "no harm found", since absence of a record is not evidence of absence. Without these elements, aggregate fairness metrics will pass systems that fail the most disadvantaged combinations. The practical test for v0.03.01 is whether a harm can be recorded for a combination of attributes without being reducible to separate single-attribute records.

---

### Metacognitive Assessment
- **Saturation:** High within Level 3. Four sub-levels are mapped.
- **Marginal Returns:** Low to Moderate. One planned sub-level remains, observed versus experienced harm.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 3.05 (observed versus experienced harm) to finish the initial sub-levels for this branch, or return to macro-level and synthesize. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 3.04. Example: "Expand 3.04."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 3.04."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 3.05."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 4 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:30:26]

**user**: return to level 4
[Timestamp: 2026/11/26 14:30:55]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 4.01 Sub-Gap under 4.00: Typology of Bearers and Standing Conditions

**Pointer reset:** I returned to Level 4 and am resuming sequential unfolding beneath 4.00. The next sub-level under it is 4.01. Branch 3.00 remains open at 3.05 (observed versus experienced harm), which we skipped.

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Harm can fall on many kinds of bearer, and each kind has a different basis for counting as harmed. A person, a community, an institution, an ecosystem and a future generation cannot all be handled by one "victim" class. If v0.03.01 has no typology of bearers with distinct standing conditions, non-individual harms will be forced into person-shaped boxes or left out.

**Key points:**

1. **Types of bearer.** Candidate types include individuals, groups and communities, organizations, institutions, publics, ecosystems, non-human animals and future generations. Each type is harmed in different ways. A typology gives each its own vocabulary of loss.
2. **Standing conditions.** Standing is the basis on which something counts as capable of being harmed, such as interests, welfare, rights or functions. Individuals have interests, institutions have functions and ecosystems have integrity. The ontology should state the standing basis for each bearer type.
3. **Membership and boundaries.** Groups and communities have fuzzy and contested boundaries. Some are self-identified, others are labeled by outsiders, such as statistical categories created by the system itself. The ontology should record how the group was defined and by whom.
4. **Representation and voice.** Many bearers cannot speak for themselves, so someone must represent them. The representative's authority and interests affect the record. The ontology should note who speaks for the bearer.
5. **Nested and overlapping bearers.** An individual belongs to groups, and groups sit within institutions and publics. A harm may hit several levels at once. Relations among bearers should be representable, so the same harm is not counted twice or missed at one level.

**Explanation:**
A harm ontology needs to say who or what can be harmed, and on what basis. Treating every bearer as a generic victim works for individuals but fails for the others. A workable typology would include individuals, groups and communities, organizations, institutions, publics, ecosystems, non-human animals and future generations, with each type carrying its own vocabulary of loss. The reason is that bearers have different standing conditions. Individuals have interests and welfare, institutions have functions and legitimacy, and ecosystems have integrity and resilience, so the basis on which each counts as harmed should be stated, not assumed. Groups raise their own difficulty: boundaries are fuzzy and contested, and some groups are labeled from outside, such as statistical categories generated by the system itself, so the ontology should record how a group was defined and by whom. Many bearers cannot speak for themselves, which means someone represents them, and the authority and interests of that representative shape the record, so the ontology should note who speaks for the bearer. Finally, bearers are nested and overlapping: a person belongs to a community, which sits within an institution and a public, and a single harm may land at several levels at once. Representing relations among bearers prevents double counting and avoids missing harm that is visible only at the collective level. Without this typology, non-individual harms are forced into person-shaped boxes or dropped. The practical test for v0.03.01 is whether it can record one harm borne by an individual, their community and a shared institution as three linked but distinct bearer entries.

---

### Metacognitive Assessment
- **Saturation:** Moderate within Level 4. The overview and one sub-level are mapped.
- **Marginal Returns:** Moderate. Sub-levels remain on commons and structural conditions, aggregation of small harms, non-human and future bearers, and the missing claimant.
- **Convergence:** Open
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 4.02 (commons, public goods and structural conditions). You can also return to Level 3 to finish 3.05. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 4.01. Example: "Expand 4.01."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 4.01."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 4.02."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 3 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:30:55]

**user**: continue sequentially
[Timestamp: 2026/11/26 14:31:23]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 4.02 Sub-Gap under 4.00: Commons, Public Goods and Structural Conditions

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Some of the most important things AI can damage are shared conditions that nobody owns, such as trust in evidence, the quality of public discourse, democratic processes and the integrity of knowledge sources. Damage to these is diffuse and hard to attribute to any one victim. If v0.03.01 records harm only as loss to identifiable bearers, degradation of these commons will not register.

**Key points:**

1. **What counts as a commons.** The information environment, public trust, electoral integrity, scientific literature, cultural heritage and open knowledge resources are shared and non-excludable. Everyone depends on them, and no one is the owner. The ontology needs a class for shared resources and conditions that can be the object of harm.
2. **Diffuse, non-rivalrous harm.** Losses are spread thinly across many people and may not deprive any individual of anything measurable. Yet the aggregate loss can be large. The model needs a notion of harm to the resource itself, separate from harm to users of it.
3. **Pollution and degradation dynamics.** Commons often erode through accumulation, such as synthetic content flooding a search index or training data contaminated by model output. Each addition is small, and the tipping point is hard to see. This links back to cumulative exposure at 1.01.
4. **Structural conditions.** Market concentration, dependence on a few providers and labor market restructuring are conditions that AI can create or worsen. They are not events and have no single incident. The ontology should be able to record structural harm as a state of affairs with contributors, not as a dated occurrence.
5. **Collective action problem.** Each actor gains from using the commons and bears only a share of the damage. Responsibility spreads across many contributors. This connects with diffusion of responsibility at 2.03.

**Explanation:**
Some of the most consequential things AI can damage belong to no one: public trust in evidence, the quality of public discourse, the integrity of democratic processes, scientific and cultural records, and open knowledge resources. These are shared and non-excludable, everyone relies on them, and harm to them is diffuse. An ontology that records harm only as loss to identifiable bearers cannot register such damage, because no single person loses anything measurable even when the aggregate loss is large. It therefore needs a class for shared resources and conditions that can themselves be the object of harm, together with a notion of harm to the resource that is separate from harm to its users. Degradation often occurs by accumulation, for example synthetic content flooding a search index or model output contaminating later training data, so each addition looks trivial and the tipping point is hard to see, which ties this gap to cumulative exposure. Structural conditions such as market concentration, dependence on a few providers and labor market restructuring raise a further problem, because they are states of affairs and not events, with no single incident and no clean date. The ontology should allow structural harm to be recorded as a condition with contributors and a trend, not as a dated occurrence. Finally, commons suffer from a collective action problem: each actor benefits from use and bears only a fraction of the damage, so responsibility spreads thinly across many contributors. Without these constructs, the ontology will favor visible, individual, event-like harms and underweight the slow erosion of shared foundations. The practical test for v0.03.01 is whether it can record harm to a shared resource, with many small contributors, where no individual bearer was measurably harmed.

---

### Metacognitive Assessment
- **Saturation:** Moderate to High within Level 4. Two sub-levels are mapped.
- **Marginal Returns:** Moderate. Aggregation of small harms, non-human and future bearers, and the missing claimant remain.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 4.03 (aggregation of small harms and measurement). Alternatively return to Level 3 to finish 3.05, or return to macro-level. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 4.02. Example: "Expand 4.02."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 4.02."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 4.03."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 3 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:31:23]

**user**: continue sequentially
[Timestamp: 2026/11/26 14:31:45]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 4.03 Sub-Gap under 4.00: Aggregation of Small Harms and Measurement

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** When a system touches millions of people, a small harm to each can add up to a very large total. Per-person severity scores rank such harms as trivial, and incident-based records never see them. If v0.03.01 has no aggregation rules, it will systematically undercount mass low-level harm.

**Key points:**

1. **Scale effects.** A one-minute delay, a small overcharge or a mild bias repeated across millions of people is a significant harm in total. Ranking by individual severity hides this. The ontology needs a way to express population size alongside per-person magnitude.
2. **Aggregation rules.** Totals can be computed by sum, by weighted sum, or by emphasizing the worst-off. Each reflects a different ethical view and gives a different ranking. The ontology should record which rule was used, so results can be compared and challenged.
3. **Distribution of the burden.** The same total can be spread evenly or concentrated on a few. Records that carry only a total lose this. A distribution attribute, or links to subgroup results, preserves it.
4. **Commensurability.** Different kinds of loss, such as time, money, dignity and safety, are hard to put on one scale. Forcing them into a single number hides value judgments. The ontology should keep dimensions of loss separate and mark any conversion as an assumption.
5. **Measurement and detectability.** Small harms are often not reported, and sampling or auditing may be the only way to see them. The record should state how the harm was measured and its likely under-detection. A missing report is not a missing harm.

**Explanation:**
Harm to millions of people at low intensity can be a major harm in total, yet it is the kind most easily missed by an incident-based ontology. A one-minute delay, a small overcharge or a mild bias repeated across a large population is trivial for each person and significant in aggregate. Ranking by per-person severity therefore buries it. To represent such cases the ontology needs population size alongside per-person magnitude, and an explicit aggregation rule. Totals can be summed, weighted, or tilted toward the worst-off, and each choice embodies a different ethical stance and yields a different ranking, so the rule used should be recorded and open to challenge. The distribution of the burden also matters, since the same total can be spread evenly or concentrated on a few people, and a record that holds only the total loses that difference. A distribution attribute, or links to subgroup results, would preserve it. Another difficulty is commensurability: time, money, dignity and safety are different kinds of loss, and forcing them onto one scale hides value judgments, so the ontology should keep dimensions of loss separate and flag any conversion as an assumption. Finally, small harms are rarely reported, and sampling or audit may be the only way to detect them, so the record should state how the harm was measured and how likely it is to be under-detected, making clear that the absence of reports is not the absence of harm. Without these elements, mass low-level harm is systematically undercounted and policy attention flows to dramatic cases. The practical test for v0.03.01 is whether it can record a harm of tiny per-person size across a very large population, with a stated aggregation rule and measurement method.

---

### Metacognitive Assessment
- **Saturation:** High within Level 4. Three sub-levels are mapped.
- **Marginal Returns:** Low to Moderate. Non-human and future bearers, and the missing claimant, remain.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 4.04 (non-human and future bearers), then 4.05 (the missing claimant) to finish this branch. You can also return to Level 3 to finish 3.05. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 4.03. Example: "Expand 4.03."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 4.03."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 4.04."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 3 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:31:45]

**user**: continue sequentially
[Timestamp: 2026/11/26 14:32:01]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 4.04 Sub-Gap under 4.00: Non-Human and Future Bearers

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** AI affects ecosystems, animals and people who do not yet exist, through energy and water use, resource extraction, habitat effects and long-lived technological lock-in. These bearers cannot report harm or claim redress. If v0.03.01 has no place for them, a whole class of AI harm will be excluded by definition.

**Key points:**

1. **Environmental harm.** Training and operating large systems consume energy, water and materials, and produce emissions, e-waste and mining impacts. These fall on ecosystems and on communities near facilities. The ontology should represent environmental bearers and the pathway from system operation to ecological damage.
2. **Non-human animals.** Systems used in agriculture, wildlife monitoring, pet products and surveillance can affect animal welfare, positively or negatively. Animals have interests but no voice. They need standing as bearers, with welfare-based loss types.
3. **Future generations.** Choices made now, such as irreversible capability releases, lock-in of values or depletion of resources, shape options for people not yet born. These bearers do not exist yet and cannot be identified. The ontology should allow a bearer defined by time horizon rather than by individual identity.
4. **Uncertainty and discounting.** Harms to distant bearers are speculative, and how heavily to weigh them is contested. A common practice of discounting the future embeds a view that should be visible. The record should state the horizon and any weighting assumptions.
5. **Irreversibility and option loss.** Harm that removes future choices, such as extinction of a language or loss of an ecosystem, is distinct from harm that can be repaired. This links to reversibility at 1.04. A construct for loss of options would capture it.

**Explanation:**
AI systems affect more than the people who use them. Training and operating large models consume energy, water and materials, and they produce emissions, electronic waste and mining impacts that fall on ecosystems and on communities near facilities. Applications in agriculture, wildlife monitoring and surveillance affect animal welfare. Decisions made now, such as releasing a capability that cannot be recalled, locking in particular values, or depleting resources, shape the options of people who do not yet exist. None of these bearers can report harm or demand redress. An ontology limited to present human persons therefore excludes them by definition, however large the effects. To include them it needs environmental bearers with a described pathway from system operation to ecological damage, non-human animals with standing based on welfare, and bearers defined by time horizon and not by individual identity, since future persons cannot be named. Because harms to distant bearers are speculative and the weight they deserve is contested, the record should state the horizon used and any discounting or weighting assumption, so that a controversial value choice is not hidden inside a number. A final dimension is irreversibility and loss of options: extinction of a language or loss of an ecosystem removes possibilities permanently, which is different in kind from damage that can be repaired. A construct for option loss would capture this and connect to reversibility. Without these constructs, the ontology measures only the harms that are present, human and reportable. The practical test for v0.03.01 is whether it can record harm to an ecosystem and to a future population, each with a stated horizon and an explicit weighting assumption.

---

### Metacognitive Assessment
- **Saturation:** High within Level 4. Four sub-levels are mapped.
- **Marginal Returns:** Low. One planned sub-level remains, the missing claimant.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 4.05 (the missing claimant and recording without complaint) to finish the branch. You can also return to Level 3 to finish 3.05, or synthesize. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 4.04. Example: "Expand 4.04."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 4.04."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 4.05."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 3 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:32:01]

**user**: return to level 5
[Timestamp: 2026/11/26 14:32:23]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 5.01 Sub-Gap under 5.00: Probabilistic, Counterfactual and Near-Miss Harm

**Pointer reset:** I returned to Level 5 and am resuming sequential unfolding beneath 5.00. The next sub-level under it is 5.01. Open items elsewhere: 3.05 and 4.05 were skipped.

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Many AI harms are not settled facts. A system may raise the chance of a bad outcome without clearly causing it, or may nearly cause one. If v0.03.01 stores only realized harm, risks, hazards and near misses will be invisible, and so will the information they carry for prevention.

**Key points:**

1. **Hazard, risk and harm.** A hazard is a potential source of harm, a risk is the likelihood and size of harm, and harm is what actually occurred. These are different entities. An ontology that holds only harm cannot represent the first two.
2. **Probabilistic contribution.** A system may increase the probability of an outcome, as with a medical tool that nudges clinicians toward a wrong diagnosis in some cases. The effect shows up statistically, not in any single case. The ontology needs a way to record contribution to likelihood.
3. **Counterfactual reasoning.** Judging harm often means asking what would have happened without the system. The baseline chosen changes the answer. The record should state the counterfactual used and its basis.
4. **Near misses.** Events where harm was narrowly avoided, by chance or by intervention, signal weaknesses. In safety-critical fields they are systematically collected for learning. The ontology should accept near misses as first-class records, with the factor that prevented harm.
5. **Exposure without outcome.** People may be exposed to a hazard and show no harm, or harm may emerge later. Recording exposure separately keeps these cases findable. This links to cumulative exposure at 1.01.

**Explanation:**
Realized harm is only part of what matters, yet most ontologies store only that. A hazard is a potential source of harm, a risk combines the likelihood and size of harm, and harm is what actually occurred, and treating these as one thing leaves no place to record the first two. Many AI effects are probabilistic: a clinical decision tool may raise the rate of a wrong diagnosis in a minority of cases, visible in statistics but in no single instance, so the ontology needs a way to record contribution to likelihood, not only to outcomes. Judging harm often depends on a counterfactual, namely what would have happened without the system, and the baseline chosen changes the conclusion, so the record should state the counterfactual used and its basis. Near misses deserve explicit treatment. In aviation, medicine and other safety-critical fields they are systematically collected because they reveal weaknesses before damage occurs, and an AI harm ontology should accept near misses as first-class records, including the factor that prevented harm, whether chance, human intervention or a safeguard. Exposure also needs separate recording, since people may be exposed to a hazard with no visible outcome, or the outcome may emerge later, and keeping exposure distinct keeps these cases findable. Without these constructs, the ontology can learn only from failures that have already hurt someone, and early warning is impossible. The practical test for v0.03.01 is whether it can record a hazard, a near miss and a probabilistic contribution to risk, none of which involved a confirmed harm.

---

### Metacognitive Assessment
- **Saturation:** Moderate within Level 5. The overview and one sub-level are mapped.
- **Marginal Returns:** Moderate. Sub-levels remain on claim status, evidence and provenance, competing and versioned accounts, and trade-offs.
- **Convergence:** Open
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 5.02 (claim status and disputed harm). You can also return to Level 3 or 4 to finish 3.05 and 4.05. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 5.01. Example: "Expand 5.01."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 5.01."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 5.02."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 4 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:32:23]

**user**: continue sequentially
[Timestamp: 2026/11/26 14:32:52]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 5.02 Sub-Gap under 5.00: Claim Status, Evidence and Provenance

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** Reports of AI harm range from audited findings to rumor, and they are often contested. A record that does not show how well established it is looks the same whether it is solid or doubtful. If v0.03.01 has no status, evidence or provenance fields, analysis built on it will mix confirmed and unconfirmed harms.

**Key points:**

1. **Claim status.** A harm may be alleged, under investigation, substantiated, disputed, dismissed or retracted. Status changes as events proceed. A controlled vocabulary for status, with dates, lets users filter by reliability.
2. **Evidence types and quality.** Evidence can be a systematic audit, a court finding, a regulator's report, a journalistic investigation, a user complaint or social media anecdote. They differ greatly in weight. The ontology should link each claim to its evidence and classify the evidence type.
3. **Confidence.** Beyond status, a graded confidence qualifier shows how strongly the evidence supports the claim. It should be attributed to an assessor, since different assessors may differ. Confidence is a judgment and should not be written as a fact.
4. **Provenance.** Who reported the harm, who recorded it, from what source and when? A chain of provenance makes it possible to trace errors and spot duplicated reports of one event. Without it, repeated citations of one source look like independent confirmation.
5. **Reporting bias.** Harms are reported unevenly, with high-profile systems and well-resourced bearers overrepresented. The record should note how it was collected so that bias can be assessed. Counts of reports are not counts of harms.

**Explanation:**
Reports of AI harm span a wide range, from audited findings and court judgments to anecdotes and rumor, and many are contested by the developers, the regulators or the affected parties themselves. An ontology that stores every record as an equally established fact cannot distinguish these. A controlled vocabulary for claim status, such as alleged, under investigation, substantiated, disputed, dismissed and retracted, with dates, lets users filter by reliability and see how a case evolved. Status should be accompanied by links to evidence, classified by type, because a systematic audit, a court finding, a regulator's report, a journalistic investigation and a social media post carry very different weight. A graded confidence qualifier adds nuance, but it is a judgment and should be attributed to a named assessor and not written as a fact about the event. Provenance is equally important: who reported the harm, who recorded it, from what source and when. A recorded chain makes it possible to trace errors, detect duplicate reports of one event, and avoid mistaking repeated citations of one source for independent confirmation. Finally, reporting is biased. High-profile systems and well-resourced bearers are overrepresented, and many harms are never reported, so the record should note how it was collected, and users should be warned that counts of reports are not counts of harms. Without these elements, aggregate statistics and policy conclusions drawn from the data compound unnoticed bias. The practical test for v0.03.01 is whether a record can show a disputed claim with typed evidence, an attributed confidence level and a documented source chain.

---

### Metacognitive Assessment
- **Saturation:** Moderate to High within Level 5. Two sub-levels are mapped.
- **Marginal Returns:** Moderate. Competing and versioned accounts, and trade-offs and co-benefits, remain.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 5.03 (competing accounts and revision history). You can also return to Level 3 or 4 to finish 3.05 and 4.05. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 5.02. Example: "Expand 5.02."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 5.02."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 5.03."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 4 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:32:52]

**user**: continue sequentially
[Timestamp: 2026/11/26 14:33:17]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 5.03 Sub-Gap under 5.00: Competing Accounts and Revision History

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** The same event is often described differently by the developer, the regulator, the press and the people affected, and understanding changes as investigations proceed. A record that holds one characterization, and overwrites it when it changes, loses both the disagreement and the history. If v0.03.01 works this way, it cannot show who said what, when, or why a classification changed.

**Key points:**

1. **Multiple characterizations.** Parties may disagree on what happened, how severe it was, what caused it and whether it counts as harm. Each account has its own source and standing. The ontology should hold several attributed assertions about one event, without forcing a single winner.
2. **Attribution of assertions.** A statement such as "this was a privacy harm" is a claim made by someone at a time. Recording the asserting party keeps interpretation separate from event. This also guards against borrowed authority, where a contested label looks like neutral fact.
3. **Versioning and revision history.** As evidence arrives, classifications are updated, severities revised and causes reattributed. Overwriting erases what was previously believed and why. Versioned assertions preserve the trail and allow reconstruction of what was known at a given date.
4. **Reconciliation and canonical views.** Users often need a single working view. The ontology can support this by marking which assertion a given view adopts and on what basis, without deleting the others. Choice of view becomes transparent.
5. **Identity of events.** Different accounts may refer to the same event or to different ones. Deciding that two reports are the same incident is itself a judgment. The ontology should allow links such as "same as", "part of" or "disputed identity" between records.

**Explanation:**
The same event is frequently described in different ways by the developer, the regulator, the press and the people affected, and the understanding of it changes as investigations proceed. An ontology that stores one characterization per event, and overwrites it when new information arrives, loses both the disagreement and the history. A sounder design holds several assertions about one event, each attributed to a source and a date, without forcing a single winner. Attribution matters because a statement such as "this was a privacy harm" is a claim made by someone, and recording who made it keeps interpretation separate from the underlying event, and prevents a contested label from passing as neutral fact. Versioning is the companion requirement: classifications are updated, severities revised and causes reattributed as evidence arrives, and overwriting erases what was previously believed and why. Versioned assertions preserve the trail and allow reconstruction of what was known on a given date, which is essential for judging foreseeability and the quality of the response. Users still need a single working view, which can be supported by marking which assertion a view adopts and on what basis, leaving the others intact, so the choice is visible. Finally, whether two reports describe the same event is itself a judgment, so the ontology should allow identity links such as same-as, part-of and disputed-identity between records, which prevents both double counting and false merging. Without these constructs, the ontology presents a tidy but false consensus. The practical test for v0.03.01 is whether one event can carry two conflicting attributed characterizations, with a revision history showing when one replaced the other.

---

### Metacognitive Assessment
- **Saturation:** High within Level 5. Three sub-levels are mapped.
- **Marginal Returns:** Low to Moderate. Trade-offs and co-benefits remain.
- **Convergence:** Open, but stabilizing.
- **Utility:** High Leverage
- **Recommendation & Options:** Continue to 5.04 (trade-offs and co-benefits) to finish the branch. You can also return to Level 3, 4 or 6 to finish 3.05, 4.05 or add 6.01, or synthesize. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 5.03. Example: "Expand 5.03."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 5.03."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 5.04."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 6 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:33:17]

**user**: continue sequentially
[Timestamp: 2026/11/26 14:33:41]

**ai**: 

### Inputs & Provenance Frontmatter
- **Input A:** What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations? `[Explicitly Provided by User]`
- **Input B:** Option 3, LLM Parametric Baseline `[Explicitly Provided by User]`
- **Input C:** General AI-harm and risk-ontology scholarship `[Assumed by Skill]`
- **Input D:** Representational adequacy of v0.03.01 against real-world AI harm situations `[Assumed by Skill]`
- **Input E:** Moderate rigor, narrative level `[Assumed by Skill]`
- **Input F:** Contemporary AI deployment era `[Assumed by Skill]`
- **Input G:** On completion, a collected set of gap assessments. Each has a 2–5 sentence summary, numbered bullets of 2–5 sentences each, and one 200–250 word explanation. On Halt & Synthesize, a design note containing all assessments. No design note before then. `[Explicitly Provided by User]`

---

## 5.04 Sub-Gap under 5.00: Trade-offs, Co-Benefits and Secondary Harm

**Caveat:** Option 3 cuts off vault access, so I did not read the v0.03.01 schema. This assessment is a hypothesis from general harm-ontology scholarship, to be checked against the schema.

**Summary:** AI systems that cause harm often also deliver real benefits, sometimes to the same people. Efforts to reduce one harm can create another. A schema that records only harm cannot show these tensions. If v0.03.01 is purely harm-centered, it will misrepresent situations where the question is a trade-off and not a simple wrong.

**Key points:**

1. **Co-benefits.** A system may harm a person in one respect and help them in another, such as a navigation tool that saves time but routes traffic through a quiet neighborhood. Recording only the harm presents half the situation. The ontology should allow linked benefit records for the same system, bearer or event.
2. **Distribution of benefit and harm.** Benefits may go to one group and harms to another, as when a service is cheaper for many and costly for a few. Who gains and who loses is central to fairness. Bearer links on both sides make the distribution visible.
3. **Mitigation side-effects.** Safeguards, filters and restrictions can create new harms, such as content moderation that suppresses legitimate speech from minority communities. Interventions need to be modeled as events that can themselves cause harm. This links to responses within a harm process at 1.03.
4. **Competing harms and values.** Reducing privacy harm may increase safety harm, and the reverse. Such conflicts reflect competing values and cannot be settled by the ontology. It should represent the conflict and the judgment made, with who made it.
5. **Counterfactual benefit.** Whether a harm is acceptable can depend on what the alternative would have been. A flawed tool may still outperform existing practice. The baseline should be recorded, linking to counterfactual reasoning at 5.01.

**Explanation:**
Systems that cause harm usually also provide real benefits, sometimes to the same people, and efforts to reduce one harm can produce another. A purely harm-centered schema cannot register this. It records half of the situation and so invites misleading conclusions, either that a system is simply bad or that its benefits excuse its costs. A more adequate ontology would allow linked benefit records attached to the same system, bearer or event, together with bearer links on both sides so that the distribution of gains and losses is visible, since fairness often turns on who benefits and who pays. Mitigation deserves special attention: safeguards, filters and restrictions can themselves cause harm, such as moderation that suppresses legitimate speech from minority communities, so interventions should be modeled as events capable of producing secondary harm. Some situations involve competing harms and competing values, for example privacy against safety, and the ontology cannot resolve these, but it should represent the conflict, the judgment that was made, and who made it, so that the choice is open to examination. Evaluating acceptability also depends on a baseline, because a flawed tool may still outperform existing practice, and recording the chosen baseline ties this to counterfactual reasoning. Care is needed, however, so that the benefit side is not used to launder serious harm, which suggests keeping benefit and harm as separate, non-netted records. Without these elements, the ontology cannot represent dilemmas, and discussion collapses into blame or defense. The practical test for v0.03.01 is whether it can record a mitigation measure that reduced one harm and created another, alongside the benefit that the system provided.

---

### Metacognitive Assessment
- **Saturation:** High within Level 5. All four planned sub-levels beneath epistemic status are mapped.
- **Marginal Returns:** Low. Further sub-levels would likely repeat earlier material.
- **Convergence:** Achieved for this branch.
- **Utility:** High Leverage
- **Recommendation & Options:** We have completed the initial proposed sub-levels for this branch. Would you like to continue to 5.05, step up, or synthesize? Open items remain at 3.05, 4.05 and Level 6 sub-levels. I recommend finishing those briefly or choosing Halt & Synthesize. No design note will be created until you choose Halt & Synthesize.

### Your Options
1. **[Expand]** Add detail, lineage or guiding questions for 5.04. Example: "Expand 5.04."
2. **[Drill Deeper]** Break this into narrower sub-levels. Example: "Drill deeper into 5.04."
3. **[Continue Sequentially]** Move to the next section at this depth. Example: "Continue to 5.05."
4. **[Step Up / Return to Level…]** Example: "Step up one level", "Return to macro-level", or "Return to Level 6 and continue".
5. **[Integrate & Branch]** Harvest a side discussion and place it in the outline. I will ask where it goes.
6. **[Halt & Synthesize]** Conclude, collect all assessments, and generate the design note.
[Timestamp: 2026/11/26 14:33:41]

**user**: halt and synthesize
[Timestamp: 2026/11/26 14:34:15]

**ai**: 
<!-- copilot-message {"tools":["write (edit): 08_Resources/design-note-harm-ontology-v0.03.01-structured-inquiry-synthesis.md","edit (edit): 08_Resources/design-note-harm-ontology-v0.03.01-structured-inquiry-synthesis.md"]} -->
[Timestamp: 2026/11/26 14:34:15]