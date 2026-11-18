---
type: outline
status: seed
tags: [ontology/harm, ontology/migration]
aliases: [v3 Provisional Release Brief, v3 ttl brief, Production Brief]
created: 2026-11-18
source: "[[Harm Ontology Migration Plan]]"
---

# Harm Ontology v3: Provisional Release Brief

> [!warning] Not started, not approved
> A brief for a **new chat**, written at the end of the 2026-11-18 testing session. It scopes the first v3 `.ttl` and a generated Compendium. It decides nothing about the ontology itself. The author said (2026-11-18) that formal v3 testing is paused and that v3 will be used informally against real-world data, so this is a provisional working release, not an adopted ontology.

## What "full" can mean now
[[Harm Ontology Migration Plan]] fixes the order of work: **Phase 1** v3 skeleton `.ttl` (no narrative) → Phase 2 crosswalk → Phase 3 carry v1/v2 narrative verbatim → Phase 4 new narrative → **Phase 5** generate the Compendium **from the `.ttl`**. So a Compendium with the carried-over v1/v2 narrative needs Phases 2–4 first. What can honestly be produced now:

| Deliverable | What it is | Plan phase |
|---|---|---|
| **D1. v3 skeleton `.ttl`** | Classes, properties and individuals from the draft structure, with labels, altLabels, a design-status flag and a source pointer. | 1 |
| **D1b. v3 narrative layer** | The explanatory content already written for v3 (HO notes, Decisions Log rationale, PerspectiveStructure notes, council-review tables), carried into annotations on the D1 elements. See "Narrative layer" below. Without this, the `.ttl` is a **naked schema**. | 4 (for v3's own content) |
| **D2. Generated Compendium** | Markdown produced by script from D1 + D1b: hierarchy, status, sources and the narrative, per element. Marked "generated, do not edit". Not the old v1/v2 Compendium. | 5 |
| **D3. Build and validation record** | The build script, a validation report, a round-trip check against the draft structure, and a narrative-coverage report. | 1, 4 |

**Still not in scope:** carrying the v1/v2 annotations (Phase 3, which needs the crosswalk, Phase 2), the crosswalk itself, and the AIRO/DPV mappings. So the v1/v2 Compendium narrative is **not** in this release. The `.ttl` is the single source of truth; the Compendium is never edited by hand.

## Inclusion rule (so test-only ideas do not leak in)
Read each element of [[Harm Ontology v3 - Draft Structure]] against [[Decisions_Log]] and tag it with `ho:designStatus`:
- **decided**: logged in the Decisions Log (cite the date).
- **open**: marked (?) in the draft structure.
- **pending**: proposed and deliberately not logged (Assessment split, causal standards, `participatesIn`, "sufficient as assessed").
- **proposedUntested**: the 2026-11-18 proposals (`occurredDuring`, AffectedEntity type as assessed, `Unclassified`, `affectedStanding`, NaturalSystem / EngineeredSystem, CollectiveNaturalGroup, Household).
- **v4Proposed**: Chain ([[HO-006 Causal Chain - an Assessed Selection with a Horizon]]).

Include `decided` and `open` elements, flagged. Include `pending`, `proposedUntested` and `v4Proposed` **only if the author wants them**, and always flagged. Never present a test result as a design decision.

**Left out by default:** the test-only machinery (Procedure, Evidence, Observation, Claim, ScopeDeclaration, Band, BandMapping, the `hoa:` attribute vocabulary, `assessmentBasis`, derived statuses). If the author wants them, put them in a **separate optional module** (`ho-test-extension.ttl`), not in the schema file. The status calculation stays outside the ontology (it lives in `toy_status.py`).

## Decisions needed from the author before building
1. Include `pending` / `proposedUntested` / `v4Proposed` elements (flagged), or only `decided` and `open`? (Recommended: flagged, so informal use against real data can try them.)
2. Test-only machinery: omit, or a separate extension module? (Recommended: separate module, built second.)
3. Namespace IRI and `owl:versionIRI` (the plan says a versioned namespace). The tests used `https://example.org/harm-ontology/v3-test#`, which must **not** be reused.
4. Declare `airo:`, `dpv:` and `vair:` prefixes now (the Migration Plan advises it), even though no mappings are built yet?
5. Hand-written Turtle in sections, or built by a small script from a table of elements? (Recommended: script, because v4 will change the table and the Compendium is generated anyway.)
6. **Narrative placement: OPEN again.** The author leaned to option 1 (2026-11-18), then opened the mini example in Protégé and found it "awful. very difficult to visualize and navigate/understand", with no domains or ranges visible on the properties (see [[Harm Ontology v3 Three-Layer Mini Example Brief]]). Do not treat the layout below as settled. Not logged in Decisions_Log. The text that follows is the earlier leaning, kept for reference. Follows the three-layers decision ([[Decisions_Log]] 2026-11-17): **separate files by layer**, tied by a loader. Layer 1 **schema** (OWL, `ho:`; named "schema" by the author, 2026-11-18, in place of "core" or "ontology") keeps a **short definition, altLabels, `designStatus` and source on each element**, plus an `rdfs:seeAlso` pointer to its hub; layer 3 vocabulary (SKOS, `hov:` hubs, discipline schemes) holds the **long narrative** (explanation, examples, history, citations, spokes, mapping grades); layer 2 profiles (SHACL, `hosh:`). The Compendium generator merges all three. A working mini example is in `ontology/tests/three_layer_mini/` (see its README), built by `ontology/scripts/build_three_layer_mini.py`. Not yet opened in Protege.
7. Is a transcript sweep wanted for explanations that never reached a note? (Recommended: not in the first release; list it as a follow-up.)

## File layout: three layers, one loader
Per [[Decisions_Log]] 2026-11-17 (three layers) and the leaning decision 6 below. Each layer is its own small ontology with its own ontology IRI and version IRI; a tiny loader imports all three, and **that loader is the file to open in Protégé**.
- `ho-schema.ttl`: layer 1, OWL, `ho:`; the bare backbone (classes, properties, hierarchy, **domain and range**, short label and definition); imports nothing from the other layers, so it works alone. D1 goes here.
- `ho-profiles.ttl`: layer 2, SHACL, `hosh:`; imports the schema.
- `ho-vocabulary.ttl`: layer 3, SKOS, `hov:` hubs plus one scheme per discipline (`law:`, `eth:`, `phil:` …); imports the schema. D1b goes here.
- `ho-all.ttl`: only `owl:imports` of the three. Plus a `catalog-v001.xml` mapping each ontology IRI to its local file, so imports resolve offline.
- **Namespaces name things; `owl:imports` loads files.** Prefixes load nothing.
- **Worked example to copy** (brief: [[Harm Ontology v3 Three-Layer Mini Example Brief]]): `ontology/tests/three_layer_mini/` (four files, the catalog and a README), built by `ontology/scripts/build_three_layer_mini.py`. The vocabulary file there is **parsed from the crosswalk note**, so hub, spoke, explanation, value-scale and original-wording text is verbatim; a post-build check confirms it. The new chat can reuse that parsing approach for the remaining hubs. Opened in Protégé by the author: hard to navigate, and the schema had no domains or ranges (so properties showed no links). **A real schema with domains and ranges, and a way to view the layers together, are needed before this layout is used.** Its SHACL shapes are demo only.
- Only three hubs exist (`congruence`, `omission`, `developmentalAltitude`). The other ★ attributes still need hubs and spokes built (new work; mapping grades proposed by Claude, reviewed by the author).

## Narrative layer (D1b): what keeps it from being a naked schema
**Principle** (from [[Harm Ontology Migration Plan]]): narrative lives in the ontology's annotations, and an explanation counts as saved only when it is written into an annotation with `dcterms:source` naming where it came from.

**Sources of v3-native narrative, and where each goes:**
| Source | Content | Annotation target |
|---|---|---|
| HO notes (HO-000, HO-I.a/b/c, HO-II.a–e, HO-III.a/b, HO-003–006, HO-premise) | Summary / "Why this is distinct", examples ("Real-world examples"), "Why it matters to the book", open questions | `skos:definition` or `skos:scopeNote` (summary), `skos:example`, `skos:editorialNote` (relevance, caveats), `skos:note` (open questions), on the elements each note covers |
| [[Decisions_Log]] | The decision and its **rationale** (the "Why" column), with date | `skos:historyNote` (decision + date) and the rationale as `skos:editorialNote`, `dcterms:source` → the log entry |
| "Original wording" blocks in the HO notes and the log | The author's verbatim words, with attribution and session | Kept **verbatim**, with `dcterms:creator` (author or the model) and `dcterms:source` (session). Never reworded |
| [[PerspectiveStructure 0.02]] and the council reviews (Classical, Cognitive, Physics, Ethics, Logic, Sci-Fi, and the others for PerspectiveStructure 0.01) | Per-attribute meaning, example, citations, **verification status**, history, modelling implication, limits | `skos:definition`, `skos:example`, `skos:historyNote`, `skos:editorialNote`, citations as `dcterms:references` / `dcterms:source`, **verification status kept** (verified / partly verified / unverified) |
| Test notes ([[HO-002.a Assessment-Everywhere Test Strategy]], toy results) | Test-only decisions and results | **Not** carried as design narrative. At most a pointer on an element ("tested in toy case, see HO-002.a"), flagged test-only |

**Rules**
- **Verbatim where it is a quote**; summaries may be condensed but must keep the claim and its caveat. **Never rewrite silently**; mark paraphrase or condensation as such.
- **Attribution kept:** author words vs model words, with the session or note. Model-written content is labelled as such.
- **Unverified stays unverified:** references from memory (legal cases, Horizon, Wilber, NESS/INUS, vocabularies, Lorenz, Meadows, the Sai Weng war ending) keep their "unverified" flag in the annotation.
- **Status flags travel with the text:** narrative about a `proposedUntested` or `pending` element is flagged the same way.
- **Language tags:** `@en`.
- **Coverage report (D3):** every section of every source note above is mapped to an element, or listed as unmapped with the reason. Report, per element, which narrative annotations it has and which it lacks. The author reviews the unmapped list.

**Not captured by this layer:** explanations that exist only in chat transcripts and were never written into a note. Those are findable only by reading transcripts (e.g. the 2026-11-14 redesign transcript, read selectively). Decide whether a sweep is wanted; if yes, do it as a separate pass, with provenance.

**Staging:** build D1 and review it first, then add the narrative one source group at a time (HO notes → Decisions Log → PerspectiveStructure and the council tables), checking coverage after each.

## Content rules
- **Names:** AffectedEntity (altLabels "patient", "moral patient"), `affectedStanding`, `forAffectedEntity`. No `Patient` IRIs. Subtype names unchanged.
- **Other renames to carry:** FactorAssembly (altLabel "causal assembly"), EvaluativeStandard (altLabel "theory of harm"), PerspectiveType (prefLabel "tradition", altLabel "lens"), PerspectiveSpecification (altLabels "viewpoint", "perspective snapshot"), CausalCandidate, Attribution merged into CausalAssessment.
- **Valence neutrality:** Factor, CausalRole and Effect carry no harmful/beneficial flag. `HarmfulEffect` is optional and only inferred from an assessment. No Harm class that is harmful in itself.
- **Perspective** is abstract with no direct members; PerspectiveType and PerspectiveSpecification are disjoint subclasses.
- **Annotations in D1:** `rdfs:label`, `skos:prefLabel` / `altLabel`, `ho:designStatus`, `dcterms:source` (the Decisions Log date or HO note), `owl:versionInfo`. Narrative annotations come from D1b, under the rules in the next section. Nothing is invented: where no source text exists, the annotation is left out and listed in the coverage report. References known to be from memory stay marked unverified.
- **Open world:** missingness (Unknown, NotApplicable, Undisclosed, Disputed, Pending) as values, not assumed.

## Checks (D3)
- Parses with rdflib; `validate_ttl.py` counts reported; no suspicious IRIs.
- **Round trip:** every element in the draft structure appears in the `.ttl` (or is listed as deliberately omitted), and every `.ttl` element appears in the draft structure.
- **SHACL (pyshacl), minimal:** every class and property has a label, a `designStatus` and a source; no `Patient` IRI; no class both `decided` and `(?)`.
- **Compendium:** regenerate and diff; every `.ttl` element appears once; nothing in it is hand-edited.
- **Narrative coverage:** every HO note section, Decisions Log entry (and rationale) and council-table row is mapped or listed as unmapped with a reason; every quote is byte-identical to its source; verification flags preserved.
- This also gives a first SHACL step (test-plan step 6), as a side effect, not as the full SHACL work.

## Files the build needs
**Attach these two at the start** (this brief is self-contained for the task; the handoff gives context and cautions):
- [[Harm Ontology v3 Provisional Release Brief]] (this note)
- [[Handoff - Harm Ontology]]

**The agent must read these (open by path; links in the draft structure are not followed automatically):**
- [[Harm Ontology v3 - Draft Structure]]: the element list (the main source for D1)
- [[Decisions_Log]] (`00_Claude_Admin/Decisions_Log.md`): which elements are `decided`, with dates
- [[Harm Ontology Migration Plan]]: phases, principles, tooling
- [[PerspectiveStructure 0.02]]: the PerspectiveType groups 0–12 and their properties (the draft structure only summarises them)
- [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]] and [[Integral Altitude Scale]]: Box D (vocabulary layer, `hov:` / `hosh:` prefixes)
- [[Handoff - Perspective Vocabulary and v3 Follow-ups]]: PerspectiveType consolidation follow-ups

