---
type: session
status: archived
tags: [ontology/harm, roadmap, assessment]
aliases: [2026-11-22 Harm Ontology Ledger Session]
created: 2026-11-22
session_date: 2026-11-22
participants: [Author, "Claude: Claude Haiku 5.5 (claude-haiku-5-5)"]
source: "Copilot chat, 2026-11-22 (session 'explore assessment structure'; file not yet saved to copilot-conversations)"
workstream: "[[Handoff - Harm Ontology]]"
harvested_through: "end of session, 2026-11-22"
continued_in:
topics: [assessment, HarmAssessment, DisciplinePerspective, enablesAssessment, roadmap, change-ledger, governance]
---

# 2026-11-22 Harm Ontology: Ledger and Assessment Session

## Summary
- Explored the assessment structure in the v3 draft and proposed `DisciplinePerspective` as an enabler of `HarmAssessment`, with functional subclasses (regulatory, forensic, diagnostic, normative critique). The relation was renamed to `enablesAssessment` at the author's suggestion.
- Agreed that the migration plan is about content, and that schema and feature decisions need a separate document. Created the **Harm Ontology v3.1 — Feature Roadmap and Change Ledger** as that document.
- Set the ledger's conventions: types (Proposal, Decision, Open Issue, Task, Defect), statuses (Seed, Draft, Under Stress-Test, Settled, Complete, Rejected), dates proposed and settled/rejected, newest first, and a source and rationale for every item.
- Collected about 110 open items across the vault, grouped by topic, each with source, rationale and blockers. Full list in the ledger.
- Author confirmed the layout, and the ledger was written.

## Decisions made
- The v3.1 ledger is named "Harm Ontology v3.1 — Feature Roadmap and Change Ledger", and is copied to v3.2 or v4.0 when v3.1 is complete. → [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] (2026-11-22)
- Ledger ordering is newest first. Complete and Rejected items stay at the bottom and are never deleted. (2026-11-22)
- "Settled" means tested or not needing testing, and ready for implementation in its target version. "Complete" means implemented and logged. (2026-11-22)
- A decision is a kind of proposal that needs resolution. (2026-11-22)
- Dates are "date settled / rejected", not "implemented / rejected". (2026-11-22)
- Nothing from this session is logged in [[Decisions_Log]]. CP-01 is a draft proposal. (2026-11-22)

## How the thinking moved
- Started with `HarmAssessment` taking a `hasDisciplinePerspective` relation. The author added that DisciplinePerspective *enables* assessments, which led to `enablesAssessment`. Claude then drew the diagram, which the author accepted.
- Asked whether the ledger should be a separate note from change tracking. Claude proposed keeping the ledger forward-looking, with settled and completed decisions in [[Decisions_Log]]. The author preferred to keep "Complete" items in the ledger, at the bottom, for a visible record.
- Claude first described the ledger as a "staging ground" but did not give it the fields the author asked for (type, dates, blockers). The author corrected this and asked for them.
- Claude first left rationale and sources out of the ledger. The author pointed out that this removed the reason each item was proposed. Rationale, source, and blocks and blocked-by fields were then added to every item.
- The author wanted the item list to be exhaustive. Claude's first pass covered about 19 items from notes already read; a second, wider search found about 110.
- Dependencies marked "(inferred)" are Claude's reading of the notes, not something a note states. They need checking.

## Concepts introduced
- **DisciplinePerspective**: a PerspectiveType that is institutionalised as a field of practice (law, public health, economics). Enables assessments. → promote to idea note? (y)
- **enablesAssessment**: object property, DisciplinePerspective (or PerspectiveType) → HarmAssessment. A perspective generates and licenses many assessments without being a tag on them. → promote to idea note? (y)
- **Functional subclasses of HarmAssessment**: RegulatoryAssessment, ForensicAssessment, DiagnosticAssessment, NormativeCritiqueAssessment. Classed by intended purpose or use, not by discipline. → promote to idea note? (y, with HO-II.a.1 bookmark, proposed)
- **Feature ledger (governance)**: a forward-looking roadmap for schema changes, separate from content migration and from [[Decisions_Log]]. → promote to idea note? (n; governance practice, record in Handoff)
- **Placement test**: does a proposed element describe a tradition (PerspectiveType), an act of assessment (HarmAssessment), the thing assessed, or an output (verdict, remedy, closure)? Already recorded as proposed in the 2026-11-21 session. → no new note.

