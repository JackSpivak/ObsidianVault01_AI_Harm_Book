"""Build the EDITOR-FIRST MINI experiment: ONE OWL file meant to be read and edited in Protege.
TEST ARTEFACT, NOT THE V3 RELEASE. Placeholder IRIs. Nothing here is a design decision.

Why: the first mini example (three_layer_mini) was judged "awful, very difficult to visualize and navigate" and had no domains/ranges
or property groups. Generated pages were rejected (author, 2026-11-18). So this experiment uses ONLY what an OWL editor shows:
  - a PROPERTY TREE that mirrors the 12 display groups of PerspectiveStructure 0.02 (abstract grouping super-properties),
  - real DOMAIN and RANGE on every property, plus 'only' restrictions on the class so the class page shows its links,
  - the hub narrative as ANNOTATIONS on the property it documents (congruence, omission, developmentalAltitude),
  - the discipline spokes as INDIVIDUALS grouped under discipline classes, each pointing at the property it documents.
One-off use of this script is migration only (it parses the vault notes once). Day-to-day work is in the editor.

Usage (vault root, conda env harm-ontology):
  python -I "02_Ideas Topics Concepts/Harm Ontology/ontology/scripts/build_editor_first_mini.py"
"""
import importlib.util
import sys
from pathlib import Path
from rdflib import Graph, Namespace, Literal, URIRef, BNode
from rdflib.namespace import RDF, RDFS, OWL, SKOS, DCTERMS, XSD
from rdflib.collection import Collection

HERE = Path("02_Ideas Topics Concepts/Harm Ontology/ontology/scripts")
spec = importlib.util.spec_from_file_location("mini", HERE / "build_three_layer_mini.py")
mini = importlib.util.module_from_spec(spec); spec.loader.exec_module(mini)

OUT = Path("02_Ideas Topics Concepts/Harm Ontology/ontology/tests/editor_first_mini")
NB = "https://example.org/harm-ontology/v3-editor-mini/"
HO = Namespace(NB + "schema#")
ONT = URIRef(NB + "ho-editor-mini")
PS02 = Path("02_Ideas Topics Concepts/Harm Ontology/PerspectiveStructure 0.02.md")

CLASSES = {  # stub classes needed as ranges (defined elsewhere in the draft structure)
    "Assessment": "one judgment = one instance (draft structure)",
    "EvaluativeStandard": "altLabel \"theory of harm\" (draft structure)",
    "AffectedEntity": "formerly Patient; altLabels \"patient\", \"moral patient\" (Decisions_Log 2026-11-18)",
    "Factor": "neutral; one contributor among many (draft structure)",
    "Effect": "neutral; one consequence among many (draft structure)",
    "Agent": "(?) open in the draft structure",
    "Person": "stub", "Event": "stub", "Community": "stub (community of inquiry)", "CausalGraph": "stub (HO-I.a)",
    "LegalResponse": "later (draft structure)", "Source": "stub (group 12a)",
}
DISC = mini.DISC
DISC_CLASS = {"law": "LawTerm", "eth": "EthicsTerm", "phil": "PhilosophyTerm", "pol": "PoliticalTheoryTerm", "sci": "ScienceStudiesTerm",
              "cog": "CognitiveScienceTerm", "lit": "LiteratureTerm", "soc": "SociologyTerm", "psy": "DevelopmentalPsychologyTerm",
              "int": "IntegralTheoryTerm"}

