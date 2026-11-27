---
fileClass: Idea
type: idea
status: seed
bookmark: draft
canonical_id:
territory: new
tags: [ontology/harm, harmfulness, assessment, reification, decision/pending]
aliases: [Harmfulness as Assessment, Reified Harmfulness]
created: 2026-11-23
---

# Harmfulness Is an Assessment - Storm, Gun and Reified Class

## Why this is distinct
It challenges the idea that harmfulness is a physical property of an object. It treats harm as always a judgment, and asks whether harmfulness should itself become a class that can be reasoned over.

## Anticipated direction
Harmfulness is modelled as an assessment that depends on an assessor, an objective standard and a criterion. Whether `AssessedHarmfulness` is a subclass of `Harmfulness` or the only first-class form is an open choice.

## Conceptual territory
Capability versus harm; relational versus intrinsic properties; the gun-rights debate; sensor-dependent judgment; reification in ontology design.

## Summary
- Physical objects have capabilities. Calling a storm or a gun harmful is always a judgment that depends on a model of the mechanism. (Paraphrase.)
- If the sensor data is skewed, the classification is an error in the assessment, not a fact about the storm. (Paraphrase.)
- The gun debate turns on the same point: capability is shared, and the disagreement moves to who holds the object, their intent or lack of skill, and the criteria used. (Paraphrase.)
- Harmfulness could become a class with its own properties (`hasAssessor`, `hasObjectiveStandard`, `hasHarmfulnessCriterion`). (Paraphrase.)
- **Pending, not decided:** either keep `Harmfulness` as a reified parent with `AssessedHarmfulness` as a subclass, or drop ontic harmfulness and make `AssessedHarmfulness` first-class.

## Original wording
> "someone or some organization may believe because of the triad of object capability that someone or something is harmful.  but inevetably that is an assessment.  weather predictions are famously falliblle and speaking of the storm as harmful may depend on the attributedMechanism being flawed.  maybe sea and atmospheric temperatures are believed to be critically moving a normal storm into a severly harmful one.  but sensor data is flawed and skews the required mechanism"
- **Attribution:** Author
- **Source:** Structured inquiry session, 2026-11-23, `copilot/copilot-conversations/agent__structured_inquiry@20261123_184258.md`

> "you said above that harmfulness until we reframe is:  You are suggesting we completely eliminate the unprovable, naive "view from nowhere" (Harmfulness as an intrinsic, objective property.  I am thinking of it rather as a thing "class" that can have all of its own properties to be reasoned over - like assessor, hasobjectivestandard or hasharmfulnessCriterion (or maybe harmfulness criterion is a subclass of ObjectiveStandard and is in the domain of hasHarmfulnessCriterion"
- **Attribution:** Author
- **Source:** Same session

- **External references:** None checked in this session. The gun-rights argument is referred to as the author framed it.

## Real-world examples
- A storm classed as severe because atmospheric temperature sensors are skewed.
- A firearm whose harm depends on the holder's intent and skill, and on who is within range.

## Why it matters to the book
It separates the capability debate, which can be settled by physics, from the harm debate, which is a dispute about assessment. That lets the book show where disagreements actually sit.

## Open questions
- Is a harmfulness criterion a technical threshold (testable) or a moral principle (argued)?
- Does any useful reasoning need an unassessed harmfulness? If so, the reified parent survives; if not, the first-class option wins.

## Related
- [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] (S37)
- [[Decisions_Log]] (pending row, 2026-11-23)
- [[Harm Ontology v0.03.01 Design Notes - Harmfulness, Imagined Harm and Causal Chains]]
