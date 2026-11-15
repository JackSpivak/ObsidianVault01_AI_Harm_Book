---
fileClass: Idea
type: idea
status: developing
bookmark: HO-II.a
canonical_id: ho-assessment-evaluative-standard
territory: new
tags: [ontology/harm]
aliases: [HO-II.a, Assessment, Evaluative Standard, Theory of Harm]
created: 2026-11-14
filed: 2026-11-14
---

# HO-II.a — Assessment and Evaluative Standard

Index: [[_Harm Ontology Bookmark Index]] · Parent: [[HO-000 Harm as Perspective-Relative Assessment|HO-000]] · Tier HO-II (judging layer)

## Why this is distinct
- **Assessment** is a class, and each instance is **one judgment**. An **EvaluativeStandard** (formerly "TheoryOfHarm", with that name kept as an alias) is the reusable rulebook the judgment applies. The relation is like a legal code and a court verdict.

## Anticipated direction
- Assessment properties: assesses (Factor / Role / Effect), underStandard, forPatient, assessor, assessedAt, horizon, chainScope, chainStatus (actual / extrapolated), verdict (Harmful / Beneficial / Mixed / Neutral / Contested).
- Standards as individuals: Experiential, Comparative, NonComparative, RightsBased, Capacity, plus legal standards (injury-in-fact, reasonable person, loss of chance…).
- Subclasses: Personal, Moral, Expert, Regulatory, Algorithmic, Judgment (see HO-II.c).

## Conceptual territory
- New. v1 had no judging layer; its classes *were* the judgments.

## Summary
- A theory of harm is a standard for judging whether something is bad *for* someone (value) or wrong *to* someone (the rights-based case). A "perspective" bundles the standard with standpoint and horizon; keeping them separate stops someone changing the horizon while claiming to apply the same theory. "TheoryOfHarm" became too narrow once verdicts could be "Beneficial", hence EvaluativeStandard.

## Original wording
> "so an assessment is a class of things? that has properties?
> how does this relate to what you had originally called an account? which we now call a TheoryOfHarm?
> isn't a theory of harm really a perspective from which harm (and therefore essentially goodness and badness) will be judged?"
- **Attribution:** Author

> "So a precise description: **a theory of harm is a standard for judging whether something is bad for someone, or wrong to someone.**"
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references:** v1 meta-categories (Bentham, Feinberg, Kant, Aristotle/Nussbaum, as cited there); Shiffrin's non-comparative account (from memory, unverified).

## Real-world examples
- The same broken leg receives several Assessment instances (the neighbours, the father, the state), each with a different verdict.

## Why it matters to the book
- It makes "who judged this, by what standard?" a required question.

## Open questions
- Should worldviews (afterlife, ancestor traditions) count as EvaluativeStandards?
- Should the Classical Council's ideas be added as standards (harm to the wrongdoer, manufactured desire)?

## Related
- [[HO-II.d Perspective - Ten Optional Properties]]
- [[HO-II.c Judgment as Assessment - Reasoning over Precedent]]
