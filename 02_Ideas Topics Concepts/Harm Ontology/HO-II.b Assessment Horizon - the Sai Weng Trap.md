---
fileClass: Idea
type: idea
status: developing
bookmark: HO-II.b
canonical_id: ho-assessment-horizon-sai-weng
territory: new
tags: [ontology/harm]
aliases: [HO-II.b, Assessment Horizon, Sai Weng Trap, 塞翁失马]
created: 2026-11-14
filed: 2026-11-14
---

# HO-II.b — Assessment Horizon: the Sai Weng Trap

Index: [[_Harm Ontology Bookmark Index]] · Parent: [[HO-000 Harm as Perspective-Relative Assessment|HO-000]] · Tier HO-II (judging layer)

## Why this is distinct
- The point at which a judge stops following the chain decides the verdict. v1's `hasTemporalTrajectory` described the *shape* of a harm over time, not the *horizon* of a judgment. Nothing in v1 captured this.

## Anticipated direction
- Every Assessment must state assessmentHorizon, assessedAt, chainScope, chainStatus (actual / extrapolated), forAffectedEntity and assessor.
- Possibly `discountRate` / `horizonWeighting`, as in climate economics (Stern vs. Nordhaus; from memory, unverified).
- Long-horizon offsetting counts only if the presence of an agent in the chain is recorded.

## Conceptual territory
- New. It draws on the Daoist parable 塞翁失马 (*Huainanzi*), the economics of discounting, and legal finality (see HO-II.c).

## Summary
- In the parable, the broken leg is a misfortune at step 3 and life-saving at step 4. Nothing about the leg changed; only the horizon did. The trap works in both directions: too short is short-sighted, and too long becomes an excuse ("who knows?"). The parable also hides two things. It concerns luck, not agency. And its scope is one household: the son is saved *because* other families' sons died.

## Original wording
> "there is an ethical trap in almost all framings of harm (i believe) and there is a dependency that i don't know if we have represented it anywhere in the ontology.   Something about the \"horizon' or timescale or length of the existing or extrapollated causal chain."
- **Attribution:** Author

> "The parable shows that **whoever sets the horizon sets the verdict.**"
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references:** 塞翁失马, *Huainanzi*, from a web search (standard mode). The result pages were not opened, and whether the war ending is original is unverified. [Wikipedia: The old man lost his horse](https://Www.Wikipedia.org/wiki/The_old_man_lost_his_horse); [USC Digital Folklore Archives](https://folklore.usc.edu/%E5%A1%9E%E7%BF%81%E5%A4%B1%E9%A9%AC%EF%BC%8C%E7%84%89%E7%9F%A5%E9%9D%9E%E7%A6%8F-sai-weng-lost-his-horse-how-can-i-know-it-is-not-a-blessing/).

## Real-world examples
- "Short-term harms are outweighed by long-term benefits" (the AI industry's horizon move). Longtermism as an extreme horizon.
- Judging a product by its launch metrics (too short).

## Why it matters to the book
- Horizon-setting is a form of power. The model can show who chose the horizon and what fell outside it.

## Open questions
- Can the "who knows?" excuse be blocked formally, for example by requiring that extrapolated links carry a confidence value?

## Related
- [[HO-III.a Divergence and Integration - True but Partial]] (horizon as an axis of divergence)
- [[HO-II.c Judgment as Assessment - Reasoning over Precedent]] (finality closes the horizon)
- [[HO-premise No Intrinsic Harmfulness]]