**Read as needed, for property details and status of individual elements:** [[HO-000 Harm as Perspective-Relative Assessment]], [[HO-I.a Factor and CausalRole]], [[HO-I.b Effect and Cascades]], [[HO-I.c Phenomenality - Observability and Experienceability]], [[HO-II.a Assessment and Evaluative Standard]], [[HO-II.b Assessment Horizon - the Sai Weng Trap]], [[HO-II.c Judgment as Assessment - Reasoning over Precedent]], [[HO-II.d Perspective - Ten Optional Properties]], [[HO-II.e Missingness Statuses and Domain Profiles]], [[HO-III.a Divergence and Integration - True but Partial]], [[HO-III.b Reusing Expert Domain Vocabularies]], [[HO-003 Causal Assembly - the Perfect Storm]], [[HO-004 Criticality, Leverage and the Limits of Scope]], [[HO-005 Assessed Membership and Systematic Omission]], [[HO-006 Causal Chain - an Assessed Selection with a Horizon]], [[HO-premise No Intrinsic Harmfulness]].

**Tooling and patterns (paths are in the vault):**
- `02_Ideas Topics Concepts/Harm Ontology/ontology/scripts/` (`validate_ttl.py`, `README.md.txt` with run commands); conda env `harm-ontology`, `python -I`, run from the vault root.
- `…/ontology/Interdisciplinary Harm Ontology v1.ttl`: the repaired v1 file, as a pattern for prefixes and annotations (do not edit).
- `…/ontology/tests/toy_branch_ledger_B.ttl`: only if the test extension module is wanted; the test namespace must not be reused.
- [[Harm Ontology v3 Test Summary]] and [[2026-11-18 Harm Ontology v3 Toy Case Results]]: background on what the test showed; **not** a source of design decisions.

