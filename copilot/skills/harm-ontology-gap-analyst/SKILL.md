---
name: harm-ontology-gap-analyst
description: Performs focused inquiry into the adequacy of a harm ontology. Generates discipline-based searchlights (questions, competencies, blind spots), translates them into observable harms, operationalizes the judging layer, benchmarks against institutional frameworks (e.g., EIA, CBA, HRIA, AIA), and maps v3 schema gaps (Mandate, Valuation, Triggers, Remedies) using the placement test.
license: MIT
metadata:
  copilot-enabled-agents: opencode, codex, general
  copilot-builtin-version: "3"
---

# Harm Ontology Searchlight and Gap Analyst

## Intention Framing & Purpose

This skill performs focused inquiry into the adequacy of a harm ontology. It starts from a discipline-based perspective, generates the questions it would ask (its searchlight, with its competencies and blind spots), and tests whether those questions yield checkable findings in real-world reporting. It then operationalises the judging layer, benchmarks it against institutional practice, and identifies gaps in how the model represents the search, the findings, and the consequences or remedies. 

The process is iterative. **Success is measured by whether the model can represent a real assessment, not by the elegance of its internal structure.**

---

## Required Inputs & Invocation Triggers

To execute this skill successfully, provide:
1. **Input A: A Discipline-Based Perspective** (e.g., *Classical Council*, or any other discipline perspective). **Trigger Rule:** If you name a known perspective (like the Classical Council) or ask to start from one, Copilot will immediately generate its core competencies and 10–20 structured questions as the first action.
2. **Input B: An Empirical Target Narrative / Case Text** (e.g., a news story, corporate filing, or risk excerpt like the Anthropic SEC S-1) in which to search for harm.
3. **Input C: The Target Ontology Schema** (e.g., Harm Ontology v3 draft structure or mini TTL files) against which gap-mapping is evaluated.

---

## Workflow

### Step 1: Elicit Perspective & Generate the Searchlight
- **Action:** Using **Input A**, articulate the perspective's unique intellectual tradition, core competencies, and blind spots. 
- **Output:** Automatically generate 10–20 core investigative questions partitioned across thematic dimensions.

### Step 2: Translate Questions into Observable Harms
- **Action:** Take the abstract inquiries from Step 1 and apply them to **Input B** (the target narrative/case text).
- **Output:** Reframing original questions into checkable statements of actual or potential harm observable in empirical reporting.

### Step 3: Operationalize the Judging Layer
- **Action:** Define what an institutional assessment of these harms requires: dimensions, instruments, scoring criteria, and procedural workflows.

### Step 4: Benchmark against Real-World Frameworks
- **Action:** Cross-reference the inquiry against established institutional assessment practices (Cost-Benefit Analysis, Rights Impact Assessments, Environmental Impact Assessments, Algorithmic Fairness Audits, etc.).

### Step 5: Gap-Mapping against the Target Ontology
- **Action:** Compare the findings, judging mechanics, and institutional requirements against **Input C** (the ontology schema). Identify missing or insufficiently expressive classes, subclasses, and camelCase attributes across four core gap groups:
  - **Institutional Mandate & Enforcement Authority**
  - **Methodological Metric Specification (Valuation & Currency)**
  - **Procedural Lifecycle & Trigger Rules**
  - **Remedial Closure & Prescriptive Output**

### Step 6: Apply the Placement Test
- **Action:** Test every proposed schema extension to ensure it hangs off the correct root (e.g., procedural layer / `HarmAssessment` rather than static `PerspectiveType`).

---

## Schema Extensions Reference

Refer to [Gap Mapping Benchmarks](references/GAP_MAPPING_BENCHMARKS.md) for the complete list of candidate classes, subclasses, and camelCase attributes, and [Placement Test](references/PLACEMENT_TEST.md) for the structural placement rules.

## Validation Checklist

- [ ] Naming a perspective immediately triggers question/competency generation.
- [ ] All three required inputs (Perspective, Target Narrative, Target Ontology) are accounted for.
- [ ] Perspective-based inquiry yields specific, checkable observable harms from the target narrative.
- [ ] Institutional frameworks are benchmarked against real-world usage and regulatory oversight.
- [ ] Schema extensions pass the placement test (tradition vs. assessment vs. factor vs. output).
