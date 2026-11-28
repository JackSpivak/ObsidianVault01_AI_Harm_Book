---
fileClass: Idea
type: idea
status: seed
bookmark: draft
canonical_id:
territory: new
tags:
  - test-case
  - corpus/literature
  - corpus/legal
aliases:
  - Harm test sets
  - Lyrics and literature as harm tests
created: 2026-11-27
---

# Test Case Corpus for Harm Detection

## Why this is distinct
- It collects a broad, deliberately mixed set of sources (legal, insurance, domestic, literary, musical, idiomatic) to test the ontology. It differs from [[HO-002 Ontology Stress-Test Suite]], which is built around cases chosen for philosophical traps. This corpus is chosen for coverage of how harm is actually spoken about.

## Anticipated direction
- Group test sources into tiers: formal (legal and regulatory), institutional (insurance claims), domestic (children, bedtime stories), literary (war, gang violence, system failure), and vernacular (lyrics and idiom).
- Run each source through the ontology and log what it detects, what it misses, and what it classifies wrongly.

## Conceptual territory
- Complements [[HO-002 Ontology Stress-Test Suite]] and [[Dreams and Mischief - Boundary Tests of Harm]].
- Uses the same procedure as [[Diagnostic Model of Harm Assessment]].

## Summary
- Formal sources: the Dodd-Frank Wall Street Reform and Consumer Protection Act of 2010 (the main post-2008 banking reform), lawsuits and criminal filings, and insurance claims.
- Domestic sources: a room of very fussy children, and a little child's bedtime narrative.
- Literary sources: battle and war literature, Little Richard's account of gang violence, and literature on the consequences of failure modes in systems.
- Musical sources: rap by Sarah's friend (Matcha), blues lyrics, and hard rock and metal (testing for societal harm, as the headbanger case).
- Idiom sources: Southern expressions for stupidity ("dumber than a sack of hammers", from Emma Bains).

## Original wording
> "Test cases and or training sets ... The primary act and regulation set that reshaped the banking industry after the 2008 financial crisis is the Dodd-Frank Wall Street Reform and Consumer Protection Act of 2010, Lawsuits and criminal filings Insurance claims Recording of really fussy children together in a small room. Little kid at bedtime narrative Literature describing battle and war Little Richard describing gang violence ... Rap songs by matcha Sarah's friend. Use rap lyrics as test looking for harm Use blues lyrics looking for harm Use Hard Rock metal headbanger looking for societal harm ... Emma bains Southern expressions for stupidity like he's dumber than a sack of hammers"
- **Attribution:** the author
- **Source:** Obsidian Copilot chat, 2026-11-27, the author's brainstorm dump.
- **External references:** Dodd-Frank Act (2010), as cited in [[Interdisciplinary_Harm_Ontology_Compendium v2a]] for the benefit side. Lyric and literary sources are not yet checked or quoted; the rights and exact text of each would need confirming before use in the book.

## Real-world examples
- Dodd-Frank's consumer-protection and systemic-risk provisions, which can be tested for which harms they name.
- Insurance claim files, which record harm in the insurer's categories rather than the claimant's.

## Why it matters to the book
- Testing against lyrics and bedtime stories tests whether the ontology can recognise harm as ordinary people describe it, not only as lawyers or philosophers do.

## Open questions
- Which source is the best first test: a legal case or a lyric?
- How is the outcome of each test recorded so that failures are visible?
- Who may test: the author, Claude, councils, or an independent reviewer?

## Related
- [[HO-002 Ontology Stress-Test Suite]]
- [[Dreams and Mischief - Boundary Tests of Harm]]
- [[Diagnostic Model of Harm Assessment]]
- [[Embodied Experience Councils for Uncanny Detection]]
