---
epoch: 1795191928346
mode: agent
backendId: opencode
sessionId: "ses_e0660ebe3ffeHzMwrWNj54oBoA"
model: '{"baseModelId":"anthropic/claude-haiku-5-5","effort":"low"}'
tags:
  - copilot-conversation
topic: "Harm Ontology v3 changes"
usage: '{"usedTokens":84923,"contextWindow":1000000,"updatedAt":1795193958555}'
---

**user**: have any of our logged discussions or decisions or directions changed structure, elements, naming or anything else in our current understanding of the Harm Ontology we are discussing since last recorded as Harm Ontology v3 draft structure
[Timestamp: 2026/11/20 09:25:28]

**ai**: **Error:** Internal error: This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.
[Timestamp: 2026/11/20 09:25:28]

**user**: please repeat last prompt
[Timestamp: 2026/11/20 09:29:13]

**ai**: Here is your previous prompt, repeated verbatim:

"have any of our logged discussions or decisions or directions changed structure, elements, naming or anything else in our current understanding of the Harm Ontology we are discussing since last recorded as Harm Ontology v3 draft structure"

I can run that search across your vault if you'd like.
[Timestamp: 2026/11/20 09:29:13]

**user**: uyes
[Timestamp: 2026/11/20 09:29:23]

**ai**: Yes. Several decisions made after the v3 draft structure was recorded have changed names and structure, and some proposals are still open. I checked the decision log and the handoffs. I did not re-verify every line of the draft note itself, so check its revision callout before relying on it.

**Changes logged in [[Decisions_Log]] since the draft**

- **2026-11-17, Perspective split.** Perspective is now an abstract umbrella with two disjoint subclasses: PerspectiveType (altLabel "lens") and PerspectiveSpecification (altLabels "viewpoint", "perspective snapshot"). "Shot" is retired. The standard properties are now `defaultEvaluativeStandard` on the type and `appliedEvaluativeStandard` on the specification. This supersedes the earlier split. See [[PerspectiveStructure 0.02]].
- **2026-11-17, causal structure.** Attribution is merged into CausalAssessment, which is now a kind of Assessment. A new parent class, CausalCandidate, has Factor and FactorAssembly as subclasses. CausalAssembly is renamed FactorAssembly and becomes a thin identifier container. Membership, sufficiency, origin and orchestrator are all supplied by assessments.
- **2026-11-17, three layers.** OWL (`ho:`) for structure, SHACL (`hosh:`) for requiredness, and SKOS (`hov:`) for vocabulary.
- **2026-11-18, rename.** "Patient" becomes AffectedEntity. `patientStanding` becomes `affectedStanding`, `forPatient` becomes `forAffectedEntity`, and the standing values become `{agent · affected · datum}`. The rename across other notes and the v1 `.ttl` is deferred to migration.
- **2026-11-18, patient types.** Patient types are inclusive, and standing is assessed per perspective. FutureGeneration, AISystem and Relationship are confirmed as types.
- **2026-11-14 entries superseded.** The Attribution and CausalAssembly names from the 2026-11-14 entries are replaced by the 11-17 changes above.

**Still open, not logged**

- Splitting Assessment into Causal, Valence and Responsibility (HO-005).
- Causal standards such as but-for, NESS and INUS, as a second family of standards.
- Reifying `participatesIn` as a claim.
- Changing HO-003's "jointly sufficient" to "as assessed".
- An evidence anchor for "everything is a view".
- The proposed HO-007 on agents, participation and assessing organizations (2026-11-19). It has no index entry and awaits your confirmation.
- Domains, ranges and property groups for the Protégé editor-first build.

Two things to check: whether the AffectedEntity rename has been applied to the draft note itself, and whether the Decisions Log's 2026-11-18 "patient" wording still matches the draft.
<!-- copilot-message {"tools":["obsidian-copilot_miyo_search (other)","grep (search)"]} -->
[Timestamp: 2026/11/20 09:29:23]

**user**: please review every line of the draft note and then produce a new visual structure based on the style of the note entitled Harm Ontology v3 draft structure representing and incorporating the changes logged above
[Timestamp: 2026/11/20 09:33:52]

**ai**: I read all 191 lines. I'll write the revised structure as a new note beside the original, so the original stays as the 2026-11-17/18 record.I read all 191 lines of [[Harm Ontology v3 - Draft Structure]] and wrote a revised version as a new note, [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)]]. The original is unchanged.

**Problems found in the original**
1. **Stale header.** It cited only the 2026-11-14 and 2026-11-15 decisions, though it had been revised on 11-17 and 11-18.
2. **Broken tree layout.** The AffectedEntity block and its proposed lines sat outside the tree, which made the Patient-to-AffectedEntity rename hard to follow.
3. **Missing omission categories.** The 2026-11-17 decision on omission assessments for left-out causes (outOfFrame, blindSpot, acceptedHarm) was absent.
4. **Missing SHACL rule.** The `sh:or` constraint on CausalCandidate was absent.
5. **Attribution cross-reference.** The merged Attribution was linked only to HO-004; the 11-17 decision cites HO-004 and HO-005.
6. **Possible subtype mismatch.** The 11-18 log names NaturalSystem and EngineeredSystem, but the draft lists NonSentientSystem. I kept it marked as proposed and flagged it for you to check against [[Decisions_Log]].
7. **Out-of-date test results.** The draft cited 42 of 42 checks; the latest run is 58 of 58.

