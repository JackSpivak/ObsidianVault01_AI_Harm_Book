---
type: research
status: developing
tags: [ontology/harm, test, nonce, sparql, traversal]
aliases: [Nonce Test Graph Queries, Traversal Queries]
created: 2026-11-25
---

# Nonce Test: Graph Queries (for review)

## Purpose
These are the fixed SPARQL queries for the traversal condition of the next test. They are written before any run, so they can be reviewed. Each query takes a class code as input. The query does the graph work; nothing in it depends on the model's reading.

## Design of the traversal condition
1. The model reads the text and proposes candidate class codes from their definitions. This is the semantic-match step, and it is the same step as in the model-only condition.
2. For each proposed code, a fixed query returns the node's structure and every narrative property attached to that same node (Q2), and its path to the root (Q3).
3. The model decides from the returned rows only.
4. The model-only condition uses the same candidates, but reads the file as text instead of receiving query results. The comparison then isolates what the query adds.

Q1 and Q4 are checks, not part of the decision step. Q1 lists the classes under a parent, so the candidate set can be checked against the full set. Q4 finds nodes that share a definition, which matters if the same text is attached to more than one owner.

## Parameter
`?code` is the class code, for example `harm:H-009` in NONCE files or `harm:HedonicHarm` in the baseline and C2 files. Replace the `VALUES` line for each run.

## Q1. All classes under a parent (transitive)
```sparql
PREFIX harm: <http://example.org/ontology/harm#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?class WHERE {
  VALUES ?parent { harm:Harm }
  ?class rdfs:subClassOf+ ?parent .
} ORDER BY ?class
```

## Q2. Everything on one node: structure, narrative and asserted properties
```sparql
PREFIX harm: <http://example.org/ontology/harm#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcterms: <http://purl.org/dc/terms/>
SELECT ?pred ?value ?valueLabel ?valueDef WHERE {
  VALUES ?code { harm:HedonicHarm }
  ?code ?pred ?value .
  FILTER(?pred != rdf:type)
  OPTIONAL { ?value skos:prefLabel ?valueLabel . }
  OPTIONAL { ?value skos:definition ?valueDef . }
} ORDER BY ?pred ?value
```
This returns every triple on the node, including `skos:definition`, `skos:scopeNote`, `skos:historyNote`, `skos:example`, `skos:note`, `dcterms:bibliographicCitation`, `skos:prefLabel` and `skos:altLabel`, and each asserted value with its own label or definition. Filter by predicate in the model's prompt if a narrower read is wanted, but keep the full result for the record.

## Q3. Path from a node to the root
```sparql
PREFIX harm: <http://example.org/ontology/harm#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?ancestor WHERE {
  VALUES ?code { harm:HedonicHarm }
  ?code rdfs:subClassOf* ?ancestor .
}
```

## Q4. Owners of a shared definition (check only)
```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?def (COUNT(DISTINCT ?node) AS ?owners) WHERE {
  ?node skos:definition ?def .
} GROUP BY ?def HAVING (COUNT(DISTINCT ?node) > 1)
```

## Run check
These queries were run once through rdflib, to confirm they parse and return rows against the baseline and CONTROL C2. The results have not been interpreted.

## Not yet decided
- The expert judgments that the results are scored against. Without them the test measures agreement, not correctness.
- Whether the candidate codes in the traversal condition come from the same model runs as the model-only condition, or from a fixed list. A fixed list keeps the comparison clean.
- Which file to test first. The baseline has full narrative; C2 isolates narrative from labels.
