---
type: session
status: developing
tags: [handoff, ontology/harm]
aliases: [Perspective Vocabulary Handoff, Handoff - PerspectiveStructure 0.03]
created: 2026-11-17
updated: 2026-11-17
workstream: Harm Ontology / Perspective (HO-II.d)
parent_handoff: "[[Handoff - Harm Ontology]]"
previous_handoff: "[[Handoff - PerspectiveStructure 0.02]]"
---

# Handoff — Perspective Vocabulary and v3 Follow-ups

*Task-scoped handoff. Attach this note to start a new chat. It picks up after [[PerspectiveStructure 0.02]] was written and filed. The wider ontology work is in [[Handoff - Harm Ontology]].*

## Where things stand (2026-11-17)
- [[PerspectiveStructure 0.02]] (HO-II.d.3) is written and filed: minimal core, 12 display groups, 2 profiles, placed in v3.
- [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]] (HO-II.d.2) holds three worked hubs: `congruence`, `omission` and `developmentalAltitude`.
- [[Integral Altitude Scale]] (HO-II.d.2.a) holds Wilber's scale as value records, with verification noted per level.
- [[Harm Ontology v3 - Draft Structure]] is updated with the decisions below (see its revision callout). No v3 `.ttl` exists yet.

## Decisions made this session (all in [[Decisions_Log]], 2026-11-17)
- **Three layers:** ontology (`ho:`), profiles (`hosh:`), vocabulary (`hov:` hubs plus discipline schemes).
- **Vocabulary rules:** simple hub names; discipline terms kept in the narrative; real disciplines, not councils, as domains; graded mappings (exact / close / narrow / broad / related), proposed by Claude and reviewed by the author.
- **Perspective** is an abstract umbrella over two disjoint subclasses: **PerspectiveType** ("tradition", altLabel "lens") and **PerspectiveSpecification** ("perspective specification", altLabels "viewpoint", "perspective snapshot"). "Shot" is retired.
- **Standards:** `defaultEvaluativeStandard` (tradition) and `appliedEvaluativeStandard` (specification), inherited when absent.
- **Terminology:** discipline; `fieldOfApplication` (was `domainOfApplicability`); "profiles" (was "domain profiles"); "domain" only in its OWL sense. Glossary in `Canon_and_Continuity.md`.
- **Causes:** v3 `Attribution` merged into `CausalAssessment` (`attributedCause`, `leftOut` → `CausalCandidate`); `CausalAssembly` renamed `FactorAssembly`, a thin container whose members, sufficiency and origin are assessed.
- **Omission hub:** three branches: out of frame, blind spot (visible but missed: negligent or suppressed), accepted harm.
- **Integral position** confirmed as group 3 of 0.02.

## Next tasks (suggested order)
1. **More concept hubs** for ★ attributes, in the crosswalk format: interiority and collectivity (with `int:` spokes from AQAL), accountability locus, consent to be seen.
2. **Verify Wilber** against *The Religion of Tomorrow* (2017): the twelve-colour sequence, the teal/turquoise names, magic-mythic red as a separate stage, and the 3rd tier. Needs the book (author's copy or a library).
3. **Verify Gilligan's own wording** of her stages (*In a Different Voice*, 1982); the crosswalk currently uses Wilber's rendering.
4. **"Domain" renames:** decide on `nameByDomain` / `definitionByDomain` → `…ByDiscipline`, and whether to rename [[HO-II.e Missingness Statuses and Domain Profiles]] (a rename breaks links; ask first).

## Open questions (undecided)
- Can a PerspectiveSpecification instantiate more than one tradition (mixed lenses)?
- Statement-level provenance (RDF-star or named graphs)?
- Attribute-space or embedding model for comparing traditions?
- Record the ontology as an instance of its own PerspectiveType?
- Split Assessment further into Valence and Responsibility (HO-005)?
- New Divergence subtypes for [[HO-III.a Divergence and Integration - True but Partial|HO-III.a]]: verdict convergence with rationale divergence; perspectival vs factual by transformation test; divergence between value scales.
- Is the Integral 3rd tier kosmocentric, or beyond the band scheme?

## Rules carried forward
- Vocabulary records use the eight-column format plus Citation verified; Explanations 100–200 words; graded mapping with a one-line reason; `meaningAsOf` and `assertedBy`.
- Citations are web-verified; person-name searches use extended mode; prefer primary texts and say when only secondary sources were used.
- New notes use the Idea template, with verbatim Original wording, each quote attributed separately, and are filed with the bookmark-index-maintainer skill.
- The author values reflection over quick agreement: offer options with a recommendation, and flag weak ideas.

## Cautions
- The seven council reviews were all voiced by one model, so their convergence is weaker evidence than it looks.
- Wilber's population percentages are his own estimates; don't cite them in the book without primary research.
- AI examples in the crosswalk and altitude notes are Claude's illustrations, not drawn from the cited authors.

## Source session
- Obsidian Copilot agent session "Read Handoff - PerspectiveStructure 0.02 and the notes it lists", 2026-11-17 (`copilot/copilot-conversations/agent__Read_Handoff_-_PerspectiveStructure_0.02_and_the_notes_it_lists,@20261117_170442.md`).
