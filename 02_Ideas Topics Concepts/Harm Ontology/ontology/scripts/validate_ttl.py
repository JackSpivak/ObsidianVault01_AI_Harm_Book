import sys
from rdflib import Graph, RDF, OWL, URIRef
from rdflib.namespace import SKOS
g = Graph()
g.parse(sys.argv[1], format="turtle")
print("triples:", len(g))
print("owl:Class:", len(set(g.subjects(RDF.type, OWL.Class))))
print("owl:ObjectProperty:", len(set(g.subjects(RDF.type, OWL.ObjectProperty))))
print("skos:Concept:", len(set(g.subjects(RDF.type, SKOS.Concept))))
print("ontologies:", list(g.subjects(RDF.type, OWL.Ontology)))
ns = set(str(n) for _, n in g.namespaces())
bad = [str(o) for s,p,o in g if isinstance(o, URIRef) and str(o).startswith(("http://w3.org","http://purl.org/" ))and "dc/terms" not in str(o)]
print("suspicious IRIs:", bad[:5])
