---
type: session
status: developing
tags: [handoff, ontology/harm]
aliases: [PerspectiveStructure Handoff, Handoff - Perspective Consolidation]
created: 2026-11-17
updated: 2026-11-17
workstream: Harm Ontology / PerspectiveType (HO-II.d.1)
parent_handoff: "[[Handoff - Harm Ontology]]"
---

# Handoff — PerspectiveStructure 0.02

*Task-scoped handoff. Attach this note to start a new chat for consolidating the seven council reviews into PerspectiveStructure 0.02. Archive it once 0.02 exists. The wider ontology work is in [[Handoff - Harm Ontology]].*

## Task
- Consolidate [[PerspectiveStructure 0.01]] and its seven council reviews into **PerspectiveStructure 0.02**.
- **Propose the pruned structure first** (as an outline or table), then wait for the author's approval before writing the note.

## Status
- 0.01 is frozen. All seven reviews are saved and bookmarked (HO-II.d.1.a–g).
- The citations in every review's vocabulary table were web-verified on 2026-11-17 in two passes. No row is "Not verified". Remaining gaps are mostly exact line, section or edition details, and each is noted in its row.
- The reviews propose 120+ attributes in total. None of them is decided yet.

## Read first (in full)
1. This note.
2. [[PerspectiveStructure 0.01]]: the base structure (eight groups, with [O]/[A]/[D] marking), plus the author's original list.
3. The seven reviews, in order:
   - [[v-0.01 ClassicalCouncil Review of - PerspectiveStructure 0.01]]
   - [[v-0.01 EthicsCouncil Review of - PerspectiveStructure 0.01]]
   - [[v-0.01 LegalCouncil Review of - PerspectiveStructure 0.01]]
   - [[v-0.01 LogicCouncil Review of - PerspectiveStructure 0.01]]
   - [[v-0.01 PhysicsCouncil Review of - PerspectiveStructure 0.01]]
   - [[v-0.01 SciFiCouncil Review of - PerspectiveStructure 0.01]] (physics-bounded)
   - [[v-0.01 CognitiveCouncil Review of - PerspectiveStructure 0.01]]
   - For a first pass, the Summary, sections 1–3 and the Moderator's summary of each review are enough. Open the vocabulary tables only when a specific attribute needs them.
4. Context: [[HO-II.d Perspective - Ten Optional Properties]], [[HO-III.a Divergence and Integration - True but Partial]], [[HO-II.e Missingness Statuses and Domain Profiles]], [[_Harm Ontology Bookmark Index]].

## Rules the author set in the earlier chat (carry forward)
- **Vocabulary tables** use eight columns: Attribute · Term (altLabels) · Definition · Example · Citation · Historical note · Key thinkers · Explanation. The **Explanation** is 100–200 words ("do not economize"). Since verification there is also a **Citation verified** column, placed directly after Citation.
- **Citations** are web-verified. All web searches are pre-approved. Person-name searches use extended mode.
- **When a table is reworked**, remove the old table and replace it with the enriched one; don't keep both.
- **New notes** use the Idea template, `fileClass: Idea`, with Summary and verbatim Original wording, each quote attributed separately. They are filed with the bookmark-index-maintainer skill. Council reviews are named `v-0.01 <Council>Council Review of - PerspectiveStructure 0.01`.
- **Sci-Fi Council scope rule:** only currently accepted physics; no premises beyond it.

## Consolidation method (from the reviews)
- **Minimal core** (Descartes): a lens is recorded only if it has a name, a canonical source, an object of attention and its foundational commitments. Everything else is optional and uses missingness statuses (HO-II.e).
- **Pragmatic test** (Peirce): keep an attribute only if some query, decision or Divergence changes when its value changes. This is the same as HO-II.d's keep-test.
- **Rank by impact** (Fermi): put the leading attributes in the core tier.
- **Description vs evaluation** (Hart): evaluative attributes, such as misnaming, blind-spot type and failures, are Assessments with `assessedBy`, not plain facts.
- **Date-stamp meanings** (Scalia): `meaningAsOf`, and `validFrom` / `validTo`.

