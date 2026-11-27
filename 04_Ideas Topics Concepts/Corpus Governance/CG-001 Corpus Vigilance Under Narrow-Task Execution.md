---
fileClass: Idea
type: idea
status: developing
bookmark: CG-001
canonical_id: cg-001-corpus-vigilance
territory: new
tags: []
aliases: [cg-001-corpus-vigilance_v1, cg-001-corpus-vigilance]
created: 2026-11-08
source: "[[2026-10-15 - 000 — Harm & Guardrails Root Exploration]]"
source_import: Nexus artifact cg-001-corpus-vigilance v1
migrated: 2026-11-10
---

# CG-001 — Corpus Vigilance Under Narrow-Task Execution

Index: [[_Corpus Governance Bookmark Index]]

*Core question: when an editor — human or AI — touches part of a living body of work to accomplish a specific, narrow task, what obligation exists to verify the touched material against current standing conventions, and how far should that obligation reasonably extend?*

- **The touch-scope discipline (the "boy scout rule"):** review what's actually touched against current conventions, not just what the narrow instruction asked for.
  *Worked example:* a skill's frontmatter initially omitted the canonical-identity marker the project had just established as a rule — because the editing process was in task-focused "build mode" and never reflexively checked the artifact being built against the rule it was itself encoding.
- **Bounded blast radius, not whole-corpus audits:** vigilance has to stay cheap enough to actually happen. Re-auditing the entire corpus on every touch would recreate the cost problem the identity-resolution skill's "When NOT to act" section was built to avoid. Reasonable scope: thoroughly check what's directly touched; flag — rather than silently chase — anything adjacent that looks like it may need the same treatment.
- **The false-signal cost of an unmaintained convention:** a marker or rule that's adopted but not reliably upheld is worse than never adopting it, because it trades an honest absence for a false guarantee.
  *Worked example:* an initial decision not to rigorously maintain a skill's version field was corrected immediately after being flagged — specifically because an unreliable version signal is more dangerous than having none.
- **Substrate/portability as its own vigilance dimension, not just an accident of which tool was used:** a document's portability depends on how it was created, not only what it contains. A plain published file is stored as the file itself; a Claude Doc is stored as a structured object (confirmed directly: MIME type `application/vnd.claude.page`, a JSON node tree) and only produces a flat markdown/HTML file on export, not at rest. This went unnoticed until something external actually depended on portability.
  *Worked example:* the original AI Governance & Safety Bookmark Index was created as a Doc, for reasons specific to that moment; everything built afterward defaulted to plain markdown by momentum rather than re-examined choice — producing a corpus with one silently less-portable member. A third-party Obsidian-import tool imported every other file and silently skipped that one. The gap wasn't visible to either human or Claude review; it surfaced only when an external tool actually exercised it. Recovered by exporting the Doc's content directly on request, which works regardless of root cause — but the lesson is upstream of the recovery: creation-method choices have portability consequences that won't show up until something outside the conversation goes looking.
  *Follow-on:* this was closed as a standing rule in the bookmark-index-maintainer skill — always create canonical content as a plain file, never as a Claude Doc, when the environment offers that choice.
- **Cross-reference to 002 (Scalability of Oversight and Control):** this bookmark is the practical, ground-level face of 002's abstract question about trustworthy self-governance — and it contributes a positive counter-example to 002.II.a's usual failure mode (human rubber-stamping/automation bias). The frontmatter gap was *caught* by attentive human oversight, not missed by it. Worth recording as a case of oversight working as intended, not only as a cautionary tale.
