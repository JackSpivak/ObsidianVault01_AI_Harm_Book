---
fileClass: Idea
type: idea
status: seed
bookmark: HO-006
canonical_id: ho-006-causal-chain-assessed-selection
territory: new
tags: [ontology/harm, ontology/v4-proposed]
aliases: [Causal Chain, CausalChain, Chain class, HO-006 Causal Chain, Horizon-bounded chain]
created: 2026-11-18
---

# Causal Chain: an Assessed Selection with a Horizon

> [!warning] v4 proposed feature. Not decided, not tested.
> Nothing here is in the v3 structure ([[Harm Ontology v3 - Draft Structure]]) or logged in [[Decisions_Log]]. It is recorded so the idea survives the session. First test: one chain assessed at two horizons in the toy case (see Anticipated direction).

## Why this is distinct
- v3 has `CausalRole` ("the part a factor plays in **one chain**") and Assessment properties `chainScope` and `chainStatus`, but **no class for the chain itself**. "Chain" is used in the notes as if it were an object, and nothing can be pointed at.
- This idea proposes a thin, assessed **Chain** whose extent is bounded by a **horizon**, so that chain-level claims (net effect, where it stops, which chain two perspectives mean) can be stated, compared and disputed without claiming completeness.

## Anticipated direction
- **A thin Chain container**, like `FactorAssembly` (decided 2026-11-17, [[HO-003 Causal Assembly - the Perfect Storm]]): identifier and label only. Supplied by assessments, not asserted: members (the Factor and Effect links followed), endpoints, and `stoppedAt` (where the assessor stopped following).
- **`CausalRole` gets something to point at:** `withinChain → Chain` (the way it has `withinAssembly (?)` now). A factor can then play different roles in different chains ([[HO-I.a Factor and CausalRole]]) and the model can say which.
- **Horizon bounds the chain.** Any assessment of the collective outcome of a chain is made with respect to a specific horizon; a finite `maxHorizon` can pin it at a finite time scale, so no limit concept is needed.
- **Horizon is part of the claim key.** The same-claim test (target + attribute + scope; [[HO-002.a Assessment-Everywhere Test Strategy]] decisions 11–12) must include horizon, otherwise "net beneficial at 2 years" and "net harmful at 20 years" show as a false **Disputed** (the same kind of false dispute as toy finding 1). It also keeps the Sai Weng effect visible ([[HO-II.b Assessment Horizon - the Sai Weng Trap]]).
- **First test (toy case):** one chain assessed at two horizons. Pass if the two horizons are separate claims with their own statuses, and a same-horizon conflict still shows as Disputed.

## Conceptual territory
- **New ground:** a chain as an object. Revisits, from a new angle, three things already in the model:
  - `Outcome` ("a cut across the ramification at a horizon"): a Chain would be the equivalent selection of a *path*, chosen by a perspective, not a thing in the world.
  - The horizon properties (`exposure (horizon)` on PerspectiveSpecification; `assessmentHorizon` and `chainScope` / `chainStatus` on Assessment, [[HO-II.a Assessment and Evaluative Standard|HO-II.a]], HO-II.b).
  - The asymmetry of time and "scope is never complete" ([[HO-004 Criticality, Leverage and the Limits of Scope]]).
- **How it relates to the limit concept:** the full causal past and future stay unreachable limit concepts. A finite horizon means *declared and bounded*, not *complete*; `scopeAdequacy` can still never be Complete.
- **Possible names:** `CausalChain` or `CausalPath` (a path is selected; "chain" implies completeness).