## Strongest convergences across councils
- **Stated vs operative congruence**, with five witnesses: Confucius (misnaming), Kant (maxim), Fuller (congruence), Arendt (*Sprachregelung*), Feynman (cargo cult). This is the strongest candidate for a first-class attribute.
- **Relations before attributes:** Laozi, Gilligan, Einstein (attribute space and invariants), Edelman (re-entry).
- **Four kinds of blind spot:** constitutive (Laozi), negligent, accepted (Le Guin), suppressed (Minsky).
- **Whose ranking:** altitude scales encode their authors' views (Confucius and Laozi; the Kohlberg–Gilligan dispute). Record `assessedBy`.
- **Three scope axes:** social size, developmental altitude and moral circle (Singer). `legalPersonhood` is the legal twin of moral circle.
- **Type/instance with defaults** is confirmed by Minsky's frames.
- **AI models are lenses** (Hinton): they should be recordable with training provenance and an objective function.

## Proposed new groups (to accept, merge or reject)
- **Stance:** bearerRole, controlLocus, effectOnHolder, practitionerCompetence, stanceTowardObject, cognitiveAlteration.
- **Normative core:** normativeForm, valueTheory, embedsStandard, distributiveConcern, impartiality, intentWeighting, conflictResolution.
- **Institutional:** validity/efficacy, recognition, acceptance, enforcementReality, standing, remedy, precedentialWeight, proceduralIntegrity.
- **Subject's side:** livedExperience, legibility, adaptiveResponse, interfaceAbstraction, modelOfSubject.
- **Power facet:** authority, whoseInterests, costBearer, whoseVoice, consentToBeSeen, powerAsymmetry.
- **Infrastructure facet:** infrastructureDependence, trainingProvenance.
- **Dynamics:** performativity, resonance, feedback, predictionErrorHandling.

## Open decisions for the author
- Adopt the PerspectiveType / Perspective (type/instance) split? Every review assumes it, but it hasn't been logged.
- Provenance at the level of each statement (RDF-star or named graphs)?
- Hybrid model: OWL for the structure, SKOS with exemplars for contested concepts like "harm" (Wittgenstein, Dworkin)?
- An attribute-space or embedding model for comparing lenses, with Divergence as distance and invariants as agreement?
- Record the ontology as an instance of its own PerspectiveType (Socrates, Hofstadter)?
- Add new Divergence subtypes to HO-III.a: verdict convergence with rationale divergence (Edelman), and perspectival vs factual by transformation test (Einstein)?
- Keep `developmentalAltitude`, given that it's contested?

## Decisions to offer for logging
None of these is in [[Decisions_Log]] yet. Offer to log each one once confirmed:
- The PerspectiveType/Perspective split.
- Separating social scope (size) from developmental altitude. The author accepted this in the earlier chat: "I love your distinction between size and developmental scope".
- The vocabulary table format (eight columns plus Citation verified; 100–200-word Explanation).

## Cautions
- **The councils are not independent.** All seven were voiced by one model (Claude Opus 5.5), so their agreement is weaker evidence than it looks (see `selfInstance` in the Cognitive review).
- **Partly verified citations.** Some confirmations rest on search snippets, not opened pages; each row says which.
- **Dialogue quotes are unchecked.** The council dialogue text in each review was not fact-checked; only the vocabulary tables were.
- **Watch for momentum.** The author values reflection over quick agreement. Present options with a recommendation and push back on weak ideas.

## Source session
- Obsidian Copilot agent session "Name this chatWhat is Perspective", 2026-11-17 (`copilot/copilot-conversations/agent__Name_this_chatWhat_is_Perspective@20261117_094622.md`). It is long, so read it selectively and don't reopen the chat.
