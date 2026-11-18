Three-layer MINI EXAMPLE for Protege (test artefact, 2026-11-18). Not the v3 release. Placeholder IRIs (example.org).

PURPOSE
  Show how the three layers decided on 2026-11-17 (Decisions_Log) look in an ontology editor and how they are tied together:
    1. ontology   (OWL,  ho:)    ho-core-mini.ttl        a handful of elements, with short definitions, designStatus, sources
    2. profiles   (SHACL, hosh:) ho-profiles-mini.ttl    DEMO shapes only (not design decisions)
    3. vocabulary (SKOS, hov: + law:, eth:, phil:, pol:, sci:, cog:, lit:, soc:, psy:, int:)
                                 ho-vocabulary-mini.ttl  the three fleshed-out hubs, all spokes, value scales, original wording
    loader                       ho-all-mini.ttl         only owl:imports of the three above

HOW TO OPEN
  Protege: File > Open > ho-all-mini.ttl. The imports load through catalog-v001.xml (same folder), which maps each ontology IRI to its
  local file. If Protege asks about missing imports, point it at the files in this folder. (Catalog behaviour is from memory of Protege 5.)

WHAT TO LOOK AT
  Classes / Object properties tabs : ho: elements. Select ho:congruence: label, definition, designStatus, source, rdfs:seeAlso -> hov:congruence.
  Individuals tab                  : hubs, spokes, schemes and levels are skos:Concept / skos:ConceptScheme individuals.
     hov:congruence, hov:omission, hov:developmentalAltitude  (hubs: definition, example, explanation, status, boundary tests)
     law:congruence, phil:zhengming, ... (spokes: altLabels, definition, example, citation, verification, history, scope note, explanation)
     mapping grades (skos:closeMatch etc.) sit on the hub or branch; the reason for each grade is an annotation on that assertion.
  Active ontology tab              : the import closure.
  Entity usage / "Usage" view      : the reverse direction (what points at an element).

CHECKS DONE (rdflib, pyshacl, 2026-11-18)
  - all four files parse; loader imports the three layers
  - the vocabulary is built by script from the vault note "Vocabulary Crosswalk - Concept Hubs and Discipline Schemes"; a post-build check
    re-parses the .ttl and confirms every carried text field is present unchanged
  - demo SHACL shapes: conforms
  NOT checked: how Protege actually displays it (Protege was not run when this was built).

REBUILD
  From the vault root (conda env harm-ontology):
    python -I "02_Ideas Topics Concepts/Harm Ontology/ontology/scripts/build_three_layer_mini.py"

TEXT HANDLING
  Text is kept as written in the note (Obsidian markdown, [[wikilinks]], backticks). Only edits: table escapes undone (\| -> |, \" -> "),
  and *italic* markers stripped from skos:altLabel values. SKOS terms are declared locally so an OWL editor shows them (alternative: import the W3C SKOS core).
  Choices of the builder, not in the note: the combined spoke phil:junzi / phil:oikeiosis is one record under phil:junzi; the scheme
  psy:careStages is named psy:careStagesScale (the spoke keeps psy:careStages); hub-to-spoke match direction is hub -> spoke.
