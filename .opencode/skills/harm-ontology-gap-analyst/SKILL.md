---
name: harm-ontology-gap-analyst
description: Performs focused inquiry into the adequacy of a harm ontology. Generates discipline-based searchlights (questions, competencies, blind spots), translates them into observable harms, operationalizes the judging layer, benchmarks against institutional frameworks (e.g., EIA, CBA, HRIA, AIA), and maps v3 schema gaps (Mandate, Valuation, Triggers, Remedies) using the placement test.
license: MIT
metadata:
  copilot-enabled-agents: opencode, codex, general
  copilot-builtin-version: "3"
---

# Harm Ontology Searchlight and Gap Analyst

## Workflow

1. **Differentiate the Perspectives:** For any discipline-based perspective (e.g., Classical, Legal, Ethical, Anthropological, Physical, Cognitive), articulate its unique competencies, blind spots, and foundational inquiries so that perspectives remain distinct rather than collapsing into generic ethics.
2. **Generate the Searchlight:** Derive core questions from the perspective's unique tradition and competencies (e.g., 10 to 20 structured inquiries across thematic dimensions).
3. **Translate Questions into Observable Harms:** Convert abstract philosophical or systemic inquiries into 10 checkable statements of actual or potential harm observable in news stories, regulatory filings, or corporate disclosures (e.g., Anthropic S-1 filings).
4. **Operationalize the Judging Layer:** Define the dimensions, instruments, scoring criteria, and procedural workflows required to assess whether a situation or organization exhibits those harms.
5. **Benchmark against Real-World Frameworks:** Cross-reference the inquiry against established institutional assessment practices (Cost-Benefit Analysis, Rights Impact Assessments, Environmental Impact Assessments, Algorithmic Fairness Audits, etc.).
6. **Gap-Mapping v3 against the Benchmark:** Identify missing or insufficiently expressive classes, subclasses, and camelCase attributes across four core institutional gap groups:
   - **Institutional Mandate & Enforcement Authority**
   - **Methodological Metric Specification (Valuation & Currency)**
   - **Procedural Lifecycle & Trigger Rules**
   - **Remedial Closure & Prescriptive Output**
7. **Apply the Placement Test:** Test every proposed schema extension to ensure it hangs off the correct root (e.g., procedural layer / `HarmAssessment` rather than static `PerspectiveType`).

## Schema Extensions Reference

Refer to [Gap Mapping Benchmarks](references/GAP_MAPPING_BENCHMARKS.md) for the complete list of candidate classes, subclasses, and camelCase attributes, and [Placement Test](references/PLACEMENT_TEST.md) for the structural placement rules.

## Validation Checklist

- [ ] Every perspective-based inquiry yields specific, checkable observable harms.
- [ ] Institutional frameworks are benchmarked against real-world usage and regulatory oversight.
- [ ] Schema extensions pass the placement test (tradition vs. assessment vs. factor vs. output).
- [ ] Attributes use camelCase and are compatible with editor-first ontology standards.
