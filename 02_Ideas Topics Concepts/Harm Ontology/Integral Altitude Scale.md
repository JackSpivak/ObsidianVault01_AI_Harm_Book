---
fileClass: Idea
type: idea
status: seed
bookmark: HO-II.d.2.a
canonical_id: ho-integral-altitude-scale
territory: new
tags: [ontology/harm]
aliases: [HO-II.d.2.a, Integral Altitude Scale, Wilber Altitudes, int:colourAltitude]
created: 2026-11-17
filed: 2026-11-17
---

# Integral Altitude Scale

Index: [[_Harm Ontology Bookmark Index]] · Parent: [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes|HO-II.d.2]]

## Why this is distinct
- [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes|HO-II.d.2]] treats Wilber's Integral scale as one spoke of the `developmentalAltitude` hub. This note holds the scale itself: its four moral bands, six Gebser stages and twelve colour levels, each as its own record, so a value can be recorded as precisely as "amber, on Wilber's scale (2017)".

## Anticipated direction
- Check the twelve-colour sequence, the teal/turquoise names and the third tier against *The Religion of Tomorrow* (2017) itself.
- Check Gilligan's own wording of her stages.
- Repeat the pattern for other scales (Kohlberg's six stages; Hierocles's circles, once verified).

## Conceptual territory
- New. A SKOS value scale: three concept schemes (`int:moralBands`, `int:gebserStages`, `int:colourAltitude`) linked by `skos:narrower`, and mapped to `psy:careStages` (Gilligan). It applies only to the PerspectiveType attribute `developmentalAltitude`, which is always an Assessment with a named scale and `assessedBy`.

## Summary

