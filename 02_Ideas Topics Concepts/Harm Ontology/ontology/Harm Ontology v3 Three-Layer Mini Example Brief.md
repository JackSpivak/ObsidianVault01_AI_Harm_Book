---
type: outline
status: seed
tags: [ontology/harm, ontology/migration]
aliases: [Three-Layer Mini Example Brief, three_layer_mini brief, ho-mini brief]
created: 2026-11-18
source: "[[Harm Ontology v3 Provisional Release Brief]]"
---

# Harm Ontology v3: Three-Layer Mini Example Brief

> [!warning] Test artefact, not the v3 release
> A small worked example built on 2026-11-18 to show how the three layers decided on 2026-11-17 ([[Decisions_Log]]) look in an ontology editor and how they are tied together. Placeholder IRIs (`example.org`). Nothing here is a design decision. **Opened in Protégé by the author on 2026-11-18. Verdict (corrected; an earlier "looks great" in this note was a mistake): "it looks awful. very difficult to visualize and navigate/understand."** Two findings below. The layout is **not** approved. Full-build scope is in [[Harm Ontology v3 Provisional Release Brief]]; this note records the experiment.

## Why it exists
- The author asked what the layers look like literally in Protégé, whether all three files must be loaded, and how the vocabulary can be seen beside the classes and attributes it describes.
- It answers by showing the pattern on real content (the three fleshed-out hubs), before any full build, so the layout can be judged and changed cheaply.
- It tests the leaning decision on narrative placement (author, 2026-11-18, "option 1"): a short definition on each schema element, the long narrative in the vocabulary layer.

## Naming
- **Folder:** `02_Ideas Topics Concepts/Harm Ontology/ontology/tests/three_layer_mini/`
- **Files:** `ho-schema-mini.ttl`, `ho-profiles-mini.ttl`, `ho-vocabulary-mini.ttl`, `ho-all-mini.ttl`, `catalog-v001.xml`, `README.md.txt`
- **"Schema" = layer 1** (the OWL backbone: classes, properties, hierarchy, domain and range, plus a short label and definition on each element). Adopted by the author 2026-11-18 in place of "core" and of "ontology (OWL)" for this layer, because "the ontology" also means the whole project. Not yet logged in [[Decisions_Log]]. The first build of this example used `ho-core-mini.ttl`.
- **Builder:** `ontology/scripts/build_three_layer_mini.py`
- The full build would drop "-mini" (`ho-schema.ttl`, `ho-profiles.ttl`, `ho-vocabulary.ttl`, `ho-all.ttl`).

## How the layers tie together
- **Namespaces name things; `owl:imports` loads files.** A prefix such as `hov:` loads nothing.
- Each layer is its own small ontology with its own ontology IRI and version IRI. A tiny loader imports all three. **Open the loader (`ho-all-mini.ttl`) in Protégé** and the imports load, so the three files do not have to be loaded by hand.
- `catalog-v001.xml` (same folder) maps each ontology IRI to its local file so the imports resolve offline. Written from memory of Protégé 5; check against the installed version.
- The schema imports nothing from the other layers, so it works alone. Profiles and vocabulary import the schema.
- **Linking:** each schema property carries an `rdfs:seeAlso` pointer to its hub, and each hub points back with `hov:documents`. The reverse view (what points at an element) is in Protégé's usage view.

## What each file contains
| File | Layer | Contents |
|---|---|---|
| `ho-schema-mini.ttl` | 1. Schema (OWL, `ho:`) | Perspective, PerspectiveType (prefLabel "tradition", altLabel "lens"), PerspectiveSpecification, Assessment, `assessedBy`, and the properties `ho:congruence`, `ho:omission`, `ho:developmentalAltitude`. Each has a short definition copied from the vault (Decisions_Log, Canon_and_Continuity glossary, draft structure, hub "Documents" fields), `designStatus`, a source, and a pointer to its hub. Domains and ranges not modelled |
| `ho-profiles-mini.ttl` | 2. Profiles (SHACL, `hosh:`) | **Demo shapes only**: hub completeness and spoke completeness. Not design decisions, and not the LegalInstitutional / LearnedModel profiles of [[PerspectiveStructure 0.02]] |
| `ho-vocabulary-mini.ttl` | 3. Vocabulary (SKOS, `hov:` plus discipline namespaces) | See below (about 900 triples) |
| `ho-all-mini.ttl` | Loader | Imports the other three |

