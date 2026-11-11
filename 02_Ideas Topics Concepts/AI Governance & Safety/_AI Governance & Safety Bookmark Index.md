---
canonical_id: ai-governance-safety-index
type: index
status: developing
tags: [index/bookmarks]
aliases: [AI Governance & Safety Bookmark Index, AI Governance & Safety Index, AIGS Index]
created: 2026-11-10
---

# AI Governance & Safety — Bookmark Index

*A living table of contents for an ongoing exploration of harm, safeguards and AI governance. It describes what has been found. It doesn't limit what can be found next.* Maintained under the bookmark-index-maintainer rules (`.claude/skills/bookmark-index-maintainer/SKILL.md`). Registered in the [[_Master Bookmark Index]].

This is the canonical copy. It replaces the Nexus import [[ai-governance-safety-bookmark-index_v1]]. The bookmark pages were migrated out of the Nexus imports on 2026-11-10 and live in this folder. Sub-items link to block IDs within them (e.g. `#^002-I-a`).

## Bookmarks
Click the arrow beside an item to open or close its branch.

- [[000 Harm & Guardrails Root Exploration|000 — Harm & Guardrails: Root Exploration]]: the harm taxonomy (physical, psychological, economic, reputational, environmental, social/structural, informational, self-regarding), Mill's harm principle, legal harm, the *Gift of the Magi* case study, AI's own capacity for harm. Source chat: [[2026-10-15 - 000 — Harm & Guardrails Root Exploration]].
	- [[001 Existential Safety Question|001 — Existential safety question]]: is "existential" risk a permanent foundational tradeoff, or an extinction-level technical risk? The two can call for *opposite* governance. Revisits 000 from a new angle.
		- [[001 Existential Safety Question#^001a|001a — Foundational-tradeoff framing]]: no guardrail setting is harm-free; governance should be iterative, correctable, transparent, decentralized.
		- [[001 Existential Safety Question#^001b|001b — Extinction-level framing]]: irreversible failure modes; governance should be precautionary and gated at the frontier.
	- [[002 Scalability of Oversight and Control|002 — Scalability of oversight and control]]: can AI safely take part in its own safety governance, or is that an unresolvable conflict of interest?
		- [[002 Scalability of Oversight and Control#^002-I|002.I — Structural defeaters]] *(upstream: if severe, the rest is damage control)*
			- [[002 Scalability of Oversight and Control#^002-I-a|002.I.a — Deceptive alignment / mesa-optimization]]
			- [[002 Scalability of Oversight and Control#^002-I-b|002.I.b — Multi-agent collusion / correlated blind spots]]
		- [[002 Scalability of Oversight and Control#^002-II|002.II — Operational gaps]] *(live regardless of Tier I)*
			- [[002 Scalability of Oversight and Control#^002-II-a|002.II.a — Human rubber-stamping / automation bias]]
			- [[002 Scalability of Oversight and Control#^002-II-b|002.II.b — Corrigibility]]
		- [[002 Scalability of Oversight and Control#^002-III|002.III — Institutional/meta]] *(governance of the governance layer)*
			- [[002 Scalability of Oversight and Control#^002-III-a|002.III.a — Who oversees the oversight infrastructure]]
			- [[002 Scalability of Oversight and Control#^002-III-b|002.III.b — Incentives of the oversight-research ecosystem]]
	- [[003 Harm Ontology from Outlines|003 — Harm ontology from outlines]]: formalize the 000 harm taxonomy as RDF/OWL/SHACL, generated from markdown outlines and YAML properties. Filed from a manual note, 2026-11-10.

## Premises
- [[002 Scalability of Oversight and Control#^002-premise|002-premise]]: **"Verification is easier than generation."** True for maths and code; unproven for value judgments and long-horizon consequences. Several Tier II and III approaches, debate especially, depend on it. Re-check it periodically.

## Open candidates
- **Scalable alignment vs scalable oversight.** Marked in 002 as "adjacent territory, not yet absorbed into the tiers." It could become 002.IV or a new bookmark. Not yet placed.

## Cross-references
- **001 and 002.II.a:** nominal human authority isn't the same as authority meaningfully exercised (001's autonomy/paternalism thread).
- **002 and [[_GSH Bookmark Index|GSH-001]]:** concentration of control links to [[GSH-001 Global Wealth Distribution]] in the Global Structural Harm index.
- **002 and [[_Corpus Governance Bookmark Index|CG-001]]:** CG-001 is the ground-level face of 002, and a counter-example to 002.II.a: a gap that attentive human oversight caught.
- **003 and [[_Corpus Governance Bookmark Index|Corpus Governance]]:** the tooling side of 003 (reading markdown outlines, storing properties in YAML) is a vault-convention question. Any answer would become a corpus-wide rule.

## Summary
The original index was created in the claude.ai "000" conversation and imported through Nexus. It predates bookmark-index-maintainer v1.3. This canonical copy was rebuilt on 2026-11-10 after an audit:
- real frontmatter
- a nested, collapsible hierarchy with links to sub-items
- the premise and open candidates listed separately
- wikilinked cross-references, including a two-way GSH link

## Original wording
- **User:** "can we audit # AI Governance & Safety — Bookmark Index ?  And update if needed. looks like it was created before current version skill"
- **User:** "yes" (approving the proposed fix: a canonical index outside the imports folder, the import copy marked superseded, and Corpus Governance included)
- **Source:** Obsidian Copilot agent session "new junk conversation test bookmarking", 2026-11-10 — [[agent__new_junk_conversation_test_bookmarking@20261109_143045]].
- **External references:** the original import, [[ai-governance-safety-bookmark-index_v1]], and the bookmark pages linked above.
