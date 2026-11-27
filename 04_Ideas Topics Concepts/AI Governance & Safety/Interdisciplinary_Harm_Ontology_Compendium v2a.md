# Comprehensive Interdisciplinary Ontology of Harm (OWL / SKOS / Dublin Core Specification)

**Compiled by the Joint Councils:** Philosophers Council, Legal Counsel, Economists & Game Theorists Council, Technologists & AI Safety Council, and Psychologists & Behavioral Scientists Council.

---

## Architecture Overview

This compendium preserves 100% of our interdisciplinary taxonomy, cross-cutting attributes, formal RDF/OWL identifiers, standard SKOS (`skos:`) documentation properties, and Dublin Core (`dcterms:`) citations.

* **Namespace Prefix:** `harm:` (`http://example.org/ontology/harm#`)
* **Layer 1 (Classes & Subclasses — `owl:Class`, `skos:Concept`):** 5 Top-Level Meta-Categories and 26 Subcategories defining *what* kind of substantive injury, setback, normative wrong, privation, or systemic breakdown is occurring.
* **Layer 2 (Cross-Cutting Properties — `owl:ObjectProperty`, `skos:Concept`):** 19 Attributes organized across 4 Functional Domains defining *who* is involved, *what substrate* is damaged, and *how* the mechanism operates.
* **Documentation Standard:** Uses W3C SKOS (`skos:prefLabel`, `skos:altLabel`, `skos:definition`, `skos:note`, `skos:scopeNote`, `skos:example`, `skos:historyNote`) and Dublin Core (`dcterms:bibliographicCitation`) to preserve all explanatory prose verbatim.
* **v2 Revision (2026-11-13), additions only:** This version adds material after a semantic comparison with [[# Master Formal Ontology of Harm (Part 1- Schema, Cross-Cutting Sub-Taxonomies & Axioms)|Master Formal Ontology of Harm]]. Nothing from v1 ([[Interdisciplinary_Harm_Ontology_Compendium]]) has been removed or reworded. New totals: **29 Subcategories**, **26 Attributes** across **5 Functional Domains** (new Domain E). Existing attributes 1–19 keep their numbers. New attributes are numbered 20–26 and placed in the domain they belong to. Every addition carries a `skos:changeNote`.
* **v2a Revision (2026-11-15), additions only — Benefit Mirror (skeleton):** Copied from [[Interdisciplinary_Harm_Ontology_Compendium v2]] with no changes to existing text. Adds Part B (end of this note): a benefit-side structure that mirrors the harm structure, kept in the `harm:` namespace. Status: **stages 1–3 drafted, awaiting author review**: skeleton (B.0–B.3), descriptions (B.4–B.5), history notes and citations (B.6). A few sources are still open (flagged in B.6). Benefit attributes are numbered B1–B23 so they don't clash with harm attributes 1–26.

---

## Master Structural Map

```text
INTERDISCIPLINARY ONTOLOGY OF HARM
├── I. harm:ExperientialHarm (Experiential & Subjective Harm — Conscious Suffering)
│   ├── 1. harm:HedonicHarm (Experiential / Hedonic Harm) [Philosophy]
│   ├── 2. harm:DignitaryRelationalHarm (Dignitary & Relational Harm) [Law]
│   ├── 3. harm:PsychologicalEmotionalTrauma (Psychological & Emotional Trauma — IIED/NIED) [Law]
│   ├── 4. harm:NuisanceSensoryOffense (Nuisance & Sensory Offense) [Philosophy/Law]
│   └── 5. harm:VicariousMoralInjury (Vicarious, Secondary & Moral Injury) [Psychology]
│   └── 6. harm:NonComparativeHarm (Non-Comparative Harm — Non-Identity Cases) [Philosophy] (v2)
│
├── II. harm:WelfareInterestHarm (Welfare & Interest-Based Harm — Counterfactual Setbacks)
│   ├── 1. harm:InterestSetbackHarm (Interest-Based Harm — Counterfactual Comparative) [Philosophy]
│   ├── 2. harm:PublicCriminalHarm (Public / Criminal Harm) [Law]
│   ├── 3. harm:PrivateTortiousHarm (Private / Tortious Harm) [Law]
│   ├── 4. harm:ExpectationRelianceHarm (Expectation & Reliance Harm) [Law]
│   ├── 5. harm:ProbabilisticRiskHarm (Probabilistic & Risk-Based Harm) [Philosophy/Law]
│   ├── 6. harm:CollectiveEnvironmentalHarm (Collective, Diffuse & Environmental Harm) [Law]
│   └── 7. harm:OpportunityCostChoiceHarm (Opportunity Cost & Choice Architecture Harm) [Econ/Psych]
│
├── III. harm:DeontologicalRightsHarm (Deontological & Rights-Based Harm — Normative Wrongs)
│   ├── 1. harm:KantianDeontologicalHarm (Deontological / Kantian Harm) [Philosophy]
│   ├── 2. harm:InjuriaSineDamnoHarm (Rights-Based Harm Without Loss — Injuria Sine Damno) [Law]
│   ├── 3. harm:EpistemicTestimonialHarm (Epistemic & Testimonial Harm) [Philosophy]
│   └── 4. harm:FiduciaryBetrayalHarm (Fiduciary & Betrayal Harm) [Law]
│   └── 5. harm:CulturalEpistemicideHarm (Cultural Harm & Epistemicide) [Law/Anthropology] (v2)
│   └── 6. harm:CognitiveLibertyHarm (Cognitive Liberty & Autonomy Subversion) [Philosophy/Law/Tech] (v2)
│
├── IV. harm:TeleologicalDeprivationHarm (Teleological & Deprivation Harm — Privation of Good & Flourishing)
│   ├── 1. harm:PerfectionistTeleologicalHarm (Teleological / Perfectionist Harm) [Philosophy]
│   ├── 2. harm:DeprivationHarm (Harm by Deprivation) [Philosophy]
│   ├── 3. harm:CapabilityStructuralHarm (Capability Deprivation & Structural Harm) [Philosophy]
│   ├── 4. harm:WrongfulDeathConsortiumHarm (Wrongful Death & Loss of Consortium) [Law]
│   ├── 5. harm:ParensPatriaePaternalisticHarm (Parens Patriae & Paternalistic Harm Prevention) [Law]
│   └── 6. harm:AttachmentDevelopmentalHarm (Attachment, Developmental & Relational Deprivation) [Psychology]
│
└── V. harm:SystemicCyberneticHarm (Systemic, Emergent & Cybernetic Harm — Network & Equilibrium Failures)
    ├── 1. harm:ExternalityCoordinationHarm (Negative Externalities & Coordination Failures) [Economics/Game Theory]
    ├── 2. harm:InformationAsymmetryHarm (Information Asymmetry & Adverse Selection Harm) [Economics/Game Theory]
    ├── 3. harm:AlgorithmicAlignmentHarm (Algorithmic, Alignment & Emergent Scale Harm) [Tech/AI Safety]
    └── 4. harm:EpistemicPollutionHarm (Epistemic Pollution & Attention Hijacking) [Tech/Behavioral Science]
```

---

## Part 1: Taxonomy of Types of Harm (`owl:Class` & `skos:Concept`)

### Meta-Category I: `harm:ExperientialHarm`
* **skos:prefLabel:** Experiential & Subjective Harm (Conscious Suffering)
* **skos:altLabel:** Hedonic Harm | Phenomenological Harm | Suffering-Based Harm
* **skos:definition:** At the highest level, this domain defines harm strictly through conscious, subjective phenomenology—negative mental or physical states experienced directly by a sentient subject.
* **skos:note:** Under this view, what you do not experience cannot harm you. It covers negative mental states—such as physical pain, emotional distress, anguish, or grief—or deprivation of positive states like pleasure and contentment.
* **skos:scopeNote:** Strictly requires conscious perception by a sentient being; excludes unperceived or posthumous setbacks.
* **skos:historyNote:** Epicurus established that physical pain (aponia's opposite) and mental distress (ataraxia's opposite) are the fundamental evils, famously arguing that death is no harm to the deceased because it involves no sensation. Jeremy Bentham formalized this in An Introduction to the Principles of Morals and Legislation (1789), building a moral calculus around the intensity and duration of pleasure and pain across all sentient beings.
* **dcterms:bibliographicCitation:** Epicurus, Letter to Menoeceus; Bentham, Jeremy. An Introduction to the Principles of Morals and Legislation (1789).
* **Inherited Attribute Defaults:** `harm:hasPhenomenologicalTransparency`: `harm:PerceivedSubjective` | `harm:hasPatientOntology`: `harm:SentientIndividual` | `harm:hasComparativeBaseline`: `harm:TemporalBaseline`

#### 1. `harm:HedonicHarm` (`rdfs:subClassOf harm:ExperientialHarm`)
* **skos:prefLabel:** Experiential Harm (Hedonic / Phenomenological Harm)
* **skos:altLabel:** Hedonic Harm | Experiential Harm | Suffering-Based Harm
* **skos:definition:** This category defines harm strictly through conscious, subjective experience. An action harms a subject if and only if it causes negative mental states—such as physical pain, emotional distress, anguish, or grief—or deprives the subject of positive states like pleasure and contentment.
* **skos:note:** Under this view, what you do not experience cannot harm you. Forms the philosophical root of subjective welfare ethics.
* **skos:example:** Physical pain, emotional distress, anguish, grief, or deprivation of pleasure and contentment.
* **skos:historyNote:** Epicurus (established physical pain and mental distress as fundamental evils); Jeremy Bentham (built moral calculus around intensity and duration of pleasure and pain across sentient beings).
* **dcterms:bibliographicCitation:** Bentham, Jeremy. An Introduction to the Principles of Morals and Legislation (1789).
* **Key Attribute Bindings:** `harm:hasObjectOfHarm`: `harm:SomaticBiologicalSubstrate` | `harm:PsychologicalCognitiveSubstrate`; `harm:hasPhenomenologicalTransparency`: `harm:PerceivedSubjective`.

#### 2. `harm:DignitaryRelationalHarm` (`rdfs:subClassOf harm:ExperientialHarm`)
* **skos:prefLabel:** Dignitary and Relational Harm
* **skos:altLabel:** Dignitary Tort | Moral Damage | Reputational Harm | Emotional Distress
* **skos:definition:** Harm to a person’s reputation, privacy, personal autonomy, or emotional tranquility.
* **skos:note:** Unlike physical or financial injury, dignitary harm requires no tangible economic loss; the legal injury lies in the affront to the person's standing, self-determination, or psychological integrity. Bridges experiential distress and deontological dignity.
* **skos:example:** Invasion of personal privacy, defamation of character, public humiliation, or intrusion upon seclusion.
* **skos:historyNote:** Samuel D. Warren & Louis D. Brandeis argued in their seminal 1890 Harvard Law Review essay "The Right to Privacy" that the common law must evolve beyond physical property to protect the "inviolate personality" against emotional and reputational intrusion. William Prosser codified the modern taxonomy of privacy and dignitary torts in the mid-20th century, giving courts clear doctrinal categories for intangible harms.
* **dcterms:bibliographicCitation:** Warren, Samuel D., & Brandeis, Louis D. "The Right to Privacy," Harvard Law Review (1890); Prosser, William L. "Privacy," California Law Review (1960).
* **Key Attribute Bindings:** `harm:hasObjectOfHarm`: `harm:DignitaryRelationalSubstrate` | `harm:PsychologicalCognitiveSubstrate`; `harm:hasNormativeStatus`: `harm:NormativeWrongful`.

#### 3. `harm:PsychologicalEmotionalTrauma` (`rdfs:subClassOf harm:ExperientialHarm`)
* **skos:prefLabel:** Psychological & Emotional Trauma
* **skos:altLabel:** Intentional Infliction of Emotional Distress (IIED) | Negligent Infliction of Emotional Distress (NIED) | Pain and Suffering Damages
* **skos:definition:** Severe mental anguish, psychiatric injury, or post-traumatic stress inflicted through extreme and outrageous conduct or severe negligence, recognized as a standalone injury even without physical impact.
* **skos:note:** Operationalizes pure mental and emotional suffering as an independent tortious injury in modern civil law.
* **skos:example:** Severe psychiatric trauma or post-traumatic stress caused by extreme and outrageous harassment or witnessing a negligent fatal accident involving a close relative.
* **skos:historyNote:** Calvert Magruder mapped the emerging common-law recognition of mental and emotional distress torts in his influential 1936 Harvard Law Review analysis. William Prosser formalized IIED as a distinct, independent tort category in the Restatement (Second) of Torts.
* **dcterms:bibliographicCitation:** Magruder, Calvert. "Mental and Emotional Disturbance in the Law of Torts," Harvard Law Review (1936); Restatement (Second) of Torts § 46 (1965).
* **Key Attribute Bindings:** `harm:hasObjectOfHarm`: `harm:PsychologicalCognitiveSubstrate`; `harm:hasVictim`: `harm:DirectPrimaryVictim` | `harm:SecondaryRelationalVictim`; `harm:hasSeverityMagnitude`: `harm:SevereRuinous`.

#### 4. `harm:NuisanceSensoryOffense` (`rdfs:subClassOf harm:ExperientialHarm`)
* **skos:prefLabel:** Nuisance and Sensory Offense
* **skos:altLabel:** Private Nuisance | Public Nuisance | Profound Offense
* **skos:definition:** Unreasonable interference with the sensory enjoyment of life or property—such as noxious odors, deafening noise, or grotesque public displays.
* **skos:note:** Philosophy distinguishes mere passing annoyance from sustained, inescapable sensory misery that degrades lived experience.
* **skos:example:** Industrial noxious odors, deafening continuous noise, or inescapable grotesque public displays interfering with enjoyment of home or public spaces.
* **skos:historyNote:** Joel Feinberg analyzed the boundary between non-actionable offense and profound, inescapable sensory/moral affronts in Offense to Others (1985). William Blackstone defined private nuisance in his Commentaries as anything done to the hurt or annoyance of the lands, tenements, or hereditaments of another.
* **dcterms:bibliographicCitation:** Feinberg, Joel. The Moral Limits of the Criminal Law, Vol. 2: Offense to Others (1985); Blackstone, William. Commentaries on the Laws of England (1765–1769).
* **Key Attribute Bindings:** `harm:hasTemporalTrajectory`: `harm:SlowAccumulativeTrajectory`; `harm:hasDistributionAggregation`: `harm:NarrowConcentrated` | `harm:DiffuseThreshold`.

#### 5. `harm:VicariousMoralInjury` (`rdfs:subClassOf harm:ExperientialHarm`)
* **skos:prefLabel:** Vicarious, Secondary & Moral Injury
* **skos:altLabel:** Moral Injury | Secondary Traumatic Stress | Vicarious Trauma
* **skos:definition:** Distinct from standard physical trauma or fear-based PTSD, moral injury occurs when a person perpetrates, witnesses, or is forced by an institution to participate in acts that transgress their deeply held moral beliefs—causing profound shame, guilt, and existential pain.
* **skos:note:** Contributed by Psychologists & Behavioral Scientists. Captures ethical and existential trauma experienced by those forced into moral compromise or repeated exposure to others' trauma.
* **skos:example:** Psychological and existential trauma experienced by combat veterans, healthcare workers forced to ration care, or content moderators exposed to graphic violence.
* **skos:historyNote:** Jonathan Shay coined Moral Injury in Achilles in Vietnam (1994) to distinguish betrayal-based ethical trauma from fear-based PTSD. Brett Litz formalized clinical frameworks for measuring moral injury as a distinct psychological harm.
* **dcterms:bibliographicCitation:** Shay, Jonathan. Achilles in Vietnam (1994); Litz, Brett T., et al. "Moral Injury and Moral Repair in War Veterans," Clinical Psychology Review (2009).
* **Key Attribute Bindings:** `harm:hasPerpetrator`: `harm:DiffuseCollectivePerpetrator` (Institutional compulsion); `harm:hasVictim`: `harm:SecondaryRelationalVictim`; `harm:hasObjectOfHarm`: `harm:PsychologicalCognitiveSubstrate`.

#### 6. `harm:NonComparativeHarm` (`rdfs:subClassOf harm:ExperientialHarm`)
* **skos:prefLabel:** Non-Comparative Harm (Non-Identity Cases)
* **skos:altLabel:** Wrongful Life Harm | Harm Without a Better-Off Counterfactual | Non-Identity Harm
* **skos:definition:** Placing a being in an intrinsically bad or miserable state, judged against an absolute threshold rather than a comparison with a baseline. It resolves cases where no "better off" counterfactual exists, because the alternative for that individual was never existing at all.
* **skos:note:** Explains why bringing a child into existence with a severe condition, or into a degraded climate or social world, can be a harm even though that same individual could not otherwise have existed. Counterfactual accounts (`harm:InterestSetbackHarm`) cannot reach these cases.
* **skos:scopeNote:** Applies only where no counterfactual baseline is available for the same individual. Where one exists, use the counterfactual or temporal baseline instead.
* **skos:example:** Wrongful-life claims; policies that create future generations in a degraded environment; decisions that bring new beings into conditions of severe suffering.
* **skos:historyNote:** Derek Parfit posed the Non-Identity Problem in Reasons and Persons (1984). Elizabeth Harman and Seana Shiffrin developed non-comparative accounts of harm in response.
* **dcterms:bibliographicCitation:** Parfit, D. (1984). *Reasons and Persons* (Part IV). Oxford University Press; Harman, E. (2004). "Can We Harm and Benefit in Creating?" *Philosophical Perspectives*, 18, 89–113; Shiffrin, S. V. (1999). "Wrongful Life, Procreative Responsibility, and the Significance of Harm." *Legal Theory*, 5(2), 117–148.
* **Key Attribute Bindings:** `harm:hasComparativeBaseline`: `harm:NonComparativeBaseline`; `harm:hasPatientOntology`: `harm:SentientIndividual` | `harm:NonSentientSystem` (future generations); `harm:hasVictim`: `harm:DiffuseRepresentativeClass`; `harm:hasTemporalTrajectory`: `harm:SlowAccumulativeTrajectory`.
* **skos:changeNote:** Added in v2 (2026-11-13) from Master Formal Ontology §1.4.

---

### Meta-Category II: `harm:WelfareInterestHarm`
* **skos:prefLabel:** Welfare & Interest-Based Harm (Counterfactual Setbacks)
* **skos:altLabel:** Setback to Interests | Counterfactual Comparative Harm (CCH) | Welfare Harm
* **skos:definition:** At the highest level, this domain defines harm objectively rather than subjectively. An entity is harmed whenever an action sets back its vital stakes, resources, or baseline position compared to what would otherwise have occurred—even if the victim never perceives the loss.
* **skos:note:** The dominant framework in modern jurisprudence and liberal political philosophy. Harm occurs when an action sets back a person's vital, ongoing stakes in their well-being (such as health, property, privacy, or liberty), leaving them worse off than they otherwise would have been. Crucially, this allows for posthumous or unperceived harm—such as a secret betrayal or slander—because a person's objective interests are damaged even if they never feel pain.
* **skos:scopeNote:** Applies to objective setbacks across vital ongoing interests (health, property, privacy, liberty); distinct from mere offense or moral disapproval, and distinguishes between non-normative harm (a setback caused by nature) and normative harm (a wrongful setback that violates a right).
* **skos:historyNote:** Emerged from 19th-century utilitarian liberalism to define the legitimate limits of state coercion, later systematized in 20th-century analytical jurisprudence as the Counterfactual Comparative Account.
* **dcterms:bibliographicCitation:** Mill, John Stuart. On Liberty (1859); Feinberg, Joel. The Moral Limits of the Criminal Law, Vol. 1: Harm to Others (1984).
* **Inherited Attribute Defaults:** `harm:hasComparativeBaseline`: `harm:CounterfactualBaseline` | `harm:hasPhenomenologicalTransparency`: `harm:UnperceivedObjective` | `harm:hasPatientOntology`: `harm:SentientIndividual` | `harm:CollectiveArtificialPerson` | `harm:NonSentientSystem`

#### 1. `harm:InterestSetbackHarm` (`rdfs:subClassOf harm:WelfareInterestHarm`)
* **skos:prefLabel:** Interest-Based Harm (The Counterfactual Comparative Account)
* **skos:altLabel:** Setback to Interests | Counterfactual Comparative Harm (CCH) | Welfare Harm
* **skos:definition:** Harm occurs when an action sets back a person's vital, ongoing stakes in their well-being (such as health, property, privacy, or liberty), leaving them worse off than they otherwise would have been.
* **skos:note:** Allows for posthumous or unperceived harm—such as a secret betrayal or slander—because a person's objective interests are damaged even if they never feel pain. Distinguishes non-normative setbacks (caused by nature) from normative setbacks (violating a right).
* **skos:example:** Secret betrayal, covert slander discovered after death, or wrongful deprivation of property or liberty.
* **skos:historyNote:** John Stuart Mill introduced the Harm Principle in On Liberty (1859), defining harm as an objective injury to the vital interests of others, distinct from mere offense or moral disapproval. Joel Feinberg systematized the concept in Harm to Others (1984), explicitly defining harm as a "setback to interests."
* **dcterms:bibliographicCitation:** Mill, John Stuart. On Liberty (1859); Feinberg, Joel. Harm to Others (1984).

#### 2. `harm:PublicCriminalHarm` (`rdfs:subClassOf harm:WelfareInterestHarm`)
* **skos:prefLabel:** Public Harm (Criminal / Societal Harm)
* **skos:altLabel:** Public Wrong | Social Harm | Malum in Se | Malum Prohibitum
* **skos:definition:** Harm that threatens the foundational order, safety, and collective peace of the political community.
* **skos:note:** Even when a crime has an individual victim (such as assault or theft), criminal law treats the act primarily as an injury against the sovereign state and the public at large.
* **skos:example:** Assault, theft, treason, public endangerment, or regulatory offenses breaching public safety duties.
* **skos:historyNote:** Cesare Beccaria argued in On Crimes and Punishments (1764) that the true measure of a crime is the harm done to society, rejecting sin or moral status as valid bases for criminal law. William Blackstone systematized the distinction in Commentaries on the Laws of England (1765–1769) between "private wrongs" (civil injuries) and "public wrongs" (crimes that breach public duties owed to the whole community).
* **dcterms:bibliographicCitation:** Beccaria, Cesare. On Crimes and Punishments (1764); Blackstone, William. Commentaries on the Laws of England (1765–1769).
* **Key Attribute Bindings:** `harm:hasVictim`: `harm:DiffuseRepresentativeClass` (The Sovereign/Public) + `harm:DirectPrimaryVictim`; `harm:hasRemedialDutyBearer`: `harm:InstitutionalSovereignGuarantor` (Criminal prosecution).

#### 3. `harm:PrivateTortiousHarm` (`rdfs:subClassOf harm:WelfareInterestHarm`)
* **skos:prefLabel:** Private Harm (Tortious / Civil Injury)
* **skos:altLabel:** Tortious Injury | Damnum Iniuria Datum (loss wrongfully caused) | Invasion of Legally Protected Interests
* **skos:definition:** Harm inflicted by one private party upon another that entitles the injured party to a civil remedy, typically monetary damages or an injunction.
* **skos:note:** This spans physical bodily injury, property damage, and economic loss, requiring a causal link between a breach of duty and an actual setback.
* **skos:scopeNote:** Requires a breach of an objective legal duty plus a causal link to an actual setback; excludes non-normative economic or physical setbacks where no legal right was violated (Damnum Absque Injuria).
* **skos:example:** Physical bodily injury, property damage, and economic loss (such as a car crash).
* **skos:historyNote:** Oliver Wendell Holmes Jr., in The Common Law (1881), shifted tort liability away from subjective moral fault toward objective standards of foreseeability and external conduct that causes measurable harm to others. H.L.A. Hart & Tony Honoré, in Causation in the Law (1959), established the modern legal framework for determining when a person's actions are the legally responsible cause of a resulting private harm.
* **dcterms:bibliographicCitation:** Holmes, Oliver Wendell Jr. The Common Law (1881); Hart, H.L.A., & Honoré, Tony. Causation in the Law (1959).
* **Key Attribute Bindings:** `harm:hasPerpetrator`: `harm:UnitaryIntentionalAgent` | `harm:VicariouslyLiablePrincipal`; `harm:hasVictim`: `harm:DirectPrimaryVictim`; `harm:hasObjectOfHarm`: `harm:SomaticBiologicalSubstrate` | `harm:MaterialPecuniarySubstrate`; `harm:hasRemedialDutyBearer`: `harm:PerpetratorAsRestorer` | `harm:VictimDutyToMitigate`; `harm:hasModality`: `harm:ActualizedHarm`; `harm:hasTemporalTrajectory`: `harm:AcuteTrajectory`.

#### 4. `harm:ExpectationRelianceHarm` (`rdfs:subClassOf harm:WelfareInterestHarm`)
* **skos:prefLabel:** Expectation and Reliance Harm (Contractual / Economic Harm)
* **skos:altLabel:** Pecuniary Harm | Expectation Loss | Reliance Loss | Pure Economic Loss
* **skos:definition:** Harm arising not from physical damage, but from broken promises, breached agreements, or unfair commercial interference.
* **skos:note:** Legal counsel measures this harm counterfactually: how much worse off is the party compared to the position they would have been in had the promise been kept (expectation) or had the promise never been made (reliance).
* **skos:example:** Breach of a supply contract resulting in lost profits (expectation loss) or wasted preparatory expenses incurred in reliance on a broken promise (reliance loss).
* **skos:historyNote:** Lon L. Fuller & William R. Perdue Jr., in their landmark 1936 article "The Reliance Interest in Contract Damages", formalized the three core categories of contractual harm: restitution, reliance, and expectation interests.
* **dcterms:bibliographicCitation:** Fuller, Lon L., & Perdue, William R. Jr. "The Reliance Interest in Contract Damages," Yale Law Journal (1936).
* **Key Attribute Bindings:** `harm:hasObjectOfHarm`: `harm:MaterialPecuniarySubstrate`; `harm:hasComparativeBaseline`: `harm:CounterfactualBaseline`; `harm:hasReversibility`: `harm:RestorableElastic`.

#### 5. `harm:ProbabilisticRiskHarm` (`rdfs:subClassOf harm:WelfareInterestHarm`)
* **skos:prefLabel:** Probabilistic and Risk-Based Harm
* **skos:altLabel:** Risk Imposition | Loss of Chance Doctrine | Toxic Tort Exposure
* **skos:definition:** Exposing an individual or population to a heightened probability of future catastrophe (such as carcinogen exposure or reckless endangerment).
* **skos:note:** Even if the physical illness has not yet manifested, the imposition of risk itself acts as an immediate setback to a person's security and life prospects.
* **skos:scopeNote:** Applies when risk imposition or statistical loss of chance precedes—or occurs independently of—an actualized physical injury; overrides standard actualized-harm requirements.
* **skos:example:** Carcinogen exposure, reckless endangerment, or when a doctor's negligence reduces a patient's survival odds from 40% to 10%.
* **skos:historyNote:** Judith Jarvis Thomson analyzed the moral boundaries of imposing non-consensual risk upon others even when no physical injury materializes. Joseph H. King Jr. formalized the modern Loss of Chance doctrine in medical malpractice law (1981), arguing that reducing a patient's statistical odds of recovery is itself a compensable injury.
* **dcterms:bibliographicCitation:** Thomson, Judith Jarvis. "Imposing Risks," in Rights, Restitution, and Risk (1986); King, Joseph H. Jr. "Causation, Valuation, and Chance in Personal Injury Torts Involving Preexisting Conditions and Future Consequences," Yale Law Journal (1981).
* **Key Attribute Bindings:** `harm:hasModality`: `harm:ProbabilisticRisk`; `harm:hasTemporalTrajectory`: `harm:LatentTrajectory`; `harm:hasObjectOfHarm`: `harm:OpportunityCapabilitySubstrate` | `harm:SomaticBiologicalSubstrate`; `harm:hasSystemOpacity`: `harm:BlackBoxOpaque`.

#### 6. `harm:CollectiveEnvironmentalHarm` (`rdfs:subClassOf harm:WelfareInterestHarm`)
* **skos:prefLabel:** Collective, Diffuse, and Environmental Harm
* **skos:altLabel:** Public Trust Harm | Antitrust Injury | Tragedy of the Commons
* **skos:definition:** Small, incremental setbacks spread across millions of people or shared ecosystems—such as price-fixing monopolies, air pollution, or data breaches—where no single victim suffers a catastrophic personal loss, yet the aggregate welfare setback is massive.
* **skos:note:** Captures harms that require class-action aggregation, antitrust enforcement, or public trust environmental doctrines to remedy.
* **skos:example:** Price-fixing monopolies overcharging millions of consumers by pennies, industrial air pollution, or massive corporate data breaches.
* **skos:historyNote:** Garrett Hardin articulated the Tragedy of the Commons (1968), showing how rational individual actions cumulatively degrade shared resources. Joseph Sax was the architect of modern Public Trust environmental doctrine (1970). Robert Bork established the consumer welfare standard in antitrust law.
* **dcterms:bibliographicCitation:** Hardin, Garrett. "The Tragedy of the Commons," Science (1968); Sax, Joseph L. "The Public Trust Doctrine in Natural Resource Law," Michigan Law Review (1970); Bork, Robert H. The Antitrust Paradox (1978).
* **Key Attribute Bindings:** `harm:hasDistributionAggregation`: `harm:DiffuseThreshold`; `harm:hasPatientOntology`: `harm:NonSentientSystem` | `harm:CollectiveArtificialPerson`; `harm:hasObjectOfHarm`: `harm:SystemicEnvironmentalSubstrate` | `harm:MaterialPecuniarySubstrate`.

#### 7. `harm:OpportunityCostChoiceHarm` (`rdfs:subClassOf harm:WelfareInterestHarm`)
* **skos:prefLabel:** Opportunity Cost & Choice Architecture Harm
* **skos:altLabel:** Opportunity Cost | Dark Patterns | Sludge
* **skos:definition:** Harm inflicted not by taking away what someone currently has, but by subtly manipulating their choice environment (via deceptive user interfaces, hidden friction, or behavioral nudges) so they consistently make suboptimal decisions—forfeiting wealth, time, or better alternatives they otherwise would have chosen.
* **skos:note:** Contributed by Economists & Behavioral Scientists. Operates by exploiting cognitive friction and decision heuristics to degrade counterfactual welfare.
* **skos:example:** Deceptive subscription cancellation flows ("roach motels"), hidden fees revealed at checkout, or intentional bureaucratic "sludge" blocking eligible citizens from claiming benefits.
* **skos:historyNote:** Richard Thaler & Cass Sunstein introduced Choice Architecture and Sludge (intentional friction that blocks people from claiming benefits or canceling subscriptions). Harry Brignull coined Dark Patterns (2010) to classify user interfaces engineered to trick users into welfare-reducing actions.
* **dcterms:bibliographicCitation:** Thaler, Richard H., & Sunstein, Cass R. Nudge (2008); Sunstein, Cass R. Sludge (2021); Brignull, Harry. Deceptive Patterns (2010).
* **Key Attribute Bindings:** `harm:hasCognitiveExploitability`: `harm:SubversiveExploitation`; `harm:hasComparativeBaseline`: `harm:CounterfactualBaseline`; `harm:hasObjectOfHarm`: `harm:MaterialPecuniarySubstrate` | `harm:OpportunityCapabilitySubstrate`.

---

### Meta-Category III: `harm:DeontologicalRightsHarm`
* **skos:prefLabel:** Deontological & Rights-Based Harm (Normative Wrongs)
* **skos:altLabel:** Dignitary Harm | Rights-Violation Harm | Kantian Wronging
* **skos:definition:** At the highest level, this domain locates harm not in pain or lowered material welfare, but in the violation of formal rights, moral status, and rational autonomy. A person is harmed simply by being wronged.
* **skos:note:** Rather than measuring pain or lowered welfare, this category locates harm in the violation of a person's moral status, rational agency, or fundamental rights. A person is harmed when they are coerced, deceived, manipulated, or used merely as a tool for someone else's ends—even if the act produces pleasure or leaves their material welfare intact.
* **skos:scopeNote:** Inherently normative (the harm is the breach of right or duty; non-normative rights violations do not exist); occurs even if the act produces pleasure, leaves material welfare intact, or remains unperceived by the victim.
* **skos:historyNote:** Immanuel Kant formulated the Humanity Formula of the Categorical Imperative in Groundwork of the Metaphysics of Morals (1785). John Locke grounded harm in the violation of natural rights (life, liberty, and property) in his Second Treatise of Government (1689). Wesley Newcomb Hohfeld mapped the correlative relationship between rights and duties (1913).
* **dcterms:bibliographicCitation:** Kant, Immanuel. Groundwork of the Metaphysics of Morals (1785); Locke, John. Second Treatise of Government (1689); Hohfeld, Wesley Newcomb. Fundamental Legal Conceptions (1913).
* **Inherited Attribute Defaults:** `harm:hasNormativeStatus`: `harm:NormativeWrongful` | `harm:hasPhenomenologicalTransparency`: `harm:UnperceivedObjective` | `harm:hasModality`: `harm:ActualizedHarm`

#### 1. `harm:KantianDeontologicalHarm` (`rdfs:subClassOf harm:DeontologicalRightsHarm`)
* **skos:prefLabel:** Deontological Harm (Rights-Based / Dignitary Harm)
* **skos:altLabel:** Dignitary Harm | Rights-Violation Harm | Kantian Wronging
* **skos:definition:** Treating a rational agent merely as a means to an end through coercion, deception, or manipulation—violating their moral agency even if the act produces pleasure or leaves material welfare intact.
* **skos:note:** Locates the moral injury strictly in the disrespect of rational agency and natural rights rather than consequentialist outcomes.
* **skos:example:** Deceiving a person into consenting to a transaction, coercing someone's choice, or covertly manipulating a person's beliefs for third-party gain.
* **skos:historyNote:** Immanuel Kant (Humanity Formula of the Categorical Imperative, 1785); John Locke (Second Treatise of Government, 1689); extended by Onora O'Neill, Christine Korsgaard, and Avishai Margalit (humiliation in The Decent Society).
* **dcterms:bibliographicCitation:** Kant, Immanuel. Groundwork of the Metaphysics of Morals (1785); Locke, John. Second Treatise of Government (1689).

#### 2. `harm:InjuriaSineDamnoHarm` (`rdfs:subClassOf harm:DeontologicalRightsHarm`)
* **skos:prefLabel:** Rights-Based Harm Without Loss (Injuria Sine Damno)
* **skos:altLabel:** Injuria Sine Damno (legal injury without actual damage) | Technical Trespass | Constitutional Violation
* **skos:definition:** A distinct legal category where a person's formal legal or constitutional right is violated, even though they suffer zero physical pain, financial loss, or emotional distress.
* **skos:note:** Conversely, the law also recognizes Damnum Absque Injuria—real economic or physical harm (such as losing customers to a fair business competitor) that is not legally actionable because no legal right was violated.
* **skos:scopeNote:** Applies strictly where a formal legal or constitutional right is breached with zero physical pain, financial loss, or emotional distress; excludes factual setbacks where no legal right was violated (Damnum Absque Injuria).
* **skos:example:** An unauthorized, harmless entry onto land (technical trespass) or an unlawful denial of the right to vote.
* **skos:historyNote:** John Austin & Wesley Newcomb Hohfeld mapped the exact correlative relationship between a legal right and a legal duty in Fundamental Legal Conceptions (1913). Joel Feinberg bridged jurisprudence and moral philosophy in The Moral Limits of the Criminal Law (1984).
* **dcterms:bibliographicCitation:** Hohfeld, Wesley Newcomb. Fundamental Legal Conceptions (1913); Feinberg, Joel. The Moral Limits of the Criminal Law (1984).
* **Key Attribute Bindings:** `harm:hasObjectOfHarm`: `harm:NormativeStatusSubstrate`; `harm:hasSeverityMagnitude`: `harm:DeMinimisTrivial` (in material loss) to `harm:SevereRuinous` (in constitutional standing).

#### 3. `harm:EpistemicTestimonialHarm` (`rdfs:subClassOf harm:DeontologicalRightsHarm`)
* **skos:prefLabel:** Epistemic and Testimonial Harm
* **skos:altLabel:** Epistemic Injustice | Testimonial Injustice | Hermeneutical Injustice | Epistemic Violence
* **skos:definition:** Harming someone specifically in their capacity as a knower and rational communicator—either by unfairly deflating their credibility due to prejudice or by depriving them of the shared social concepts needed to articulate their own experiences.
* **skos:note:** Separates testimonial injustice (when prejudice causes a listener to deflate a speaker's credibility) from hermeneutical injustice (when a society lacks the shared concepts or vocabulary for a person to make sense of their own traumatic experiences).
* **skos:example:** Unfairly deflating a speaker's credibility in court or medicine due to identity prejudice; lacking shared social vocabulary to articulate workplace harassment or medical trauma.
* **skos:historyNote:** Miranda Fricker formalized Epistemic Injustice (2007), separating testimonial injustice from hermeneutical injustice. Gayatri Chakravorty Spivak introduced epistemic violence to describe how dominant discourses silence marginalized subjects' ways of knowing.
* **dcterms:bibliographicCitation:** Fricker, Miranda. Epistemic Injustice: Power and the Ethics of Knowing (2007); Spivak, Gayatri Chakravorty. "Can the Subaltern Speak?" (1988).
* **Key Attribute Bindings:** `harm:hasObjectOfHarm`: `harm:PsychologicalCognitiveSubstrate` | `harm:NormativeStatusSubstrate`; `harm:hasCausationMechanism`: `harm:StructuralAttribution`.

#### 4. `harm:FiduciaryBetrayalHarm` (`rdfs:subClassOf harm:DeontologicalRightsHarm`)
* **skos:prefLabel:** Fiduciary and Betrayal Harm
* **skos:altLabel:** Breach of Fiduciary Duty | Constructive Fraud | Abuse of Trust
* **skos:definition:** A normative wrong occurring when someone entrusted with loyal care over another's interests (a trustee, doctor, lawyer, or corporate director) engages in self-dealing or disloyalty.
* **skos:note:** Even if the beneficiary still makes a profit, the breach of the duty of loyalty itself is a legally actionable wrong requiring disgorgement.
* **skos:example:** A corporate director secretly profiting from a transaction adverse to the company, or a trustee engaging in undisclosed self-dealing even when the trust portfolio grows.
* **skos:historyNote:** Benjamin N. Cardozo defined the fiduciary standard as "not honesty alone, but the punctilio of an honor the most sensitive" in Meinhard v. Salmon (1928). Tamar Frankel systematized modern fiduciary law as a distinct legal category grounded in structural trust and vulnerability.
* **dcterms:bibliographicCitation:** Meinhard v. Salmon, 249 N.Y. 458 (1928) (Cardozo, C.J.); Frankel, Tamar. Fiduciary Law (2011).
* **Key Attribute Bindings:** `harm:hasObjectOfHarm`: `harm:DignitaryRelationalSubstrate` | `harm:NormativeStatusSubstrate`; `harm:hasRemedialDutyBearer`: `harm:PerpetratorAsRestorer` (Disgorgement of profits).

#### 5. `harm:CulturalEpistemicideHarm` (`rdfs:subClassOf harm:DeontologicalRightsHarm`)
* **skos:prefLabel:** Cultural Harm & Epistemicide
* **skos:altLabel:** Cultural Genocide | Epistemicide | Cultural Erasure | Linguicide
* **skos:definition:** The systematic destruction or erosion of a group's language, sacred heritage, collective memory, ways of knowing, or cultural identity. It is distinct from any individual property or bodily injury.
* **skos:note:** The patient is the group and its continuity across generations, not only its individual members. Epistemicide extends this to destroying a community's knowledge systems, including by displacing them with a dominant system of knowledge.
* **skos:scopeNote:** Collective in scope. For harm to an individual knower's credibility or interpretive resources, use `harm:EpistemicTestimonialHarm`.
* **skos:example:** Suppressing an Indigenous language through schooling policy; destroying sacred sites; low-resource languages and minority knowledge being crowded out as dominant-language AI systems become the default interface to information.
* **skos:historyNote:** Raphael Lemkin's original concept of genocide included the destruction of a group's culture. Boaventura de Sousa Santos developed "epistemicide" to describe the destruction of non-dominant knowledge systems.
* **dcterms:bibliographicCitation:** Lemkin, Raphael. Axis Rule in Occupied Europe (1944); Santos, Boaventura de Sousa. Epistemologies of the South: Justice Against Epistemicide (2014).
* **Key Attribute Bindings:** `harm:hasObjectOfHarm`: `harm:CulturalCollectiveIdentitySubstrate`; `harm:hasPatientOntology`: `harm:CollectiveArtificialPerson`; `harm:hasTemporalTrajectory`: `harm:SlowAccumulativeTrajectory`; `harm:hasReversibility`: `harm:IrreversibleHysteresis`; `harm:hasDistributionAggregation`: `harm:DiffuseThreshold`.
* **skos:changeNote:** Added in v2 (2026-11-13) from Master Formal Ontology §5.2 (truncated in the source; expanded here).

#### 6. `harm:CognitiveLibertyHarm` (`rdfs:subClassOf harm:DeontologicalRightsHarm`)
* **skos:prefLabel:** Cognitive Liberty & Autonomy Subversion
* **skos:altLabel:** Autonomy Subversion | Cognitive Manipulation | Mental Integrity Violation | Neuro-Rights Violation
* **skos:definition:** Hijacking an individual's belief formation, attention, or decision-making through deception, algorithmic dark patterns, synthetic media, or neurotechnical tampering. No physical coercion is involved, and the person's own mind is what is harmed.
* **skos:note:** Choice architecture is used as a weapon to bypass rational deliberation while preserving the *illusion* of voluntary consent. It differs from `harm:OpportunityCostChoiceHarm`, which measures the welfare *loss*, and from `harm:EpistemicPollutionHarm`, which concerns the *shared* information environment. Here the harm is the violation of the individual's cognitive liberty itself, whether or not any material loss follows.
* **skos:example:** A personalised persuasion system that steers a voter's beliefs; a deepfake engineered to change one person's decision; an addictive engagement loop tuned to a user's vulnerabilities; neural data used to influence behaviour.
* **skos:historyNote:** Behavioural economics (Kahneman, Thaler & Sunstein) mapped the cognitive biases that make subversion possible. Susser, Roessler & Nissenbaum defined online manipulation as hidden influence. Jan Christoph Bublitz and Nita Farahany developed cognitive liberty and mental integrity as rights-based concepts.
* **dcterms:bibliographicCitation:** Thaler, R. H., & Sunstein, C. R. (2008). *Nudge*. Yale University Press; Susser, D., Roessler, B., & Nissenbaum, H. (2019). "Online Manipulation: Hidden Influences in a Digital World." *Georgetown Law Technology Review*, 4(1), 1–45; Bublitz, J. C. "My Mind Is Mine!? Cognitive Liberty as a Legal Concept" (2013); Farahany, Nita A. The Battle for Your Brain (2023).
* **Key Attribute Bindings:** `harm:hasObjectOfHarm`: `harm:PsychologicalCognitiveSubstrate` | `harm:NormativeStatusSubstrate`; `harm:hasCognitiveExploitability`: `harm:SubversiveExploitation`; `harm:hasConsentStatus`: `harm:SubvertedConsent`; `harm:hasCausalVector`: `harm:InformationalAlgorithmicVector` | `harm:NeurotechnicalVector`; `harm:hasScalabilityAsymmetry`: `harm:ZeroMarginalCostReplication`.
* **skos:changeNote:** Added in v2 (2026-11-13) from Master Formal Ontology §4.2.

---

### Meta-Category IV: `harm:TeleologicalDeprivationHarm`
* **skos:prefLabel:** Teleological & Deprivation Harm (Privation of Good & Flourishing)
* **skos:altLabel:** Perfectionist Harm | Aretaic Harm | Privation of Flourishing | Deprivationism
* **skos:definition:** At the highest level, this domain defines harm structurally and comparatively across time: not by inflicting an active injury, but by blocking an entity from attaining the goods, capabilities, or future existence it ought naturally to possess or enjoy.
* **skos:note:** Rooted in classical virtue ethics and comparative deprivation theory. Allows for harm to occur even when a victim feels content, consents, or no longer exists (as in death).
* **skos:historyNote:** Aristotle defined the human good as eudaimonia in the Nicomachean Ethics. Thomas Aquinas developed the Privation Theory of Evil (privatio boni). Thomas Nagel articulated the modern Deprivation Account of death (1970).
* **dcterms:bibliographicCitation:** Aristotle. Nicomachean Ethics; Aquinas, Thomas. Summa Theologiae; Nagel, Thomas. "Death," Noûs (1970).
* **Inherited Attribute Defaults:** `harm:hasComparativeBaseline`: `harm:CounterfactualBaseline`; `harm:hasPhenomenologicalTransparency`: `harm:UnperceivedObjective`; `harm:hasTemporalTrajectory`: `harm:SlowAccumulativeTrajectory`

#### 1. `harm:PerfectionistTeleologicalHarm` (`rdfs:subClassOf harm:TeleologicalDeprivationHarm`)
* **skos:prefLabel:** Teleological Harm (Perfectionist / Eudaimonic Harm)
* **skos:altLabel:** Perfectionist Harm | Aretaic Harm | Privation of Flourishing
* **skos:definition:** Any impediment that prevents an entity from fulfilling its natural function, developing its core capabilities, or achieving human flourishing (eudaimonia), even if the person consents and feels content.
* **skos:note:** Views harm as the absence or corruption of a good that a being ought naturally to possess, such as intellectual growth, moral character, or community.
* **skos:example:** Corrupting a person's moral character, stunting intellectual development, or depriving an individual of meaningful social community.
* **skos:historyNote:** Aristotle (Nicomachean Ethics); Thomas Aquinas (Privation Theory of Evil / privatio boni).
* **dcterms:bibliographicCitation:** Aristotle. Nicomachean Ethics; Aquinas, Thomas. Summa Theologiae, I, q. 48.

#### 2. `harm:DeprivationHarm` (`rdfs:subClassOf harm:TeleologicalDeprivationHarm`)
* **skos:prefLabel:** Harm by Deprivation (Comparative Non-Existence / Omission)
* **skos:altLabel:** Deprivationism | Harm by Omission
* **skos:definition:** Blocking access to a good state a subject would otherwise have enjoyed—most notably death, which harms a person by depriving them of the future goods, experiences, and projects they would have had if they had continued living.
* **skos:note:** Resolves the Epicurean puzzle of how death harms the dead without requiring a conscious subject at the time of the loss.
* **skos:example:** Premature death depriving a person of future life projects and experiences, or wrongful omission blocking access to a life-saving opportunity.
* **skos:historyNote:** Lucretius explored the symmetry of pre-natal and post-mortem non-existence in De Rerum Natura. Thomas Nagel articulated the modern Deprivation Account in his seminal 1970 essay "Death".
* **dcterms:bibliographicCitation:** Lucretius. De Rerum Natura; Nagel, Thomas. "Death," Noûs (1970).

#### 3. `harm:CapabilityStructuralHarm` (`rdfs:subClassOf harm:TeleologicalDeprivationHarm`)
* **skos:prefLabel:** Capability Deprivation & Structural Harm
* **skos:altLabel:** Capability Deprivation | Structural Violence
* **skos:definition:** Systemic social, economic, or institutional barriers (such as lack of education, healthcare, or political voice) that prevent individuals from converting basic resources into real human functioning and agency.
* **skos:note:** Operates diffusely across institutions without requiring individual malice or a single visible assailant.
* **skos:example:** Systemic lack of access to basic education, preventive healthcare, clean water, or political representation preventing human flourishing.
* **skos:historyNote:** Amartya Sen & Martha Nussbaum formalized the Capabilities Approach, shifting welfare evaluation from raw resources to what people are actually able to do and become. Johan Galtung coined Structural Violence (1969).
* **dcterms:bibliographicCitation:** Sen, Amartya. Development as Freedom (1999); Nussbaum, Martha C. Creating Capabilities (2011); Galtung, Johan. "Violence, Peace, and Peace Research," Journal of Peace Research (1969).

#### 4. `harm:WrongfulDeathConsortiumHarm` (`rdfs:subClassOf harm:TeleologicalDeprivationHarm`)
* **skos:prefLabel:** Wrongful Death & Loss of Consortium
* **skos:altLabel:** Wrongful Death | Survival Actions | Loss of Consortium
* **skos:definition:** The direct legal translation of Deprivationism. Because the dead cannot sue for their own lost future, statutes grant surviving family members the right to recover for the deprivation of future financial support, companionship, guidance, and relational goods that death stole.
* **skos:note:** Overturned the ancient common-law rule (actio personalis moritur cum persona) that personal tort actions died with the victim.
* **skos:example:** A surviving spouse or child suing a negligent party for lost future financial support, parental guidance, and marital companionship following a fatal accident.
* **skos:historyNote:** Lord Campbell was the architect of the Fatal Accidents Act 1846 (Lord Campbell's Act). Roscoe Pound analyzed relational interests and family consortium as legally protected goods against third-party deprivation.
* **dcterms:bibliographicCitation:** Fatal Accidents Act 1846 (9 & 10 Vict. c. 93); Pound, Roscoe. "Individual Interests in the Domestic Relations," Michigan Law Review (1916).

#### 5. `harm:ParensPatriaePaternalisticHarm` (`rdfs:subClassOf harm:TeleologicalDeprivationHarm`)
* **skos:prefLabel:** Parens Patriae & Paternalistic Harm Prevention
* **skos:altLabel:** Parens Patriae | Legal Moralism | Soft Paternalism
* **skos:definition:** The legal operationalization of Teleological Harm. The state steps in to protect vulnerable persons (minors, incapacitated adults) or prohibit self-corrupting behaviors on the grounds that certain actions stunt human development and flourishing regardless of consent.
* **skos:note:** Justifies protective state intervention even when the protected party does not perceive harm or purports to consent.
* **skos:example:** Compulsory education laws, child labor bans, guardianship for incapacitated adults, or restrictions on severe self-harm.
* **skos:historyNote:** Patrick Devlin argued in The Enforcement of Morals (1965) that society has a legitimate interest in using law to preserve shared moral and developmental conditions. Ronald Dworkin analyzed the boundaries of paternalism in Taking Rights Seriously (1977).
* **dcterms:bibliographicCitation:** Devlin, Patrick. The Enforcement of Morals (1965); Dworkin, Ronald. Taking Rights Seriously (1977).

#### 6. `harm:AttachmentDevelopmentalHarm` (`rdfs:subClassOf harm:TeleologicalDeprivationHarm`)
* **skos:prefLabel:** Attachment, Developmental & Relational Deprivation
* **skos:altLabel:** Attachment Trauma | Adverse Childhood Experiences (ACEs) | Developmental Neglect
* **skos:definition:** Harm caused during critical neurodevelopmental windows by the absence of safe, responsive caregiving or social stimulation. Even without active physical abuse, early deprivation alters brain architecture, emotional regulation, and lifelong capacity for human flourishing.
* **skos:note:** Contributed by Psychologists & Behavioral Scientists. Demonstrates irreversible biological and psychological hysteresis resulting from early relational privation.
* **skos:example:** Severe institutional neglect in infancy or chronic emotional unavailability during critical childhood developmental windows impairing lifelong stress regulation and health.
* **skos:historyNote:** John Bowlby & Mary Ainsworth established Attachment Theory. Vincent Felitti & Robert Anda conducted the landmark ACE Study (1998), proving how early developmental stressors and neglect causally degrade adult health and life expectancy.
* **dcterms:bibliographicCitation:** Bowlby, John. Attachment and Loss (1969); Felitti, Vincent J., et al. "Relationship of Childhood Abuse and Household Dysfunction to Many of the Leading Causes of Death in Adults," American Journal of Preventive Medicine (1998).

---

### Meta-Category V: `harm:SystemicCyberneticHarm`
* **skos:prefLabel:** Systemic, Emergent & Cybernetic Harm (Network & Equilibrium Failures)
* **skos:altLabel:** Emergent Harm | Equilibrium Failure | Network Contagion Harm
* **skos:definition:** At the highest level, this domain defines harm not as a linear act by an agent against a victim, but as a destabilizing shift in a complex system, incentive structure, or information network. Harm emerges from feedback loops, misaligned equilibria, and scale—where individually rational or benign actions produce catastrophic collective or systemic breakdown.
* **skos:note:** Contributed by the Tri-Council Panel (Economists & Game Theorists, Technologists & AI Safety, Psychologists & Behavioral Scientists). Captures modern socio-technical harms that occur without a villain or direct rights violation.
* **skos:historyNote:** Rooted in mid-20th-century cybernetics (Norbert Wiener), strategic game theory (Thomas Schelling), commons governance (Elinor Ostrom), and modern AI alignment safety (Nick Bostrom).
* **dcterms:bibliographicCitation:** Wiener, Norbert. Cybernetics (1948); Schelling, Thomas C. Micromotives and Macrobehavior (1978); Ostrom, Elinor. Governing the Commons (1990); Bostrom, Nick. Superintelligence (2014).

#### 1. `harm:ExternalityCoordinationHarm` (`rdfs:subClassOf harm:SystemicCyberneticHarm`)
* **skos:prefLabel:** Negative Externalities & Coordination Failures
* **skos:altLabel:** Negative Externality | Nash Equilibrium Trap | Collective Action Failure
* **skos:definition:** Harm inflicted on uninvolved third parties as an unpriced byproduct of an economic transaction or strategic interaction, or situations where rational individual incentives lock all players into a mutually destructive outcome.
* **skos:note:** Occurs when private costs diverge from social costs or when strategic incentives prevent cooperative risk reduction.
* **skos:example:** Industrial pollution imposed on uninvolved downwind residents, systemic financial contagion, bank runs, or multi-party arms races.
* **skos:historyNote:** Arthur Pigou defined negative externalities in The Economics of Welfare (1920). Thomas Schelling demonstrated in Micromotives and Macrobehavior (1978) how small, non-malicious individual preferences aggregate into severe macro-level harm.
* **dcterms:bibliographicCitation:** Pigou, Arthur C. The Economics of Welfare (1920); Schelling, Thomas C. Micromotives and Macrobehavior (1978).

#### 2. `harm:InformationAsymmetryHarm` (`rdfs:subClassOf harm:SystemicCyberneticHarm`)
* **skos:prefLabel:** Information Asymmetry & Adverse Selection Harm
* **skos:altLabel:** Moral Hazard | Adverse Selection | Predatory Signalling
* **skos:definition:** Harm generated when one party exploits superior information to shift hidden risks onto another party, degrading market trust and causing systemic collapse.
* **skos:note:** Undercuts institutional stability and penalizes honest participants through hidden risk transfer.
* **skos:example:** Reckless financial risk-taking when losses are socialized onto taxpayers (moral hazard), opaque algorithmic pricing, or collapse of insurance/credit markets due to hidden risks.
* **skos:historyNote:** George Akerlof demonstrated in "The Market for 'Lemons'" (1970) how information asymmetry destroys functional markets. Joseph Stiglitz formalized the mechanics of screening, signaling, and systemic harm caused by asymmetric information.
* **dcterms:bibliographicCitation:** Akerlof, George A. "The Market for 'Lemons'," Quarterly Journal of Economics (1970); Stiglitz, Joseph E. "The Contributions of the Economics of Information to Twentieth Century Economics," QJE (2000).

#### 3. `harm:AlgorithmicAlignmentHarm` (`rdfs:subClassOf harm:SystemicCyberneticHarm`)
* **skos:prefLabel:** Algorithmic, Alignment & Emergent Scale Harm
* **skos:altLabel:** Specification Gaming | Reward Hacking | Distributional Shift | Systemic Algorithmic Bias
* **skos:definition:** Harm arising when an autonomous or automated system optimizes a proxy goal too literally, scales subtle historical biases across millions of decisions instantaneously, or fails catastrophically when deployed outside its training distribution—causing harm without human malice or conscious intent.
* **skos:note:** Driven by zero-marginal-cost digital replication, black-box opacity, and literal proxy optimization.
* **skos:example:** Automated hiring or lending models systematically excluding protected groups at scale, or an AI optimization system executing destructive shortcuts to maximize a flawed reward metric.
* **skos:historyNote:** Norbert Wiener warned in 1960 ("Some Moral and Technical Consequences of Automation") that automated systems given literal goals without human values will execute outcomes harmful to their creators. Stuart Russell & Nick Bostrom formalized the modern AI Alignment Problem and Instrumental Convergence.
* **dcterms:bibliographicCitation:** Wiener, Norbert. "Some Moral and Technical Consequences of Automation," Science (1960); Bostrom, Nick. Superintelligence (2014); Russell, Stuart. Human Compatible (2019).

#### 4. `harm:EpistemicPollutionHarm` (`rdfs:subClassOf harm:SystemicCyberneticHarm`)
* **skos:prefLabel:** Epistemic Pollution & Attention Hijacking
* **skos:altLabel:** Information Cascade | Algorithmic Radicalization | Attention Extraction
* **skos:definition:** The degradation of a society’s shared epistemic environment through synthetic media, automated outrage amplification, and variable-reward engagement loops. This harms both individual cognitive sovereignty and collective democratic sense-making.
* **skos:note:** Exploits innate cognitive biases while polluting the public information commons at exponential network speed.
* **skos:example:** Automated outrage amplification algorithms driving polarization, synthetic media flooding public discourse, or variable-reward social feeds hijacking human attention.
* **skos:historyNote:** Herbert A. Simon coined the Attention Economy (1971), noting that a wealth of information creates a poverty of attention. Cass Sunstein & Tristan Harris analyzed how algorithmic echo chambers and persuasive design hijack human cognitive vulnerabilities at scale.
* **dcterms:bibliographicCitation:** Simon, Herbert A. "Designing Organizations for an Information-Rich World" (1971); Sunstein, Cass R. #Republic (2017).

---

## Part 2: Cross-Cutting Attributes of Harm (`owl:ObjectProperty` & `skos:ConceptScheme`)

### Domain A: Epistemic & Causal Structure

1. **`harm:hasComparativeBaseline` (The Comparative Baseline — Counterfactual vs. Temporal)**
   * **Definition:** Measures whether a subject is worse off *now* than they were *before* the event (*Temporal Comparison*: `harm:TemporalBaseline`) or worse off *now* than they *would have been* had the event never occurred (*Counterfactual Comparison*: `harm:CounterfactualBaseline`, crucial for omissions and blocked opportunities).
   * **Domains of Applicability:** Contract & Commercial Law (*Expectation Damages*), Medical Malpractice (*Loss of Chance*), Intergenerational Ethics (*Non-Identity Problem*), Microeconomics (*Opportunity Cost*).
   * **v2 added value:** `harm:NonComparativeBaseline`: the subject is judged against an absolute threshold of a minimally decent state, because no counterfactual exists for that individual (non-identity cases; see `harm:NonComparativeHarm`). *skos:changeNote: added in v2 (2026-11-13).*

2. **`harm:hasCausationMechanism` (Causation, Proximity, and Attribution)**
   * **Definition:** Tethers an external state of affairs to an agent's action or omission via factual causation (`harm:FactualButForCausation`), proximate foreseeability (`harm:ProximateCausation`), simultaneous independent causes (`harm:OverdeterminedCausation`), or institutional/systemic causation (`harm:StructuralAttribution`).
   * **Domains of Applicability:** Tort & Criminal Liability, AI Alignment & Autonomous Systems ("responsibility gap"), Multi-Agent Game Theory.

20. **`harm:hasCausalVector` (Causal Vector — Medium or Pathway of Harm)** *(v2)*
   * **Definition:** The medium or pathway through which the source's action reaches the object of harm. Values: physical force (`harm:KineticVector`), chemical, thermal or biological agents (`harm:ChemicalBiologicalVector`), information and algorithms such as recommender systems, dark patterns and synthetic media (`harm:InformationalAlgorithmicVector`), money and markets (`harm:FinancialEconomicVector`), rules, policies and administrative processes (`harm:InstitutionalNormativeVector`), relationships and verbal or behavioural conduct (`harm:RelationalBehavioralVector`), and direct interfaces with the nervous system (`harm:NeurotechnicalVector`).
   * **Note:** Complements `harm:hasCausationMechanism`. That attribute says *how responsibility is attributed* (but-for, proximate, structural); this one says *what physically or informationally carried the harm*.
   * **Domains of Applicability:** Product Liability, AI Governance & Platform Regulation, Neurotechnology Law, Administrative Law.
   * *skos:changeNote:* Added in v2 (2026-11-13) from Master Formal Ontology attribute 10 (`hasCausalVector`).

3. **`harm:hasPhenomenologicalTransparency` (Phenomenological Transparency — Perceived vs. Unperceived)**
   * **Definition:** Distinguishes between subjective harms existing only inside conscious awareness (`harm:PerceivedSubjective` — pain, grief, terror) and objective harms existing in the world outside awareness (`harm:UnperceivedObjective` — damage to interests, dignity, or reputation even if never discovered).
   * **Domains of Applicability:** Animal Welfare & Bioethics, Privacy/Defamation/Fiduciary Law, Posthumous & Estate Law.

4. **`harm:hasSystemOpacity` (System Opacity & Legibility — Transparent vs. Black-Box)**
   * **Definition:** Measures whether the mechanism causing the harm can be inspected and audited (`harm:TransparentLegible`) or is obscured by deep neural network complexity, proprietary trade secrets, or distributed supply chains (`harm:BlackBoxOpaque`).
   * **Domains of Applicability:** Algorithmic Auditing (lending, hiring, sentencing), High-Frequency Financial Trading, Data-Broker Ecosystems.

---

### Domain B: Dynamic, Scaling & Magnitude Behavior

5. **`harm:hasTemporalTrajectory` (Temporal Trajectory — Acute, Latent, and Slow)**
   * **Definition:** Maps the geometry of harm across time: immediate impact and manifestation (`harm:AcuteTrajectory`), immediate exposure followed by decades of dormancy (`harm:LatentTrajectory`), or incremental generational degradation (`harm:SlowAccumulativeTrajectory`).
   * **Domains of Applicability:** Toxic Torts & Occupational Health (asbestos, radiation), Climate & Environmental Law (*Slow Violence*).
   * **v2 added values:** `harm:ChronicPersistentTrajectory`: an ongoing harm sustained at a roughly constant level while exposure continues, neither accumulating nor dormant (chronic pain, persistent harassment, continuous surveillance). `harm:TransientEpisodicTrajectory`: a harm that lasts only during exposure and ends when exposure ends (passing offense, temporary service outage). *skos:changeNote: added in v2 (2026-11-13).*

6. **`harm:hasDistributionAggregation` (Distribution & Aggregation — Concentrated vs. Diffuse)**
   * **Definition:** Measures spatial and population spread: a focused blow landing on a single identifiable victim (`harm:NarrowConcentrated`) versus microscopic losses spread across millions of people or tiny contributions crossing a collective tipping point (`harm:DiffuseThreshold`).
   * **Domains of Applicability:** Class Action & Consumer Protection Law, Data Privacy micro-leaks, Collective Action Ethics (*Harmless Torturer* paradox).

7. **`harm:hasFeedbackDynamics` (Feedback & Amplification Dynamics — Linear vs. Non-Linear)**
   * **Definition:** Measures whether damage remains proportional to initial force (`harm:LinearStatic`) or triggers self-reinforcing positive feedback loops, panic contagion, or algorithmic cascades (`harm:NonLinearAmplifying`).
   * **Domains of Applicability:** Systemic Financial Contagion (bank runs), Social Media Recommendation Algorithms, Networked Infrastructure cascades.

21. **`harm:hasConsequentialCascade` (Consequential & Cascading Harm Profile)** *(v2)*
   * **Definition:** The foreseeable downstream, secondary and cross-domain effects that follow from a primary harm, bounded by foreseeability. Values: immediate follow-on harms in the same domain (`harm:DirectConsequential`); harms that cross into another domain, such as discounted medical testimony leading to misdiagnosis and then physical injury (`harm:CrossDomainCascade`); harms magnified by a victim's pre-existing vulnerability, the eggshell-skull rule (`harm:VulnerabilityAmplification`); and effects too remote to attribute (`harm:RemoteCutoff`).
   * **Note:** Differs from `harm:hasFeedbackDynamics`. That attribute describes self-reinforcing *system* behaviour; this one traces a *single harm's* chain of consequences. The `harm:RemoteCutoff` value stops causal chains from running on forever.
   * **Domains of Applicability:** Tort Law (*Palsgraf* proximate cause, *Eggshell Skull* rule), Risk Science (second-order and cascading effects), AI Incident Analysis.
   * **dcterms:bibliographicCitation:** Palsgraf v. Long Island Railroad Co., 248 N.Y. 339 (1928); Hart, H.L.A., & Honoré, Tony. Causation in the Law (1959).
   * *skos:changeNote:* Added in v2 (2026-11-13) from Master Formal Ontology attribute 14 (`hasConsequentialCascade`).

8. **`harm:hasScalabilityAsymmetry` (Marginal Cost & Scalability Asymmetry)**
   * **Definition:** Captures the ratio between effort required to inflict harm and resulting damage: proportional human effort per victim (`harm:HighFrictionProportional`) versus replicating severe harm across millions of targets instantaneously at near-zero additional cost (`harm:ZeroMarginalCostReplication`).
   * **Domains of Applicability:** Cybersecurity & Ransomware, Synthetic Media & Deepfakes, Biosecurity & Dual-Use Research.

9. **`harm:hasReversibility` (Reversibility & Hysteresis — Restorable vs. Irreversible)**
   * **Definition:** Measures whether a harmed entity or system can return to its prior baseline once the harmful activity stops (`harm:RestorableElastic`, e.g., returning stolen funds) or permanently alters the system's path and structure (`harm:IrreversibleHysteresis`, e.g., extinction, severe developmental trauma).
   * **Domains of Applicability:** Environmental Conservation, Neurodevelopmental Psychology, Existential Risk & Restorative Justice.
   * **v2 added value:** `harm:PartiallyMitigable`: the harm can be reduced but not fully undone (chronic pain eased by treatment, trauma improved by therapy, reunification after a family separation that still leaves developmental effects). It sits between `harm:RestorableElastic` and `harm:IrreversibleHysteresis`, and it determines whether compensation alone can make the victim whole. *skos:changeNote: added in v2 (2026-11-13).*

10. **`harm:hasSeverityMagnitude` (Severity & Magnitude — De Minimis vs. Catastrophic)**
    * **Definition:** Measures the depth and intensity of the setback: barely noticeable/negligible (`harm:DeMinimisTrivial`), substantial and warranting restitution (`harm:ModerateCompensable`), life-altering or bankrupting (`harm:SevereRuinous`), or civilization/species-threatening (`harm:CatastrophicExistential`).
    * **Domains of Applicability:** Criminal & Tort Proportionality, Regulatory Exposure Thresholds, Existential Risk Ethics.

---

### Domain C: Normative & Strategic Context

11. **`harm:hasNormativeStatus` (Normativity vs. Non-Normativity — Setback vs. Wronging)**
    * **Definition:** Separates purely descriptive setbacks caused by nature or fair competition (`harm:NonNormativeSetback` / *Damnum Absque Injuria*) from wrongful setbacks caused by violating a moral duty or legal right (`harm:NormativeWrongful` / *Injuria*).
    * **Domains of Applicability:** Antitrust & Free Market Economics, Criminal & Constitutional Law (*Injuria Sine Damno*).

12. **`harm:hasModality` (Modality — Actualized vs. Probabilistic Risk)**
    * **Definition:** Distinguishes between damage that has already materialized (`harm:ActualizedHarm`) and the imposition of heightened danger that narrows a victim's safe life options before physical injury occurs (`harm:ProbabilisticRisk`).
    * **Domains of Applicability:** Public Health & FDA Safety Regulation, Reckless Endangerment Law, Nuclear & Existential Risk Ethics.
   * **v2 added value:** `harm:ImminentThreat`: harm that is concrete and close in time but has not yet materialised. It sits between actualised harm and diffuse probabilistic risk, and is the threshold for criminal attempt, threats, and emergency injunctive relief. *skos:changeNote: added in v2 (2026-11-13).*

13. **`harm:hasIncentiveAlignment` (Incentive & Strategic Alignment — Malicious vs. Structural/Emergent)**
    * **Definition:** Identifies the motivational architecture producing the harm: deliberate cruelty (`harm:MaliciousIntentional`), careless disregard (`harm:NegligentCareless`), or agents/AI systems following rational incentives or literal proxy goals that produce collateral damage without hostility (`harm:StructurallyAlignedEmergent`).
    * **Domains of Applicability:** Game-Theoretic Market Failures (*Tragedy of the Commons*), Principal-Agent Moral Hazard, AI Specification Gaming.

14. **`harm:hasCognitiveExploitability` (Cognitive & Volitional Exploitability — Coercive vs. Subversive)**
    * **Definition:** Measures whether harm overrides a victim's will through brute force or explicit threats (`harm:OvertCoercion`) or bypasses rational defenses by exploiting cognitive biases, addiction pathways, or emotional vulnerabilities (`harm:SubversiveExploitation`).
    * **Domains of Applicability:** Behavioral Economics & Consumer Protection (dark patterns, sludge), Persuasive Technology & Addiction, Undue Influence Law.

22. **`harm:hasConsentStatus` (Consent & Voluntariness)** *(v2)*
   * **Definition:** Whether the patient validly consented to the act or exposure. Values: informed, capable and freely given (`harm:ValidConsent`); obtained by threat or force (`harm:CoercedConsent`); obtained by deception or by hiding material facts (`harm:DeceivedConsent`); produced by manipulation that bypasses deliberation (`harm:SubvertedConsent`); impossible because the patient lacks capacity, as with children, incapacitated adults or future generations (`harm:IncapableOfConsent`); or exposure with no reasonable way out (`harm:CaptiveExposure`).
   * **Note:** The main validity filter. Valid consent (*volenti non fit injuria*) can turn an apparent harm into a permissible interaction, while every other value defeats that defence. Differs from `harm:hasCognitiveExploitability`, which describes the *mechanism* of influence rather than whether the resulting consent is *valid*. Relevant to AI terms of service, clickwrap agreements and data-use consent.
   * **Domains of Applicability:** Medical & Research Ethics (informed consent), Contract & Consumer Law, Data Protection Law, Criminal Law (*volenti* defence).
   * **dcterms:bibliographicCitation:** Feinberg, Joel. The Moral Limits of the Criminal Law, Vol. 3: Harm to Self (1986).
   * *skos:changeNote:* Added in v2 (2026-11-13) from Master Formal Ontology attribute 9 (`hasConsentStatus`).

---

### Domain D: Relational Roles, Object & Standing

15. **`harm:hasPatientOntology` (Patient Ontology — Who or What Can Be Harmed?)**
    * **Definition:** Defines the ontological boundary of entities capable of holding interests or suffering setbacks: humans and animals capable of experience (`harm:SentientIndividual`), corporations, states, and cultural groups (`harm:CollectiveArtificialPerson`), and ecosystems, rivers, or future unconceived generations (`harm:NonSentientSystem`).
    * **Domains of Applicability:** Bioethics, Corporate & International Law, Environmental Personhood, Intergenerational Justice.

16. **`harm:hasPerpetrator` (Moral & Legal Agency — The Perpetrator / Causal Source)**
    * **Definition:** Defines the nature, culpability, and structure of the entity from which the harm originates: single human acting with *mens rea* (`harm:UnitaryIntentionalAgent`), employer/principal held liable (`harm:VicariouslyLiablePrincipal`), distributed human actors (`harm:DiffuseCollectivePerpetrator`), or natural forces/autonomous AI systems (`harm:NonAgenticAutonomousSource`).
    * **Domains of Applicability:** Criminal Law (*mens rea*), Tort & Product Liability (*respondeat superior*, strict liability), AI & Robotics Governance.

23. **`harm:hasSecondaryAgent` (Secondary & Complicit Agency)** *(v2)*
    * **Definition:** Actors who do not carry out the primary harmful act but bear moral or legal responsibility because they enabled it. Values: supplying the means, such as weapons, tools, models, compute or data (`harm:MaterialFacilitation`); responsibility through an employment or authority relationship (`harm:VicariousAgency`); encouraging, ordering or coordinating the act (`harm:InstigationConspiracy`); a duty-holder failing to stop a known risk, such as auditors, moderators or reviewers ignoring reports (`harm:GatekeeperNegligence`); and contributing to the norms, incentives or infrastructure that make the harm likely (`harm:SystemicContribution`).
    * **Note:** Spreads responsibility across organisational and technical networks, where facilitators and gatekeepers enable harm without carrying it out. In AI harm this separates the model developer, deployer, platform, data supplier and auditor. Where the primary source is non-agentic (`harm:NonAgenticAutonomousSource`), accountability shifts mainly to secondary and protective agents.
    * **Domains of Applicability:** Criminal Law (complicity, accomplice liability), Tort Law (vicarious and contributory liability), AI Supply-Chain Governance, Platform Liability.
    * **dcterms:bibliographicCitation:** Kutz, Christopher. Complicity: Ethics and Law for a Collective Age (2000); Kadish, Sanford H. "Complicity, Cause and Blame: A Study in the Interpretation of Doctrine," California Law Review (1985).
    * *skos:changeNote:* Added in v2 (2026-11-13) from Master Formal Ontology attribute 17 and Part 2A (`hasSecondaryAgent`).

24. **`harm:hasBeneficiaryRole` (Beneficiary & Value-Capture Role)** *(v2)*
    * **Definition:** Who captures financial gain, avoided compliance costs, competitive advantage, power or utility from the harm. This separates *causing* the harm from *profiting* by it. Values: the direct perpetrator (`harm:PerpetratorBeneficiary`); the principal or institution that employs or deploys the perpetrator (`harm:PrincipalInstitutionalBeneficiary`); downstream market actors who profit without directing the harm, such as advertisers, shareholders or platforms monetising engagement (`harm:DownstreamMarketBeneficiary`); and cases with no material beneficiary (`harm:NoBeneficiary`).
    * **Note:** Makes externalities visible: the party that profits is often not the party that causes the harm or the one that pays for it. This is central to structural and AI-industry harms.
    * **Domains of Applicability:** Unjust Enrichment & Disgorgement Law, Welfare Economics (externalities, moral hazard), Political Philosophy (benefiting from injustice), Corporate & Securities Disclosure.
    * **dcterms:bibliographicCitation:** Pigou, Arthur C. The Economics of Welfare (1920); Coase, Ronald H. "The Problem of Social Cost," Journal of Law and Economics (1960); Young, Iris Marion. Responsibility for Justice (2011); Butt, Daniel. "On Benefiting from Injustice," Canadian Journal of Philosophy (2007).
    * *skos:changeNote:* Added in v2 (2026-11-13) from Master Formal Ontology attribute 18 (`hasBeneficiaryRole`).

17. **`harm:hasVictim` (Victimhood & Standing — The Recipient / Moral Patient)**
    * **Definition:** Maps the concrete relational position of the party suffering the setback: immediate target (`harm:DirectPrimaryVictim`), party harmed via legal or emotional tether (`harm:SecondaryRelationalVictim`), or unidentifiable future generations/public requiring a legal proxy (`harm:DiffuseRepresentativeClass`).
    * **Domains of Applicability:** Constitutional & Civil Procedure (*Locus Standi*), Victimology & Restorative Justice.

18. **`harm:hasObjectOfHarm` (Object of Harm — Locus of Injury / Protected Substrate)**
    * **Definition:** Defines the specific asset, faculty, or state of being that absorbs the setback: physical body/health (`harm:SomaticBiologicalSubstrate`), mental tranquility/attention/cognition (`harm:PsychologicalCognitiveSubstrate`), property/wealth/expectancy (`harm:MaterialPecuniarySubstrate`), reputation/privacy/consortium/trust (`harm:DignitaryRelationalSubstrate`), constitutional/voting/moral status (`harm:NormativeStatusSubstrate`), developmental potential/survival odds (`harm:OpportunityCapabilitySubstrate`), or shared ecology/epistemic commons (`harm:SystemicEnvironmentalSubstrate`).
    * **Domains of Applicability:** Legal Pleading & Remedies, Insurance & Actuarial Underwriting, Bioethics & Neuro-Rights.
    * **v2 added value:** `harm:CulturalCollectiveIdentitySubstrate`: a group's language, heritage, collective memory, knowledge systems and cultural continuity, held by the group rather than by any one member (see `harm:CulturalEpistemicideHarm`). *skos:changeNote: added in v2 (2026-11-13).*

19. **`harm:hasRemedialDutyBearer` (Remedial & Protective Duty-Bearing — Rescuer / Mitigator / Restorer)**
    * **Definition:** Defines the entity bearing an affirmative obligation to intervene, rescue, minimize ongoing impact, or restore the victim: the wrongdoer owing restitution (`harm:PerpetratorAsRestorer`), fiduciaries/parents/common carriers (`harm:SpecialRelationshipRescuer`), the state/responders/insurers (`harm:InstitutionalSovereignGuarantor`), or the victim's own duty not to worsen injury (`harm:VictimDutyToMitigate`).
    * **Domains of Applicability:** Tort & Contract Remedies (*Avoidable Consequences Doctrine*, *duty to rescue*), Administrative & Disaster Law (*parens patriae*), Humanitarian Law (*Responsibility to Protect*).
    * **v2 added values:** `harm:RegulatoryAuthority`: agencies with a duty to prevent or police harm (consumer protection, election, data protection or AI safety regulators). `harm:Whistleblower`: insiders or allies who expose harm and bear personal risk for doing so. `harm:RestorativeAgent`: clinicians, therapists and repair specialists who restore the victim after harm.
    * **v2 scope clarification:** In v2 this attribute names *who* protects or restores. The non-agentic *tools* they use are in attribute 25, and the *remedies* that resolve the harm are in attribute 26. *skos:changeNote: added in v2 (2026-11-13), from Master Formal Ontology attribute 19 (`hasProtectiveAgent`).*

---

### Domain E: Protection, Remedy & Accountability *(v2)*

25. **`harm:hasMitigatingMechanism` (Protective & Mitigating Mechanisms — Non-Agentic Safeguards)** *(v2)*
    * **Definition:** The non-agentic tools, engineering controls, legal instruments and institutional protocols that protective agents use *before or during* harm to block, interrupt or limit it. Values: engineering and technical controls such as kill-switches, interlocks, encryption, rate limits, model guardrails and content provenance watermarks (`harm:TechnicalControl`); procedures and protocols such as triage, review gates, red-teaming and incident response (`harm:ProceduralProtocol`); legal instruments such as restraining orders, *habeas corpus*, recalls and injunctions (`harm:LegalInstrument`); and design-level friction such as cooling-off prompts, opt-in defaults and content warnings (`harm:DesignFriction`).
    * **Note:** Keeps *agents* (attribute 19) separate from the *instruments* they use. AI guardrails, monitoring and safety evaluations belong here, so it's possible to ask whether a safeguard existed, whether it was deployed, and whether it failed.
    * **Domains of Applicability:** Safety Engineering, AI Safety & Model Governance, Product Safety Regulation, Emergency Law.
    * **dcterms:bibliographicCitation:** Shue, Henry. Basic Rights: Subsistence, Affluence, and U.S. Foreign Policy (1980).
    * *skos:changeNote:* Added in v2 (2026-11-13) from Master Formal Ontology attribute 20 (`hasMitigatingMechanism`).

26. **`harm:hasAccountabilityMechanism` (Remedial & Accountability Mechanism — Ex-Post Resolution)** *(v2)*
    * **Definition:** The legal, financial, punitive or structural remedies used *after* harm to compensate victims, take back unjust gains, punish, and deter. Values: compensation for actual loss (`harm:CompensatoryDamages`); damages that recognise a rights violation or punish egregious conduct (`harm:NominalPunitiveDamages`); stripping profits gained from the harm (`harm:Disgorgement`); court-ordered changes to systems or institutions, including receivership (`harm:StructuralInjunction`); criminal penalties such as fines or imprisonment (`harm:CriminalSanction`); administrative fines, product bans or mandated deletion of models and data, also called algorithmic disgorgement or unlearning (`harm:RegulatorySanction`); and acknowledgement, apology and repair processes (`harm:RestorativeRecognition`).
    * **Note:** Each remedy should match its diagnosis: compensatory damages for counterfactual losses, nominal or punitive damages for rights violations, disgorgement for unjust enrichment (attribute 24), and structural injunctions for systemic harms. A mismatch, such as only a fine for a systemic harm, is itself an analysable gap in accountability.
    * **Domains of Applicability:** Tort & Contract Remedies, Criminal Sentencing, Regulatory Enforcement, Restorative Justice, AI Liability Regimes.
    * *skos:changeNote:* Added in v2 (2026-11-13) from Master Formal Ontology attribute 21 (`hasAccountabilityMechanism`).

---

# Part B: Benefit Mirror *(v2a, stage 1 skeleton)*

> [!todo] Drafted, not yet reviewed
> B.0–B.3 hold the skeleton; the one-line definitions in those tables are superseded by the full descriptions in B.4–B.5. B.6 holds history notes and citations, which were sourced rather than inverted. Open sources are flagged in B.6.

**Scope:** benefit *derived from harm* (value capture), not benefit in general.

## B.0 Serialization conventions (keeps benefit from being inferred as harm)

1. `harm:ValueCapture` is a top class. It is **not** a subclass of `harm:Harm`, and the two are declared `owl:disjointWith`.
2. Every benefit-side property has `rdfs:domain harm:ValueCapture`.
3. Where an attribute applies to both sides, a **parent property** with no `rdfs:domain` holds the shared range. The harm-side property (unchanged name, domain `harm:Harm`) and the benefit-side property (new name, domain `harm:ValueCapture`) are each `rdfs:subPropertyOf` the parent. Value vocabularies are shared, not copied.
4. Naming: parents `harm:hasEvent…`; benefit-side properties `harm:hasBenefit…` or a distinct benefit term; value-vocabulary classes `harm:…Value`, as in v1.
5. Existing v2 harm-side properties gain only an `rdfs:subPropertyOf` statement. Nothing else about them changes.

## B.1 Linking structure

| Term | Type | Domain → Range | Placeholder definition |
|---|---|---|---|
| `harm:ValueCapture` | `owl:Class`, `skos:Concept` (top concept) | — | A gain captured by some party that derives from a harm. |
| `harm:derivesFrom` | `owl:ObjectProperty` | `ValueCapture` → `Harm` | The harm from which this gain is captured. |
| `harm:yieldsValueCapture` | `owl:ObjectProperty`, `owl:inverseOf harm:derivesFrom` | `Harm` → `ValueCapture` | A gain captured from this harm. |

## B.2 Class layer: kinds of value capture

```text
harm:ValueCapture
├── I. harm:ExperientialGain            (mirrors ExperientialHarm)
│   ├── harm:GratificationGain
│   └── harm:DominanceSatisfactionGain
├── II. harm:MaterialPecuniaryGain      (mirrors WelfareInterestHarm)
│   ├── harm:DirectProfitGain
│   ├── harm:AvoidedCostGain
│   └── harm:AssetDataAccumulationGain
├── III. harm:WrongfulGain              (mirrors DeontologicalRightsHarm)
│   ├── harm:UnjustEnrichmentGain
│   └── harm:FiduciaryBreachGain        (pairs with FiduciaryBetrayalHarm)
├── IV. harm:CapabilityPositionalGain   (mirrors TeleologicalDeprivationHarm)
│   ├── harm:CompetitiveAdvantageGain
│   ├── harm:PowerInfluenceGain
│   └── harm:OpportunityCaptureGain
└── V. harm:SystemicRentGain            (mirrors SystemicCyberneticHarm)
    ├── harm:RentExtractionGain
    ├── harm:NetworkLockInGain
    ├── harm:AttentionCaptureGain       (pairs with EpistemicPollutionHarm)
    └── harm:RegulatoryArbitrageGain
```

## B.3 Attributes

### B1. Structural relation

| # | Property | Range (values) | Placeholder definition |
|---|---|---|---|
| B1 | `harm:hasValueRelation` | `ValueRelationValue`: `TransferRelation`, `CostAvoidanceRelation`, `ValueCreationFromHarmRelation`, `PositionalRelation` | How the gain relates to the loss: moved from the victim, saved by shifting costs, newly produced by harming, or relative only. No harm-side counterpart. |

### B2–B13. Shared attributes (parent property + benefit-side property)

| # | Parent (no domain) | Harm side (existing) | Benefit side (new) | Shared range |
|---|---|---|---|---|
| B2 | `harm:hasEventTemporalTrajectory` | `harm:hasTemporalTrajectory` (5) | `harm:hasBenefitTemporalTrajectory` | `TemporalTrajectoryValue` |
| B3 | `harm:hasEventDistributionAggregation` | `harm:hasDistributionAggregation` (6) | `harm:hasBenefitDistributionAggregation` | `DistributionAggregationValue` |
| B4 | `harm:hasEventFeedbackDynamics` | `harm:hasFeedbackDynamics` (7) | `harm:hasBenefitFeedbackDynamics` | `FeedbackDynamicsValue` |
| B5 | `harm:hasEventScalabilityAsymmetry` | `harm:hasScalabilityAsymmetry` (8) | `harm:hasBenefitScalabilityAsymmetry` | `ScalabilityAsymmetryValue` |
| B6 | `harm:hasEventReversibility` | `harm:hasReversibility` (9) | `harm:hasBenefitReversibility` (can the gain be clawed back?) | `ReversibilityValue` |
| B7 | `harm:hasEventMagnitude` | `harm:hasSeverityMagnitude` (10) | `harm:hasBenefitMagnitude` | `SeverityMagnitudeValue` |
| B8 | `harm:hasEventNormativeStatus` | `harm:hasNormativeStatus` (11) | `harm:hasBenefitNormativeStatus` | `NormativeStatusValue` |
| B9 | `harm:hasEventModality` | `harm:hasModality` (12) | `harm:hasBenefitModality` (actual vs expected gain) | `ModalityValue` |
| B10 | `harm:hasEventIncentiveAlignment` | `harm:hasIncentiveAlignment` (13) | `harm:hasBenefitIncentiveAlignment` | `IncentiveAlignmentValue` |
| B11 | `harm:hasEventPhenomenologicalTransparency` | `harm:hasPhenomenologicalTransparency` (3) | `harm:hasBenefitVisibility` (is the gain visible?) | `PhenomenologicalTransparencyValue` |
| B12 | `harm:hasEventSystemOpacity` | `harm:hasSystemOpacity` (4) | `harm:hasBenefitSystemOpacity` | `SystemOpacityValue` |
| B13 | `harm:hasEventConsequentialCascade` | `harm:hasConsequentialCascade` (21) | `harm:hasBenefitCascade` (compounding downstream gains) | `ConsequentialCascadeValue` (new value class: v2 attribute 21 has no `.ttl` yet) |

### B14–B23. Mirrored attributes (benefit side only, domain `harm:ValueCapture`)

| # | Property | Mirrors | Range (values) | Placeholder definition |
|---|---|---|---|---|
| B14 | `harm:hasValueCaptureChannel` | `hasCausalVector` (20) | `ValueCaptureChannelValue`: `DirectTransferChannel`, `MarketPricingChannel`, `CostExternalisationChannel`, `AssetAccumulationChannel`, `PositionalPowerChannel`, `IntermediatedBookingChannel` | The medium or pathway by which value reaches the beneficiary. |
| B15 | `harm:hasFormOfValue` | `hasObjectOfHarm` (18) | `FormOfValueValue`: `FinancialValue`, `AvoidedCostValue`, `DataValue`, `AttentionValue`, `PowerValue`, `LegitimacyReputationValue`, `UtilityValue` | What kind of value is captured. |
| B16 | `harm:hasBeneficiaryOntology` | `hasPatientOntology` (15) | `BeneficiaryOntologyValue`: `IndividualBeneficiary`, `CorporateBeneficiary`, `StateBeneficiary`, `DiffuseShareholderBeneficiary`, `NonHumanSystemBeneficiary` | What kind of entity captures the value. |
| B17 | `harm:hasBeneficiaryStanding` | `hasVictim` (17) | `BeneficiaryStandingValue`: `DirectBeneficiary`, `IndirectBeneficiary`, `DiffuseBeneficiaryClass` | How directly the beneficiary stands to the gain. |
| B18 | `harm:hasGainBaseline` | `hasComparativeBaseline` (1) | `GainBaselineValue`: `LawfulCounterfactualBaseline`, `CompetitiveNormBaseline`, `TemporalGainBaseline` | What the gain is measured against. |
| B19 | `harm:hasCaptureAttribution` | `hasCausationMechanism` (2) | `CaptureAttributionValue`: `DirectTraceableAttribution`, `ProximateAttribution`, `StructuralAttribution` | How directly the gain traces to the harm (relevant to disgorgement). |
| B20 | `harm:hasBeneficiaryKnowledge` | `hasConsentStatus` (22) | `BeneficiaryKnowledgeValue`: `KnowingBeneficiary`, `WilfullyBlindBeneficiary`, `UnawareBeneficiary` | What the beneficiary knew about the harm behind the gain. |
| B21 | `harm:hasValueCaptureIntermediary` | `hasPerpetrator` (16) / `hasSecondaryAgent` (23) | `ValueCaptureIntermediaryValue`: `ShellEntityIntermediary`, `PlatformIntermediary`, `ContractorIntermediary`, `FinancialIntermediary` | Entities that route value to the beneficiary. |
| B22 | `harm:hasCaptureBarrier` | `hasMitigatingMechanism` (25) | `CaptureBarrierValue`: `ProfitCapBarrier`, `StructuralSeparationBarrier`, `TransparencyRuleBarrier`, `ConflictOfInterestRuleBarrier` | Non-agentic safeguards that block profiting from harm. |
| B23 | `harm:hasRecaptureMechanism` | `hasAccountabilityMechanism` (26) | `RecaptureMechanismValue`: `Disgorgement` (shared with 26), `ClawbackRecapture`, `WindfallTaxRecapture`, `BenefitSharingRecapture`, `RestitutionToVictim` | Ex-post ways to take the gain back. |

### Addition to an existing harm-side attribute

* `harm:hasBeneficiaryRole` (24): adds value `harm:FacilitatorBeneficiary`, an enabler (attribute 23) who is also paid for enabling, such as a data supplier or compute provider. Enabling and benefiting remain independent; this value covers the case where both apply.

### Harm attributes with no benefit counterpart

* `hasCognitiveExploitability` (14): its role is taken by B20.
* `hasRemedialDutyBearer` (19): covered by B23.
* `hasPatientOntology`, `hasPerpetrator`, `hasVictim`, `hasObjectOfHarm`, `hasCausalVector`, `hasComparativeBaseline`, `hasCausationMechanism`, `hasConsentStatus`, `hasMitigatingMechanism`, `hasAccountabilityMechanism`, `hasSecondaryAgent`: mirrored by separate properties (B14–B23) rather than shared, because their values differ.

## B.4 Class descriptions *(stage 2)*

### Top class: `harm:ValueCapture`
* **skos:prefLabel:** Value Capture (Harm-Derived Benefit)
* **skos:altLabel:** Harm-Derived Gain | Benefit from Harm | Wrongful Gain (broad sense)
* **skos:definition:** A gain in money, avoided cost, data, attention, power, position, gratification or utility that some party captures *because* a harm occurred. It is linked to that harm by `harm:derivesFrom`.
* **skos:note:** The counterpart of `harm:Harm`. A harm describes what a victim loses; a value capture describes what someone else gains. The two are rarely equal in size, timing or visibility, and are often held by different parties. That gap is what this part of the ontology exists to show.
* **skos:scopeNote:** Covers only gains that derive from a harm. Gains from lawful, harmless activity are out of scope. A value capture can exist even where no one intended the harm and the beneficiary did not know of it (see B20).
* **skos:example:** Advertising revenue from engagement driven by outrage; compliance costs saved by skipping a safety review; a training dataset assembled from scraped personal data that keeps producing returns.

### I. `harm:ExperientialGain` (mirrors `harm:ExperientialHarm`)
* **skos:prefLabel:** Experiential Gain (Subjective Satisfaction from Harm)
* **skos:altLabel:** Hedonic Gain | Gratification from Harm
* **skos:definition:** A pleasant or satisfying conscious state that a party experiences because another suffers a harm.
* **skos:note:** Where experiential harm locates injury in felt suffering, experiential gain locates benefit in felt satisfaction. It is usually the smallest gain in money terms and often the strongest motive.
* **skos:scopeNote:** Restricted to sentient beneficiaries. Material profits that also bring satisfaction belong under `harm:MaterialPecuniaryGain`.
* **Key Attribute Bindings:** `harm:hasFormOfValue`: `harm:UtilityValue`; `harm:hasBeneficiaryOntology`: `harm:IndividualBeneficiary`; `harm:hasValueRelation`: `harm:PositionalRelation` | `harm:ValueCreationFromHarmRelation`.

#### `harm:GratificationGain` (`rdfs:subClassOf harm:ExperientialGain`)
* **skos:prefLabel:** Gratification Gain
* **skos:altLabel:** Schadenfreude | Entertainment from Harm
* **skos:definition:** Pleasure or amusement taken in another's misfortune, humiliation or pain.
* **skos:example:** Audiences who seek out and share humiliating synthetic media of a person; spectators of pile-ons.
* **Key Attribute Bindings:** `harm:hasBeneficiaryStanding`: `harm:DiffuseBeneficiaryClass`; `harm:hasBeneficiaryKnowledge`: `harm:KnowingBeneficiary`.

#### `harm:DominanceSatisfactionGain` (`rdfs:subClassOf harm:ExperientialGain`)
* **skos:prefLabel:** Dominance Satisfaction Gain
* **skos:altLabel:** Control Satisfaction | Gain from Coercive Control
* **skos:definition:** The felt satisfaction of control, superiority or revenge that a perpetrator gains from harming a specific person.
* **skos:example:** An abuser using stalkerware to monitor a partner; a harasser who targets someone with fabricated images.
* **Key Attribute Bindings:** `harm:hasBeneficiaryRole` (on the harm): `harm:PerpetratorBeneficiary`; `harm:hasBeneficiaryStanding`: `harm:DirectBeneficiary`.

### II. `harm:MaterialPecuniaryGain` (mirrors `harm:WelfareInterestHarm`)
* **skos:prefLabel:** Material & Pecuniary Gain
* **skos:altLabel:** Financial Gain from Harm | Economic Benefit
* **skos:definition:** An improvement in a party's money, assets or cost position, compared with what it would have been had the harm not occurred.
* **skos:note:** Mirrors the counterfactual logic of welfare harm: the beneficiary is better off than in the lawful, harmless counterfactual. This is the form that law most readily measures and recovers.
* **skos:scopeNote:** Includes avoided costs, which often leave no trace in accounts because they are expenses that never happened.
* **Key Attribute Bindings:** `harm:hasGainBaseline`: `harm:LawfulCounterfactualBaseline`; `harm:hasFormOfValue`: `harm:FinancialValue` | `harm:AvoidedCostValue` | `harm:DataValue`.

#### `harm:DirectProfitGain` (`rdfs:subClassOf harm:MaterialPecuniaryGain`)
* **skos:prefLabel:** Direct Profit Gain
* **skos:definition:** Revenue or profit earned directly from the harmful act or product.
* **skos:example:** Fees from a scam service; sales of a product known to be dangerous; subscription income from an app built on deceptive design.
* **Key Attribute Bindings:** `harm:hasValueRelation`: `harm:TransferRelation` | `harm:ValueCreationFromHarmRelation`; `harm:hasValueCaptureChannel`: `harm:DirectTransferChannel` | `harm:MarketPricingChannel`.

#### `harm:AvoidedCostGain` (`rdfs:subClassOf harm:MaterialPecuniaryGain`)
* **skos:prefLabel:** Avoided Cost Gain
* **skos:altLabel:** Cost Externalisation Gain | Savings from Negligence
* **skos:definition:** Money a party keeps by not paying for safety, compliance, testing, labour protections or clean-up, so that the cost falls on others as harm.
* **skos:note:** The direct counterpart of `harm:ExternalityCoordinationHarm`. It is probably the most common and least visible gain in AI-industry harms: the saving appears as speed or margin, never as a line item.
* **skos:example:** Releasing a model without red-teaming to reach market first; paying content moderators too little to cover their psychological care; siting a data centre where water costs are borne by local residents.
* **Key Attribute Bindings:** `harm:hasValueRelation`: `harm:CostAvoidanceRelation`; `harm:hasValueCaptureChannel`: `harm:CostExternalisationChannel`; `harm:hasBenefitVisibility`: `harm:UnperceivedObjective`.

#### `harm:AssetDataAccumulationGain` (`rdfs:subClassOf harm:MaterialPecuniaryGain`)
* **skos:prefLabel:** Asset & Data Accumulation Gain
* **skos:altLabel:** Data Extraction Gain | Accumulated Capital from Harm
* **skos:definition:** A lasting stock of data, models, intellectual property or other assets acquired through a harm, which keeps producing returns after the harm itself has ended.
* **skos:note:** Unlike a one-off profit, an accumulated asset compounds. A dataset taken without consent may be used for years, so the gain keeps growing while the harm stays fixed in the past.
* **skos:example:** Personal data collected through deceptive consent flows; creative works scraped and used to train a commercial model.
* **Key Attribute Bindings:** `harm:hasValueCaptureChannel`: `harm:AssetAccumulationChannel`; `harm:hasBenefitTemporalTrajectory`: `harm:SlowAccumulativeTrajectory`; `harm:hasBenefitReversibility`: `harm:IrreversibleHysteresis`.

### III. `harm:WrongfulGain` (mirrors `harm:DeontologicalRightsHarm`)
* **skos:prefLabel:** Wrongful Gain (Gain through a Wrong)
* **skos:altLabel:** Unjust Gain | Ill-Gotten Gain
* **skos:definition:** A gain that is objectionable because of *how* it was obtained, through violating someone's rights or a duty owed to them, whatever its size.
* **skos:note:** Deontological harm says a person can be harmed simply by being wronged. Wrongful gain says a person can be unjustly enriched simply by profiting from a wrong, even if the victim lost nothing measurable. This is why disgorgement can be ordered when there are no damages.
* **skos:scopeNote:** Applies where the wrong itself, not the size of the gain, is the ground for recapture.
* **Key Attribute Bindings:** `harm:hasBenefitNormativeStatus`: `harm:NormativeWrongful`; `harm:hasRecaptureMechanism`: `harm:Disgorgement`.

#### `harm:UnjustEnrichmentGain` (`rdfs:subClassOf harm:WrongfulGain`)
* **skos:prefLabel:** Unjust Enrichment Gain
* **skos:definition:** A benefit received at another's expense in circumstances that make it unjust to keep.
* **skos:example:** A company keeping revenue earned by using people's likenesses without permission.
* **Key Attribute Bindings:** `harm:hasValueRelation`: `harm:TransferRelation`; `harm:hasRecaptureMechanism`: `harm:RestitutionToVictim` | `harm:Disgorgement`.

#### `harm:FiduciaryBreachGain` (`rdfs:subClassOf harm:WrongfulGain`)
* **skos:prefLabel:** Fiduciary Breach Gain
* **skos:altLabel:** Self-Dealing Gain | Secret Profit
* **skos:definition:** Profit a fiduciary makes by using a position of trust for themselves rather than for the person they serve.
* **skos:note:** The benefit-side partner of `harm:FiduciaryBetrayalHarm`. In that class's note, "the beneficiary" means the person the fiduciary serves, who is the *victim* here. In this class the gaining party is the fiduciary. The two senses of "beneficiary" should not be confused.
* **skos:example:** A trustee who invests trust assets for personal gain; a platform that holds itself out as acting for users while selling their data.
* **Key Attribute Bindings:** `harm:hasBeneficiaryKnowledge`: `harm:KnowingBeneficiary`; `harm:hasRecaptureMechanism`: `harm:Disgorgement`.

### IV. `harm:CapabilityPositionalGain` (mirrors `harm:TeleologicalDeprivationHarm`)
* **skos:prefLabel:** Capability & Positional Gain
* **skos:altLabel:** Advantage Gain | Power Gain
* **skos:definition:** An increase in a party's options, position, influence or future capabilities that results from others being harmed or deprived.
* **skos:note:** Deprivation harm blocks a victim from goods they should have had. Positional gain is often the other side of the same process: the opportunity closed to one party opens to another.
* **Key Attribute Bindings:** `harm:hasValueRelation`: `harm:PositionalRelation`; `harm:hasFormOfValue`: `harm:PowerValue` | `harm:LegitimacyReputationValue`.

#### `harm:CompetitiveAdvantageGain` (`rdfs:subClassOf harm:CapabilityPositionalGain`)
* **skos:prefLabel:** Competitive Advantage Gain
* **skos:definition:** Market share or lead time gained over rivals who bore costs or limits that the beneficiary avoided by causing harm.
* **skos:example:** A firm that cuts safety testing and so reaches market before careful competitors.

#### `harm:PowerInfluenceGain` (`rdfs:subClassOf harm:CapabilityPositionalGain`)
* **skos:prefLabel:** Power & Influence Gain
* **skos:definition:** Increased ability to shape others' choices, institutions or public opinion that results from a harm.
* **skos:example:** A political actor who gains from a disinformation campaign that degraded an election.

#### `harm:OpportunityCaptureGain` (`rdfs:subClassOf harm:CapabilityPositionalGain`)
* **skos:prefLabel:** Opportunity Capture Gain
* **skos:definition:** Jobs, contracts, places or resources that pass to one party because another was excluded or deprived by a harm.
* **skos:example:** Applicants who benefit when a biased screening model filters out qualified candidates from another group.
* **Key Attribute Bindings:** `harm:hasBeneficiaryKnowledge`: `harm:UnawareBeneficiary`; `harm:hasBeneficiaryStanding`: `harm:DiffuseBeneficiaryClass`.

### V. `harm:SystemicRentGain` (mirrors `harm:SystemicCyberneticHarm`)
* **skos:prefLabel:** Systemic Rent Gain
* **skos:altLabel:** Structural Rent | Network Gain
* **skos:definition:** Recurring gains captured from a party's position in a market, network or rule system, where the system's failures produce harm to others.
* **skos:note:** Systemic harm is a breakdown in a network or incentive structure. Systemic rent is what someone earns from that breakdown, often without any single harmful act.
* **Key Attribute Bindings:** `harm:hasBenefitFeedbackDynamics`: `harm:NonLinearAmplifying`; `harm:hasBenefitScalabilityAsymmetry`: `harm:ZeroMarginalCostReplication`; `harm:hasValueRelation`: `harm:ValueCreationFromHarmRelation` | `harm:CostAvoidanceRelation`.

#### `harm:RentExtractionGain` (`rdfs:subClassOf harm:SystemicRentGain`)
* **skos:prefLabel:** Rent Extraction Gain
* **skos:altLabel:** Rent-Seeking Gain
* **skos:definition:** Income captured by controlling access to something others need, rather than by producing new value.
* **skos:example:** Charging dependent users rising fees after alternatives have disappeared.

#### `harm:NetworkLockInGain` (`rdfs:subClassOf harm:SystemicRentGain`)
* **skos:prefLabel:** Network & Lock-In Gain
* **skos:definition:** Gains from users or institutions being unable to leave a system because of switching costs or network effects, even when the system harms them.
* **skos:example:** A platform that keeps users despite known harms because their contacts, records or livelihoods are tied to it.

#### `harm:AttentionCaptureGain` (`rdfs:subClassOf harm:SystemicRentGain`)
* **skos:prefLabel:** Attention Capture Gain
* **skos:altLabel:** Engagement Gain
* **skos:definition:** Revenue or influence earned by capturing human attention, where the methods used to capture it cause harm.
* **skos:note:** The benefit-side partner of `harm:EpistemicPollutionHarm`. The harm is spread thinly across many users; the gain is concentrated in a few firms and their advertisers.
* **Key Attribute Bindings:** `harm:hasFormOfValue`: `harm:AttentionValue`; `harm:hasValueCaptureChannel`: `harm:MarketPricingChannel`; `harm:hasBenefitDistributionAggregation`: `harm:NarrowConcentrated`.

#### `harm:RegulatoryArbitrageGain` (`rdfs:subClassOf harm:SystemicRentGain`)
* **skos:prefLabel:** Regulatory Arbitrage Gain
* **skos:definition:** Gains from structuring activity or booking profits so as to escape the rules that would otherwise prevent or price the harm.
* **skos:example:** Locating risky operations in a jurisdiction with weak oversight while booking profits in a low-tax one; using a shell company to separate a facility from its owner.
* **Key Attribute Bindings:** `harm:hasValueCaptureChannel`: `harm:IntermediatedBookingChannel`; `harm:hasValueCaptureIntermediary`: `harm:ShellEntityIntermediary`.

## B.5 Attribute descriptions *(stage 2)*

### Linking properties
* **`harm:derivesFrom`**: links a value capture to the harm or harms it comes from. One harm can yield many value captures, and one value capture can draw on many harms. **`harm:yieldsValueCapture`** is its inverse.

### B1. `harm:hasValueRelation` (Value Relation — How Gain Relates to Loss)
* **Definition:** How the beneficiary's gain stands to the victim's loss. Values: value moved from victim to beneficiary, so that one's loss is the other's gain (`harm:TransferRelation`); value kept by the beneficiary by pushing costs onto others (`harm:CostAvoidanceRelation`); new value produced by the harmful activity itself, which the victim never held (`harm:ValueCreationFromHarmRelation`); and gain that exists only relative to others who were set back (`harm:PositionalRelation`).
* **Note:** Explains why gains and losses rarely balance. In transfers they roughly match. In cost avoidance a small saving can cause a very large diffuse harm. In value creation the gain can far exceed any one victim's loss. Remedies that assume transfer, such as returning what was taken, fail for the other three.
* **Domains of Applicability:** Restitution Law, Welfare Economics, Political Philosophy of Exploitation.

### B2–B13. Shared attributes: benefit-side readings
The value lists are shared with the harm side. Only the reading changes:
* **B2 `hasBenefitTemporalTrajectory`:** when and how the gain arrives: at once, after a delay, or accumulating.
* **B3 `hasBenefitDistributionAggregation`:** whether the gain is concentrated in a few parties or spread across many. Often the reverse of the harm's distribution.
* **B4 `hasBenefitFeedbackDynamics`:** whether gains reinforce themselves, for example by funding more of the harmful activity.
* **B5 `hasBenefitScalabilityAsymmetry`:** whether the gain scales at near-zero marginal cost.
* **B6 `hasBenefitReversibility`:** whether the gain can be recovered. Gains that are spent, moved offshore or built into models may be practically irreversible.
* **B7 `hasBenefitMagnitude`:** the size of the gain, on the same scale as harm severity, so the two can be compared.
* **B8 `hasBenefitNormativeStatus`:** whether keeping the gain is itself a wrong, or only a setback-linked advantage.
* **B9 `hasBenefitModality`:** whether the gain is realised or only expected (for example, valuation based on future returns from the harm).
* **B10 `hasBenefitIncentiveAlignment`:** whether the gain was the motive for the harm or an emergent by-product of a system.
* **B11 `hasBenefitVisibility`:** whether the gain is apparent to victims, regulators or the public, or hidden in accounts and corporate structure.
* **B12 `hasBenefitSystemOpacity`:** how legible the mechanism producing the gain is.
* **B13 `hasBenefitCascade`:** downstream gains that follow from the first gain, such as investment, acquisitions or market power.

### B14. `harm:hasValueCaptureChannel` (Value-Capture Channel — Medium or Pathway of Benefit)
* **Definition:** The medium or pathway through which value produced by a harm reaches the beneficiary. Values: direct seizure of the victim's money or property (`harm:DirectTransferChannel`); prices and market exchange, such as engagement sold as ad inventory (`harm:MarketPricingChannel`); costs avoided by pushing them onto victims or the public, such as skipped safety testing or unpaid environmental costs (`harm:CostExternalisationChannel`); accumulation of data, models or assets that keep producing returns (`harm:AssetAccumulationChannel`); gains in market position, influence or legitimacy (`harm:PositionalPowerChannel`); and routing through intermediaries, subsidiaries or other jurisdictions (`harm:IntermediatedBookingChannel`).
* **Note:** Mirrors `harm:hasCausalVector`. That attribute traces *what carried the harm to the victim*; this one traces *what carried the gain to the beneficiary*. The two pathways are often unequal: harm may arrive directly and physically, while the gain arrives indirectly, sometimes legally, and is often hard to see. Complements B19, which says how directly the gain can be traced back to the harm.
* **Domains of Applicability:** Restitution & Unjust Enrichment, Tax & Transfer-Pricing Law, Competition Law, Platform & Data Governance.

### B15. `harm:hasFormOfValue` (Form of Value — What Is Gained)
* **Definition:** The kind of value the beneficiary captures. Values: money and financial assets (`harm:FinancialValue`); costs not paid (`harm:AvoidedCostValue`); data and the models built from it (`harm:DataValue`); human attention (`harm:AttentionValue`); power over others' choices or institutions (`harm:PowerValue`); standing, reputation or perceived legitimacy (`harm:LegitimacyReputationValue`); and satisfaction or other non-material utility (`harm:UtilityValue`).
* **Note:** Mirrors `harm:hasObjectOfHarm`. The object of harm is what the victim loses; the form of value is what the beneficiary gains. They need not match: a victim may lose privacy (dignitary) while the beneficiary gains data (asset).
* **Domains of Applicability:** Remedies & Valuation, Accounting, Data Governance, Political Economy.

### B16. `harm:hasBeneficiaryOntology` (Beneficiary Ontology — Who or What Can Gain?)
* **Definition:** The kind of entity that captures the value. Values: a natural person (`harm:IndividualBeneficiary`); a company or other legal person (`harm:CorporateBeneficiary`); a state or public body (`harm:StateBeneficiary`); dispersed owners such as shareholders or fund holders (`harm:DiffuseShareholderBeneficiary`); and an automated system whose objective is served, such as an optimiser meeting its target (`harm:NonHumanSystemBeneficiary`).
* **Note:** Mirrors `harm:hasPatientOntology`. The last value is analytical rather than moral: a system does not benefit in a morally relevant sense, but naming it shows where an objective function, rather than a person, drives the gain.
* **Domains of Applicability:** Corporate Law, Public Law, AI Alignment.

### B17. `harm:hasBeneficiaryStanding` (Beneficiary Standing — Directness of Gain)
* **Definition:** How directly the beneficiary stands to the gain. Values: the party that receives the gain first-hand (`harm:DirectBeneficiary`); a party that gains through a relationship with the direct beneficiary, such as a parent company or investor (`harm:IndirectBeneficiary`); and a dispersed class that gains slightly each, such as consumers paying lower prices (`harm:DiffuseBeneficiaryClass`).
* **Note:** Mirrors `harm:hasVictim`. Standing determines who can be made to give the gain back. Diffuse beneficiary classes are the counterpart of diffuse victims and are just as hard to reach through law.
* **Domains of Applicability:** Restitution, Class Actions, Tax Policy.

### B18. `harm:hasGainBaseline` (Gain Baseline — Better Off Than What?)
* **Definition:** The baseline against which the gain is measured. Values: what the beneficiary would have had had they acted lawfully and harmlessly (`harm:LawfulCounterfactualBaseline`); what comparable actors who bore the costs achieved (`harm:CompetitiveNormBaseline`); and the beneficiary's own earlier position (`harm:TemporalGainBaseline`).
* **Note:** Mirrors `harm:hasComparativeBaseline`. The choice of baseline decides how much is recoverable: a lawful counterfactual baseline captures avoided costs, while a temporal baseline may miss them entirely.
* **Domains of Applicability:** Damages & Disgorgement Calculation, Competition Law, Welfare Economics.

### B19. `harm:hasCaptureAttribution` (Capture Attribution — How Traceable Is the Gain?)
* **Definition:** How directly the gain can be traced to the harm. Values: the gain can be traced through identifiable transactions or records (`harm:DirectTraceableAttribution`); the gain follows the harm closely enough to be attributed in law (`harm:ProximateAttribution`); and the gain can be linked only through the structure of a system or market (`harm:StructuralAttribution`).
* **Note:** Mirrors `harm:hasCausationMechanism`. Courts generally require the gain to be traceable before ordering its return. Structural attribution is the hardest to recover and the most common in platform and AI harms.
* **Domains of Applicability:** Restitution & Tracing, Securities Enforcement, Competition Law.

### B20. `harm:hasBeneficiaryKnowledge` (Beneficiary Knowledge — What the Gainer Knew)
* **Definition:** What the beneficiary knew about the harm behind the gain. Values: knew of the harm (`harm:KnowingBeneficiary`); suspected it and deliberately avoided confirming it (`harm:WilfullyBlindBeneficiary`); and did not know (`harm:UnawareBeneficiary`).
* **Note:** Takes the place, on the benefit side, of `harm:hasConsentStatus` and `harm:hasCognitiveExploitability`, which concern the victim's will. Knowledge affects blame but not necessarily whether the gain should be returned: an unaware beneficiary may still be obliged to give up a gain once they learn its source.
* **Domains of Applicability:** Restitution (knowing receipt), Criminal Law (wilful blindness), Political Philosophy (benefiting from injustice).

### B21. `harm:hasValueCaptureIntermediary` (Value-Capture Intermediary — Who Routes the Gain)
* **Definition:** Entities that route value from the harm to the beneficiary without being the ultimate beneficiary. Values: shell or special-purpose companies (`harm:ShellEntityIntermediary`); platforms and marketplaces (`harm:PlatformIntermediary`); contractors and outsourcing firms (`harm:ContractorIntermediary`); and banks, funds and payment providers (`harm:FinancialIntermediary`).
* **Note:** Mirrors `harm:hasPerpetrator` and `harm:hasSecondaryAgent`. Those attributes spread responsibility for causing the harm across a network; this one tracks how the gain is spread or hidden across a network. An intermediary may also be a secondary agent and a facilitator beneficiary; the attributes stay independent.
* **Domains of Applicability:** Corporate & Tax Law, Anti-Money-Laundering, Supply-Chain Governance.

### B22. `harm:hasCaptureBarrier` (Capture Barrier — Safeguards Against Profiting from Harm)
* **Definition:** Non-agentic safeguards in place *before* harm that stop or limit profiting from it. Values: caps on returns or pricing (`harm:ProfitCapBarrier`); required separation of business lines or functions (`harm:StructuralSeparationBarrier`); disclosure and reporting duties (`harm:TransparencyRuleBarrier`); and rules against conflicts of interest (`harm:ConflictOfInterestRuleBarrier`).
* **Note:** Mirrors `harm:hasMitigatingMechanism`. Mitigation reduces the harm; capture barriers remove the incentive to cause it. A harm with strong mitigation but no capture barrier is likely to recur.
* **Domains of Applicability:** Corporate Governance, Financial Regulation, AI Governance.

### B23. `harm:hasRecaptureMechanism` (Recapture Mechanism — Taking the Gain Back)
* **Definition:** Remedies used *after* harm to take back the gain. Values: stripping profits made from the harm (`harm:Disgorgement`, shared with attribute 26); recovering pay or bonuses after misconduct or misstatement (`harm:ClawbackRecapture`); special taxes on gains from extraordinary conditions (`harm:WindfallTaxRecapture`); arrangements that return a share of gains to the communities whose resources produced them (`harm:BenefitSharingRecapture`); and returning to the victim what was taken (`harm:RestitutionToVictim`).
* **Note:** Mirrors `harm:hasAccountabilityMechanism`. Accountability compensates the victim; recapture removes the gain from the beneficiary. The two can diverge: compensation may be paid while the gain is kept, or the gain may be taken by the state while the victim receives nothing.
* **Domains of Applicability:** Restitution Law, Securities Regulation, Tax Policy, International Biodiversity Law.

## B.6 History notes and citations *(stage 3)*

> [!warning] Verification level
> Each citation below was confirmed to exist, with its bibliographic details, through web catalog, publisher, repository or court listings on 2026-11-15. The works themselves were **not opened**, so each gist and history note rests on those listings' abstracts and summaries. Open questions are flagged inline. When generating the `.ttl`, each entry maps to `skos:historyNote` and `dcterms:bibliographicCitation` on the term named.

### `harm:ValueCapture`, B1 `hasValueRelation`
* **skos:historyNote:** Welfare economics framed the gap between private gain and social cost from Pigou onward; Coase argued that transaction costs decide whether that gap is ever bargained away. Political philosophers later asked what those who gain from injustice owe, even when they did not cause it (Butt; Goodin & Barry; Young).
* **dcterms:bibliographicCitation:** Pigou, A.C. *The Economics of Welfare*. London: Macmillan, 1920; Coase, R.H. "The Problem of Social Cost." *Journal of Law and Economics* 3 (1960): 1–44; Butt, Daniel. "On Benefiting from Injustice." *Canadian Journal of Philosophy* 37(1) (2007): 129–152; Goodin, Robert E., & Barry, Christian. "Benefiting from the Wrongdoing of Others." *Journal of Applied Philosophy* 31(4) (2014): 363–376; Young, Iris Marion. *Responsibility for Justice*. Oxford: OUP, 2011.

### `harm:ExperientialGain`, `harm:GratificationGain`, `harm:DominanceSatisfactionGain`
* **skos:historyNote:** Social psychology has studied pleasure in others' misfortune (*schadenfreude*) as driven by envy, rivalry and a sense of justice.
* **dcterms:bibliographicCitation:** Smith, Richard H. *The Joy of Pain: Schadenfreude and the Dark Side of Human Nature*. New York: OUP, 2013.
* > [!question] No source yet for `DominanceSatisfactionGain`. A source on coercive control would be needed; none has been verified.

### `harm:MaterialPecuniaryGain`, `harm:AvoidedCostGain`, B14 `CostExternalisationChannel`
* **skos:historyNote:** Kapp documented how private firms routinely shift social and environmental costs onto society, building on Pigou's account of the gap between private and social cost.
* **dcterms:bibliographicCitation:** Kapp, K. William. *The Social Costs of Private Enterprise*. Cambridge, MA: Harvard University Press, 1950; Pigou (1920), above.

### `harm:AssetDataAccumulationGain`, `harm:AttentionCaptureGain`, B15 `DataValue` / `AttentionValue`
* **skos:historyNote:** Simon observed in 1971 that "a wealth of information creates a poverty of attention." Wu traced the business of harvesting attention and reselling it to advertisers from the penny press to platforms. Zuboff argued that taking human experience as behavioural data to predict and shape behaviour is a new logic of accumulation.
* **dcterms:bibliographicCitation:** Simon, Herbert A. "Designing Organizations for an Information-Rich World." In M. Greenberger (ed.), *Computers, Communications, and the Public Interest*. Baltimore: Johns Hopkins Press, 1971 (quoted passage pp. 40–41; chapter start page unconfirmed); Wu, Tim. *The Attention Merchants*. New York: Knopf, 2016; Zuboff, Shoshana. *The Age of Surveillance Capitalism*. New York: PublicAffairs, 2019.

### `harm:WrongfulGain`, `harm:UnjustEnrichmentGain`, B23 `RestitutionToVictim`
* **skos:historyNote:** Birks organised unjust enrichment around five questions (enrichment, at the claimant's expense, unjust, what right, defences). The American Law Institute restated US law in 2011: a person unjustly enriched at another's expense is liable in restitution.
* **dcterms:bibliographicCitation:** Birks, Peter. *Unjust Enrichment*. 2nd ed. Oxford: OUP, 2005; American Law Institute. *Restatement (Third) of Restitution and Unjust Enrichment*. St. Paul: ALI, 2011.

### `harm:FiduciaryBreachGain`
* **skos:historyNote:** Uses the same fiduciary-law tradition as `harm:FiduciaryBetrayalHarm`, viewed from the side of the fiduciary's gain.
* **dcterms:bibliographicCitation:** Frankel, Tamar. *Fiduciary Law*. New York: OUP, 2011 (some listings give 2010).

### `harm:CapabilityPositionalGain`, `harm:CompetitiveAdvantageGain`, `harm:OpportunityCaptureGain`, B1 `PositionalRelation`
* **skos:historyNote:** Hirsch introduced "positional goods," whose value depends on relative scarcity, so that one party's gain is tied to others falling behind.
* **dcterms:bibliographicCitation:** Hirsch, Fred. *Social Limits to Growth*. Cambridge, MA: Harvard University Press, 1976.

### `harm:PowerInfluenceGain`, B15 `PowerValue`
* **skos:historyNote:** Lukes's "three-dimensional" view of power includes shaping people's preferences and keeping issues off the agenda, not only winning open conflicts.
* **dcterms:bibliographicCitation:** Lukes, Steven. *Power: A Radical View*. London: Macmillan, 1974.

### `harm:SystemicRentGain`, `harm:RentExtractionGain`
* **skos:historyNote:** Tullock showed that resources spent chasing or defending transfers are a social loss; Krueger named this "rent-seeking." Mazzucato argued that value extraction is routinely mistaken for, and rewarded above, value creation.
* **dcterms:bibliographicCitation:** Tullock, Gordon. "The Welfare Costs of Tariffs, Monopolies, and Theft." *Western Economic Journal* 5(3) (1967): 224–232; Krueger, Anne O. "The Political Economy of the Rent-Seeking Society." *American Economic Review* 64(3) (1974): 291–303; Mazzucato, Mariana. *The Value of Everything*. London: Allen Lane, 2018.

### `harm:NetworkLockInGain`
* **skos:historyNote:** Arthur showed that under increasing returns, small chance events can lock a market into a technology that is hard to change. Shapiro and Varian set out strategy around switching costs and network effects.
* **dcterms:bibliographicCitation:** Arthur, W. Brian. "Competing Technologies, Increasing Returns, and Lock-In by Historical Events." *Economic Journal* 99(394) (1989): 116–131; Shapiro, Carl, & Varian, Hal R. *Information Rules*. Boston: Harvard Business School Press, 1999.

### `harm:RegulatoryArbitrageGain`, B14 `IntermediatedBookingChannel`, B21 `hasValueCaptureIntermediary`
* **skos:historyNote:** Fleischer gave the first broad theory of regulatory arbitrage, arguing that it shifts regulatory costs onto others and reduces transparency. Zucman estimated that about 8% of global household financial wealth sits in tax havens. The OECD's arm's-length principle governs pricing between parts of one multinational.
* **dcterms:bibliographicCitation:** Fleischer, Victor. "Regulatory Arbitrage." *Texas Law Review* 89 (2010): 227; Zucman, Gabriel. *The Hidden Wealth of Nations*. Chicago: University of Chicago Press, 2015; OECD. *OECD Transfer Pricing Guidelines for Multinational Enterprises and Tax Administrations 2022*. Paris: OECD Publishing, 2022.

### B10 `hasBenefitIncentiveAlignment`
* **skos:historyNote:** Holmström analysed contracts where an agent's effort cannot be observed (moral hazard), the setting in which gains and risks fall on different parties.
* **dcterms:bibliographicCitation:** Holmström, Bengt. "Moral Hazard and Observability." *Bell Journal of Economics* 10(1) (1979): 74–91.

### B20 `hasBeneficiaryKnowledge`
* **skos:historyNote:** US law treats wilful blindness, meaning believing a fact highly probable and deliberately avoiding confirming it, as knowledge. English law holds a recipient liable for knowing receipt when their knowledge makes it unconscionable to keep the benefit. Butt and Goodin & Barry argue that even unaware beneficiaries may owe something to victims.
* **dcterms:bibliographicCitation:** *Global-Tech Appliances, Inc. v. SEB S.A.*, 563 U.S. 754 (2011); *Bank of Credit and Commerce International (Overseas) Ltd v Akindele* [2001] Ch 437 (CA); Butt (2007) and Goodin & Barry (2014), above.

### B22 `hasCaptureBarrier`
* > [!question] No source verified yet. Wertheimer's *Exploitation* (Princeton UP, 1996), a theory of exploitation as unfair advantage, is a possible fit for the rationale but not for the specific barriers.

### B23 `hasRecaptureMechanism`
* **skos:historyNote:** The US Supreme Court held that disgorgement is allowed as equitable relief only up to net profits and for victims. Dodd-Frank and SEC Rule 10D-1 require listed companies to claw back wrongly awarded incentive pay after restatements. The Nagoya Protocol requires fair and equitable sharing of benefits from genetic resources with their providers.
* **dcterms:bibliographicCitation:** *Liu v. SEC*, 591 U.S. 71 (2020) (page 71 not seen in sources; check); Dodd-Frank Wall Street Reform and Consumer Protection Act §954 (2010); SEC Rule 10D-1 (adopted 26 Oct. 2022); Nagoya Protocol on Access to Genetic Resources and the Fair and Equitable Sharing of Benefits Arising from their Utilization to the Convention on Biological Diversity (adopted 2010; in force 2014).
* > [!question] `WindfallTaxRecapture` has no source yet.

*skos:changeNote:* Part B added in v2a (2026-11-15). Stage 1 skeleton, stage 2 descriptions and stage 3 sources written in an Obsidian Copilot discussion of the benefit mirror. Not yet reviewed by the author.
