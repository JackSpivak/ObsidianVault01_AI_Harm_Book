---
fileClass: Idea
type: idea
status: developing
bookmark: HO-II.d
canonical_id: ho-perspective-ten-properties
territory: new
tags: [ontology/harm]
aliases: [HO-II.d, Perspective, Photographic Perspective]
created: 2026-11-14
filed: 2026-11-14
---

# HO-II.d — Perspective: Ten Optional Properties

Index: [[_Harm Ontology Bookmark Index]] · Parent: [[HO-000 Harm as Perspective-Relative Assessment|HO-000]] · Tier HO-II (judging layer)

> [!note] Revision 2026-11-17
> The class described here is now **PerspectiveSpecification** (altLabels "viewpoint", "perspective snapshot"), one of two disjoint subclasses of an abstract **Perspective** umbrella; the other is **PerspectiveType** ("tradition", [[PerspectiveStructure 0.02]]). A specification `instantiates` a tradition and inherits its defaults. The property `standard` is now `appliedEvaluativeStandard`, inherited from the tradition's `defaultEvaluativeStandard` when absent. See [[Decisions_Log]] 2026-11-17.

## Why this is distinct
- A **Perspective** is a reusable class (`Assessment —takenFrom→ Perspective`), modelled on taking a photograph. It makes visible every setting that can change a verdict on its own.

## Anticipated direction
- **Position:** standpoint, direction
- **Time:** timestamp (assessedAt), exposure (horizon)
- **Optics:** framing (scope), resolution (granularity), sensitivity (threshold)
- **Purpose:** domain of intent, standard, fitness (how well the standard suits the intent)
- **Operator:** assessor (who holds the camera, as distinct from whose standpoint is taken)
- All properties are optional (see HO-II.e). Perspectives can be compared to find the property where two views differ.

## Conceptual territory
- New. It extends the three-part "standard / standpoint / horizon" split from the same session.

## Summary
- The author proposed six elements: standpoint, direction, timestamp, utility, domain of intent, standard. Claude added exposure, framing, resolution, sensitivity and operator. "Utility" became **fitness**, to avoid confusion with utilitarianism. Fitness flags a valid standard used for a question it can't answer, for example a population-welfare standard applied to an individual-rights question. Test for keeping a property: it must be able to flip a verdict on its own.

## Original wording
> "you made an interesting point about the three elements of a perspective.  i suggest there should be more. if you think of a perspective literally - as in photography - each perspective has:
> standpoint - where you/camera is actually standing
> direction - where you/camera is actually pointing
> timestamp - temporal point at which you take the picture
> utility - perhaps the applicability of the standard you mention for the perspective with respect to a domain of intent
> domain of intent  - what is the perspective intended to reveal
> standard - what counts ad a revelation"
- **Attribution:** Author

> "Your timestamp is *when the shutter fires*. Exposure is *how much time the image captures*."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references:** none.

## Real-world examples
- Sai Weng: change only the framing (one household → the whole village), and the broken leg goes from blessing to evidence of a war that killed other families' sons.

## Why it matters to the book
- A "perspective" in a harm dispute can be taken apart setting by setting. That is often the most revealing question: on exactly which setting do the regulator's view and the victim's view differ?

## Open questions
- Does fitness belong to the Perspective or to the standard–intent pairing?

## Related
- [[HO-II.e Missingness Statuses and Domain Profiles]]
- [[HO-III.a Divergence and Integration - True but Partial]]
