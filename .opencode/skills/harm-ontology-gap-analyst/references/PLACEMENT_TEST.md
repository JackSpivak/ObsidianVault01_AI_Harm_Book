# The Placement Test

When proposing new classes, subclasses, or attributes for the Harm Ontology, every element must undergo the **Placement Test** to verify its ontological attachment point.

## The Rule
Given a proposed schema element, ask:
1. **Does it describe a tradition or lens?** (`PerspectiveType`, defaults only) — *e.g., historical school of thought, philosophical tradition.*
2. **Does it describe a particular act of assessment?** (`HarmAssessment` / `Assessment` / Procedure) — *e.g., statutory basis, mandatory trigger, deadline duration, valuation methodology.*
3. **Does it describe the thing assessed?** (`Factor`, `Effect`, `AffectedEntity`) — *e.g., objective properties, causal roles, affected populations.*
4. **Does it describe an output or resolution?** (`RemedialObligation`, `PrescriptiveOutput`, closure status) — *e.g., injunctions, mitigation requirements, audit closure.*

## Guidelines
- **Split Elements:** If an element fits multiple categories, split it into its component parts.
- **Unclear Elements:** Record unclear items as open placement questions rather than defaulting them incorrectly to `PerspectiveType`.
- **Reasoning:** A tradition (`PerspectiveType`) has no statute, deadline, or remedy of its own. Procedural requirements and enforcement powers belong on the assessment/regulatory layer (e.g., `HarmAssessment`), while remedies belong on the prescriptive output layer.
