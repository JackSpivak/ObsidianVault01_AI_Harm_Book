---
canonical_id: master-bookmark-index
type: index
status: developing
tags: [index/master]
aliases: [Index of Indices]
created: 2026-11-10
---

# Master Bookmark Index

*Lists every bookmark index in the vault: indices only, never individual bookmarks. Each index stays the single source of truth for its own entries.* The bookmark-index-maintainer skill uses this list to route ideas to the right index.

## Indices

- [[GSH Bookmark Index|Global Structural Harm]]: **live**
	- `canonical_id: gsh-bookmark-index` · prefix `GSH-`
	- Scope: AI harm in global structural domains (wealth, hunger, war, child labor) and cases that cut across them.
- [[ai-governance-safety-bookmark-index_v1|AI Governance & Safety]]: **import-only**
	- `canonical_id: ai-governance-safety-index` · prefix: plain numbers (`000`, `001`, `002`)
	- Scope: the harm taxonomy, existential safety, scalability of oversight and control.
	- Only a Nexus import copy exists, in `00_Claude_Admin/Nexus Attachment Imports/`. Its `canonical_id` sits inside the import wrapper, not in the file's own frontmatter. It needs a proper canonical home before routing to it is reliable.
- **Corpus Governance**: **planned / not found**
	- prefix `CG-`
	- Scope: the architecture, conventions and governance of this body of work itself (according to the AI Governance & Safety index).
	- No index file found in the vault. Only an imported page, `cg-001-corpus-vigilance_v1`, exists. This is a natural home for 4a process and rule insights about the corpus.

## Summary
The master index was created so the routing check in bookmark-index-maintainer v1.3 has one place to find all indices.

## Original wording
- **Claude (Opus 5.5, claude-opus-5-5):** "**An index of indices.** There's no \"master index\" listing GSH, AI Governance & Safety and any future ones."
- **User:** "yes.  go ahead with all of this and i like your proposal to not use callouts or html details. please dont"
- **Source:** Obsidian Copilot agent session "new junk conversation test bookmarking", 2026-11-10 — [[agent__new_junk_conversation_test_bookmarking@20261109_143045]].
