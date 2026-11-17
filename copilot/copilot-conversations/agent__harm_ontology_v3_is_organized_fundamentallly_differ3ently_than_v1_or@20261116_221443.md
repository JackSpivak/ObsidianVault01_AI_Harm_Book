---
epoch: 1794892483139
mode: agent
backendId: claude
sessionId: "947e513d-268e-4d1c-bbec-d2a3fa509008"
topic: "harm ontology v3 is organized fundamentallly differ3ently th…"
model: '{"baseModelId":"default","effort":"low"}'
tags:
  - copilot-conversation
usage: '{"usedTokens":41670,"contextWindow":1000000,"inputTokens":2,"outputTokens":3,"cacheReadTokens":34484,"cacheWriteTokens":7181,"updatedAt":1794892521575}'
---

**user**: harm ontology v3 is organized fundamentallly differ3ently than v1 or v2a.  what is the best way to identify where v2a can be used to define or enrich existinhg class and structure
[Timestamp: 2026/11/16 22:14:43]

**ai**: The best approach is to **break each v2a element into the claims it makes, then route each claim to a v3 home**. Matching v2a class names against v3 class names won't work.

## Why name-matching fails

v1 and v2a are classification hierarchies: "X *is a kind of* harm." v3 puts no harm in the classes themselves. Factors and Effects are neutral, and valence lives only in Assessments taken from a Perspective ([[HO-premise No Intrinsic Harmfulness]]). So one v2a class usually bundles several things that v3 keeps apart. Take `ProbabilisticRiskHarm`:

| Part of the v2a class | v3 home |
|---|---|
| "a risk exists" | `Factor › Risk` |
| "it may or may not happen" | Effect `modality` / `temporalStatus: Pending` |
| "risk itself counts as harm" | an EvaluativeStandard (`LossOfChance`) |
| "it is harm" | a **verdict** in an Assessment, not a class |

The mapping is one-to-many. A simple "old → new" crosswalk will either drop parts or force the old framing back into v3.

## Method: a decomposition crosswalk (Phase 2)

**1. Inventory by script.** Use rdflib in your `harm-ontology` environment to list every class, property, individual and annotation in v1, plus the v2a attributes. Output one row per element as CSV/markdown. Phase 0 counted 51 classes, 19 properties and 106 concepts in v1. Add the v2a Compendium attributes to that list.

**2. Ask the same routing questions about every element.** Each "yes" adds a target:
- Does it name **something that happens or exists** (an act, process, structure or exposure)? → **Factor** kind
- Does it name **what happens to someone**? → **Effect** kind, plus Patient / ObjectOfHarm
- Does it describe **how things combine** (thresholds, aggregation, innocuous parts)? → **CausalAssembly** pattern or a **CausalRole** property
- Does it give a **reason something counts as harm**? → **EvaluativeStandard** individual (philosophical, legal or causal)
- Does it reflect **who is judging, when, or how**? → **Perspective** property or Assessment profile
- Is it a **graded dimension** (severity, reversibility, observability)? → **property** on Effect, Role or Assessment
- Is it a **legal consequence** (cause of action, remedy)? → **LegalResponse**
- Does it build in **valence** ("harmful X")? → split it: neutral kind + standard + example Assessment
- None of the above? → **gap** (v3 may be missing something) or **retire** (with reason)

**3. Crosswalk row schema:**
`old IRI | claim fragment | v3 target(s) | relation (exact / narrower / split / enriches / gap / retired) | narrative to carry | external match (AIRO/DPV) | status`

A row is a *fragment* of the old element, not the whole element. The "enriches" relation is how v2a helps you: a v2a attribute often becomes a new property or value on an existing v3 class, not a new class.

**4. Pilot one meta-category first.** I'd start with Meta-category V, because it touches Factor, CausalAssembly and criticality. Its abstract, non-legal classes will test the routing questions hardest. Change the questions if needed, then run the rest.

**5. Count the gaps.** Gaps are the most useful result. They're where v2a *defines* v3 rather than just filling it in. Capability Approach is already one: functionings and conversion factors don't have an obvious home. Treat each gap as a design decision for the [[Decisions_Log]], not a migration task.

## Two cautions
- **Don't migrate narrative yet.** Phase 3 copies text verbatim to the new IRIs. If one old definition is split across three homes, decide which home is primary and add an `editorialNote` on the others. Settle that per row before any text moves.
- **Resolve open v3 items when a row needs them.** Some rows will depend on undecided questions (Condition split, Agent, Assent as an object of harm). Mark those rows `blocked: <question>` so the crosswalk shows which open questions block the most migration.

If you'd like, I can write the inventory script and draft the pilot crosswalk for Meta-category V next.
<!-- copilot-message {"tools":["Glob (read)","Read (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md","Read (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology Migration Plan.md"]} -->
[Timestamp: 2026/11/16 22:14:43]