## Bookmarks proposed (not added to [[_Harm Ontology Bookmark Index]]; needs author approval)
- **HO-II.a.1 — Harm assessment: function and purpose.** Covers `HarmAssessment`, `enablesAssessment`, and the functional subclasses. Proposed under HO-II.a. Source: this session, ledger item S1.
- **HO-II.d.4 — Searchlight and gap schema.** Already proposed in the 2026-11-21 session. Ledger items S26–S29.
- **HO-007 — Agents, participation and assessing organisations.** Already proposed 2026-11-19. Ledger items S2, S3, K3, T10.
- **HO-II.d.3 — Hub and spoke pattern.** Already proposed 2026-11-20. Ledger items V1–V12.

## Open questions
- Is a discipline's perspective the same kind of thing as a tradition's? Working answer is yes. Ledger S21 is the blocker for CP-01.
- Are the functional subclasses of HarmAssessment mutually exclusive, or can one assessment be both forensic and regulatory?
- How do functional subclasses interact with the Valence / Responsibility / Causal split (K1)?
- Should the functional subclasses be a class hierarchy, or a controlled vocabulary of purpose values on one class?
- Does Protégé show multi-level assessment subclasses without clutter?
- Which two open items should be tested first, the non-expert test (A2) or the Horizon test (A5)? Both block A1.
- Do the Physics and Integral coverage test and the overlap test (S24, S25) need to run before any schema logging? The skeleton says yes.

## Original wording
> "i am thinking that we need a more focused update path/plan for features, schema additions, rationale and status notes like seed idea drraft proposal and settled"
- **Attribution:** Author

> "I think we need more than a ledger. need to track at least status, priority, target version for implementation, rationale and any blockers, issues and problems to be resolved - before implementation."
- **Attribution:** Author

> "i believe that the ledger should be in reverse chronological order. newest at top oldest at bottom"
- **Attribution:** Author

> "i am thinking that a decision is really a type of proposal - a proposed item that needs resolution"
- **Attribution:** Author

> "you seem to have lost the rationale somewhere along the way. if this is to be meaningful we need to retain why we proposed it in the first place."
- **Attribution:** Author

> "perhaps enablesAssessment should be used because a perspective may be an enabler of many things"
- **Attribution:** Author

## External references
| Reference | Used for | Status (verified / from memory / unverified) |
|---|---|---|
| None | | |

## Artifacts touched
- Read: [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)]], [[Harm Ontology Migration Plan]], [[_Harm Ontology Bookmark Index]], [[HO-II.a Assessment and Evaluative Standard]], [[Harm Ontology v3.1 - Skeleton Schema (proposed)]], [[Handoff - Harm Ontology]], [[Decisions_Log]], [[Canon_and_Continuity]], and the HO notes and council reviews listed in the ledger sources.
- Created: [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]] (ledger, full version with rationale, sources and blockers).
- Created: this session note.
- Edited: [[Handoff - Harm Ontology]] (current focus added).

## Follow-ups
- [ ] Author: confirm the proposed bookmarks (HO-II.a.1, HO-II.d.4, HO-007, HO-II.d.3) before adding them to the index.
- [ ] Author: answer the open questions above, starting with whether a discipline's perspective is a PerspectiveType (S21).
- [ ] Check the inferred dependencies in the ledger.
- [ ] Verify the source anchors marked as note-level links in the ledger.
- [ ] Decide whether CP-01 moves from Draft to Under Stress-Test.
- [ ] Run S24 and S25 (coverage and overlap tests) when the author gives the go-ahead.
- [ ] Run A2 and A5 (non-expert and Horizon tests) to settle A1.
- [ ] Locate or recreate the missing methodology note referenced in the 2026-11-20 session (T5).

## Closing checklist
A session = one Copilot chat, from its first message to this checklist. Pauses don't end it.
- [x] Harvest new ideas (incremental, from `harvested_through`)
- [x] Update `harvested_through`
- [x] Add anything after the last update to this note
- [x] Rewrite the workstream's Handoff note (forward-facing, short)
- [x] Set `status: archived`; later set `continued_in`
- [ ] Rename the chat in Copilot history: "[CLOSED] Harm Ontology ledger and assessment → see session note" (author action)
- [x] Start a new chat with the Handoff note attached. Don't reopen this one; read its transcript selectively if needed.

## Related
- [[Handoff - Harm Ontology]]
- [[Harm Ontology v3.1 — Feature Roadmap and Change Ledger]]
- [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)]]
- [[2026-11-21 Harm Ontology Searchlight and Gap Session]]
- [[2026-11-20 Harm Ontology Sample Review and Methodology]]