# group key -> (label, parent key). Labels are those of PerspectiveStructure 0.02.
GROUPS = {
    "0": ("0 CORE (required)", None), "1": ("1 RELATIONS (relations before attributes)", None),
    "2": ("2 IDENTITY & LINEAGE", None), "3": ("3 INTEGRAL POSITION (confirmed 2026-11-17)", None),
    "3.1": ("3.1 quadrant axes (Wilber, AQAL)", "3"), "3.2": ("3.2 scope axes (kept separate)", "3"),
    "4": ("4 EXTENT", None), "5": ("5 AIM & NORMATIVE CORE", None), "6": ("6 EPISTEMICS", None),
    "7": ("7 STANCE (holder's side)", None), "8": ("8 SUBJECT'S SIDE", None), "9": ("9 POWER", None),
    "10": ("10 DYNAMICS & MATERIALITY", None),
    "11": ("11 ASSESSMENTS (each an Assessment with assessedBy -> PerspectiveType)", None),
    "12": ("12 PROVENANCE & TRUST (about the record)", None), "12a": ("12a Sources", "12"),
    "12b": ("12b PROV", "12"), "12c": ("12c verification, evidence, confidence, canon status", "12"),
    "S1": ("PerspectiveSpecification: Position", None), "S2": ("PerspectiveSpecification: Time", None),
    "S3": ("PerspectiveSpecification: Optics", None), "S4": ("PerspectiveSpecification: Purpose", None),
    "S5": ("PerspectiveSpecification: Operator", None),
}
# (group(s), name, kind o|d, range, tier, allowed values, note, parent property for sub-properties)
T = "\u2605"; TT = "\u2605\u2605"
ROWS = [
    ("0", "name", "d", "string", T + " required", "", "", None),
    ("0", "canonicalSource", "d", "string", T + " required", "", "absorbs foundationalWork, canonicalText", None),
    ("0", "objectOfAttention", "o", "Factor|Effect|AffectedEntity", T + " required", "", "", None),
    ("0", "foundationalCommitments", "d", "string", T + " required", "", "absorbs assumption, principles, priors/baseRates", None),
    ("1", "divergesFrom", "o", "PerspectiveType", T, "", "reified in HO-III.a", None),
    ("1", "convergesWith", "o", "PerspectiveType", T, "", "reified in HO-III.a", None),
    ("1", "specializes", "o", "PerspectiveType", "", "", "absorbs formalCause", None),
    ("1", "generalizes", "o", "PerspectiveType", "", "", "", None),
    ("1", "partOf", "o", "PerspectiveType", "", "", "", None),
    ("1", "hasSublens", "o", "PerspectiveType", "", "", "", None),
    ("1", "complements", "o", "PerspectiveType", "", "", "", None),
    ("1", "complementaryWith", "o", "PerspectiveType", "", "", "", None),
    ("1", "definedAgainst", "o", "PerspectiveType", "", "", "", None),
    ("1", "coupledWith", "o", "PerspectiveType", "", "", "resonance and feedback between traditions", None),
    ("1", "correctedBy", "o", "Community", "", "", "community of inquiry", None),
    ("2", "nameByDomain", "d", "string", "", "", "rename pending: domain -> discipline (with meaningAsOf)", None),
    ("2", "definitionByDomain", "d", "string", "", "", "rename pending: domain -> discipline (with meaningAsOf)", None),
    ("2", "conceptStructure", "d", "string", "", "definitional \u00b7 family resemblance \u00b7 prototype \u00b7 interpretive", "", None),
    ("2", "exemplars", "d", "string", "", "", "goes with conceptStructure", None),
    ("2", "lensKind", "d", "string", "", "designed \u00b7 tacit \u00b7 learned \u00b7 cultural technology", "", None),
    ("2", "lineage", "o", "Person", "", "", "", None),
    ("2", "originatingCircumstance", "o", "Event", "", "", "", None),
    ("2", "transmissionMode", "d", "string", "", "text \u00b7 apprenticeship \u00b7 ritual \u00b7 institution \u00b7 narrative \u00b7 trained model", "", None),
    ("2", "historicalNote", "d", "string", "", "", "", None),
    ("3.1", "interiority", "d", "string", T, "interior \u00b7 exterior \u00b7 both", "", None),
    ("3.1", "collectivity", "d", "string", T, "individual \u00b7 collective \u00b7 both", "", None),
    ("3.1", "quadrant", "d", "string", "", "UL interior\u2013individual \u00b7 LL interior\u2013collective \u00b7 UR exterior\u2013individual \u00b7 LR exterior\u2013collective", "derived", None),
    ("3.2", "socialScope", "d", "string", "", "individual \u00b7 family \u00b7 community \u00b7 tribe \u00b7 nation \u00b7 species \u2026", "size", None),
    ("3.2", "moralCircle", "o", "AffectedEntity", T, "", "which beings count", None),
    (("3.2", "11"), "developmentalAltitude", "o", "Assessment", "", "", "an Assessment; scale + assessedBy required; displayed in group 3, belongs to group 11", None),
    ("4", "spatialScope", "d", "string", "", "", "", None), ("4", "systemicScope", "d", "string", "", "", "", None),
    ("4", "temporalScope", "d", "string", "", "", "", None), ("4", "discountRate", "d", "string", "", "", "goes with temporalScope", None),
    ("4", "scaleValidity", "d", "string", "", "", "", None),
    ("5", "statedPurpose", "d", "string", T, "", "operative side is assessed under congruence (group 11)", None),
    ("5", "normativeForm", "d", "string", T, "deontic \u00b7 consequentialist \u00b7 aretaic \u00b7 relational \u00b7 contractualist", "plural", None),
    ("5", "valueTheory", "d", "string", "", "", "", None),
    ("5", "defaultEvaluativeStandard", "o", "EvaluativeStandard", "", "", "HO-II.a", None),
    ("5", "unitOfMeasure", "d", "string", T, "", "goes with commensurability", None),
    ("5", "commensurability", "d", "string", "", "", "", None),
    ("5", "intentWeighting", "d", "string", T, "intent \u00b7 outcome \u00b7 mixed", "", None),
    ("5", "distributiveConcern", "d", "string", "", "", "", None),
    ("5", "conflictResolution", "d", "string", "", "lexical \u00b7 weighing \u00b7 deadlock", "", None),
    ("5", "fieldOfApplication", "d", "string", "", "", "formerly domainOfApplicability; jurisdiction in the Legal profile", None),
    ("6", "method", "d", "string", T, "", "goes with instrumentResponse", None),
    ("6", "instrumentResponse", "d", "string", T, "threshold \u00b7 false alarm \u00b7 miss", "", None),
    ("6", "criterionOfTruth", "d", "string", "", "", "goes with inferenceModes", None),
    ("6", "inferenceModes", "d", "string", "", "", "", None),
    ("6", "causalModel", "o", "CausalGraph", "", "", "HO-I.a", None),
    ("6", "errorHandling", "d", "string", "", "update \u00b7 act on world \u00b7 suppress \u00b7 immunize", "", None),
    ("6", "explorationMode", "d", "string", "", "explore \u00b7 exploit", "", None),
    ("6", "factHandling", "d", "string", "", "preserves \u00b7 blurs \u00b7 dissolves", "", None),
    ("6", "manipulability", "d", "string", "", "", "", None), ("6", "authenticityAssumption", "d", "string", "", "", "goes with manipulability", None),
    ("7", "bearerRole", "d", "string", "", "", "", None), ("7", "controlLocus", "d", "string", "", "", "", None),
    ("7", "stanceTowardObject", "d", "string", "", "physical \u00b7 design \u00b7 intentional", "", None),
    ("7", "governingAnalogies", "d", "string", "", "", "", None),
    ("7", "effectOnHolder", "d", "string", T, "affective \u00b7 dispositional \u00b7 cognitive \u00b7 physical/observer cost", "", None),
    ("8", "standingOfSubjects", "d", "string", T, "agent \u00b7 affected \u00b7 datum", "\"patient\" -> \"affected\", 2026-11-18", None),
    ("8", "modelOfSubject", "d", "string", "", "", "", None), ("8", "legibility", "d", "string", "", "", "", None),
    ("8", "interfaceAbstraction", "d", "string", "", "", "goes with legibility", None),
    ("8", "consentToBeSeen", "d", "string", T, "", "qualified by powerAsymmetry", None),
    ("8", "adaptiveResponse", "d", "string", "", "", "", None), ("8", "livedExperience", "d", "string", "", "", "", None),
    ("9", "authority", "o", "Agent", "", "", "bound parties", None),
    ("9", "authorityBasis", "d", "string", "", "coercive \u00b7 legal \u00b7 expert \u00b7 moral \u00b7 customary", "", None),
    ("9", "whoseInterests", "o", "AffectedEntity", T, "", "kind and range assigned by the builder", None),
    ("9", "costBearer", "d", "string", T, "", "kind assigned by the builder; goes with differentialBurden", None),
    ("9", "differentialBurden", "d", "string", "", "", "", None),
    ("9", "whoseVoice", "d", "string", T, "", "kind assigned by the builder; goes with precisionWeighting", None),
    ("9", "precisionWeighting", "d", "string", "", "", "", None),
    ("9", "powerAsymmetry", "d", "string", "", "low \u00b7 high \u00b7 total", "", None),
    ("9", "accountabilityLocus", "o", "Agent", T, "named agent \u00b7 role \u00b7 institution \u00b7 Nobody", "", None),
    ("9", "laundering", "d", "string", "", "", "goes with accountabilityLocus", None),
    ("9", "remedy", "o", "LegalResponse", "", "", "", None),
    ("10", "performativity", "d", "string", T, "none \u00b7 self-confirming \u00b7 self-defeating", "", None),
    ("10", "infrastructureDependence", "d", "string", "", "", "", None),
    ("10", "validFrom", "d", "date", "", "", "", None), ("10", "validTo", "d", "date", "", "", "", None),
    ("10", "changeMode", "d", "string", "", "", "", None),
    ("10", "prevalence", "d", "string", "", "dominant \u00b7 contested \u00b7 marginal \u00b7 emerging", "", None),
    ("11", "congruence", "o", "Assessment", TT, "", "stated vs operative; hub drafted in HO-II.d.2", None),
    ("11", "omission", "o", "Assessment", T, "", "hub drafted in HO-II.d.2; replaces blindSpot", None),
    ("11", "outOfFrame", "o", "Assessment", "", "", "constitutive: excluded by design; not visible to this lens", "omission"),
    ("11", "blindSpot", "o", "Assessment", "", "negligent \u00b7 suppressed", "visible but missed", "omission"),
    ("11", "negligentBlindSpot", "o", "Assessment", "", "", "should have been seen", "blindSpot"),
    ("11", "suppressedBlindSpot", "o", "Assessment", "", "", "suspected, and deliberately not looked at", "blindSpot"),
    ("11", "acceptedHarm", "o", "Assessment", "", "", "seen and tolerated", "omission"),
    ("11", "failureMode", "o", "Assessment", "", "excess \u00b7 deficiency", "", None),
    ("11", "epistemicStanding", "o", "Assessment", "", "", "corroboration \u00b7 calibration + uncertainty \u00b7 anomalies \u00b7 orderOfMagnitude", None),
    ("11", "corroboration", "o", "Assessment", "", "", "", "epistemicStanding"),
    ("11", "calibration", "o", "Assessment", "", "", "", "epistemicStanding"),
    ("11", "uncertainty", "o", "Assessment", "", "", "", "epistemicStanding"),
    ("11", "anomalies", "o", "Assessment", "", "", "", "epistemicStanding"),
    ("11", "orderOfMagnitude", "o", "Assessment", "", "", "", "epistemicStanding"),
    ("11", "proceduralIntegrity", "o", "Assessment", "", "", "Fuller's eight", None),
    ("11", "publicJustifiability", "o", "Assessment", "", "", "", None),
    ("11", "knownCritique", "o", "Assessment", "", "", "", None),
    ("11", "critiquedBy", "o", "PerspectiveType", "", "", "target of knownCritique", None),
    ("12a", "keyReference", "d", "string", "", "", "", None), ("12a", "citation", "d", "string", "", "", "", None),
    ("12b", "wasAttributedTo", "o", "Agent", "", "", "PROV", None), ("12b", "wasGeneratedBy", "d", "string", "", "", "PROV", None),
    ("12b", "wasDerivedFrom", "d", "string", "", "", "PROV", None), ("12b", "created", "d", "date", "", "", "", None),
    ("12b", "modified", "d", "date", "", "", "", None), ("12b", "originalWording", "d", "string", "", "", "", None),
    ("12c", "verificationStatus", "d", "string", "", "", "citations only", None), ("12c", "evidenceLabel", "d", "string", "", "", "", None),
    ("12c", "confidence", "d", "string", "", "", "", None), ("12c", "canonStatus", "d", "string", "", "", "", None),
]
SPEC_ROWS = [  # PerspectiveSpecification facets (draft structure)
    ("S1", "standpoint", "d", "string", "", "", "", None), ("S1", "direction", "d", "string", "", "", "", None),
    ("S2", "timestamp", "d", "date", "", "", "altLabel assessedAt", None), ("S2", "exposure", "d", "string", "", "", "the horizon", None),
    ("S2", "predictabilityHorizon", "d", "string", "", "", "(?) open in the draft structure", None),
    ("S3", "framing", "d", "string", "", "", "", None), ("S3", "resolution", "d", "string", "", "", "", None),
    ("S3", "sensitivity", "d", "string", "", "", "threshold", None),
    ("S4", "intent", "d", "string", "", "", "", None),
    ("S4", "appliedEvaluativeStandard", "o", "EvaluativeStandard", "", "", "inherits defaultEvaluativeStandard if absent", None),
    ("S4", "fitness", "d", "string", "", "", "", None), ("S4", "inclusionCriteria", "d", "string", "", "", "", None),
    ("S4", "aggregationRule", "d", "string", "", "", "", None),
    ("S5", "assessor", "o", "Agent", "", "", "", None),
]
XSD_MAP = {"string": XSD.string, "date": XSD.date}
ANN = {}  # name -> IRI of custom annotation properties


