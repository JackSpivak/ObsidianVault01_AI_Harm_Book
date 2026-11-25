# Harm Ontology v0.03.01 Design Guide: Vision, Principles, Commitments, Rationale

**Status:** Proposed Core Design Guide  
**Version:** v0.03.01  
**Related Indexes:** [[_Harm Ontology v0.03.1 Bookmark Index]]  
**Supersedes:** All prior v1/v2/v3 structural assumptions regarding ontic harm objects.

---

## 1. Vision & Core Premise

Harm Ontology v0.03.01 establishes a radically honest, epistemically grounded foundation for modeling harm, risk, and structural impact across disciplines. 

The foundational commitment of v0.03.01 is simple and non-negotiable: **Harm is an assessment, never an intrinsic property.** 

There are no objective, ontic "harms" floating in physical reality. A physical event (such as a storm, a chemical reaction, or an algorithmic denial of service) is neutrally real. Whether that event, process, or structure counts as "harmful"—and how contributions to it are attributed—is **inevitably an assessment made from a perspective**. 

---

## 2. Core Principles & Commitments

1. **Describe vs. Classify:** Theories of harm and discipline perspectives *describe and judge* situations; they do not classify intrinsic properties of the universe as "harmful" or "harmless."
2. **Assessment-Everywhere Architecture:** All evaluations of valence (harmful/beneficial), cause (attribution), and responsibility are modeled as first-class assessments (`HarmAssessment`, `CausalAssessment`) linked to an evaluating perspective.
3. **The Thin Container Pattern:** Complex groupings—such as causal assemblies (`FactorAssembly`) or causal chains—are treated as "thin containers" (an identifier and label only). Their membership, sufficiency, boundaries, and omissions are never asserted as objective facts; they are supplied entirely by competing or aligned assessments.
4. **Perspective-Relative Worldviews:** Every evaluation is anchored to a `PerspectiveType` (the tradition, lens, or discipline framework) and instantiated via a `PerspectiveSpecification` (the specific analytical snapshot or "shot").
5. **Open World & Explicit Missingness:** The schema assumes an open world where omissions, blind spots, and unstated assumptions are first-class objects of inquiry rather than hidden edge cases.

---

## 3. Rationale: Abandoning Ontic Harm

Earlier iterations of harm ontologies attempted to maintain taxomadic trees of "harm types" (e.g., somatic, psychological, pecuniary) as intrinsic classes of things. This created an unresolvable philosophical trap: the same event (such as cutting down a forest) would simultaneously have to be classified as both "environmental harm" (under an ecological lens) and "economic benefit" (under a resource extraction lens), generating logical contradictions in an OWL reasoner.

v0.03.01 resolves this by removing "Harm" as a first-class class. Instead:
- **Reality is neutral:** Acts, processes, omissions, conditions, and structures are represented as neutral **Factors** and **Effects**.
- **Judgments are perspectival:** When an institution or discipline evaluates reality, it generates a **HarmAssessment** against a stated Evaluative Standard, utilizing its own conceptual vocabulary (its "Spoke" scheme).
- **Disagreement is structural:** Divergent verdicts between disciplines (e.g., legal liability versus economic efficiency) are represented natively as first-class divergences between assessments, preserving multidisciplinary integrity without forcing a false consensus.

---

## 4. Architectural Layers

- **Layer 1 (Neutral Backbone):** `Factor`, `Effect`, `FactorAssembly` (thin container), `CausalRole`. Completely valence-neutral.
- **Layer 2 (Perspectival & Judging Layer):** `PerspectiveType`, `PerspectiveSpecification`, `HarmAssessment`, `CausalAssessment`. Handles the machinery of evaluation, standards, horizons, and scope.
- **Layer 3 (Discipline Modules & Vocabularies):** SKOS Concept Schemes (`eco:scheme`, `law:scheme`, `int:scheme`) attached via the Hub-and-Spoke pattern, allowing individual disciplines to extend the ontology with their own objects, relations, and worldviews.