**Vocabulary file contents** (parsed from [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]]):
- **Three hubs:** `congruence`, `omission`, `developmentalAltitude`. Each has definition, example, scope, explanation, status and the diagram gloss. `omission` also has its boundary tests and branches (out of frame, blind spot, negligent, suppressed, accepted harm).
- **Seventeen spokes:** 5 congruence, 8 omission, 4 altitude (including Gilligan's care stages). Each has altLabels, definition, example, citation, citation verification, historical note, key thinkers, scope note, discipline, meaning-as-of, asserted-by and its full explanation (with provenance: verbatim from a council review, or new draft).
- **Mapping grades** (exact, close, narrow, broad, related) on the hub or branch, with the reason for each grade attached to the link as an annotation.
- **Value scales** with ordered levels: Integral bands, Gebser stages, colour altitude, Gilligan, Kohlberg, Stoic circles; the band-stage-colour grouping; the proposed level mappings with their reasons.
- **Original wording:** 19 quotes, verbatim, with attribution and the session source.
- **Ten discipline schemes** (law, ethics, philosophy, political theory, science studies, cognitive science, literature, sociology, developmental psychology, Integral theory) and a hubs scheme.

## Method and checks
- **Built by script from the vault note**, so text is carried verbatim, not retyped. After the build the script re-reads the `.ttl` and confirms that all **420** carried text fields are present unchanged.
- **Two edits only:** table escapes undone (`\|` → `|`, `\"` → `"`), and italic markers (`*…*`) stripped from `skos:altLabel` values.
- **Checked (rdflib, pyshacl):** all four files parse; the loader imports the three layers; the demo SHACL shapes conform; each schema property and its hub point at each other.
- **Not checked:** how Protégé displays it; whether the SHACL demo shapes are the right shape of profile.

## Choices made by the builder (not in the source note)
- The combined spoke `phil:junzi / phil:oikeiosis` is one record under `phil:junzi`, with an editorial note saying so.
- The Gilligan scale scheme is `psy:careStagesScale`, because `psy:careStages` is already the spoke.
- Hub-to-spoke match direction runs hub → spoke (for `narrowMatch`: the spoke is narrower than the hub).
- SKOS terms are declared inside the files so an editor shows them (alternative: import the W3C SKOS core, which needs web access or a local copy).
- Stage and colour levels are linked to their band with `skos:broadMatch`; the uncertain third tier (indigo to white) uses `skos:relatedMatch` and carries a note.

## What to look at in Protégé
- **Classes and object properties tabs:** the `ho:` elements. Select `ho:congruence`: label, definition, `designStatus`, source, `rdfs:seeAlso`.
- **Individuals tab:** hubs, spokes, schemes and levels appear as `skos:Concept` / `skos:ConceptScheme` individuals (Protégé is an OWL editor, so SKOS is not shown as a browsable thesaurus). Select `hov:congruence`, `law:congruence`, `hov:omission`.
- **Active ontology tab:** the import closure.
- **Entity usage:** the reverse direction.
- Protégé does not run SHACL; pyshacl does.

## Limits
- Only three hubs exist. The other ★ attributes of [[PerspectiveStructure 0.02]] still need hubs and spokes built (new work; Claude proposes mapping grades, the author reviews).
- The schema is a handful of elements with no domains or ranges; the profiles are demo shapes.
- Placeholder namespace; the real IRI and `owl:versionIRI` are decisions still open in the Provisional Release Brief.
- Mapping grades are those proposed in the crosswalk note and reviewed there (congruence reviewed 2026-11-17; omission and altitude grades still marked for review in that note).

## Findings from the author's Protégé check (2026-11-18)
1. **Hard to visualise, navigate and understand.** The hubs, spokes and levels show as a flat list of individuals with long annotations. Protégé is an OWL editor and does not present SKOS as a browsable hierarchy. The author's reading: the vocabulary layer may suit **queries that build a view** with everything needed in one place, with the link between narrative and classes or attributes obvious.
2. **The object properties do not show where they apply.** They appear as lists. **Cause (mine):** the mini schema deliberately modelled no domains or ranges, so nothing said what links to what. The test layout was judged on an empty schema, which was an unfair test of the display, and I should not have treated it as a layout check. Domains and ranges are needed (see the Provisional Release Brief: derive them from the draft structure's `→` targets).

3. **The property groupings are missing (author, 2026-11-18).** In the structure diagrams, the PerspectiveType and PerspectiveSpecification attributes sit under meaningfully labelled groups (the 12 display groups of [[PerspectiveStructure 0.02]]: 0 CORE (required), 1 RELATIONS, 2 IDENTITY & LINEAGE, 3 INTEGRAL POSITION, 4 EXTENT, 5 AIM & NORMATIVE CORE, 6 EPISTEMICS, 7 STANCE, 8 SUBJECT'S SIDE, 9 POWER, 10 DYNAMICS & MATERIALITY, 11 ASSESSMENTS, 12 PROVENANCE & TRUST; and for PerspectiveSpecification the Position / Time / Optics / Purpose / Operator facets in the draft structure). The author: "this subgrouping was essential to understanding". The mini example had no such grouping. How to carry it (the groups were decided as "display facets, not OWL classes") is an open design question; see the chat of 2026-11-18.

4. **Requirement: editor-first (author, 2026-11-18).** Generated pages made by script are rejected as the way to read or maintain the model: "i am not interested in the script approach at all. it is a miserable way to interact with the data if someone wanted to maintain or extend the ontology in an editor." Everything needed to understand and extend the model must be visible and editable in an OWL editor (Protégé): structure, groups, domain and range, and the narrative beside the element it describes. Scripts remain acceptable only for one-off migration of existing content, not for reading or maintenance.

## Next steps
1. ~~Author opens `ho-all-mini.ttl` in Protégé~~ Done 2026-11-18: negative verdict (above).
2. **Decide how the layers are to be viewed** (generated views per class vs narrative as annotations on the schema elements; options in the chat of 2026-11-18, to be recorded here once chosen).
3. Rebuild the mini example with a **real schema** (the draft structure's classes and properties with domains and ranges) and re-test.
4. **Do not log the narrative-placement decision** (option 1) in [[Decisions_Log]] yet. It was leaning decided, and the check does not support confirming it.

## Rebuild
From the vault root, in the conda env `harm-ontology`:
`python -I "02_Ideas Topics Concepts/Harm Ontology/ontology/scripts/build_three_layer_mini.py"`

## Related
- [[Harm Ontology v3 Provisional Release Brief]]
- [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]]
- [[PerspectiveStructure 0.02]]
- [[Harm Ontology Migration Plan]]
- [[Decisions_Log]] (2026-11-17, three layers)
- [[Handoff - Harm Ontology]]
