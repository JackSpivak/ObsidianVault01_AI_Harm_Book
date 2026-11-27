"""Inventory of v1 (.ttl) and v2a (Compendium markdown) elements for the v3 crosswalk.

Usage: python -I inventory.py <v1.ttl> <v2a.md> <out.csv>

One row per element: iri, kind (class / property / value), parent, section,
in_v1, in_v2a, v2a_line, prefLabel, annotation fields present.
"""
import csv
import re
import sys

from rdflib import Graph, Namespace, RDF, RDFS, OWL
from rdflib.namespace import SKOS, DCTERMS

HARM = Namespace("http://example.org/ontology/harm#")
ANNOS = [SKOS.prefLabel, SKOS.altLabel, SKOS.definition, SKOS.note, SKOS.scopeNote,
         SKOS.example, SKOS.historyNote, DCTERMS.bibliographicCitation]


def short(u):
    return "harm:" + str(u).split("#")[-1]


def load_v1(path):
    g = Graph().parse(path, format="turtle")
    rows = {}
    for s in set(g.subjects()):
        if not str(s).startswith(str(HARM)):
            continue
        types = set(g.objects(s, RDF.type))
        if OWL.ObjectProperty in types:
            kind = "property"
        elif OWL.Class in types and SKOS.ConceptScheme in types:
            kind = "value-scheme"
        elif OWL.Class in types:
            kind = "class"
        else:
            kind = "value"
        parent = next(g.objects(s, RDFS.subClassOf), None) or next(
            (t for t in types if str(t).startswith(str(HARM))), None)
        label = next(g.objects(s, SKOS.prefLabel), "")
        annos = ";".join(a.split("#")[-1].split("/")[-1] for a in map(str, ANNOS)
                         if (s, ANNOS[[str(x) for x in ANNOS].index(a)], None) in g)
        rows[short(s)] = dict(iri=short(s), kind=kind,
                              parent=short(parent) if parent else "",
                              section="", in_v1="yes", in_v2a="", v2a_line="",
                              prefLabel=str(label), v1_annotations=annos)
    return rows


CLASS_H = re.compile(r"^#{3,4} .*?`(harm:\w+)`(?:.*?rdfs:subClassOf (harm:\w+))?")
PROP_L = re.compile(r"^\s*(?:\d+|B\d+)?\.?\s*\*\*`(harm:has\w+)`")
TABLE_P = re.compile(r"^\| (B\d+) \| `(harm:\w+)`")
VALUE = re.compile(r"`(harm:[A-Z]\w+)`")


def load_v2a(path, rows):
    section, cur_prop = "", None
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            if line.startswith("## ") or line.startswith("# Part") or line.startswith("### Domain") \
                    or line.startswith("### Meta-Category"):
                section = line.strip("# \n")[:60]
            m = CLASS_H.match(line)
            if m and not m.group(1).startswith("harm:has"):
                _add(rows, m.group(1), "class", m.group(2) or "", section, n)
                cur_prop = None
                continue
            m = PROP_L.match(line) or TABLE_P.match(line)
            if m:
                iri = m.group(m.lastindex)
                _add(rows, iri, "property", "", section, n)
                cur_prop = iri
                # benefit-side table rows list their values in the same line
                if line.startswith("|"):
                    for v in VALUE.findall(line.split("|")[3] if line.count("|") > 4 else ""):
                        _add(rows, v, "value", iri, section, n)
                continue
            if cur_prop and ("Definition:" in line or "added value" in line):
                for v in VALUE.findall(line):
                    if v not in rows or rows[v]["kind"] == "value":
                        _add(rows, v, "value", cur_prop, section, n)
    return rows


def _add(rows, iri, kind, parent, section, n):
    r = rows.setdefault(iri, dict(iri=iri, kind=kind, parent=parent, section="", in_v1="",
                                  in_v2a="", v2a_line="", prefLabel="", v1_annotations=""))
    r["in_v2a"] = "yes"
    r["section"] = r["section"] or section
    r["v2a_line"] = r["v2a_line"] or str(n)
    r["parent"] = r["parent"] or parent


def main(v1, v2a, out):
    rows = load_v2a(v2a, load_v1(v1))
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(next(iter(rows.values())).keys()))
        w.writeheader()
        for r in sorted(rows.values(), key=lambda r: (r["kind"], int(r["v2a_line"] or 99999))):
            w.writerow(r)
    from collections import Counter
    c = Counter((r["kind"], bool(r["in_v1"]), bool(r["in_v2a"])) for r in rows.values())
    print(f"{len(rows)} elements -> {out}")
    for (k, a, b), n in sorted(c.items()):
        print(f"  {k:13} v1={'Y' if a else '-'} v2a={'Y' if b else '-'}  {n}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