### Sources and how far each is verified
| Source | Type | What it confirms | Status |
|---|---|---|---|
| Wilber, "The Leading Edge of the Unknown in the Human Being" ([PDF](http://integral-life-home.s3.amazonaws.com/Wilber-WakeUpGrowUp-TheEdgeOfTheUnknown.pdf)) | Primary (talk transcript, undated; mentions SAND) | Four bands = Gilligan's four stages; Gebser's six stages; how stages group into bands; 1st and 2nd tier; stage descriptions, ages and emergence dates | Read in full, 2026-11-17 |
| Wilber, "Integral Semiotics" ([PDF](https://integral-life-home.s3.amazonaws.com/Ken%20Wilber%20-%20Integral%20Semiotics.pdf)) | Primary (excerpt from unpublished vol. 2 of the Kosmos Trilogy, undated) | Colours red, amber, orange, green and indigo as altitudes; "tribal red", amber "religious traditionalism", orange "modern science", green "postmodernism + multiculturalism"; quadrants | Read (first part), 2026-11-17 |
| Wilber, *The Religion of Tomorrow* (2017), p. 349 | Primary, **not seen** | Twelve-colour sequence, as quoted by [Visser](https://www.integralworld.net/visser101.html) | Secondary only |
| [Visser](https://www.integralworld.net/visser101.html); [Deep Psychology](https://deep-psychology.com/ken-wilber-levels-of-consciousness/) | Secondary | Stage names for magenta, red, teal, turquoise and the third tier | Secondary only; they conflict on teal and turquoise |

**Level numbering varies between Wilber's texts.** "Integral Semiotics" numbers red as Level 10 and green as Level 13 (counting physical and biological levels too). The numbers 1–12 below are this note's order only, not Wilber's.

### Three nested schemes
```text
int:moralBands      egocentric ─────────────── ethnocentric ── worldcentric ──────── kosmocentric ──────── (3rd tier: band not stated)
int:gebserStages    archaic · magic (· magic-mythic) mythic        rational · pluralistic  integral
int:colourAltitude  infrared · magenta · red     amber           orange · green          teal · turquoise     indigo · violet · ultraviolet · white
tier                ─────────────────────────────── 1st tier ───────────────────────────  2nd tier            3rd tier
psy:careStages      selfish                       care            universal care          integrated
```
Bands to Gebser stages and bands to Gilligan's stages: Wilber's own words (primary). Stages to colours: primary for red, amber, orange and green; secondary for the rest.

### Bands
| Band | Gilligan (per Wilber) | Pronoun | Definition | Status |
|---|---|---|---|---|
| **egocentric** | selfish | "me" | Moved only by its own immediate needs; can't take the role of another | Primary |
| **ethnocentric** | care | "us" | Care extends to one's own group, with a sharp us-versus-them division | Primary |
| **worldcentric** | universal care | "all of us" | Attempts to treat all people fairly, "regardless of race, color, sex, or religious creed" | Primary |
| **kosmocentric** | integrated | "all beings" | Integrates both voices; others extend it to "all sentient beings and all life" | Primary |

### Levels
Each record: colour (prefLabel) · stage name (altLabel) · band · tier · definition · example · explanation · verification. The AI examples are Claude's illustrations, not Wilber's.

**1 · Infrared · Archaic** · egocentric · 1st tier
- **Definition:** The earliest stage, the transition from great apes to humans; in today's individual, the first year or so of life.
- **Example:** An infant whose world is only its own immediate needs.
- **Explanation:** Wilber, following Gebser, places archaic consciousness at the very start of both human history and individual development, and says it has "no explicit religion". For this ontology it marks the floor of the scale. No adult tradition sits here, so it matters mainly as a reminder that every person starts at the bottom and climbs; a tradition's altitude describes where its holders typically operate, not where they began. It is grouped with magic as egocentric. In AI terms, almost no institutional lens would be assessed here; the level is recorded for completeness, so the scale isn't cut off at its lower end.
- **Verified:** stage and band, primary ("Leading Edge"); colour name, secondary.

**2 · Magenta · Magic** · egocentric · 1st tier
- **Definition:** Self and surroundings are not fully differentiated, so manipulating an image of a thing is felt to change the thing itself.
- **Example:** Wilber's examples: voodoo dolls; snake-handling congregations who believe faith protects them from bites.
- **Explanation:** Wilber dates the magic stage's emergence to around 200,000 years ago in collective evolution, and to roughly ages 1 to 3 or 4 in individuals. Its signature is the collapse of symbol and object: the sign is treated as if it were the thing. That gives the ontology a useful diagnostic for AI harm, because magical thinking about technology is common: treating a model's output as the reality it describes, or believing that naming a risk ("we have a safety policy") controls it. That second pattern also links to the `congruence` hub. A lens assessed here sees cause and effect through resemblance, not mechanism.
- **Verified:** stage, description, dates and band, primary; colour name "magenta", secondary (earlier schemes used purple).

**3 · Red · Magic-Mythic** · egocentric · 1st tier
- **Definition:** A separate but fragile self in a world experienced as hostile; power-driven.
- **Example:** "Tribal red" (Wilber). AI example: a deployment judged only by "does it help us win".
- **Explanation:** Red is where a separate self first stands against the world, and power becomes the organising value. Wilber calls it "tribal red" in "Integral Semiotics", but the "Leading Edge" talk, which uses Gebser's six stages, doesn't list magic-mythic separately, so its status as a distinct stage depends on which of Wilber's texts is followed. For AI harm, red describes lenses that judge any harm by whether it serves the holder's dominance: competitive "race" framings in which others' losses don't register as harm at all. A red lens's omissions are mostly out of frame, not negligent: other people's harms aren't part of what it looks at.
- **Verified:** colour and "tribal red", primary ("Integral Semiotics"); stage name "magic-mythic", secondary; band egocentric, secondary (Deep Psychology).

**4 · Amber · Mythic** · ethnocentric · 1st tier
- **Definition:** Myths taken as literally and absolutely true; identity from group membership; rules, order and "chosen people".
- **Example:** Wilber: fundamentalist religion of any faith. AI example: "safety" defined as protecting only our own users, citizens or customers.
- **Explanation:** Wilber dates mythic consciousness to around 10,000 years ago, and to roughly ages 5 to 10 in individuals, and calls it "deeply ethnocentric". It is the only stage in the ethnocentric band. Care is real and strong, but it stops at the group's edge, and those outside are suspect. Wilber estimates that 60 to 70 percent of the world's population is at this level or lower (his figure, not verified here). For this ontology, amber explains a common pattern in harm disputes: two lenses that both care sincerely, but about different "us"es. It is also the level at which rules are absolute, which links it to deontic normative forms and to the risk of misnaming (a group's rules called "universal").
- **Verified:** stage, description, dates, band and colour ("religious traditionalism"), primary.

**5 · Orange · Rational** · worldcentric · 1st tier
- **Definition:** Capable of a universal, third-person perspective: care for all people regardless of group.
- **Example:** Wilber: the Enlightenment; the Buddha's rational presentation of his teaching. AI example: universal fairness metrics and benchmarks applied to everyone alike.
- **Explanation:** Wilber stresses that "rational" doesn't mean dry or analytic; it means able to take a worldcentric, universal perspective. He dates its widespread emergence to the Western Enlightenment and links it to the abolition of slavery and to democratic revolutions; in individuals it becomes available in adolescence. In "Integral Semiotics" orange is "modern science". Most formal harm frameworks for AI (rights, fairness metrics, risk assessment) are orange: universal in intent. Its characteristic omission is what can't be universalised or measured, which the green level then raises. It is the first worldcentric stage.
- **Verified:** stage, description, dates, band and colour ("modern science"), primary.

**6 · Green · Pluralistic** · worldcentric · 1st tier
- **Definition:** Multicultural, diversity-oriented and relativistic; recognises many valid perspectives and is wary of hierarchy.
- **Example:** Wilber: the 1960s and much of postmodernism. AI example: participatory audits; "nothing about us without us".
- **Explanation:** Wilber says the pluralistic stage emerged significantly with the 1960s and becomes available in young adulthood; "Integral Semiotics" calls green "postmodernism + multiculturalism". It keeps orange's universal care but adds suspicion of any single universal standard, and insists on hearing marginalised voices. For AI harm, green lenses surface harms orange metrics miss (lived experience, cultural harm, whose voice counts), which links to the Subject's side and Power groups of PerspectiveType. Wilber's critique is that every first-tier stage, green included, believes its own values are the only true ones; green's relativism can make it intolerant of hierarchy even where hierarchy is real.
- **Verified:** stage, description, dates, band and colour, primary.

**7 · Teal · Holistic** (also named "Integral" in some sources) · kosmocentric · 2nd tier
- **Definition:** Systemic, multi-perspectival and flexible: values every earlier stage as partial and necessary.
- **Example:** AI example: a governance approach that deliberately combines rights, metrics, participation and security lenses, and records their disagreements.
- **Explanation:** In the "Leading Edge" talk, the integral stage is the 2nd tier, distinguished from all 1st-tier stages because it alone "thinks that all of the stages have some sort of importance". Wilber says only around 5 percent of the West's population is there (his estimate). Whether teal or turquoise carries the name "Integral" differs between sources, and this record follows Visser's table. In the talk's four-band scheme, the integral stage is "integrated or kosmocentric". For this ontology, teal is the altitude the ontology itself aspires to: treating lenses as "true but partial" ([[HO-III.a Divergence and Integration - True but Partial|HO-III.a]]). That is also a warning: an ontology that ranks its own stance highest is exactly the self-placement the "whose ranking" rule guards against.
- **Verified:** 2nd tier and kosmocentric band for "the integral stage", primary; colour and name "Holistic", secondary; teal/turquoise naming conflict unresolved.

**8 · Turquoise · Integral** (also "Super-Integral" or "Advanced Integral") · kosmocentric · 2nd tier
- **Definition:** A further 2nd-tier stage: more holistic and communal, open to ways of knowing beyond the intellect.
- **Example:** None drawn from the sources checked.
- **Explanation:** Not described in the primary texts read. The secondary sources disagree on its name and say little about its content, so this record holds the place in the sequence without a substantive Explanation. It shouldn't be used as a value in assessments until checked against *The Religion of Tomorrow*.
- **Verified:** secondary only.

**9 · Indigo · Para-mind** · 3rd tier (band not stated in primary text)
**10 · Violet · Meta-mind** · 3rd tier
**11 · Ultraviolet · Overmind** · 3rd tier
**12 · White (clear light) · Supermind** · 3rd tier
- **Definition, example and explanation:** Not written. Wilber calls the 3rd tier tentative, drawing on Aurobindo (secondary). "Integral Semiotics" mentions indigo as an altitude but doesn't describe it. A secondary source assigns all four to the kosmocentric band. Recorded for completeness only; there is no Gilligan or Kohlberg equivalent, which is itself a Divergence between scales.
- **Verified:** indigo as an altitude, primary; the rest, secondary only.

### Mappings to other scales
| Integral | Grade | Other scale | Basis |
|---|---|---|---|
| egocentric | exactMatch | `psy:selfish` (Gilligan) | Wilber, primary |
| ethnocentric | exactMatch | `psy:care` | Wilber, primary |
| worldcentric | exactMatch | `psy:universalCare` | Wilber, primary |
| kosmocentric | closeMatch | `psy:integrated` | Wilber, primary; he extends it beyond Gilligan's integration |
| egocentric / ethnocentric / worldcentric | closeMatch | Kohlberg pre-conventional / conventional / post-conventional | Claude's proposal |
| kosmocentric | no match | Kohlberg | Divergence between scales |

### Rule for use
A value from this scale is always recorded as an Assessment: "**amber** on `int:colourAltitude` (meaningAsOf 2017), assessedBy → *assessor*". Band-level values ("ethnocentric") are allowed when the finer level is uncertain. Never record a bare altitude.

## Original wording
> "im concerned about the integral altitudes.  the altitudes listed seem to correspond to macro level groupings of a 12 level color scheme with their own names, definitions, explanation and example"
- **Attribution:** Author

> "can you verify with primary text references?"
- **Attribution:** Author

> "the archaic and magic stages are both egocentric; the mythic stage, as we just pointed out, is ethnocentric; the rational and pluralistic stages are worldcentric; and the integral stage is integrated or kosmocentric."
- **Attribution:** Ken Wilber, "The Leading Edge of the Unknown in the Human Being" (primary text)

> "Gilligan's stages (selfish, care, universal care, integrated—or egocentric, ethnocentric, worldcentric, kosmocentric)"
- **Attribution:** Ken Wilber, "The Leading Edge of the Unknown in the Human Being" (primary text)

> "integral group confirmed. altitude  note then write perspective structure"
- **Attribution:** Author

- **Source:** Obsidian Copilot agent session "Read Handoff - PerspectiveStructure 0.02 and the notes it lists", 2026-11-17 (`copilot/copilot-conversations/agent__Read_Handoff_-_PerspectiveStructure_0.02_and_the_notes_it_lists,@20261117_170442.md`).
- **External references:** the Wilber primary texts and secondary sources listed above; Gilligan, *In a Different Voice* (1982).

## Real-world examples
- Competing AI "safety" framings: national advantage (ethnocentric), universal rights and metrics (worldcentric: orange), participatory and plural (worldcentric: green).

## Why it matters to the book
- Many harm disputes are disputes between altitudes that each think they are the only one. The scale lets the book name that without taking Wilber's ranking as fact.

## Open questions
- Verify the twelve-colour sequence, teal/turquoise names and the 3rd tier against *The Religion of Tomorrow* (2017).
- Is magic-mythic (red) a separate stage? The "Leading Edge" text omits it.
- Check Gilligan's own wording of her stages.
- Wilber's population percentages are his estimates; don't cite them in the book without a primary research source.

## Related
- [[Vocabulary Crosswalk - Concept Hubs and Discipline Schemes]]
- [[PerspectiveStructure 0.01]]
- [[HO-III.a Divergence and Integration - True but Partial]]
- [[_Harm Ontology Bookmark Index]]
