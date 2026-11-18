---
fileClass: Idea
type: idea
status: developing
bookmark: HO-I.b
canonical_id: ho-effect-cascades
territory: new
tags: [ontology/harm]
aliases: [HO-I.b, Effect, Harm Cascades]
created: 2026-11-14
filed: 2026-11-14
---

# HO-I.b — Effect and Cascades

Index: [[_Harm Ontology Bookmark Index]] · Parent: [[HO-000 Harm as Perspective-Relative Assessment|HO-000]] · Tier HO-I (core model)

## Why this is distinct
- Effect is a separate, **neutral** class. It carries AffectedEntity-specific properties that Factors don't have. Effects can also bear roles and lead to further effects, so harm and benefit can cascade.

## Anticipated direction
- Kinds of effect as subclasses (SleepLoss, ReputationalDamage, Deskilling, CapturedAssent, Death…); actual occurrences as instances.
- Properties: affects (AffectedEntity), hasObjectOfHarm, experienceability, severity, reversibility, temporal trajectory, modality, isPosthumous, isStatistical, isDispositional.
- `Effect —leadsTo→ Effect` for cascades. Effect and Factor are not disjoint.
- An optional `HarmfulEffect` class, *inferred* only from a Harmful assessment.

## Conceptual territory
- New relative to v1, where effects were fused into harm classes and attributes.

## Summary
- Most standards judge the effect, so it needs its own class. But "cause" and "effect" are positions in a chain: organ damage is the effect of the bullet and the cause of death. A harmful effect for one person can become a beneficial factor for another (grief → activism → reform), and a beneficial one can become harmful (convenience → dependence → deskilling).

## Original wording
> "I think an effect is a seperate class with a variety of harmfulEffects being possible as instances
> what do you think"
- **Attribution:** Author

> "just as a given role may be harmful or helpful depending on the circumstance, so can be an effect. especially if the state induced in the obeject of harm itself becomes a beneficial agent in a causation chain."
- **Attribution:** Author

> "An effect is simply a factor seen from the receiving end."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references:** none.

## Real-world examples
- Wrongful credit denial → lost housing → job loss → depression (a cascade).
- A whistleblower is fired → public outrage → regulatory reform (a harmful effect becoming a beneficial factor).

## Why it matters to the book
- Cascades are how AI harm spreads beyond the first victim, and how benefits get cited to excuse harms.

## Open questions
- Should net results across a chain ever be assessed, or only individual links? (The current lean is both, always labelled with scope.)

## Related
- [[HO-I.a Factor and CausalRole]]
- [[HO-premise No Intrinsic Harmfulness]]