## Summary
- **The gap:** the draft structure has no Chain class. A "chain" is only the graph formed by `Factor causes → Factor | Effect` and `Effect leadsTo → Effect`, so "one chain" is really one Factor–Effect pair or an implied path. Chain-level questions can't be asked directly: which chain did an assessment cover, do two perspectives mean the same chain, where does it stop, what is the net result across it ([[HO-I.b Effect and Cascades]] lists the last as open).
- **Why it might be deliberate:** effects ramify into an open future; a complete chain is a limit concept and is never instantiated, so a Chain class risks implying completeness. The horizon idea answers this.
- **The author's point:** any assessment of the collective outcome of a chain can be made with respect to a specific horizon, and a `maxHorizon` pins it at a finite time scale.
- **Claude's caveats (proposals, not decisions):**
  1. **Reuse horizon, don't add a third.** It already exists as `exposure` on the perspective and `assessmentHorizon` on the assessment. A perspective may assess the same chain at several horizons, so the horizon belongs on the assessment, not only on the perspective.
  2. **Separate the assessor's horizon from a ceiling.** The assessor's horizon is how far this judgment looked. `maxHorizon` is the longest horizon a standard, procedure or query will entertain (foreseeability, a limitation period). It would sit on a `Procedure` or `EvaluativeStandard`, and an assessment's horizon must not exceed it.
  3. **Horizon in the claim key** (see above).
  4. **Open sub-questions:** what the horizon is measured from (the factor, the effect, or `assessedAt`); a horizon past today forces `chainStatus: Extrapolated`; whether the horizon cuts the chain at a time, a number of links, or a probability level.
- **Not yet checked:** only the HO notes were searched for "chain". The other notes, the v1 `.ttl` and the council reviews were not, so a Chain concept may already exist elsewhere.

## Original wording
> "i notice thatt we currently have CausalRole which characterizes the role a factor might play in a chain. but i amnot aware that we have a thing(classs) representing a chain how can this be"
- **Attribution:** Author
- **Source:** Obsidian Copilot agent session "what are open issues", 2026-11-18 (`copilot/copilot-conversations/agent__what_are_open_issues@20261118_114926.md`).

> "first, any assessment of the collective outcome of a chain could be assessed with respect to a specific horizon. and we don't have to go to a limit, some maxHorizon could pin it at some finite timescale"
- **Attribution:** Author
- **Source:** same session

> "lets capture all these thoughts about what to do about chains in an idea note and bookmark it appropriately as a v4 proposed feature"
- **Attribution:** Author
- **Source:** same session

- **External references:** [[HO-I.a Factor and CausalRole]]; [[HO-I.b Effect and Cascades]]; [[HO-II.b Assessment Horizon - the Sai Weng Trap]]; [[HO-003 Causal Assembly - the Perfect Storm]]; [[HO-004 Criticality, Leverage and the Limits of Scope]]; [[HO-002.a Assessment-Everywhere Test Strategy]]; [[Harm Ontology v3 - Draft Structure]].

## Real-world examples
- Not yet gathered. Natural candidates: [[HO-II.b Assessment Horizon - the Sai Weng Trap]] (verdict flips with the horizon) and the Horizon (R01) slice in [[HO-002 Ontology Stress-Test Suite]] (a chain assessed at different horizons by different perspectives). Both unverified until sourced.

## Why it matters to the book
- The book is about harms that go unseen. Whoever picks where to stop following a chain picks the verdict; making the stopping point a visible, declared value, rather than an implicit choice, is the same move the ontology makes for scope and omission.

## Open questions
- Is a Chain a class at all, or only a view over the existing links? (Author's observation: v3 uses the word without an object.)
- What is the horizon measured from, and does it cut by time, link count or probability?
- Where does `maxHorizon` live (Procedure, EvaluativeStandard, query) and who may override it?
- Is a chain-level net assessment ever legitimate, or only per-link ones ([[HO-I.b Effect and Cascades]] leans to both, labelled with scope)?
- Does the status calculation need a change, beyond adding horizon to the claim key?
- Does a Chain overlap `FactorAssembly` (convergent causes) enough to share a parent class, e.g. under `CausalCandidate`?

## Related
- [[HO-I.a Factor and CausalRole]] (also under)
- [[HO-I.b Effect and Cascades]]
- [[HO-II.b Assessment Horizon - the Sai Weng Trap]]
- [[HO-003 Causal Assembly - the Perfect Storm]]
- [[HO-004 Criticality, Leverage and the Limits of Scope]]
- [[HO-005 Assessed Membership and Systematic Omission]]
- [[HO-002.a Assessment-Everywhere Test Strategy]]
- [[Harm Ontology v3 - Draft Structure]]
