---
fileClass: Idea
type: idea
status: seed
bookmark: draft
canonical_id:
territory: new
tags: []
aliases: [Ontology vs LLM, Why a Harm Ontology]
created: 2026-11-16
---

# Advantages of a Harm Ontology vs Strict LLM Training

## Why this is distinct
- This note argues for why the harm ontology should exist at all, as opposed to relying on a trained LLM to analyze harm. Other ontology notes are about what goes inside it.

## Anticipated direction
- Becomes the "why" section of the ontology documentation and possibly a book argument: what an LLM can't guarantee, a formal ontology can.
- Each advantage could become a test case in [[HO-002 Ontology Stress-Test Suite]]: does v3 actually deliver it?

## Conceptual territory
- New as a standalone argument. It draws on [[Interdisciplinary_Harm_Ontology_Compendium v2a]] (its class and property names) and [[Harm Ontology v3 - Draft Structure]].

## Summary
- A formal ontology has 14 advantages over relying only on a trained LLM to analyze harm, on top of 9 core benefits named earlier (no drift, standard terms, completeness, deterministic inference, auditability, reproducibility, separate governance, graph queries, less popularity bias).
- **Epistemological:** it records what a harm *isn't* as well as what it is, leaves unsupported claims as visible gaps instead of fluent prose, lets frameworks disagree on the same event, and keeps facts apart from moral or legal judgment.
- **Computational:** it's compact for context windows, modular through imports, validatable with SHACL, migratable across versions, and runnable cheaply offline.
- **Governance:** it frees harm criteria from vendor safety filters, can be read and amended by non-engineers, allows shared reporting across institutions, supports counterfactual "flip one property" simulation, and keeps institutional memory.
- **The gap:** governing harm through model training versus governing it through an explicit, auditable ontology is a real gap. I found no public evidence that labs such as Anthropic use a formal harm ontology; they publish prose principles. See [[#Do labs use formal harm ontologies? (research, 2026-11-16)]].

## Main text (verbatim, as provided by the author)

Beyond the core structural benefits already discussed (eliminating drift, standardizing terminology, enforcing completeness, deterministic inference, auditability, reproducibility, decoupled governance, knowledge-graph querying, and mitigating training-data popularity bias), removing brevity constraints reveals **14 additional technical, epistemological, legal, and operational advantages** of using a formal ontology rather than relying solely on a trained LLM for harm analysis:

### Overview

| # | Advantage | Group |
|---|---|---|
| 1 | Explicit Preservation of Normative Boundaries (`skos:scopeNote` Exclusion Rules) | I. Epistemological & Analytical |
| 2 | Protection Against "Fluency Bias" & Persuasive Hallucination | I. Epistemological & Analytical |
| 3 | Preservation of Cross-Disciplinary Tension Without Premature Synthesis | I. Epistemological & Analytical |
| 4 | Separation of Descriptive Fact from Normative Judgment | I. Epistemological & Analytical |
| 5 | Token-Window & Context-Budget Efficiency | II. Computational & Engineering |
| 6 | Composable & Modular Architecture (`owl:imports`) | II. Computational & Engineering |
| 7 | Automated Completeness & Missing-Data Detection (SHACL / ShEx Validation) | II. Computational & Engineering |
| 8 | Backward & Forward Schema Migration | II. Computational & Engineering |
| 9 | Lightweight Edge & Air-Gapped Execution | II. Computational & Engineering |
| 10 | Decoupling Domain Policy from Proprietary AI Safety Filters | III. Governance, Legal & Institutional |
| 11 | Multi-Stakeholder & Democratic Deliberation | III. Governance, Legal & Institutional |
| 12 | Standardized Cross-Institutional Data Sharing & Federated Reporting | III. Governance, Legal & Institutional |
| 13 | Counterfactual & Sensitivity Simulation | III. Governance, Legal & Institutional |
| 14 | Institutional Memory & Pedagogical Scaffolding | III. Governance, Legal & Institutional |

### I. Epistemological & Analytical Advantages

1. **Explicit Preservation of Normative Boundaries (`skos:scopeNote` Exclusion Rules):**
   An LLM relies on statistical association, often blurring neighboring concepts together. A formal ontology explicitly encodes negative boundaries—defining not just what a harm *is*, but what it *is not* (e.g., strictly separating actionable `harm:InjuriaSineDamnoHarm` from non-actionable competitive losses like *Damnum Absque Injuria*, or distinguishing `harm:ProbabilisticRiskHarm` from actualized injury).

2. **Protection Against "Fluency Bias" & Persuasive Hallucination:**
   LLMs are optimized to produce coherent, confident, and persuasive prose. When analyzing ambiguous scenarios, an LLM can invent plausible-sounding moral or legal rationalizations that mask analytical gaps. An ontology forces claims into rigid, falsifiable slots—if a required property (such as `harm:hasCausationMechanism` or `harm:hasVictim`) cannot be grounded in evidence, the gap remains visibly empty rather than papered over with eloquent prose.

3. **Preservation of Cross-Disciplinary Tension Without Premature Synthesis:**
   In complex socio-technical scenarios, philosophical ethics, tort law, behavioral economics, and AI safety often disagree on whether an event constitutes a harm. An LLM naturally smooths over these tensions to produce a unified summary. An ontology allows multiple conflicting frameworks (e.g., `harm:HedonicHarm` vs. `harm:PerfectionistTeleologicalHarm` vs. `harm:KantianDeontologicalHarm`) to coexist explicitly on the same event record, preserving theoretical pluralism.

4. **Separation of Descriptive Fact from Normative Judgment:**
   LLMs frequently conflate empirical setbacks with moral wrongness due to alignment tuning (RLHF). An ontology structurally decouples the empirical mechanics of an event (`harm:hasComparativeBaseline`, `harm:hasCausationMechanism`, `harm:hasSeverityMagnitude`) from its moral or legal status (`harm:hasNormativeStatus`: `harm:NonNormativeSetback` vs. `harm:NormativeWrongful`), allowing analysts to record factual damage without prematurely assigning blame.

### II. Computational & Engineering Advantages

5. **Token-Window & Context-Budget Efficiency:**
   Prompting an LLM with tens of thousands of words of legal doctrine, philosophical definitions, and edge-case rules on every API call is expensive, slow, and degrades attention over long contexts ("lost in the middle"). An ontology compresses domain expertise into lightweight, high-density URIs and class hierarchies that can be injected selectively or traversed externally via graph queries.

6. **Composable & Modular Architecture (`owl:imports`):**
   Formal ontologies are modular by design. A general harm ontology can cleanly import domain-specific sub-ontologies (e.g., medical bioethics, financial compliance, cybersecurity CVEs, or child safety) without breaking existing definitions or requiring a monolithic model update.

7. **Automated Completeness & Missing-Data Detection (SHACL / ShEx Validation):**
   Using graph validation languages like SHACL (Shapes Constraint Language), an ontology-driven pipeline can mathematically verify whether a harm assessment is structurally valid before it is accepted—for example, automatically rejecting an assessment of `harm:PrivateTortiousHarm` if it lacks a populated `harm:hasPerpetrator`, `harm:hasVictim`, and `harm:hasRemedialDutyBearer`.

8. **Backward & Forward Schema Migration:**
   When a harm taxonomy evolves (e.g., splitting a broad class into two finer-grained subclasses), formal ontology versioning (`owl:equivalentClass`, `owl:deprecated`, `skos:broader`/`skos:narrower`) allows historical harm logs to be migrated and re-queried programmatically. With raw LLM text outputs, historical assessments must be completely re-run from scratch whenever analytical definitions change.

9. **Lightweight Edge & Air-Gapped Execution:**
   Once events are mapped into ontological triples, downstream rule evaluation, risk triage, and compliance checks can run in milliseconds on standard CPUs without GPU infrastructure, external API calls, or internet connectivity—critical for classified, air-gapped, or high-throughput real-time systems.

### III. Governance, Legal & Institutional Advantages

10. **Decoupling Domain Policy from Proprietary AI Safety Filters:**
    Commercial LLMs embed opaque, vendor-controlled safety guardrails that may refuse to analyze sensitive harms (e.g., self-harm, violence, hate speech, or biological risks) or apply a single corporation's moral stance. An external ontology allows an organization, court, or research institution to define and enforce *its own* transparent, domain-appropriate harm criteria independently of the underlying foundation model.

11. **Multi-Stakeholder & Democratic Deliberation:**
    Non-technical stakeholders—philosophers, judges, economists, ethicists, regulators, and affected communities—can directly read, debate, and amend a structured ontology (as demonstrated by the Joint Councils structure in your compendium). By contrast, modifying an LLM's internal behavior requires specialized machine learning engineering (fine-tuning, RLHF, or activation steering).

12. **Standardized Cross-Institutional Data Sharing & Federated Reporting:**
    When hospitals, regulators, AI labs, and insurers need to pool incident data (e.g., tracking systemic AI failures or public health hazards), free-text LLM reports create insurmountable entity-resolution problems. Shared ontological URIs allow disparate institutions to aggregate harm telemetry without exposing sensitive raw text.

13. **Counterfactual & Sensitivity Simulation:**
    Because ontological attributes are discrete, structured variables, analysts can run deterministic counterfactual simulations—flipping a single property (e.g., changing `harm:hasModality` from `harm:ProbabilisticRisk` to `harm:ActualizedHarm`, or `harm:hasScalabilityAsymmetry` from `harm:HighFrictionProportional` to `harm:ZeroMarginalCostReplication`) to observe how downstream legal standing, duty-bearing, and risk scores shift.

14. **Institutional Memory & Pedagogical Scaffolding:**
    An ontology captures not just labels, but intellectual lineage (`skos:historyNote`, `dcterms:bibliographicCitation`). It serves as an enduring, self-documenting institutional knowledge base that trains both human analysts and AI agents in the precise conceptual heritage behind every harm category, preventing institutional amnesia as teams and models turn over.

## Original wording
> The full verbatim text is the **Main text** section above, copied unchanged at the author's request ("please structure the markdown using the following material verbatim"). Only the layout changed on 2026-11-16 (overview table added, spacing evened, `---` dividers removed); the words did not.

> "new idea note please for advantages of a Harm Ontology vs strict LLM training"
- **Attribution:** Author (request). The main text was pasted by the author. It reads as output from an AI conversation ("your compendium", "removing brevity constraints"), but which model or session produced it isn't stated, and I couldn't locate it in the vault.
- **Source:** Obsidian Copilot agent session, 2026-11-16 (`copilot/copilot-conversations/agent__are_you_able_to_find_a_conversation_segment_in_which@20261115_182550.md`).
- **External references:** [[Interdisciplinary_Harm_Ontology_Compendium v2a]] (the `harm:` classes and properties cited, and the Joint Councils structure). Technical claims (SHACL, "lost in the middle", `owl:imports`) are **unverified** here.

## Do labs use formal harm ontologies? (research, 2026-11-16)

### Summary
- **Anthropic:** no public evidence of a formal, machine-readable harm ontology used in training or governance. What's published is prose: Claude's Constitution (January 2026, CC0) and the Usage Policy (updated October 8, 2026, per secondary sources). A "Unified Harm Framework" is mentioned by one secondary source (unverified; contents not found).
- **Inference (not sourced):** training on principles (Constitutional AI, RLHF) turns them into model weights. Nothing in the weights enforces the guarantees listed above. Those benefits come from an ontology *alongside* the model.
- **Public alternatives exist**, though none matches this compendium's philosophical and legal depth:

| Resource | Form | Notes |
|---|---|---|
| AIRO (AI Risk Ontology), ADAPT Centre | OWL 2, open source | EU AI Act + ISO 31000 based |
| VAIR (Vocabulary of AI Risks) | Taxonomy on AIRO | Draft, "no official standing" |
| IBM Risk Atlas Nexus | Open source, ontology-based | Reuses AIRO |
| MIT AI Risk Repository | Database + taxonomies | 7 domains / 24 subdomains; causal taxonomy |
| CSET AI Harm Taxonomy | Taxonomy | About 10 harm types; MIT severity scale 1–5 |
| MLCommons AILuminate | Hazard taxonomy | 12 hazard categories (secondary sources) |

- **Book angle:** governing harm through model training versus governing it through an explicit, auditable ontology is a real gap, not just a rhetorical one.

### Original wording
> "does claude use standard, well established, explicit, rich ontologies like this one in the prodction of their llms to guarantee that the benefits mentioned above are persistant and governed across development, training and use?  are these standard ontologies of harm available in the public domain?  if not are they published by anthropic anywhere and available for use"
- **Attribution:** Author

> "I found no public evidence that Anthropic trains or governs Claude with a formal, machine-readable harm ontology (OWL/SKOS) like yours. What it publishes is written in prose."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

> "The benefits in your note belong to an ontology *alongside* a model, not to a model trained on principles."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5). Inference, not sourced.

> "The comparison holds up as a real gap: governing harm through model training versus governing it through an explicit, auditable ontology."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session, 2026-11-16 (`copilot/copilot-conversations/agent__are_you_able_to_find_a_conversation_segment_in_which@20261115_182550.md`).
- **External references** (from web search results; pages not opened, so details are unverified):
	- [Claude's Constitution (PDF)](https://www-cdn.anthropic.com/cffd979fd050fbc0d8874b8c58b24cc10554e208/claudes-constitution_webPDF_26-01.26a.pdf)
	- Usage Policy update, secondary: [MindStudio](https://www.mindstudio.ai/blog/anthropic-cruelty-policy-claude), [Progressive Robot](https://www.progressiverobot.com/2026/10/09/anthropic-usage-policy-cruel-behavior-claude-ai/)
	- [AIRO](https://w3id.org/AIRO) · [OECD catalogue: AIRO](https://oecd.ai/en/catalogue/tools/airo-ai-risk-ontology) · [AIRO paper (Zenodo)](https://zenodo.org/records/6821845) · [VAIR](https://w3id.org/vair)
	- [MIT AI Risk Repository paper](https://futuretech.mit.edu/publication/the-ai-risk-repository-a-meta-review-database-and-taxonomy-of-risks-from-artificial-intelligence) · [MIT Incident Tracker harm taxonomy](https://airisk.mit.edu/ai-incident-tracker/harm-taxonomy) · [MIT update incl. MLCommons](https://airisk.mit.edu/blog/april-2025-update-of-the-ai-risk-repository-2)

## Real-world examples
- None yet.

## Why it matters to the book
- It explains why the book builds a formal harm ontology instead of trusting a model's judgment. Advantage 2 (fluency bias) and advantage 10 (vendor safety filters) are themselves AI-harm themes.

## Open questions
- Several examples use v1/v2a names (`harm:HedonicHarm`, `harm:PrivateTortiousHarm`, `harm:hasVictim`). In v3, where harm is judged rather than intrinsic, many of these change. Should the examples be rewritten in v3 terms?
- Advantage 3 (frameworks coexisting on one event) is close to v3's "divergence is first-class". Is that a match, or does v3 go further?
- Which of these claims are true of *any* ontology, and which depend on the pipeline built around it?

## Related
- [[Harm Ontology v3 - Draft Structure]]
- [[HO-000 Harm as Perspective-Relative Assessment]]
- [[HO-002 Ontology Stress-Test Suite]]
- [[Harm Ontology Migration Plan]]
