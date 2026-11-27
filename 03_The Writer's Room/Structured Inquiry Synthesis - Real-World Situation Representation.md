---
type: note
status: active
tags: [ontology/harm, structured-inquiry, gap-analysis, d-u-l, synthesis]
aliases: [Structured Inquiry Synthesis - Real-World Situation Representation, Harm Ontology Gap Analysis Synthesis]
created: 2026-11-26
workstream: "[[Handoff - Harm Ontology]]"
---

# Structured Inquiry Synthesis: Real-World Situation Representation in Harm Ontology v0.03.01+

## Executive Summary
This synthesis captures the results of a structured inquiry (via the Sequential Epistemic Unfolder using Option 4 / Multi-Modal Synthesis) addressing how ontology v0.03.01 represents real-world situations, identifying its structural gaps, and establishing the relator-based situation characterization framework.

## 1. The Representational Deficit in v0.03.01
- **State vs. Situation Ambiguity:** DUL's lack of a native `State` class creates tension between treating states as `Qualities` with time intervals versus complex `Situations`.
- **Omission and Non-Action:** Harms arising from omissions or non-agentive changes risk being unrepresented if tied strictly to active agentive causes (`dul:Action`).
- **Perspectival Divergence:** While multiple determinations of a single event are possible, v0.03.01 needed a clearer mechanism to explain *why* observers carve up the same situation into different causal boundaries and severity horizons.

## 2. The Tripartite Situation Characterization Framework
To correctly represent real-world situations, the ontology characterizes them across three axes:
1. **Structural Axis:** Entities, roles (`ImpactedRole`), and emergent collective unity (`unitySource`, `unityLocus`) so that group and systemic harms are preserved.
2. **Epistemic Axis:** Assessor perspective and declared temporal horizons (`atHorizon`), separating immediate kinetic impact from delayed chronic degradation.
3. **Modal Axis:** Determination subclasses (`Condition`, `Exposure`, `Relevance`, `Chain`, `Responsibility`, `Consent`, `Remedy`, and `FunctionalHarmDetermination`) covering somatic, psychological, pecuniary, normative, and functional (availability, integrity, confidentiality) impairments.

## 3. Architectural Guardrails
- **Shallow-Tree Rule:** Avoid over-specification by subclassing primarily on physical versus social, delegating complexity to open semantic properties (`unitySource`, `manifestsAs`, `hasModality`).
- **Competency Testing:** Validate all structures against bidirectional coverage matrices (questions-to-classes and classes-to-questions) tested on real case scenarios like the surgeon-sued case.

## Related Vault Notes
- [[2026-11-24 Harm Ontology Common Schema and DUL Alignment Session]]
- [[Model Structure Test Note - Competency Questions and Coverage]]
- [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]]
- [[Decisions_Log]]
