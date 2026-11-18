"""Build the three-layer MINI EXAMPLE (core / profiles / vocabulary / loader) for Protege.
TEST ARTEFACT, NOT THE V3 RELEASE. Placeholder IRIs (example.org). Nothing here is a design decision.

Usage (from the vault root):
  python -I "02_Ideas Topics Concepts/Harm Ontology/ontology/scripts/build_three_layer_mini.py"

The vocabulary file is PARSED from the vault note
  02_Ideas Topics Concepts/Harm Ontology/Vocabulary Crosswalk - Concept Hubs and Discipline Schemes.md
so that hub, spoke, explanation, value-scale and original-wording text is carried verbatim, not retyped.
Text is kept as written (Obsidian markdown, [[wikilinks]] and backticks included). Only two edits are made:
 - markdown table escapes (\\| -> |, \\" -> ") are undone;
 - italic markers (*...*) are stripped from skos:altLabel values only, so they read cleanly in an editor.
A post-build check re-parses the written .ttl and confirms every carried text field is present, unchanged.
"""
import re
import sys
from pathlib import Path
from rdflib import Graph, Namespace, Literal, URIRef, BNode
from rdflib.namespace import RDF, RDFS, OWL, SKOS, DCTERMS, XSD
from rdflib.collection import Collection

ROOT = Path("02_Ideas Topics Concepts/Harm Ontology")
SRC = ROOT / "Vocabulary Crosswalk - Concept Hubs and Discipline Schemes.md"
OUT = ROOT / "ontology/tests/three_layer_mini"

BASE = "https://example.org/harm-ontology/v3-mini/"
HO = Namespace(BASE + "core#")
HOSH = Namespace(BASE + "profiles#")
HOV = Namespace(BASE + "vocab#")
SH = Namespace("http://www.w3.org/ns/shacl#")
DISC = {  # discipline prefix -> (label)
    "law": "Law vocabulary", "eth": "Ethics vocabulary", "phil": "Philosophy vocabulary",
    "pol": "Political theory vocabulary", "sci": "Science studies vocabulary (philosophy and history of science)",
    "cog": "Cognitive science vocabulary", "lit": "Literature vocabulary", "soc": "Sociology vocabulary",
    "psy": "Developmental psychology vocabulary", "int": "Integral theory vocabulary",
}
NS = {k: Namespace(BASE + k + "#") for k in DISC}
ONT_CORE, ONT_PROF, ONT_VOCAB, ONT_ALL = (URIRef(BASE + n) for n in
                                           ("ho-core-mini", "ho-profiles-mini", "ho-vocabulary-mini", "ho-all-mini"))
GRADES = {g: getattr(SKOS, g) for g in ("exactMatch", "closeMatch", "narrowMatch", "broadMatch", "relatedMatch")}
SPLIT = re.compile(r"(?<!\\)\|")
EXPECTED = []  # (subject, predicate, text, lang) for the verbatim check


def iri(qname):
    p, l = qname.split(":")
    if p == "hov":
        return HOV[l]
    if p == "ho":
        return HO[l]
    return NS[p][l]


def unesc(s):
    return s.replace("\\|", "|").replace('\\"', '"')


def cells(line):
    parts = SPLIT.split(line.strip())
    parts = parts[1:-1] if parts and parts[0] == "" else parts
    return [unesc(c).strip() for c in parts]


def table_after(lines, i):
    """Rows of the first markdown table at or after line i (separator rows dropped)."""
    while i < len(lines) and not lines[i].lstrip().startswith("|"):
        i += 1
    rows = []
    while i < len(lines) and lines[i].lstrip().startswith("|"):
        if not re.match(r"^\s*\|[\s\-:|]+\|\s*$", lines[i]):
            rows.append(cells(lines[i]))
        i += 1
    return rows


def lit(g, s, p, text, lang="en", check=True):
    g.add((s, p, Literal(text, lang=lang) if lang else Literal(text)))
    if check:
        EXPECTED.append((s, p, text, lang))


