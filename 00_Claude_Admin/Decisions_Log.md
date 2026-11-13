---
type: admin
status: developing
tags: [admin]
---

# Decisions Log

Settled decisions, newest first. Re-open only deliberately.

| Date | Decision | Why | Related |
|---|---|---|---|
| 2026-11-13 | **Note shape has three separate axes, each recorded in one place:** kind = `type` (one template per kind); maturity = `status` (`stub → seed → developing → stable → archived`); filing state = `bookmark` (`draft` / `ready` / index ID) plus folder. The `Idea Stub` template is retired. Stubs and full ideas both use the single [[Idea]] template; a stub is `type: idea`, `status: stub`, with only a sentence or two filled in. | A stub is "a place holder for a thought or direction that is not yet developed", while full ideas need the full template. Separate templates mixed maturity up with kind. | [[Idea]] template; bookmark-index-maintainer skill |
| 2026-11-13 | **One filing process for all idea notes.** New ideas, stub or full, go in `02_Ideas Topics Concepts/_Unfiled Ideas/` with `bookmark: draft` and are filed into a bookmark index by the skill. Filing never downgrades `status`. | Author: "i think full ideas should go through the filing process too." Developed ideas belong on the same map as stubs. | bookmark-index-maintainer skill |
| 2026-11-13 | **Keep the name "bookmark" for now** despite the clash with Obsidian's core Bookmarks plugin (a sidebar pin list). Markdown indices plus frontmatter stay the source of truth, and the Bookmarks plugin is not part of the process. Bases views are to be trialled for the live inventory and status lists. A rename can be revisited later. | The Bookmarks plugin covers only navigation, not IDs, reasoning, status or filing. Bases can generate status lists without hand-kept copies. | [[_Master Bookmark Index]] |
| 2026-11-05 | Characters may carry complex or frightening **fictional** legal circumstances (new "Legal and shadow circumstances" section). These are built from archetypes and patterns only, never from a real person's actual case, parties, court, dates or allegations. | Author: "include the possible existance of complex or even frightening legal circumstances in the character's perssonaality structure while maintaining a boundary... for the actual identifiable details of a research target's backiground" | [[Character]] template |
| 2026-11-05 | Character development uses **real-world reference profiles**: run `/deep_person_research` on 2–4 people with similar backgrounds, save the factual findings as research notes, then draft Vision, Desires/wants/needs, Fears, Values and Superpowers in the character note. Each item is tagged [canon], [inferred: Source] or [imagined], and only [canon] items go into `Canon_and_Continuity.md`. | Author wants to "infer/imagine/develop/hallucinate personality attributes" from people with similar background, profession, culture and geography, while keeping real people's research factual. | [[Character]] template |
