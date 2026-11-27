EDITOR-FIRST MINI EXPERIMENT (test artefact, 2026-11-18). Not the v3 release. Placeholder IRIs (example.org).

OPEN:  File > Open > ho-editor-mini.ttl   (ONE file; no imports, no catalog needed)

WHY
  The first mini example (three_layer_mini) was judged awful to navigate, had no domain/range and no property groups, and generated pages were
  rejected. This experiment uses only what an OWL editor shows. It collapses the three layers into one file ON PURPOSE, to test the display;
  the 2026-11-17 three-layers decision is not changed by it.

WHAT TO LOOK AT (Protege; these are the features I expect, from general knowledge, not tested)
  Object properties tab  -> a TREE that mirrors the 12 display groups of PerspectiveStructure 0.02:
      "0 CORE (required)", "1 RELATIONS ...", "3 INTEGRAL POSITION" > "3.2 scope axes", "11 ASSESSMENTS" > congruence, omission > outOfFrame /
      blindSpot > negligentBlindSpot / suppressedBlindSpot / acceptedHarm, ... Select a property: domain and range are on its page.
  Data properties tab    -> the same group tree for the text/enumerated attributes (OWL keeps object and data properties in separate trees,
      so each group appears once in each; the group parents say so in their comment).
  Classes tab            -> Perspective > PerspectiveType, PerspectiveSpecification; the range classes. Select PerspectiveType: its
      'SubClass Of' section lists restrictions such as "divergesFrom only PerspectiveType" (these say what links to what; they do not force
      anything to exist).
  Select ho:congruence / omission / developmentalAltitude (Object properties tab): the hub narrative is in the Annotations pane
      (definition, example, scope note, explanation, boundary tests, hub status, gloss line).
  Individuals tab       -> 17 discipline "spokes" under classes such as LawTerm, EthicsTerm, PhilosophyTerm... Each has its own annotations
      and 'maps to property' (the property it documents), the mapping grade and the reason.
  Tip: set the renderer to show rdfs:label (Preferences), so the tree shows the group names instead of IRI fragments.

WHAT IS IN / NOT IN
  In: all PerspectiveType attributes of PerspectiveStructure 0.02 (128 properties incl. PerspectiveSpecification facets), groups and tiers
      (annotation 'tier': star, double star, required), allowed values as an annotation, domain/range, 'only' restrictions.
  Not in: the two profiles (LegalInstitutional, LearnedModel), value scales and levels, original-wording quotes, the other classes of the
      draft structure (Factor, Effect, ... are stubs used as ranges), SHACL, SKOS hierarchy for the hubs.

BUILDER'S CHOICES (to review)
  - Which attributes are object properties (links, Assessments) and which are data properties (text/enumerations) was assigned by the builder.
    Enumerated lists are an annotation ('allowed values'), not individuals.
  - Group parents are abstract sub-property parents. 0.02 decided "groups are display facets, not OWL classes"; super-properties are not classes,
    but they are OWL entities and OWL would infer a parent link from each child link. Never use them in data.
  - developmentalAltitude sits under both 3.2 (displayed there) and 11 (where it belongs).
  - Spokes are NamedIndividuals typed by a discipline class (e.g. LawTerm); in the earlier mini example they were skos:Concepts. The pointer to the
    property is an annotation with an IRI value ('maps to property'); I do not know how well Protege lists it in the property's usage view.

REBUILD (one-off migration only)
  From the vault root: python -I "02_Ideas Topics Concepts/Harm Ontology/ontology/scripts/build_editor_first_mini.py"
  (parses PerspectiveStructure-derived tables in the script and the Vocabulary Crosswalk note; day-to-day work is meant to happen in the editor)