def axiom(g, s, p, o, comment):
    a = BNode()
    g.add((a, RDF.type, OWL.Axiom))
    g.add((a, OWL.annotatedSource, s))
    g.add((a, OWL.annotatedProperty, p))
    g.add((a, OWL.annotatedTarget, o))
    lit(g, a, RDFS.comment, comment)


def camel(words):
    w = [x for x in re.split(r"[^A-Za-z0-9]+", words) if x]
    return w[0].lower() + "".join(x.capitalize() for x in w[1:])


def bind(g):
    g.bind("ho", HO); g.bind("hosh", HOSH); g.bind("hov", HOV); g.bind("skos", SKOS)
    g.bind("dcterms", DCTERMS); g.bind("owl", OWL); g.bind("rdfs", RDFS); g.bind("sh", SH)
    for k, v in NS.items():
        g.bind(k, v)


def declare_skos(g):
    """Declare the SKOS terms locally so an OWL editor shows them (alternative: import the W3C SKOS core)."""
    for c in (SKOS.Concept, SKOS.ConceptScheme, SKOS.OrderedCollection):
        g.add((c, RDF.type, OWL.Class))
    for p in (SKOS.prefLabel, SKOS.altLabel, SKOS.definition, SKOS.example, SKOS.scopeNote, SKOS.historyNote,
              SKOS.editorialNote, SKOS.note):
        g.add((p, RDF.type, OWL.AnnotationProperty))
    for p in (SKOS.broader, SKOS.narrower, SKOS.related, SKOS.inScheme, SKOS.memberList, *GRADES.values()):
        g.add((p, RDF.type, OWL.ObjectProperty))
    for p in (DCTERMS.source, DCTERMS.creator, DCTERMS.bibliographicCitation, DCTERMS.references, DCTERMS.title):
        g.add((p, RDF.type, OWL.AnnotationProperty))


def ontology_header(g, ont, title, comment, imports=()):
    g.add((ont, RDF.type, OWL.Ontology))
    g.add((ont, OWL.versionIRI, URIRef(str(ont) + "/0.1")))
    lit(g, ont, DCTERMS.title, title, check=False)
    lit(g, ont, RDFS.comment, comment, check=False)
    lit(g, ont, OWL.versionInfo, "mini example 0.1 (2026-11-18). Not the v3 release.", lang=None, check=False)
    for i in imports:
        g.add((ont, OWL.imports, i))


