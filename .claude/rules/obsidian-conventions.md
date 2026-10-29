# Obsidian conventions

## Linking
- Use wikilinks: `[[Note Name]]`, `[[Note Name|display text]]`, `[[Note Name#Heading]]`.
- Link the first meaningful mention of a character, place, concept, or source in a note — not every mention.
- Before creating a link, check whether the target note exists (including aliases). Prefer linking to an existing note over creating a near-duplicate.
- Unresolved links are allowed as intentional "notes to write later," but list any you create in your response.
- Never use bare file paths or markdown `[text](file.md)` links for internal notes.

## Frontmatter (properties)
Every new note starts with YAML frontmatter:

```yaml
---
type: character | location | concept | research | chapter | scene | outline | session | idea
status: seed | developing | stable | archived
tags: []
aliases: []
created: YYYY-MM-DD
---
```

- Keep tags few and structural (e.g. `theme/surveillance`, `harm/bias`); use links, not tags, for specific entities.
- Add `aliases` for alternate names so links resolve.

## Formatting
- One H1 per note matching the note's purpose; H2/H3 for sections.
- Short paragraphs and bullet lists in reference notes; manuscript notes are prose only.
- Use callouts for meta-commentary: `> [!todo]`, `> [!question]`, `> [!warning] Continuity`.
- Use footnotes or a `## Sources` section for citations in research notes.

## Right level of notes (atomicity)
- One note per entity (character, place, concept, source). Split a note when it covers two things that get linked separately.
- Don't create a note for something mentioned once with no further use — keep it inline until it earns its own note.
- Merge notes that duplicate each other; propose merges, don't do them unasked.
- Prefer updating an existing note over creating a new one.
- Session/brainstorm notes go in `01_The Writer's Room/`; promote durable conclusions into the proper folder and link back.

## File naming
- Human-readable titles with spaces (e.g. `Dr Mira Okafor.md`), no dates in entity notes.
- Session notes: `YYYY-MM-DD Topic.md`.
- Manuscript: `Ch01 Title.md`, scenes `Ch01-S01 Title.md`.
- Use templates from `00_Claude_Admin/Templates/` when creating notes of those types.