**Also needed for the narrative layer (D1b):** the council review notes in `02_Ideas Topics Concepts/Harm Ontology/` (`v-0.01 … Council Review of - PerspectiveStructure 0.01.md`: Classical, Cognitive, Physics, Ethics, Logic, Sci-Fi, and any others), because they hold the per-attribute definitions, examples, citations and verification status. Find them with a glob on `v-0.01 *Review*`. Also the "Original wording" blocks in every HO note.

**Not needed:** the 2026-11-14 redesign transcript (only if a transcript sweep is chosen), the old root files, and the v1/v2 compendia (Phase 3 material, out of this release).

## Suggested order for the new chat
1. Attach this brief and [[Handoff - Harm Ontology]]; have the agent open the files listed above.
2. Get the five decisions above from the author.
3. Build the element table (one row per element: name, kind, parent, status, source, altLabels). Author reviews the table before any Turtle is written.
4. Generate D1, run the checks, fix.
5. Add the narrative layer (D1b) one source group at a time; run the coverage report after each; the author reviews the unmapped list.
6. Generate D2 (including the narrative) and diff.
7. Record the build, the checks and the coverage in a session note; update the handoff.

## Cautions
- **Momentum:** do not accept the table wholesale. The author values reflection over quick agreement.
- A skeleton in a file can look more settled than it is. Keep `designStatus` visible in both D1 and D2.
- **Do not edit** the old root files (`Interdisciplinary_Harm_Ontology_Compendium.md`, `Interdisciplinary Harm Ontology.ttl`); they await an archive decision.
- Large files: build in sections or by script and write straight to the vault (see Migration Plan, Tooling).
- Tooling: conda env `harm-ontology` (`python -I`, rdflib, pyshacl); scripts in `ontology/scripts/`; test files in `ontology/tests/`, outside the schema.

## Related
- [[Handoff - Harm Ontology]]
- [[Harm Ontology Migration Plan]]
- [[Harm Ontology v3 - Draft Structure]]
- [[Harm Ontology v3 Test Summary]]
- [[Decisions_Log]]