# ------------------------------------------------------------------ vocabulary
def build_vocab():
    lines = SRC.read_text(encoding="utf-8").splitlines()
    g = Graph(); bind(g); declare_skos(g)
    ontology_header(g, ONT_VOCAB, "Harm Ontology mini example: vocabulary layer (SKOS, hov:)",
                    "Hubs, spokes, discipline schemes and value scales parsed from the vault note 'Vocabulary Crosswalk - "
                    "Concept Hubs and Discipline Schemes' (HO-II.d.2). TEST ARTEFACT: placeholder IRIs; statuses are the "
                    "note's own ('candidate'). Mapping grades are Claude's proposals as reviewed in that note.",
                    imports=[ONT_CORE])
    # custom annotation / object properties
    for name, label in (("explanation", "explanation"), ("explanationProvenance", "explanation provenance"),
                        ("citationVerification", "citation verification"), ("verificationNote", "verification note"),
                        ("keyThinkers", "key thinkers"), ("discipline", "discipline"), ("meaningAsOf", "meaning as of"),
                        ("assertedBy", "asserted by"), ("status", "status"), ("boundaryTests", "boundary tests"),
                        ("glossLine", "gloss line (from the diagram)")):
        g.add((HOV[name], RDF.type, OWL.AnnotationProperty)); lit(g, HOV[name], RDFS.label, label, check=False)
    for name, label in (("documents", "documents"), ("bandsTakenFrom", "bands taken from")):
        g.add((HOV[name], RDF.type, OWL.ObjectProperty)); lit(g, HOV[name], RDFS.label, label, check=False)
    g.add((HOV.SourceQuote, RDF.type, OWL.Class)); lit(g, HOV.SourceQuote, RDFS.label, "source quote (original wording)", check=False)
    g.add((RDF.value, RDF.type, OWL.AnnotationProperty))
    # schemes
    hubs = HOV["hubs"]
    g.add((hubs, RDF.type, SKOS.ConceptScheme)); lit(g, hubs, SKOS.prefLabel, "Concept hubs", check=False)
    for p, label in DISC.items():
        s = NS[p][p + "Scheme"] if False else URIRef(str(NS[p]) + "scheme")
        g.add((s, RDF.type, SKOS.ConceptScheme)); lit(g, s, SKOS.prefLabel, label, check=False)
    scheme = lambda p: URIRef(str(NS[p]) + "scheme")

    # ---- locate the three worked examples
    def sec(start_pat, end_pat):
        a = next(i for i, l in enumerate(lines) if re.match(start_pat, l))
        b = next((i for i in range(a + 1, len(lines)) if re.match(end_pat, lines[i])), len(lines))
        return a, b
    spans = {
        "congruence": sec(r"## Worked example: `hov:congruence`", r"## Worked example"),
        "omission": sec(r"## Worked example: `hov:omission`", r"## Worked example"),
        "developmentalAltitude": sec(r"## Worked example: `hov:developmentalAltitude`", r"## Original wording"),
    }
    gloss = {"congruence": "The fit between what a lens says it does and what it actually does.",
             "omission": "What a lens leaves out of its verdicts.",
             "developmentalAltitude": "How widely and reflectively a lens's values extend concern."}
    summary = {}
    for hub, (a, b) in spans.items():
        sl = lines[a:b]
        hub_iri = HOV[hub]
        g.add((hub_iri, RDF.type, SKOS.Concept)); g.add((hub_iri, SKOS.inScheme, hubs))
        lit(g, hub_iri, SKOS.prefLabel, hub)
        lit(g, hub_iri, HOV.glossLine, gloss[hub])
        # hub table
        rows = table_after(sl, next(i for i, l in enumerate(sl) if l.startswith("### Hub")))
        for r in rows[1:]:
            k, v = r[0], r[1]
            if k == "Scope": lit(g, hub_iri, SKOS.scopeNote, v)
            elif k == "Documents":
                lit(g, hub_iri, HOV.documents if False else SKOS.note, "Documents: " + v)
                m = re.search(r"`ho:(\w+)`", v)
                g.add((hub_iri, HOV.documents, HO[m.group(1)]))
            elif k == "Definition": lit(g, hub_iri, SKOS.definition, v)
            elif k == "Example": lit(g, hub_iri, SKOS.example, v)
            elif k == "Explanation": lit(g, hub_iri, HOV.explanation, v)
            elif k == "Boundary tests": lit(g, hub_iri, HOV.boundaryTests, v)
            elif k == "Status": lit(g, hub_iri, HOV.status, v)
        # spoke tables
        spoke_tables = []
        h = next(i for i, l in enumerate(sl) if l.startswith("### Spokes") or l.startswith("### Branches and spokes"))
        spoke_tables.append(table_after(sl, h))
        for i, l in enumerate(sl):
            if l.startswith("**Added spoke:"):
                spoke_tables.append(table_after(sl, i))
        # explanations
        expl = {}
        for l in sl:
            m = re.match(r"^\*\*`([a-z]+:\w+)`(?: / `[a-z]+:\w+`)?(.*?)\*\*(.*)$", l)
            if m and not l.startswith("**Explanations"):
                sid, rest = m.group(1), m.group(3).strip()
                prov = None
                pm = re.match(r"^\((.*?)\)\.\s*(.*)$", rest)
                if pm: prov, rest = pm.group(1), pm.group(2)
                expl[sid] = (rest, prov)
            elif l.startswith("**Explanation (new draft).**"):
                expl["psy:careStages"] = (l[len("**Explanation (new draft).**"):].strip(), "new draft")
        n_spokes = 0
        for rows in spoke_tables:
            header = rows[0]
            for ci in range(1, len(header)):
                ids = re.findall(r"`([a-z]+:\w+)`", header[ci])
                sid = ids[0]
                s = iri(sid); pref = sid.split(":")[0]
                g.add((s, RDF.type, SKOS.Concept)); g.add((s, SKOS.inScheme, scheme(pref)))
                if len(ids) > 1:
                    lit(g, s, SKOS.editorialNote,
                        f"The source note records this spoke jointly with {ids[1]} as one combined column; kept here as one record under {sid}.")
                f = {r[0]: r[ci] for r in rows[1:] if len(r) > ci}
                grade = reason = None
                for k, v in f.items():
                    if k == "Discipline": lit(g, s, HOV.discipline, v)
                    elif k == "Term (altLabels)":
                        terms = [re.sub(r"\*([^*]+)\*", r"\1", t.strip()) for t in v.split(";") if t.strip()]
                        lit(g, s, SKOS.prefLabel, terms[0])
                        for t in terms: lit(g, s, SKOS.altLabel, t)
                    elif k == "Definition": lit(g, s, SKOS.definition, v)
                    elif k == "Example": lit(g, s, SKOS.example, v)
                    elif k == "Citation": lit(g, s, DCTERMS.bibliographicCitation, v)
                    elif k == "Citation verified": lit(g, s, HOV.citationVerification, v)
                    elif k == "Historical note": lit(g, s, SKOS.historyNote, v)
                    elif k == "Key thinkers": lit(g, s, HOV.keyThinkers, v)
                    elif k.startswith("Scope note"): lit(g, s, SKOS.scopeNote, v)
                    elif k.startswith("meaningAsOf"):
                        a_, b_ = [x.strip() for x in v.split("\u00b7")]
                        lit(g, s, HOV.meaningAsOf, a_); lit(g, s, HOV.assertedBy, b_)
                    elif k.startswith("Grade"):
                        m = re.search(r"\*\*(\w+Match)\*\*", v)
                        grade = m.group(1)
                        reason = v[m.end():].strip()
                        if reason.startswith(":"): reason = reason[1:].strip()
                if sid in expl:
                    text, prov = expl[sid]
                    lit(g, s, HOV.explanation, text)
                    if prov: lit(g, s, HOV.explanationProvenance, prov)
                # mapping from hub (or branch) to spoke
                frm = hub_iri
                if "Maps to" in f:
                    br = f["Maps to"]
                    frm = HOV["outOfFrame" if "outOfFrame" in br else "acceptedHarm" if "acceptedHarm" in br
                              else "negligentBlindSpot" if "negligent" in br else "suppressedBlindSpot"]
                g.add((frm, GRADES[grade], s)); axiom(g, frm, GRADES[grade], s, reason)
                n_spokes += 1
        summary[hub] = n_spokes

    # ---- omission branches (from the diagram in the note)
    br = {"outOfFrame": "excluded by design; not visible to this lens", "blindSpot": "visible but missed",
          "negligentBlindSpot": "should have been seen", "suppressedBlindSpot": "suspected, and deliberately not looked at",
          "acceptedHarm": "seen, and tolerated"}
    for k, d in br.items():
        g.add((HOV[k], RDF.type, SKOS.Concept)); g.add((HOV[k], SKOS.inScheme, hubs))
        lit(g, HOV[k], SKOS.prefLabel, k); lit(g, HOV[k], SKOS.definition, d)
    for c in ("outOfFrame", "blindSpot", "acceptedHarm"): g.add((HOV.omission, SKOS.narrower, HOV[c]))
    for c in ("negligentBlindSpot", "suppressedBlindSpot"): g.add((HOV.blindSpot, SKOS.narrower, HOV[c]))
    # diagram: Wilber's bands taken from Gilligan
    g.add((iri("int:altitude"), HOV.bandsTakenFrom, iri("psy:careStages")))

    # ---- value scales and level mappings (altitude section)
    a, b = spans["developmentalAltitude"]
    sl = lines[a:b]
    levels = {}
    i0 = next(i for i, l in enumerate(sl) if l.startswith("### Value scales"))
    scale_rows = table_after(sl, i0)[1:]
    extra = [cells(l) for l in sl if l.startswith("| `phil:oikeiosisCircles`")]
    for r in scale_rows + extra:
        sc = re.search(r"`([a-z]+:\w+)`", r[0]).group(1)
        pref = sc.split(":")[0]
        sc_iri = iri(sc + ("Scale" if sc == "psy:careStages" else ""))
        g.add((sc_iri, RDF.type, SKOS.ConceptScheme))
        lit(g, sc_iri, SKOS.prefLabel, sc)
        if sc == "psy:careStages":
            lit(g, sc_iri, SKOS.editorialNote, "Scheme IRI has the suffix 'Scale' to avoid clashing with the spoke concept psy:careStages.")
        paren = re.search(r"\((.*)\)", r[1])
        if paren: lit(g, sc_iri, SKOS.note, "Levels note: " + paren.group(1))
        names = [n.strip() for n in re.sub(r"\(.*\)", "", r[1]).split("\u2192") if n.strip()]
        members = []
        for n in names:
            lv = iri(f"{pref}:" + ("circle" + n.capitalize() if sc == "phil:oikeiosisCircles" else camel(n)))
            g.add((lv, RDF.type, SKOS.Concept)); g.add((lv, SKOS.inScheme, sc_iri)); lit(g, lv, SKOS.prefLabel, n)
            members.append(lv); levels[n.lower()] = lv
        coll = URIRef(str(sc_iri) + "Order")
        g.add((coll, RDF.type, SKOS.OrderedCollection)); lit(g, coll, SKOS.prefLabel, sc + " (order, lowest to highest)")
        lst = BNode(); Collection(g, lst, members); g.add((coll, SKOS.memberList, lst))
        lit(g, sc_iri, DCTERMS.source, r[2]); lit(g, sc_iri, HOV.verificationNote, r[3])
    # band <-> stage <-> colour (note's table)
    i1 = next(i for i, l in enumerate(sl) if l.startswith("**Band \u2194 stage"))
    lit(g, URIRef(str(iri("int:moralBands")) + "Order"), SKOS.editorialNote, sl[i1].strip("*"))
    band_rows = [r for r in table_after(sl, i1 + 1)[1:] if len(r) == 3]
    for band, stage, colour in band_rows:
        uncertain = band.endswith("?")
        bn = band.rstrip("?").strip()
        bi = iri("int:" + camel(bn)); prop = SKOS.relatedMatch if uncertain else SKOS.broadMatch
        for cell in (stage, colour):
            for name, lv in levels.items():
                if re.search(r"(?<![A-Za-z\-])" + re.escape(name) + r"(?![A-Za-z\-])", cell.lower()) and \
                        (lv, SKOS.inScheme, None) in g and str(lv).split("#")[0].endswith("/int") and name not in ("care",):
                    if bn not in name and name not in ("egocentric", "ethnocentric", "worldcentric", "kosmocentric"):
                        g.add((lv, prop, bi))
        if uncertain:
            lit(g, bi, SKOS.editorialNote, "Third-tier colours (indigo to white): the source note marks the band 'kosmocentric?' (uncertain; secondary sources only).")
    # proposed value-level mappings
    i2 = next(i for i, l in enumerate(sl) if l.startswith("### Proposed value-level mappings"))
    for fr, gr, to, rs in table_after(sl, i2)[1:]:
        f_id = re.search(r"`([a-z]+:\w+)`", fr).group(1)
        if gr.startswith("("):
            lit(g, iri(f_id), SKOS.editorialNote, f"No match in psy:kohlbergLevels: {rs}")
            continue
        t_id = re.search(r"`([a-z]+:\w+)`", to).group(1)
        for cid in (f_id, t_id):
            if (iri(cid), RDF.type, SKOS.Concept) not in g:
                g.add((iri(cid), RDF.type, SKOS.Concept))
        g.add((iri(f_id), GRADES[gr], iri(t_id))); axiom(g, iri(f_id), GRADES[gr], iri(t_id), rs)

    # ---- original wording (verbatim, with attribution)
    ow = next(i for i, l in enumerate(lines) if l.startswith("## Original wording"))
    block = lines[ow + 1:next(i for i in range(ow + 1, len(lines)) if lines[i].startswith("## "))]
    n = 0; cur = None; session = None
    for l in block:
        if l.startswith("> "):
            n += 1; cur = HOV[f"quote{n:02d}"]
            text = unesc(l[2:].strip())
            if text.startswith('"') and text.endswith('"'): text = text[1:-1]
            g.add((cur, RDF.type, HOV.SourceQuote)); lit(g, cur, RDF.value, text)
            g.add((ONT_VOCAB, DCTERMS.references, cur))
        elif l.startswith("- **Attribution:**") and cur is not None:
            lit(g, cur, DCTERMS.creator, l.split("**Attribution:**")[1].strip())
        elif l.startswith("- **Source:**"):
            session = l.split("**Source:**")[1].strip()
    if session: lit(g, ONT_VOCAB, DCTERMS.source, session, check=False)
    return g, summary, n


