---
fileClass: Idea
type: idea
status: seed
bookmark: HO-004
canonical_id: ho-004-criticality-leverage-scope-limits
territory: new
tags: [ontology/harm]
aliases: [HO-004, Limits of Scope, Butterfly Effect, Temporal Asymmetry]
created: 2026-11-14
filed: 2026-11-14
---

# HO-004 — Criticality, Leverage and the Limits of Scope

Index: [[_Harm Ontology Bookmark Index]] · Top-level

## Why this is distinct
- Every assessment sees a vanishingly small part of what contributes to and follows from a state. It can't know whether it has captured the relevant harm. Magnitude is not a safe test for inclusion, because small factors at critical points can produce vast effects. And time's direction makes the model **asymmetric**: causes converge into a settled past, while effects ramify into an open future.

## Anticipated direction
- **Limit concepts (never instantiated):** the full causal past and the full causal future. There's no `Ramification` class.
- **Bounded selections:** `Attribution` (the factors counted as "the cause") and `Outcome` (a cut across the ramification at a horizon).
- **Scope:** `declaredScope`, `acknowledgedExclusions`, and `scopeAdequacy` (default Unknown, never Complete).
- **Inclusion:** the Perspective's `inclusionCriteria` (magnitude *and* leverage) and `aggregationRule`.
- **Criticality** (as assessed, model-relative): `sensitivity`/`leverage`, `criticality`, `predictabilityHorizon`.
- **Provisional verdicts** on still-unfolding effects. Finality comes only from institutional closure.

## Conceptual territory
- New. It draws on chaos theory (Lorenz, the "butterfly effect"), critical points and tipping points in complex systems, sensitivity analysis (statistics and control systems), leverage points (Meadows), and the arrow of time. All of these are from memory and unverified.

## Summary
- The past and the future are both unbounded, so the difference between them isn't size but **modality**: the past is fixed and can be traced through evidence; the future is open, branching and unfinished. So the model gives up its wish for symmetry. It models bounded selections on both sides, enforces humility about scope, and judges inclusion by leverage as well as magnitude. Sensitivity itself is an attack vector: adversarial perturbations at critical points, and low-and-slow harms kept under the assessment's threshold.

## Original wording
> "in some sense, every point in time has a state which potentially influences every downstream state. the effects that we are assessing are a very vanishingly small subset of the \"events\" (things, circumstance, processes - everything) that contribute to a state snapshot.  it seems that somehow our assessments must also have some natural implicit and explicit scope because we are not (and cannot) pay attention to everything.  and even more critical, we cannot know that the scope of our assessment even assesses the relevant elements of harm."
- **Attribution:** Author

> "magnitude of harm seems obvious but insufficient for inclusion.  small but pivitol harms may generate huge but unforseen downstream effects.  Think of the 'butterfly effect\" popularized in complex systems research."
- **Attribution:** Author

> "This sensitivity (sensitivity analysis is something routinely performed in statistics and control system design) might also be an intentional target or vector of cyberatack"
- **Attribution:** Author

> "it may be inherently true that the structure of reality, because of the irreversability of time makes our aesthetic desire for a symmetrical structure impossible. an assembly of causes produce an infinitely rammifying chain of events  - very much not a mirror image"
- **Attribution:** Author

> "The model enforces humility: no assessment may claim it captured all relevant harm."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references (from memory, unverified):** Edward Lorenz (the butterfly effect); Donella Meadows, "Leverage Points"; sensitivity analysis; adversarial examples in machine learning.

## Real-world examples
- Adversarial examples: an invisible pixel change flips a classifier's output.
- An impact assessment reporting "no harm found", which is a claim of completeness the model forbids.

## Why it matters to the book
- It gives a principled answer to "how could anyone have known?": often no one could, and the ontology says so in advance. It also shows a quieter danger: harms designed to stay small, scattered and below every threshold until they tip.

## Open questions
- How is `criticality` assessed without a full model of the system?
- Does `predictabilityHorizon` belong to the Perspective or to the system being assessed?
- How does a provisional verdict become final outside law?

## Related
- [[HO-003 Causal Assembly - the Perfect Storm]]
- [[HO-II.b Assessment Horizon - the Sai Weng Trap]]
- [[HO-II.e Missingness Statuses and Domain Profiles]]
- [[HO-002 Ontology Stress-Test Suite]] (T22–T27)
