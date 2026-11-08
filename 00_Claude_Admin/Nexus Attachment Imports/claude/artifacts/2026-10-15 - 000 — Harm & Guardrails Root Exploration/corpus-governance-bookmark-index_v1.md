---
nexus: nexus-ai-chat-importer
plugin_version: "1.8.1"
provider: claude
artifact_id: corpus-governance-bookmark-index
version_uuid: toolu_013GtePwFSdvt3kE7HvtrUYm
version_number: 1
command: create
conversation_id: 64b2a4a8-7f90-4f04-8155-c5e3ef00900b
create_time: 2026-11-07T19:54:04.000Z
format: markdown
aliases: [corpus-governance-bookmark-index, corpus-governance-bookmark-index_v1]
---

# corpus-governance-bookmark-index (Version 1)

**Conversation:** [[07_Imported Chat Test/claude/2026/10/2026-10-15 - 000 — Harm & Guardrails Root Exploration|000 — Harm & Guardrails: Root Exploration]]

## Content

# Corpus Governance — Bookmark Index

*A sibling taxonomy to the "AI Governance & Safety — Bookmark Index," tracking the architecture, structure, conventions, and governance of how this body of work is built and maintained — distinct from, but cross-referenced with, the substantive AI-harm/governance content it emerged from. Kept separate specifically because its scope is domain-general: it applies to any collaborative documentation effort (including the Obsidian book-vault project), not only to this one.*

## CG-000 — Root

This bookmark set originated inside the AI-harm exploration (chat "000"), at the point where the conversation's own documentation process became its own subject of scrutiny. Whether this territory moves into its own dedicated chat and/or project is an open, related decision — see the project-organization-and-conventions doc for the current recommendation.

## CG-001 — Corpus Vigilance Under Narrow-Task Execution

*Core question: when an editor — human or AI — touches part of a living body of work to accomplish a specific, narrow task, what obligation exists to verify the touched material against current standing conventions, and how far should that obligation reasonably extend?*

- **The touch-scope discipline (the "boy scout rule"):** review what's actually touched against current conventions, not just what the narrow instruction asked for.
  *Worked example:* a skill's frontmatter initially omitted the canonical-identity marker the project had just established as a rule — because the editing process was in task-focused "build mode" and never reflexively checked the artifact being built against the rule it was itself encoding.
- **Bounded blast radius, not whole-corpus audits:** vigilance has to stay cheap enough to actually happen. Re-auditing the entire corpus on every touch would recreate the cost problem the identity-resolution skill's "When NOT to act" section was built to avoid. Reasonable scope: thoroughly check what's directly touched; flag — rather than silently chase — anything adjacent that looks like it may need the same treatment.
- **The false-signal cost of an unmaintained convention:** a marker or rule that's adopted but not reliably upheld is worse than never adopting it, because it trades an honest absence for a false guarantee.
  *Worked example:* an initial decision not to rigorously maintain a skill's version field was corrected immediately after being flagged — specifically because an unreliable version signal is more dangerous than having none.
- **Cross-reference to 002 (Scalability of Oversight and Control):** this bookmark is the practical, ground-level face of 002's abstract question about trustworthy self-governance — and it contributes a positive counter-example to 002.II.a's usual failure mode (human rubber-stamping/automation bias). The frontmatter gap was *caught* by attentive human oversight, not missed by it. Worth recording as a case of oversight working as intended, not only as a cautionary tale.

## Notes

- This index grows alongside its sibling, the AI Governance & Safety — Bookmark Index, but is kept as a separate document rather than folded into it.
- Future candidates for this index: any further editorial/process conventions that emerge from maintaining either taxonomy, the Obsidian/git port itself, and tooling decisions (like the bookmark-index-maintainer skill) as they evolve.