# ------------------------------------------------------------------ core, profiles, loader
def build_core(vocab_notes):
    g = Graph(); bind(g); declare_skos(g)
    ontology_header(g, ONT_CORE, "Harm Ontology mini example: ontology layer (OWL, ho:)",
                    "A handful of elements only, to show how the layers tie together. Short definitions are copied from the vault "
                    "(Decisions_Log, Canon_and_Continuity glossary, draft structure, hub 'Documents' fields), with sources. "
                    "Domains and ranges are NOT modelled in this mini example.", imports=[])
    g.add((HO.designStatus, RDF.type, OWL.AnnotationProperty)); lit(g, HO.designStatus, RDFS.label, "design status", check=False)
    g.add((RDFS.seeAlso, RDF.type, OWL.AnnotationProperty))
    g.add((RDFS.comment, RDF.type, OWL.AnnotationProperty)); g.add((RDFS.label, RDF.type, OWL.AnnotationProperty))
    def cls(c, label, comment, status, source, alts=(), pref=None, sub=None):
        g.add((c, RDF.type, OWL.Class)); lit(g, c, RDFS.label, label, check=False)
        if pref: lit(g, c, SKOS.prefLabel, pref, check=False)
        for a_ in alts: lit(g, c, SKOS.altLabel, a_, check=False)
        lit(g, c, SKOS.definition, comment, check=False); lit(g, c, HO.designStatus, status, lang=None, check=False)
        lit(g, c, DCTERMS.source, source, check=False)
        if sub: g.add((c, RDFS.subClassOf, sub))
    cls(HO.Perspective, "Perspective",
        "Abstract umbrella class with no direct members: either a tradition (PerspectiveType) or a perspective specification (PerspectiveSpecification). Carries only a definition and Explanation.",
        "decided", "Canon_and_Continuity glossary; Decisions_Log 2026-11-17")
    cls(HO.PerspectiveType, "PerspectiveType",
        "A reusable way of seeing and judging, with a lineage: Utilitarianism, Tort Law, Public Health, a trained AI model. Subclass of Perspective; prefLabel \"tradition\"; altLabel \"lens\".",
        "decided", "Canon_and_Continuity glossary; Decisions_Log 2026-11-17", alts=("lens",), pref="tradition", sub=HO.Perspective)
    cls(HO.PerspectiveSpecification, "PerspectiveSpecification",
        "Reusable; all properties optional (draft structure). altLabels: \"viewpoint\", \"perspective snapshot\".",
        "decided", "Harm Ontology v3 - Draft Structure; Decisions_Log 2026-11-17", alts=("viewpoint", "perspective snapshot"), sub=HO.Perspective)
    g.add((HO.PerspectiveType, OWL.disjointWith, HO.PerspectiveSpecification))
    cls(HO.Assessment, "Assessment", "one judgment = one instance",
        "decided", "Harm Ontology v3 - Draft Structure; Decisions_Log 2026-11-14")
    g.add((HO.assessedBy, RDF.type, OWL.ObjectProperty)); lit(g, HO.assessedBy, RDFS.label, "assessedBy", check=False)
    lit(g, HO.assessedBy, SKOS.definition, "Referred to in the hub 'Documents' fields; its domain and range are not modelled in this mini example.", check=False)
    for prop, hub in (("congruence", "congruence"), ("omission", "omission"), ("developmentalAltitude", "developmentalAltitude")):
        p = HO[prop]
        g.add((p, RDF.type, OWL.ObjectProperty)); lit(g, p, RDFS.label, prop, check=False)
        lit(g, p, SKOS.definition, vocab_notes[prop], check=False)
        lit(g, p, HO.designStatus, "candidate", lang=None, check=False)
        lit(g, p, DCTERMS.source, "Vocabulary Crosswalk (hub 'Documents' field); status is the hub's own", check=False)
        g.add((p, RDFS.seeAlso, HOV[hub]))
    return g


