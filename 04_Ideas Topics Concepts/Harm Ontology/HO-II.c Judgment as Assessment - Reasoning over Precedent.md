---
fileClass: Idea
type: idea
status: seed
bookmark: HO-II.c
canonical_id: ho-judgment-as-assessment-precedent
territory: new
tags: [ontology/harm, law]
aliases: [HO-II.c, Judgment as Assessment, Precedent Reasoning]
created: 2026-11-14
filed: 2026-11-14
---

# HO-II.c — Judgment as Assessment: Reasoning over Precedent

Index: [[_Harm Ontology Bookmark Index]] · Parent: [[HO-000 Harm as Perspective-Relative Assessment|HO-000]] · Tier HO-II (judging layer)

## Why this is distinct
- A court judgment is a **subclass** of Assessment. It shares the core properties and adds authority, jurisdiction, binding force, procedure, ratio, precedent links (cites / distinguishes / overrules), remedy and finality. That could make bodies of precedent queryable with the same model used for moral and regulatory judgments.

## Anticipated direction
- Encode standing cases as Assessments to see which standard and horizon the courts actually apply, and where they are inconsistent.
- Link legal standards to the philosophical standard each most resembles.
- Possible reuse of LKIF-Core, Akoma Ntoso, LegalRuleML and ECLI (from memory, unverified).

## Conceptual territory
- New ground for this vault. There's precedent in AI-and-law work: Ashley's HYPO/CATO model cases as sets of factors (from memory, unverified).

## Summary
- Finality is law's institutional answer to the horizon problem: courts must extrapolate and then commit. Limits: legal reasoning works by analogy, the ratio is itself contested, and jurisdictions conflict. So the model supports retrieval and consistency checks, not mechanical decisions. A thematic warning for the book: an AlgorithmicAssessment is one subclass away from a Judgment, and can copy the core properties while lacking authority, procedure, reasons and accountability.

## Original wording
> "Would an assessment in the sense you propose be identical and interchangeable with the udgement pronounced by a human (or AI) judge? or supream court justice?
>
> this would be a wonderful fortuitous and significant overlap with the domain of law and regulation if it is and would make an entire body of precident directly inferable and (reason-able)"
- **Attribution:** Author

> "Law **deliberately closes the horizon**."
- **Attribution:** Claude: Opus 5.5 (claude-opus-5-5)

- **Source:** Obsidian Copilot agent session "philosopher adverse stress test harm ontology", 2026-11-14; [[2026-11-14 Harm Ontology Redesign]].
- **External references (all from memory, unverified):** *Clapper v. Amnesty International* (2013), on "certainly impending" harm; *Spokeo v. Robins* (2016), on "concrete" injury; *TransUnion v. Ramirez* (2021), on whether risk alone supports damages; Ashley, HYPO/CATO.

## Real-world examples
- US standing doctrine as a long-running argument about horizon, modality and concreteness.

## Why it matters to the book
- Most AI harms are risk-based, statistical or unfelt, which is exactly where standing law tends not to recognise injury.

## Open questions
- Who encodes the ratio? (That is itself a MoralAssessment about a Judgment.)
- Test case: *TransUnion*.

## Related
- [[HO-II.a Assessment and Evaluative Standard]]
- [[HO-II.b Assessment Horizon - the Sai Weng Trap]]
- [[002 Scalability of Oversight and Control]] (rubber-stamped algorithmic judgments)
