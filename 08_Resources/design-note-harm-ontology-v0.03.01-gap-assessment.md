---
title: Design Note - Harm Ontology v0.03.01 Gap Assessment (Section 1.00)
type: design-note
skill: structured-inquiry-epistemic-unfolder
skill_version: "1.0"
section: "1.00"
grounding_mode: LLM Parametric Baseline
input_a: "What aspect or level of the proposed harm ontology v0.03.01 is not sufficiently represented to capture real world situations?" [Explicitly Provided by User]
input_b: "Option 3 - LLM Parametric Baseline" [Explicitly Provided by User]
input_c: "General AI-harm / risk-ontology scholarship" [Assumed by Skill]
input_d: "Representational adequacy of v0.03.01 against real-world AI harm situations" [Assumed by Skill]
input_e: "Moderate conceptual rigor, narrative level" [Assumed by Skill]
input_f: "Contemporary (current AI deployment era)" [Assumed by Skill]
input_g: "Narrative gap assessments: 2-5 sentence summary, numbered 200-250 word explanations, design note" [Explicitly Provided by User]
status: hypotheses-to-test
---

# Harm Ontology v0.03.01: Gap Assessment (Section 1.00)

> [!warning] Epistemic caveat
> Grounding mode was LLM Parametric Baseline, so vault access was cut off. The v0.03.01 schema was not read. Each gap below is a hypothesis drawn from general harm-ontology scholarship. Each needs checking against the actual schema.

## Summary

Harm ontologies for AI systems commonly model harm as a discrete event with one cause, one individual victim and a fixed severity. Real situations differ in five ways. They unfold over time, have many contributing actors, depend on context, fall on collective or non-human bearers, and are known only with uncertainty. Version v0.03.01 is most likely under-represented on these five dimensions. Each gap below names the likely missing constructs and a test to apply to the schema.

## Gaps

1. **Temporal and processual structure.** Most harm ontologies model harm as a discrete event: an incident occurs, an affected party suffers a loss, a category is assigned. Real situations involving AI systems rarely behave this way. Harm often accumulates slowly through repeated low-level exposures, such as a recommender system gradually shifting a teenager's self-image, or a hiring filter that quietly narrows a career over years. Other harms are latent, with the damaging decision made at deployment but the consequence surfacing months later, or only when conditions change. An ontology that lacks first-class representation of duration, onset delay, escalation, recurrence, reversibility and recovery will flatten these trajectories into a single timestamped record, losing exactly what makes them hard to detect and remedy. The likely missing constructs are a harm process or trajectory entity distinct from the harm event, with phases (exposure, onset, amplification, stabilization, residual effects), thresholds separating tolerable from damaging accumulation, and explicit links to intervention points where the course could have been altered. Without these, the ontology cannot answer when a harm became foreseeable, whether remediation arrived in time, or whether a minor incident belongs to a larger pattern. Test: does time appear only as an attribute on events, or as a structural dimension of the model?

2. **Distributed causation and attribution.** Real-world AI harms seldom have a single identifiable author. A model is trained by one organization on data gathered by others, fine-tuned by a second, integrated by a third, deployed by a fourth and operated by users who may adapt it in unforeseen ways. Harm emerges from interactions across this chain, and sometimes between several systems at once, as in automated trading or moderation pipelines feeding one another. An ontology that models a harm with one cause, one responsible agent and one affected party cannot express this. The probable gaps are the absence of a causal contribution structure allowing partial, necessary, enabling or merely facilitating causes; of roles separating developer, deployer, operator, user, data provider and infrastructure supplier; and of a distinction between causal responsibility, moral responsibility, legal liability and capacity to prevent. Also missing may be emergent system-level behavior that no component exhibits alone, and diffusion of responsibility, where each actor believes someone else guards against the risk. Without such structure, accountability analysis defaults to blaming the most visible actor, and remediation targets the wrong point. Test: can v0.03.01 represent one incident with five contributing parties, each with a different type and degree of contribution, without duplicating the incident record?

3. **Context, vulnerability and relational severity.** Harm is not a property of an output alone; it depends on who encounters it, in what circumstances, and with what resources. The same chatbot reply may be benign for one user and dangerous for someone in crisis, and the same biased score may be an inconvenience for one applicant and a life-altering barrier for another. Ontologies that classify harms by type, such as privacy, discrimination or physical safety, tend to treat severity as intrinsic, neglecting vulnerability, power asymmetry, dependency, consent and the availability of recourse. Cultural and legal context also changes whether something counts as harm at all. Another probable gap is intersectionality, where compounded identities produce harms not reducible to single-category effects. Equally important is the difference between harm as measured by an observer and harm as experienced or reported by the affected person, which can diverge sharply and carry different legitimacy in different institutions. The model likely needs a contextual layer linking harm instances to situated bearers, conditions of exposure, moderating factors and sources of perspective, so that severity becomes relational and derived rather than fixed. Test: are severity and affected-party classes context-dependent, or hard-coded?

4. **Non-individual and non-human bearers.** Many harm ontologies implicitly assume that the bearer of harm is an individual human being. Yet significant AI-related harms fall on communities and demographic groups, organizations, democratic institutions, labor markets, the information environment, ecosystems affected by energy and water use, non-human animals and future generations. Harm to such bearers often cannot be decomposed into harm to identifiable individuals. Erosion of shared trust in evidence, homogenization of cultural production, or degraded representation of a language community are cases where each person's loss may be slight while the collective loss is large. Likely gaps include the lack of a typology of bearers with different standing conditions, the absence of constructs for commons, public goods and structural conditions, and no way to represent harm that is diffuse, non-rivalrous or spread thinly across many people. Individual-centered models also assume a victim who can notice, report and claim, while collective and future harms have no natural claimant, which affects how they are recorded and prioritized. A sufficiently expressive ontology would make the bearer a polymorphic class with aggregation rules and distinct notions of loss per type. Test: does the bearer class extend beyond persons, and how are aggregate harms expressed?

5. **Epistemic status, uncertainty and trade-offs.** Real harm records are uncertain, disputed and incomplete, yet ontologies often store them as settled facts. Many AI harms are counterfactual or probabilistic: a model may have increased the likelihood of an outcome without determinably causing it. Others are near misses, exposures that produced no damage yet, or alleged harms contested by developers, regulators and affected parties. Evidence quality varies from rigorous audit to anecdote, and interpretations change as investigations proceed. An ontology without epistemic metadata cannot distinguish a confirmed incident from a hypothesis, represent competing accounts of the same event, or revise a classification without erasing history. Probable missing constructs include evidence and provenance links, confidence qualifiers, status values (alleged, substantiated, disputed, retracted), versioned assertions attributed to the asserting party, and modeling of risk and hazard as distinct from realized harm. Related is the omission of trade-offs: an intervention preventing one harm may cause another, or a harm may coexist with real benefits to the same party, and a purely harm-centered schema cannot register this. Test: can a single event carry multiple, conflicting, sourced characterizations with confidence levels and revision history?

## Metacognitive Assessment

- Saturation: Low
- Marginal Returns: High
- Convergence: Open
- Utility: High Leverage
- Recommendation: validate each hypothesis against the actual v0.03.01 schema (switching to Vault-Grounded mode), then drill into the highest-impact gaps.
