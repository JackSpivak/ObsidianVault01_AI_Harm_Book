---
nexus: nexus-ai-chat-importer
plugin_version: "1.8.1"
provider: claude
artifact_id: SKILL
version_uuid: toolu_0132dLUf162H91f4BVqiTnki
version_number: 12
command: update
conversation_id: 64b2a4a8-7f90-4f04-8155-c5e3ef00900b
create_time: 2026-11-08T05:31:00.000Z
format: markdown
aliases: [SKILL, SKILL_v12]
---

# SKILL (Version 12)

**Conversation:** [[07_Imported Chat Test/claude/2026/10/2026-10-15 - 000 — Harm & Guardrails Root Exploration|000 — Harm & Guardrails: Root Exploration]]

## Content

---
name: bookmark-index-maintainer
metadata:
  version: "1.2"
description: Maintains and extends a numbered "bookmark" taxonomy index (e.g. 001, 002, lettered a/b sub-framings, tiered I/II/III structures, standalone -premise tags) that tracks branches of an ongoing exploration. Use this skill whenever a new tension, question, or subtopic comes up that might not fit the existing index, whenever the user asks to bookmark, track, extend, reorganize, or revisit part of a conversation, or whenever it's worth checking if the current taxonomy still holds. Trigger even without the word "bookmark" — phrases like "this feels like its own thing," "where does this fit," "should we track this separately," or the user clearly opening a new line of inquiry within a tracked exploration should all trigger this skill. Also use it proactively, unprompted, when you notice a new branch emerging that the existing index doesn't cover.
---

# Bookmark Index Maintainer

A skill for proposing, placing, and maintaining a numbered reference taxonomy across a long-running, multi-session exploration — without letting the taxonomy calcify into something that constrains new findings rather than describing them.

## Core principle

**The index describes what's been found. It does not gate what's allowed to be found next.**

If a new direction doesn't cleanly fit an existing bookmark, that's a signal the taxonomy needs to flex — not that the finding should be bent to fit. Hold every placement as provisional, and periodically ask, unprompted, whether the existing structure still carves the territory at its real joints.

## When to act

Don't file a new direction into the index silently, and don't ignore it either. When something that might be bookmark-worthy comes up:

1. **Flag it explicitly** in your reply — name what seems new or distinct.
2. **Propose a placement** using the conventions below.
3. **Ask for confirmation** before touching the actual index artifact. Placement is a judgment call; let the user veto or adjust it.
4. Once confirmed, **update the canonical index document** (the actual doc/artifact — not just memory). Memory should track *how to behave*, not serve as the archive of record; the doc is the one source of truth for the structure itself.

## When NOT to act

Noticing a possible new branch or tension is a normal part of following the conversation and costs nothing extra — keep doing that freely and unprompted, as above. This section is specifically about when to spend an actual **resolution step** (a lookup, a grep, a re-read of the canonical document) versus when not to — that step has a real cost, and an unwarranted one is pure overhead, not caution:

- **Don't re-resolve identity to discuss or reference content already in hand within the current task**, where nothing could plausibly have changed it since it was last read.
- **Do re-resolve across a session or meaningful time gap, or in any environment where something other than this exact conversation could have changed the document** — a different session, a different account, a direct edit to the vault, another tool. "Already read it earlier" is not the same guarantee as "still current"; the risk here is staleness from an external change, not merely whether a read has happened. When in doubt whether time or another actor could have intervened, resolve again — it's cheap insurance against the more expensive failure of silently working from a stale copy.
- **Don't trigger the full resolution procedure on a casual mention** of a related word ("harm," "index," "bookmark") that isn't actually about extending, modifying, or verifying the taxonomy.
- **Always resolve before any write** to what might be the canonical document, with no exceptions — an unnecessary read-check only wastes some effort; a write to the wrong file is a real, possibly silent, error.

## Creating or recreating the canonical index

When creating this index for the first time, or recreating it from scratch, in a claude.ai environment: always create it as a plain published artifact (a markdown or HTML file), never as a Claude Doc. A Doc's content is stored as a structured object, not a portable file — it only produces a flat file on export, not at rest — which undermines the cross-environment, cross-account portability this system depends on. This is not a hypothetical concern: an early version of this project's index was created as a Doc, and a third-party import tool later silently failed to find it among otherwise-portable files — the gap surfaced only once something external actually depended on portability, not during normal use. In a filesystem context (e.g. Obsidian), this specific choice doesn't arise — every note is inherently a plain file — but the underlying principle still applies: don't let canonical content live only in a format that requires an explicit export step to become portable.

## Idea and topic pages

### Creating a bookmark: the stub page

Every confirmed bookmark gets a page immediately — never left page-less, and never left as a placeholder whose content has to be invented later. The required content is already produced by the placement step itself: a bookmark can't legitimately be proposed without already being able to say why it's distinct and where it's headed, so writing the stub is recording that justification, not inventing new content on top of it.

Stub frontmatter and structure:

```
---
canonical_id: <unique slug>
type: idea
status: stub
bookmark: <e.g. CG-002>
territory: new            # new | revisited
revisits: [[<page>]]      # present only if territory: revisited
created: <date>
---

# <Title>

## Why this is distinct
<1-2 sentences>

## Anticipated direction
<what this branch is expected to develop into>

## Conceptual territory
<new ground, or previously-entered territory approached differently — and how>
```

Status moves from `stub` toward more developed values as the page grows, tracked only in the page's own frontmatter — never duplicated as a second field in the index. A hand-maintained copy of a fact that already lives on the page it describes is the same two-copies-drift problem this whole pattern exists to avoid. If the index should show status at a glance, that's a live query (e.g. Dataview) over each page's frontmatter, not a second, separately-maintained source of truth.

