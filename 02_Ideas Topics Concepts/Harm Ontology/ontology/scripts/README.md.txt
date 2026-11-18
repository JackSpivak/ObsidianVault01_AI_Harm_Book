Harm ontology scripts (moved into the vault 2026-11-18 so they are tracked in git)

Environment: conda env `harm-ontology` (Python 3.12, rdflib, pyshacl)
  C:\Users\conta\anaconda3\envs\harm-ontology\python.exe -I <script> <args>
Run from the vault root. Use `-I` (isolated mode).

toy_status.py <A.ttl> <B.ttl>
  Toy-case runner for HO-002.a. Computes variant B statuses (Settled, Disputed, Corroborated,
  SingleSource, PartiallyAssessed, Incommensurable, NotAssessed), runs the competency questions,
  and prints PASS/FAIL checks with a SUMMARY line. Fictional data only.
  Example (from the vault root):
    python -I "02_Ideas Topics Concepts/Harm Ontology/ontology/scripts/toy_status.py" \
      "02_Ideas Topics Concepts/Harm Ontology/ontology/tests/toy_branch_ledger_A.ttl" \
      "02_Ideas Topics Concepts/Harm Ontology/ontology/tests/toy_branch_ledger_B.ttl"
  Expected at 2026-11-18 (after the chain test and snapshot fix): SUMMARY: 48 passed, 0 failed, of 48 checks.
  The snapshot section is a reader-facing view: legend, Effect labels, observed core, seven plain status words.
  Attribute kinds it understands: graded, non-exclusive (deniesValue / soleValue),
  interval ("YYYY-YYYY" overlap), and single-valued exclusive (subtype and Unclassified aware).

validate_ttl.py <file.ttl>
  Parses a Turtle file and prints counts (triples, classes, object properties, concepts) and
  suspicious IRIs. Used to validate the v1 .ttl.

inventory.py <v1.ttl> <v2a.md> <out.csv>
  Migration Phase 0: one row per element found in the v1 .ttl and the v2a Compendium markdown.
  inventory_v1_v2a.csv is its output.

Notes
- This file is README.md.txt (not .md) so Obsidian does not list it as a note.
- Third-party .ttl downloads (e.g. AIRO, DPV-RISK) stay OUTSIDE the vault in ~/harm-ontology-scripts/.
- The older copy in ~/harm-ontology-scripts/ is now a duplicate; the vault copy is the one to edit.