**What the revision adds**
- Every logged decision from 2026-11-14 to 11-18, placed in the same ASCII tree style.
- The 2026-11-19 HO-007 proposal on agents and assessing organizations, marked as proposed.
- A revision history and a list of open items, including the Protégé domains and ranges and the narrative placement.

I did not edit [[Decisions_Log]] or any other note. The rename across other notes and the v1 `.ttl` remains deferred to migration.
<!-- copilot-message {"tools":["read (read): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure.md","write (edit): 02_Ideas Topics Concepts/Harm Ontology/ontology/Harm Ontology v3 - Draft Structure (rev 2026-11-20).md"]} -->
[Timestamp: 2026/11/20 09:33:52]

**user**: what is the purpose/meaning of the sections Box A thru Box D in this ontology structure? How is that different from their meaning/purpose/structure in the previous Harm Ontology v3 draft structure
[Timestamp: 2026/11/20 09:53:17]

**ai**: The four boxes are the same in both versions. I did not change them in the 2026-11-20 revision.

**What each box is**

- **Box A (Phenomenality).** A property with three values (Phenomenal, NonPhenomenal, ConditionallyPhenomenal), applied through two separate properties: *observability* (whether something can be seen, and by whom) and *experienceability* (whether the affected entity can feel it). It is tagged "(box A)" on Factor (observability) and Effect (experienceability). Source: the 2026-11-14 decision in [[Decisions_Log]].
- **Box B (Missingness).** The statuses for absent information: absent means "not considered", plus Unknown, NotApplicable, Undisclosed, Disputed and Pending. Source: the 2026-11-14 open-world decision, detailed in [[HO-II.e Missingness Statuses and Domain Profiles]]. Unlike Box A, no tree node carries a "(box B)" tag, though the governing commitments point to it.
- **Box C (Reuse).** The rule to map to existing vocabularies, not import them, followed by a list of candidate vocabularies (BFO, PROV-O, OWL-Time, legal, cyber, AI incident). Every candidate is marked unverified. Source: the 2026-11-14 reuse decision and [[HO-III.b Reusing Expert Domain Vocabularies]].
- **Box D (Vocabulary layer).** The three-layer rule (ontology, profiles, vocabulary) and graded mappings (exact, close, narrow, broad, related). Source: the 2026-11-17 decision and [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]].

**Difference from the 2026-11-15 draft**

The boxes sit outside the tree in both versions. They are cross-cutting rules and property sets that apply to several classes. They are not classes. The differences are:
- **Box D was already in the original.** It was added in the 2026-11-17 revision, so both versions have it.
- **Box D's content is repeated in my revision.** The three-layer rule now also appears under "Governing commitments", which duplicates Box D. I should have removed one of them.
- **Nothing else changed.** The boxes are unchanged in the revision. The changes I made elsewhere, such as the AffectedEntity block, the omission categories and the SHACL rule, are all in the tree.

If you want the boxes to carry the same status as the tree, I can give Box B the same "(box B)" tags and remove the duplicate three-layer line.
[Timestamp: 2026/11/20 09:53:17]

**user**: we made a provisional investigation into whether to break the structure into 3 ontologies -  a schema, a vocabulary, a shacl  is this still provisional or is it logged as a decision yet?
[Timestamp: 2026/11/20 09:59:04]

**ai**: It is still provisional. The three-layer idea is logged, but the split into separate files is not.

**Logged (Decisions_Log, 2026-11-17):** Harm ontology uses three layers: ontology (OWL, `ho:`) for structure, profiles (SHACL, `hosh:`) for requiredness, and vocabulary (SKOS, `hov:`) for words and meaning. This is the decision behind the "three layers" in [[Harm Ontology v3 - Draft Structure (rev 2026-11-20)]].

**Not logged:**
- **Renaming layer 1 from "ontology" to "schema".** On 2026-11-18 I proposed logging it, because "the ontology" also means the whole project. The transcript records your "yes" to the rename, but [[Decisions_Log]] has no entry for it. I asked whether to log it and have not done so.
- **Separate files and a loader.** The layout (`ho-schema.ttl`, `ho-profiles.ttl`, `ho-vocabulary.ttl`, and `ho-all.ttl` to import them) appears only in [[Harm Ontology v3 Provisional Release Brief]] and in the mini example. The mini example's brief says its layout is not approved. The release brief says it is "not started, not approved".

So the three-way split is a logged layering with a provisional file layout. Logging the schema rename and the file layout would need your confirmation. I can draft those entries for you to approve.
<!-- copilot-message {"tools":["grep (search)","obsidian-copilot_miyo_search (other)"]} -->
[Timestamp: 2026/11/20 09:59:04]