def build_profiles():
    g = Graph(); bind(g)
    ontology_header(g, ONT_PROF, "Harm Ontology mini example: profiles layer (SHACL, hosh:)",
                    "DEMO shapes only, to show the layer. They check that the vocabulary examples are complete. They are NOT design "
                    "decisions and not the LegalInstitutional / LearnedModel profiles of PerspectiveStructure 0.02.", imports=[ONT_CORE])
    g.add((SH.NodeShape, RDF.type, OWL.Class))
    def shape(s, label, target, needs):
        g.add((s, RDF.type, SH.NodeShape)); lit(g, s, RDFS.label, label, check=False)
        g.add((s, SH.targetSubjectsOf, target))
        for p in needs:
            ps = BNode(); g.add((s, SH.property, ps)); g.add((ps, SH.path, p)); g.add((ps, SH.minCount, Literal(1)))
    shape(HOSH.HubShape, "Hub completeness (demo)", HOV.documents,
          [SKOS.definition, SKOS.example, HOV.explanation, HOV.status, HOV.documents])
    shape(HOSH.SpokeShape, "Spoke completeness (demo)", HOV.assertedBy,
          [SKOS.definition, SKOS.example, DCTERMS.bibliographicCitation, HOV.citationVerification, HOV.meaningAsOf,
           HOV.discipline, SKOS.inScheme, HOV.explanation])
    return g


