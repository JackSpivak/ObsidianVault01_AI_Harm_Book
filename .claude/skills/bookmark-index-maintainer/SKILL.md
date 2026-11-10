---
name: bookmark-index-maintainer
metadata:
  version: "1.3"
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

### Master index (index of indices)

Keep one master index that lists every bookmark index, identified by `canonical_id: master-bookmark-index`. It holds, for each index: a wikilink, its `canonical_id`, its ID prefix (e.g. `GSH-`), a one-line scope, and its status (live / import-only / planned). It is the lookup table the routing check uses to find "a different existing index."

- Resolve it like any canonical document: exact `canonical_id` match, ask on zero or multiple matches.
- When a new index is created, offer to register it in the master index in the same step.
- The master index lists indices only — never individual bookmarks. Each index remains the single source of truth for its own entries.

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

- **Deeper levels** — when a tier item itself branches, extend the same pattern one level down with numbers: `002.I.a.1`, `002.I.a.2`. Apply the same test at every level (peers in tension → letters; upstream/downstream → tiers; independent → numbers). If an item needs more than four levels, that's a signal it may deserve its own top-level bookmark or its own index — raise it rather than nesting further.

- **Not bookmark-worthy** — a clarifying question, a request for an example, or a tangent that resolves within a few exchanges usually doesn't need a number. Use judgment; not everything needs to be filed. Before deciding, run the routing check below — "not here" is not the same as "nowhere."

## Routing: right idea, wrong index

Before placing a possible branch, ask *which* index it belongs to, not just *where* in the current one. Classify by **where the idea should end up**, not by what it's about:

1. **Fits the current index** — place it here per the conventions above.
2. **Fits a different existing index** — say so briefly, name that index (resolved via the master index and its `canonical_id`), and offer to add a stub there with `originated_in:` pointing back to the source conversation. Don't add a branch here.
3. **Worthy, but no index fits** — propose a new conversation and a new index, with this idea as its first entry, and offer to register it in the master index.
4. **Not a topic idea** — don't bookmark it in any index, even if it uses bookmark/index vocabulary. Then ask whether it changes *how we work*:
   - **a. Yes — a process or rule insight** (e.g. "why did you miss this?" yielding a better research rule): offer to record it where it governs behavior — `CLAUDE.md` / `.claude/rules/`, the relevant skill file, `Decisions_Log.md`, or memory.
   - **b. No — housekeeping or a quick clarification**: no record needed.

In every case, ask before writing to any index or rule file — especially one outside the current conversation. Keep the routing note to one short line per idea; don't repeat it.

## Index format (filesystem / Obsidian)

Render the hierarchy so it's collapsible and every entry is a clickable `[[wikilink]]`:

- **Headings (H2/H3)** for major sections of the index (e.g. bookmarks, premises, cross-references).
- **Nested bullet lists** for the bookmark hierarchy itself — one indent level per taxonomy level. Each item: `[[page|ID — short title]]` followed by a one-line description. Obsidian folds nested list items natively, so each branch can be opened or closed.
- An item may appear under more than one parent when it genuinely depends on both (e.g. a case under two domains) — mark the secondary appearance with "(also under …)" so the duplication is visibly deliberate.
- **Do not use callouts or HTML `<details>`** for the hierarchy. Callouts nest poorly and reset their fold state; wikilinks inside HTML blocks generally don't render as links in Obsidian.

## The anti-lock-in check

Periodically — not on every turn, but when it's been a while or when a placement feels forced — ask explicitly whether the existing structure still holds, rather than waiting to be asked. This is the same correlated-error concern the taxonomy itself may be tracking (self-evaluation sharing structure with what it evaluates) applied reflexively to the indexing process: a taxonomy that only ever gets added to, never questioned, risks the same kind of quiet bias it may have been built to study.

## Cross-referencing

When a new or existing item has a real dependency on another (e.g., "if X turns out to be severe, it's a plausible path into the failure Y is concerned with"), say so explicitly in the index rather than leaving bookmarks as isolated silos. Connections between branches are often as important as the branches themselves.
