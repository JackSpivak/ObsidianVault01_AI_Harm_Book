---
fileClass: Idea
type: idea
status: seed
bookmark: HO-003
canonical_id: ho-003-causal-assembly-perfect-storm
territory: new
tags: [ontology/harm]
aliases: [HO-003, Causal Assembly, Perfect Storm, participatesIn]
created: 2026-11-14
filed: 2026-11-14
---

# HO-003 — Causal Assembly: the Perfect Storm

Index: [[_Harm Ontology Bookmark Index]] · Top-level

> [!note] Revision 2026-11-17
> The class `CausalAssembly` is renamed **`FactorAssembly`** (altLabel "causal assembly") and is now a **thin container**: an identifier and label that rival assessments refer to. Its members, `sufficientFor`, `individuallyInnocuous`, `hasUnknownMembers`, `origin` and `orchestrator` are supplied by `CausalAssessment`, not asserted on the assembly. Factor and FactorAssembly share the parent class `CausalCandidate`. See [[Decisions_Log]] 2026-11-17 and [[Harm Ontology v3 - Draft Structure]].

> [!warning] Revision pending (2026-11-15)
> "Jointly sufficient" and membership are **as assessed**, not plain facts. See [[HO-005 Assessed Membership and Systematic Omission]]. Not yet logged; to be decided after the re-attribution tests.

## Why this is distinct
- A cause is not a single thing. It is an **assembly of participating factors**, often with some members unknown or unknowable. Factors `participatesIn` a `CausalAssembly`. The assembly, not any one factor, is jointly sufficient for an effect or outcome.

## Anticipated direction
- `CausalAssembly`: hasMember → Factor (inverse of `participatesIn`); hasUnknownMembers (Unknown / Undisclosed / Pending); individuallyInnocuous; origin (Emergent / Exploited / Engineered); orchestrator → Agent (?); sufficientFor → Effect / Outcome.
- `Factor —participatesIn→ CausalAssembly`. A factor can take part in many assemblies.
- A new divergence pattern: **factor-level vs. assembly-level.** Every member is judged Neutral; the assembly is judged Harmful.
- Possible reuse: the OBO Relation Ontology has a "participates in" relation (from memory, unverified). Needs checking for fit, since it's defined for continuants participating in processes.

## Conceptual territory
- New in this model. It's similar to the Swiss cheese model (Reason), mosaic theory (intelligence and privacy), attack chains (cybersecurity) and task-decomposition jailbreaks (AI safety), all from memory and unverified.

## Summary
- "Perfect storm" names the idea exactly: no factor is sufficient alone, but together they are. Cause can be inferred, loosely, from the assembly even when it's incomplete. The dangerous version is an **attack vector**: an assembly deliberately built from parts that each pass inspection, or an emergent one that someone exploits. It's hard to detect, easy to deny ("my part was harmless"), and well suited to AI, which can assemble harmless parts at scale.

## Original wording
> "i believe we chose factor over cause because as a foundational claim, it would be illusory to claim that a single entity is a cause of harm..  typically many things, circumstances, interventions, etc are causative factors."
- **Attribution:** Author

> "yes. i like to think that we could infer or deduce cause (i am speaking loosely) from an assembly of participating factors.  perhaps worth noting this is the actual meaning behind the notion of \"a perfect storm\".  even if all factors are not known or knowable.  also, this seems to be a very likely vector of attack that creates harm - if it were created intentionaly or even came about unintentionally and was exploited"
- **Attribution:** Author

> "i love the idea of causal assembly especially because i see factors as \"participating in\" a cause which we now make expllicit as participating in a causal assembly.  also it suggests a property on factor object property participatesIn"
- **Attribution:** Author

> "Its defining feature is that **each factor passes inspection on its own.**"
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references (all from memory, unverified):** James Reason, Swiss cheese model; mosaic theory; cybersecurity attack chains; task-decomposition jailbreaks; OBO Relation Ontology "participates in".

## Real-world examples
- A harmful request split into sub-requests that each look harmless (task decomposition).
- Several low-severity vulnerabilities chained into a serious breach.

## Why it matters to the book
- It gives a precise form to a defence typical of AI harm: every contributor's part was harmless. It also suggests how a harmful AI might act without any single action ever looking harmful.

## Open questions
- How does CausalRole relate to the assembly? Is a role borne *within* an assembly (`CausalRole —withinAssembly→ CausalAssembly`)?
- Can assemblies be nested (sub-assemblies)?
- Can "jointly sufficient" be established when members are Unknown?

## Related
- [[HO-I.a Factor and CausalRole]]
- [[HO-III.a Divergence and Integration - True but Partial]]
- [[HO-002 Ontology Stress-Test Suite]] (T19, T20)
- [[HO-II.e Missingness Statuses and Domain Profiles]]