def build_loader():
    g = Graph(); bind(g)
    ontology_header(g, ONT_ALL, "Harm Ontology mini example: loader",
                    "Open THIS file in Protege. It only imports the three layers: core (OWL), profiles (SHACL), vocabulary (SKOS).",
                    imports=[ONT_CORE, ONT_PROF, ONT_VOCAB])
    return g


def catalog():
    items = "".join(f'  <uri id="User Entered Import Resolution" name="{o}" uri="{f}"/>\n'
                    for o, f in ((ONT_CORE, "ho-core-mini.ttl"), (ONT_PROF, "ho-profiles-mini.ttl"),
                                 (ONT_VOCAB, "ho-vocabulary-mini.ttl"), (ONT_ALL, "ho-all-mini.ttl")))
    return ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
            '<catalog prefer="public" xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">\n' + items + '</catalog>\n')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    vg, summary, nq = build_vocab()
    notes = {}
    for hub in ("congruence", "omission", "developmentalAltitude"):
        for o in vg.objects(HOV[hub], SKOS.note):
            if str(o).startswith("Documents: "):
                notes[hub] = str(o)[len("Documents: "):]
    out = {"ho-core-mini.ttl": build_core(notes), "ho-profiles-mini.ttl": build_profiles(),
           "ho-vocabulary-mini.ttl": vg, "ho-all-mini.ttl": build_loader()}
    for name, g in out.items():
        g.serialize(OUT / name, format="turtle")
    (OUT / "catalog-v001.xml").write_text(catalog(), encoding="utf-8")
    # post-build verbatim check
    g2 = Graph().parse(OUT / "ho-vocabulary-mini.ttl")
    # blank-node ids change on re-parse, so axiom comments are checked by (predicate, text) only
    miss = [(s, p, t[:60]) for s, p, t, lang in EXPECTED
            if not ((None, p, Literal(t, lang=lang)) in g2 if isinstance(s, BNode) else (s, p, Literal(t, lang=lang)) in g2)]
    print("spokes per hub:", summary, "| original-wording quotes:", nq)
    print("carried text fields checked:", len(EXPECTED), "| missing or changed after re-parse:", len(miss))
    for m in miss[:10]:
        print("  MISSING", m)
    for name in out:
        gg = Graph().parse(OUT / name)
        print(f"{name}: {len(gg)} triples")
    return 1 if miss else 0


if __name__ == "__main__":
    sys.exit(main())