### Dedup before creating

Before creating a new idea or topic page, check whether one already exists for the same concept — same discipline as locating the index itself: exact match on `canonical_id` or a sufficiently distinctive title, never semantic/similarity search for this purpose, ask on ambiguity rather than guessing or silently duplicating. If an existing page covers the same ground from a different angle, prefer linking to it via `revisits` over creating a near-duplicate.

## Locating the canonical index

This skill is written to be portable across accounts, so it deliberately does not hard-code a document path, URL, or folder location. Baking in a specific address would defeat portability and recreate the exact lock-in problem the index itself is meant to avoid: the moment the document moves, gets renamed, gets recreated, or ends up in a different project, a hardcoded reference breaks silently and nobody notices until it's wrong.

Instead, find it each time by a **recognizable identifying pattern**, not a fixed address:

1. **On claude.ai:** use the Artifact tool's list action and match by title (e.g., containing "Bookmark Index," or whatever name the user has established in this context).
2. **In a filesystem context (e.g. an Obsidian vault via Claude Code):** the canonical document carries a unique marker in its own YAML frontmatter — a block of `key: value` pairs between two `---` lines at the very top of the file, e.g. `canonical_id: <a unique slug or generated id>`. Find it with an **exact** search (e.g. `grep -rl "canonical_id: <value>"`), not a title search and not a semantic/vector-similarity search, even if one is available in the environment. A semantic or vector-search tool answers "what content is relevant to this topic" with ranked, probabilistic matches — useful for searching across a large body of content, but not a reliable way to resolve the identity of one specific canonical document, where an exact, deterministic match is required. Keep these two jobs separate even when one tool happens to be capable of both.
3. Exactly one match → use it.
4. No match, or more than one plausible match (e.g., an old version alongside a newer one, or a missing/duplicated marker) → say so explicitly and ask the user which is canonical. Don't guess silently.
5. When creating a new canonical marker, choose a sufficiently distinctive value (not a generic word like "index") — the multiple-match check above is a safety net for collisions, not a substitute for a reasonably unique value in the first place.
6. Don't cache the resolved location in a separate memory system. The frontmatter marker (or, on claude.ai, the artifact itself) is the single source of truth; a second stored copy of the same pointer is itself a thing that can drift out of sync and shouldn't exist. Re-resolve each time the skill triggers — it's cheap, and it's what keeps the skill genuinely location-agnostic.

### Multiple indices: folder scope

More than one project/book folder may each have its own index, maintained by this same skill — not a separate skill per folder. Scope resolution to the relevant folder first (the folder does most of the disambiguation on its own), then apply identity-marker resolution within that scope, so a same-named index in a different folder is never mistaken for the one in play.

### Wikilinks and re-verification

Link to pages with real `[[wikilinks]]`, not descriptive text alone. Obsidian updates wikilinks automatically when a file is renamed from inside the app — but a rename or move performed directly on disk (e.g. by Claude Code) bypasses that mechanism, and links can go stale silently. Treat a linked page the same way the index itself is treated: re-resolve by its `canonical_id` rather than trusting a stored link blindly, especially after anything outside Obsidian's own UI has touched the file.

## Placement conventions

Decide which shape a new item takes by asking what its relationship is to what already exists:

- **New top-level number** (e.g. 003) — when a genuinely new root-level question emerges that isn't a direct descendant of an existing bookmark. It stands on its own, the way 001 (existential safety) and 002 (scalability of oversight) are independent of each other.

- **Lettered a/b sub-framing** — when two (or more) framings of the *same* question are in real tension, each a coherent alternative to the other, with neither clearly subordinate.
  *Worked example:* 001a (foundational-tradeoff framing) and 001b (extinction-level framing) are peers — both legitimate readings of "what does existential mean here," genuinely in tension, neither upstream of the other.

- **Tiered I/II/III (with a/b within each tier)** — when a bookmark's subtopics are *not* peers: some are upstream and would make the others moot if severe, some are operationally live regardless of how the upstream ones resolve, and some are institutional/meta (governance of the governance layer). Flat lettering would lose that upstream/downstream relationship, so use tiers instead.
  *Worked example:* 002 uses 002.I (structural defeaters — would make the rest "damage control, not solution" if severe), 002.II (operational gaps — live regardless), 002.III (institutional/meta — one level removed), each with internal a/b items.

- **Standalone "-premise" tag** — when there's a testable, load-bearing assumption that multiple sub-items quietly depend on. Keep it visible as its own tag rather than burying it as just another numbered item, specifically because its truth or falsity would change how much weight the dependent items deserve.
  *Worked example:* 002-premise — "verification is easier than generation" — several of 002's tiers depend on this holding, and it's periodically worth re-checking rather than assuming.

- **Not bookmark-worthy** — a clarifying question, a request for an example, or a tangent that resolves within a few exchanges usually doesn't need a number. Use judgment; not everything needs to be filed.

## The anti-lock-in check

Periodically — not on every turn, but when it's been a while or when a placement feels forced — ask explicitly whether the existing structure still holds, rather than waiting to be asked. This is the same correlated-error concern the taxonomy itself may be tracking (self-evaluation sharing structure with what it evaluates) applied reflexively to the indexing process: a taxonomy that only ever gets added to, never questioned, risks the same kind of quiet bias it may have been built to study.

## Cross-referencing

When a new or existing item has a real dependency on another (e.g., "if X turns out to be severe, it's a plausible path into the failure Y is concerned with"), say so explicitly in the index rather than leaving bookmarks as isolated silos. Connections between branches are often as important as the branches themselves.