def en(g, s, p, text, lang="en"):
    g.add((s, p, Literal(text, lang=lang) if lang else Literal(text)))


def main():
    g = Graph()
    for k, v in (("ho", HO), ("skos", SKOS), ("dcterms", DCTERMS), ("owl", OWL), ("rdfs", RDFS), ("xsd", XSD)):
        g.bind(k, v)
    disc_ns = {p: Namespace(NB + p + "#") for p in DISC}
    for p, ns in disc_ns.items():
        g.bind(p, ns)
    g.add((ONT, RDF.type, OWL.Ontology))
    en(g, ONT, DCTERMS.title, "Harm Ontology editor-first mini experiment (one file, for Protege)")
    en(g, ONT, RDFS.comment,
       "TEST ARTEFACT, not the v3 release. One OWL file so everything is visible and editable in an editor: property group tree "
       "(PerspectiveStructure 0.02), domain and range, narrative as annotations, discipline spokes as individuals. Placeholder IRIs. "
       "Object/data kinds and ranges were assigned by the builder and need review.")
    g.add((ONT, OWL.versionInfo, Literal("editor-first mini 0.1 (2026-11-18). Not the v3 release.")))

    # annotation properties
    for p in (RDFS.label, RDFS.comment, RDFS.seeAlso, SKOS.prefLabel, SKOS.altLabel, SKOS.definition, SKOS.example,
              SKOS.scopeNote, SKOS.historyNote, SKOS.editorialNote, DCTERMS.source, DCTERMS.title, DCTERMS.bibliographicCitation):
        g.add((p, RDF.type, OWL.AnnotationProperty))
    for name, label in (("tier", "tier"), ("allowedValues", "allowed values"), ("displayGroup", "display group"),
                        ("designStatus", "design status"), ("explanation", "explanation"), ("explanationProvenance", "explanation provenance"),
                        ("boundaryTests", "boundary tests"), ("hubStatus", "hub status"), ("glossLine", "gloss line"),
                        ("citationVerification", "citation verification"), ("keyThinkers", "key thinkers"), ("discipline", "discipline"),
                        ("meaningAsOf", "meaning as of"), ("assertedBy", "asserted by"), ("mapsToProperty", "documents / maps to property"),
                        ("mappingGrade", "mapping grade"), ("mappingReason", "mapping reason")):
        ANN[name] = HO[name]
        g.add((HO[name], RDF.type, OWL.AnnotationProperty)); en(g, HO[name], RDFS.label, label)

    # classes
    def cls(name, comment, parent=None, label=None):
        g.add((HO[name], RDF.type, OWL.Class)); en(g, HO[name], RDFS.label, label or name)
        if comment: en(g, HO[name], SKOS.definition, comment)
        if parent: g.add((HO[name], RDFS.subClassOf, HO[parent]))
    cls("Perspective", "Abstract umbrella class with no direct members: either a tradition (PerspectiveType) or a perspective specification (PerspectiveSpecification). Carries only a definition and Explanation.")
    cls("PerspectiveType", "A reusable way of seeing and judging, with a lineage: Utilitarianism, Tort Law, Public Health, a trained AI model. Subclass of Perspective; prefLabel \"tradition\"; altLabel \"lens\".", "Perspective")
    en(g, HO.PerspectiveType, SKOS.prefLabel, "tradition"); en(g, HO.PerspectiveType, SKOS.altLabel, "lens")
    cls("PerspectiveSpecification", "Reusable; all properties optional (draft structure). altLabels: \"viewpoint\", \"perspective snapshot\".", "Perspective")
    en(g, HO.PerspectiveSpecification, SKOS.altLabel, "viewpoint"); en(g, HO.PerspectiveSpecification, SKOS.altLabel, "perspective snapshot")
    g.add((HO.PerspectiveType, OWL.disjointWith, HO.PerspectiveSpecification))
    for c, d in CLASSES.items():
        cls(c, d)
        en(g, HO[c], ANN["designStatus"], "stub: range target only in this experiment")
    cls("DisciplineTerm", "A discipline's own term for an idea that one of the hub properties documents (a 'spoke'). Individuals of the discipline subclasses below.")
    for p, c in DISC_CLASS.items():
        cls(c, DISC[p], "DisciplineTerm", label=DISC[p])

    # properties
    made = {}  # group key -> {'o': iri, 'd': iri}

    def group_prop(key, kind, domain):
        if key in made and kind in made[key]:
            return made[key][kind]
        label, parent = GROUPS[key]
        iri = HO[f"grp_{key.replace('.', '_')}_{'obj' if kind == 'o' else 'data'}"]
        g.add((iri, RDF.type, OWL.ObjectProperty if kind == "o" else OWL.DatatypeProperty))
        en(g, iri, RDFS.label, label)
        en(g, iri, RDFS.comment, "DISPLAY GROUP (PerspectiveStructure 0.02): an abstract grouping property so the property tree mirrors the "
                                  "diagram. Do not use it in data. Groups are display facets, not OWL classes. "
                                  + ("Object-property" if kind == "o" else "Data-property") + " side of the group (OWL keeps the two trees apart).")
        g.add((iri, RDFS.domain, domain))
        en(g, iri, ANN["displayGroup"], label)
        if parent: g.add((iri, RDFS.subPropertyOf, group_prop(parent, kind, domain)))
        made.setdefault(key, {})[kind] = iri
        return iri

    def make(row, domain):
        groups, name, kind, rng, tier, values, note, parent = row
        groups = groups if isinstance(groups, tuple) else (groups,)
        p = HO[name]
        g.add((p, RDF.type, OWL.ObjectProperty if kind == "o" else OWL.DatatypeProperty))
        en(g, p, RDFS.label, name)
        g.add((p, RDFS.domain, domain))
        if kind == "o":
            ranges = rng.split("|")
            if len(ranges) == 1:
                g.add((p, RDFS.range, HO[ranges[0]]))
                r = BNode(); g.add((r, RDF.type, OWL.Restriction)); g.add((r, OWL.onProperty, p))
                g.add((r, OWL.allValuesFrom, HO[ranges[0]])); g.add((domain, RDFS.subClassOf, r))
            else:
                u = BNode(); g.add((u, RDF.type, OWL.Class)); lst = BNode()
                Collection(g, lst, [HO[x] for x in ranges]); g.add((u, OWL.unionOf, lst)); g.add((p, RDFS.range, u))
        else:
            g.add((p, RDFS.range, XSD_MAP[rng]))
        if parent:  # a sub-property of another attribute inherits that attribute's group
            g.add((p, RDFS.subPropertyOf, HO[parent]))
        for gk in groups:
            if not parent:
                g.add((p, RDFS.subPropertyOf, group_prop(gk, kind, domain)))
            en(g, p, ANN["displayGroup"], GROUPS[gk][0])
        if tier: en(g, p, ANN["tier"], tier)
        if values: en(g, p, ANN["allowedValues"], values)
        if note: en(g, p, RDFS.comment, note)
        src = "PerspectiveStructure 0.02" if domain == HO.PerspectiveType else "Harm Ontology v3 - Draft Structure (PerspectiveSpecification)"
        en(g, p, DCTERMS.source, src + ", group " + ", ".join(groups))
        en(g, p, ANN["designStatus"], "proposed (kind and range assigned by the builder; to be reviewed)")
        return name

    names = []
    for row in ROWS:
        names.append(make(row, HO.PerspectiveType))
    for row in SPEC_ROWS:
        names.append(make(row, HO.PerspectiveSpecification))
    # instantiates (PerspectiveSpecification -> PerspectiveType)
    g.add((HO.instantiates, RDF.type, OWL.ObjectProperty)); en(g, HO.instantiates, RDFS.label, "instantiates")
    g.add((HO.instantiates, RDFS.domain, HO.PerspectiveSpecification)); g.add((HO.instantiates, RDFS.range, HO.PerspectiveType))
    en(g, HO.instantiates, RDFS.comment, "inherits the tradition's defaults; may override")
    r = BNode(); g.add((r, RDF.type, OWL.Restriction)); g.add((r, OWL.onProperty, HO.instantiates))
    g.add((r, OWL.allValuesFrom, HO.PerspectiveType)); g.add((HO.PerspectiveSpecification, RDFS.subClassOf, r))
    g.add((HO.assessedBy, RDF.type, OWL.ObjectProperty)); en(g, HO.assessedBy, RDFS.label, "assessedBy")
    g.add((HO.assessedBy, RDFS.domain, HO.Assessment)); g.add((HO.assessedBy, RDFS.range, HO.PerspectiveType))
    en(g, HO.assessedBy, RDFS.comment, "each group-11 Assessment is taken with assessedBy -> PerspectiveType (PerspectiveStructure 0.02)")
    assert len(names) == len(set(names)), "duplicate property names"

    # hub narrative -> annotations on the property it documents
    vg, summary, nq = mini.build_vocab()
    HOV = mini.HOV
    for hub in ("congruence", "omission", "developmentalAltitude"):
        h, p = HOV[hub], HO[hub]
        for src_p, dst_p in ((SKOS.definition, SKOS.definition), (SKOS.example, SKOS.example), (SKOS.scopeNote, SKOS.scopeNote),
                             (HOV.explanation, ANN["explanation"]), (HOV.boundaryTests, ANN["boundaryTests"]),
                             (HOV.status, ANN["hubStatus"]), (HOV.glossLine, ANN["glossLine"])):
            for o in vg.objects(h, src_p):
                g.add((p, dst_p, o))
        en(g, p, DCTERMS.source, "Vocabulary Crosswalk - Concept Hubs and Discipline Schemes (HO-II.d.2), hub hov:" + hub)

    # spokes -> individuals under discipline classes
    reasons = {}
    for a in vg.subjects(RDF.type, OWL.Axiom):
        reasons[(vg.value(a, OWL.annotatedSource), vg.value(a, OWL.annotatedProperty), vg.value(a, OWL.annotatedTarget))] = \
            str(vg.value(a, RDFS.comment))
    spokes = set(vg.subjects(HOV.assertedBy, None))
    n_sp = 0
    for s in sorted(spokes, key=str):
        base, local = str(s).rsplit("#", 1)
        pref = base.rsplit("/", 1)[1]
        iri = disc_ns[pref][local]
        g.add((iri, RDF.type, OWL.NamedIndividual)); g.add((iri, RDF.type, HO[DISC_CLASS[pref]]))
        for p_src, p_dst in ((SKOS.prefLabel, RDFS.label), (SKOS.prefLabel, SKOS.prefLabel), (SKOS.altLabel, SKOS.altLabel),
                             (SKOS.definition, SKOS.definition), (SKOS.example, SKOS.example), (SKOS.historyNote, SKOS.historyNote),
                             (SKOS.scopeNote, SKOS.scopeNote), (SKOS.editorialNote, SKOS.editorialNote),
                             (DCTERMS.bibliographicCitation, DCTERMS.bibliographicCitation), (HOV.explanation, ANN["explanation"]),
                             (HOV.explanationProvenance, ANN["explanationProvenance"]), (HOV.citationVerification, ANN["citationVerification"]),
                             (HOV.keyThinkers, ANN["keyThinkers"]), (HOV.discipline, ANN["discipline"]),
                             (HOV.meaningAsOf, ANN["meaningAsOf"]), (HOV.assertedBy, ANN["assertedBy"])):
            for o in vg.objects(s, p_src):
                g.add((iri, p_dst, o))
        for gp, gname in mini.GRADES.items():
            for frm in vg.subjects(gname, s):
                if str(frm).startswith(str(HOV)):
                    target = HO[str(frm).split("#")[1]]
                    g.add((iri, ANN["mapsToProperty"], target))
                    en(g, iri, ANN["mappingGrade"], gp)
                    rs = reasons.get((frm, gname, s))
                    if rs: en(g, iri, ANN["mappingReason"], rs)
        n_sp += 1
    # check target properties exist
    for _, _, t in g.triples((None, ANN["mapsToProperty"], None)):
        assert (t, RDF.type, OWL.ObjectProperty) in g, f"spoke points at a missing property: {t}"

    OUT.mkdir(parents=True, exist_ok=True)
    g.serialize(OUT / "ho-editor-mini.ttl", format="turtle")
    # cross-check attribute names against PerspectiveStructure 0.02
    txt = PS02.read_text(encoding="utf-8")
    missing = [n for n in names if n not in txt and n not in ("timestamp", "standpoint", "direction", "exposure", "predictabilityHorizon",
               "framing", "resolution", "sensitivity", "intent", "fitness", "inclusionCriteria", "aggregationRule", "assessor",
               "appliedEvaluativeStandard", "critiquedBy", "keyReference", "outOfFrame", "negligentBlindSpot", "suppressedBlindSpot",
               "acceptedHarm", "blindSpot", "corroboration", "calibration", "uncertainty", "anomalies", "orderOfMagnitude")]
    g2 = Graph().parse(OUT / "ho-editor-mini.ttl")
    n_obj = len(list(g2.subjects(RDF.type, OWL.ObjectProperty))); n_dat = len(list(g2.subjects(RDF.type, OWL.DatatypeProperty)))
    n_grp = sum(1 for s in g2.subjects(RDF.type, None) if str(s).split("#")[-1].startswith("grp_"))
    print(f"triples: {len(g2)} | object props: {n_obj} | data props: {n_dat} (incl. group parents: {n_grp}) | attributes in table: {len(names)}")
    print(f"spokes as individuals: {n_sp} | attribute names not found in PerspectiveStructure 0.02 text: {missing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
