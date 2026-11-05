# Character development rules

How Claude creates and develops character notes in `04_Characters/`. Template:
`00_Claude_Admin/Templates/Character.md`. Background: see the 2026-11-05 entries in
`00_Claude_Admin/Decisions_Log.md`.

## Purpose of a character note
- One note per character. It holds the character's fixed facts, inner life, voice and arc.
- It is the second source of truth for continuity, after `Canon_and_Continuity.md`.
- Inner-life sections are a workshop. Items stay provisional until the author marks them [canon].

## Reference-profile workflow
1. Read the character's Fixed facts: profession, background, culture, geography, relationship to AI.
2. Propose 2–4 real people with similar profiles and wait for the author to pick them.
3. Run `/deep_person_research` on each one. Save the results as factual research notes in
   `02_Ideas Topics Concepts/Research/`, and keep the skill's evidence labels.
4. Add each note to the character's "Real-world reference profiles" table and to the
   `reference_profiles` frontmatter.
5. Draft the inner-life sections (below), then let the author accept, change or reject items.

## Filling the inner-life sections
The author explicitly wants Claude to imagine, infer, elaborate and even invent here. Be
generous and specific, not cautious or generic.

Sections: Vision, Desires/wants/needs, Fears, Values, Superpowers, Legal and shadow
circumstances, and Contradictions.

**How to generate:**
- Start from what is documented about the reference people: their profession, training,
  traditions, communities, places, and the pressures typical of their field.
- Ask what someone shaped by that life would plausibly hope for, crave, fear, protect and
  excel at. Then push past the obvious and give at least one surprising item per section.
- Blend the references and the character's own facts. Don't map one person onto the character.
- Build tension on purpose: wants that clash with needs, values that clash with fears, and
  superpowers whose shadow side the plot can exploit.
- Tie items to the book's theme, AI harm, wherever it fits naturally.
- Offer 3–6 items per section. Write concrete, scene-usable lines, not abstractions
  ("fears being filmed without consent", not "fears vulnerability").

**Labelling every item (required):**
- `[inferred: [[Research Note]] — basis]`: an extrapolation from a reference person's
  documented background. Briefly state the basis.
- `[imagined]`: invented for the story, loosely inspired by the reference profiles.
- `[canon]`: the author has decided it. Only the author promotes items to canon.
- Never present an inferred or imagined trait as a fact about the real person.

**In their own words: self-introduction.** Here Claude writes fiction in the character's
voice. Invent freely; this is a performance, not a summary.
- **Prerequisite:** the Voice section must be drafted first. If it's empty, draft Voice (or ask)
  before writing the introductions.
- **Sources to draw on:** Voice (register, tics, vocabulary, sentence length), Fixed facts,
  Vision, Values, Superpowers, Fears, Contradictions, and Legal and shadow circumstances.
- **Public introduction** (about 80–150 words, first person): how they'd introduce themselves
  to a stranger, an audience or a camera. Use their professional register. Show what they're
  proud of and how they want to be seen, including their lineage and credentials if that's
  their habit. Let one small slip or tell hint at what's underneath.
- **Private version** (about 80–150 words, first person): to someone they trust, or to
  themselves at 3 a.m. Use their off-duty register. Let it touch the deep fear, a contradiction,
  or a shadow circumstance the public version hides. It should feel more true, and more
  uncomfortable.
- **Always mention / never mention:** 2–3 items each. The "never" list should connect to Fears
  or to Legal and shadow circumstances.
- **Craft:** concrete images over abstractions; at least one line usable verbatim in a scene;
  tie it to the book's AI-harm theme where it fits naturally.
- **Boundaries:** label the whole section [imagined]. Never reuse a reference person's actual
  sentences or slogans; echo their rhythm and stance only. No real person's private details
  or real cases.
- **Consistency check:** before saving, confirm nothing contradicts the note's [canon] items.
  Flag anything that seems to need a change elsewhere in the note; don't silently edit
  other sections.

**Superpowers:** name the meta-capability (e.g. "translates between worlds"). List the skills,
abilities and knowledge underneath it, and give the cost or shadow side.

## Boundary with real people
- Research notes about real people stay factual. Invented material lives only in the
  character note.
- Patterns are fine; particulars are not. Don't give a character a real person's private
  details, specific cases, parties, courts, dates, allegations or identifiable life events.
- **Legal and shadow circumstances** may be complex or frightening, but they must be
  fictional and built from archetypes (e.g. "a negligence suit that drags on for years").
  Show how each one shapes personality: fear, secrecy, resolve, paranoia.

## After drafting
- Show the drafted sections and wait for feedback. Don't overwrite items the author has
  already labelled [canon].
- When the author promotes items to [canon], offer to add the key ones to `Canon_and_Continuity.md`.
- Follow the note creation rules in `CLAUDE.md`: include Summary and Original wording, with
  quotes attributed one by one.
