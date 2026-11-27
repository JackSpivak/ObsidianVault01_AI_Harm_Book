 # Master Formal Ontology of Harm (Part 1: Schema, Cross-Cutting Sub-Taxonomies & Axioms)

## Part 1: Master 21-Attribute Ontology Schema

Every harm class or instance in this ontology is defined across **21 formal sub-attributes**, organized into **4 Major Attribute Categories**.

### Attribute Category 1: Classification, Definition & Provenance

1. **Framework & Subtype (`hasClassHierarchy`)**  
   * `skos:definition`: Identifies the top-level philosophical lens and the specific legal, social, or applied subclass to which the harm belongs.  
   * `skos:scopeNote`: Separates abstract moral theories (what harm *is* fundamentally) from applied legal and institutional translations (how courts, regulators, and systems classify and adjudicate it).  
2. **Core Definition (`skos:definition`)**  
   * `skos:definition`: Provides a concise, plain-language statement of the essential meaning of a class, subtype, or attribute.  
   * `skos:scopeNote`: Serves as the primary semantic anchor for human readers and formal reasoning systems under the W3C SKOS standard.  
3. **Scope Note / Background (`skos:scopeNote`)**  
   * `skos:definition`: Captures the interdisciplinary background, historical rationale, boundary problems, and cross-field terminology explaining *why* the concept exists and *how* it resolves real-world edge cases.  
   * `skos:scopeNote`: Follows ISO 25964 and W3C SKOS conventions to supply contextual guidance without cluttering strict logical definitions.  
4. **Key Thinkers (`hasTheoreticalProvenance`)**  
   * `skos:definition`: Names the foundational philosophers, jurists, sociologists, or legal theorists who formulated or championed the concept.  
   * `skos:scopeNote`: Establishes intellectual lineage across classical philosophy, jurisprudence, welfare economics, and contemporary ethics.  
5. **Bibliographic Provenance (`dcterms:bibliographicCitation`)**  
   * `skos:definition`: Lists the seminal books, articles, legal cases, or statutory codes that establish the philosophical or jurisprudential foundation for the class.  
   * `skos:scopeNote`: Follows the Dublin Core Metadata Initiative (DCMI) standard so scholarly citations travel directly with each class node during automated queries or exports and can be iteratively expanded.  
6. **Domain / Locus (`hasInstitutionalLocus`)**  
   * `skos:definition`: Specifies the primary legal, social, regulatory, or technical arenas where this harm typically occurs and is contested.  
   * `skos:scopeNote`: Maps abstract concepts to concrete institutional jurisdictions such as Tort Law, Bioethics, AI Governance, or Earth Jurisprudence.

### Attribute Category 2: Target, Patient & Consent

7. **Object of Harm (`hasProtectedObject`)**  
   * `skos:definition`: Pinpoints the specific asset, physiological state, capability, right, bond, or condition that is damaged, diminished, or violated.  
   * `skos:scopeNote`: Distinguishes *what* is harmed (e.g., bodily homeostasis, informational self-determination, ecological integrity) from *who* holds that interest.  
8. **Moral Patient (`hasMoralPatient`)**  
   * `skos:definition`: Identifies the entity—whether an individual, vulnerable dependent, collective group, ecosystem, or future generation—that suffers the setback or risk.  
   * `skos:scopeNote`: Accommodates both traditional individual legal persons and non-traditional moral patients such as animals, rivers, future persons, and marginalized populations.  
9. **Consent & Voluntariness (`hasConsentStatus`)**  
   * `skos:definition`: Captures whether the Moral Patient validly consented (*volenti non fit injuria*), was coerced or deceived, or lacked the capacity to consent.  
   * `skos:scopeNote`: Serves as a primary moral and legal validity filter; valid consent often transforms an apparent harm into a permissible interaction, whereas manipulated or bypassed consent invalidates the defense.

### Attribute Category 3: Causal Dynamics, Modality & Measurement

10. **Causal Mechanism / Vector (`hasCausalVector`)**  
    * `skos:definition`: Explains the medium or pathway through which the source's action reaches the Object of Harm (e.g., kinetic, informational, financial, or institutional).  
    * `skos:scopeNote`: Bridges physical causation with non-physical vectors such as algorithmic nudging, normative exclusion, and contractual breach.  
11. **Temporal & Causal Profile (`hasTemporalDynamics`)**  
    * `skos:definition`: Classifies the time horizon and accumulation pattern of the harm, distinguishing acute/instantaneous events from chronic/cumulative or latent/delayed effects.  
    * `skos:scopeNote`: Essential for modeling slow-moving harms (like toxic exposure, structural bias, or climate change) that defeat simple single-moment legal tests.  
12. **Modality & Probability (`hasEpistemicModality`)**  
    * `skos:definition`: Distinguishes harms that have already materialized (actualized) from imminent threats, pure probabilistic risks, and counterfactual baselines.  
    * `skos:scopeNote`: Enables the ontology to represent criminal attempts, injunctive relief thresholds, and pure risk imposition where no physical injury has yet occurred.  
13. **Reversibility & Permanence (`hasReversibilityState`)**  
    * `skos:definition`: Evaluates whether the damaged Object of Harm can be fully restored, partially mitigated, or is permanently or irreversibly lost.  
    * `skos:scopeNote`: Determines whether financial restitution ("make-whole" damages) is coherent or whether injunctive prevention is mandatory due to incommensurable loss.  
14. **Consequential & Cascading Harm Profile (`hasConsequentialCascade`)**  
    * `skos:definition`: Maps the foreseeable downstream, secondary, and cross-domain ripple effects triggered by the primary harm, bounded by causal foreseeability and systemic coupling (defined in Part 2C).  
    * `skos:scopeNote`: Governed in jurisprudence by Proximate Cause (*Palsgraf* foreseeability) and the Thin Skull (Eggshell Plaintiff) rule, and in risk science by Second-Order / Cascading Effects—preventing infinite causal chains while capturing real-world domino effects.  
15. **Evidentiary & Measurement Standard (`hasMeasurementMetric`)**  
    * `skos:definition`: Defines how the harm and its causal cascade are proven, audited, or quantified in law, science, or policy.  
    * `skos:scopeNote`: Translates philosophical harm into operational proof standards such as actuarial tables, DSM clinical criteria, disparate-impact ratios, or presumed statutory violations.

### Attribute Category 4: Multi-Agent Architecture & Resolution

16. **Primary Moral Agent (`hasPrimaryPerpetrator`)**  
    * `skos:definition`: Identifies the direct perpetrator, proximate human actor, or non-agentic hazard that executes the wrongful act or triggers the harm.  
    * `skos:scopeNote`: Establishes the primary causal anchor; where a non-agentic system or natural hazard triggers the harm, accountability shifts to Secondary and Protective Agents (*Axiom 3*).  
17. **Secondary / Complicit Agency (`hasSecondaryAgent`)**  
    * `skos:definition`: Classifies indirect actors who do not execute the primary act but bear responsibility because they instigate, facilitate, supervise, fail to guard against, or structurally enable it (defined in Part 2A).  
    * `skos:scopeNote`: Studied in criminal law under *complicity* and *accomplice liability*, in tort law under *vicarious liability*, and in philosophy under *collective action* (Christopher Kutz, Sanford Kadish).  
18. **Beneficiary / Value-Capture Role (`hasBeneficiaryRole`)**  
    * `skos:definition`: Identifies the entity or entities that capture financial gain, avoided compliance costs, competitive advantage, power, or utility from the harm, separating causal execution from value capture (defined in Part 2D).  
    * `skos:scopeNote`: Governed in law by Unjust Enrichment and Disgorgement, in economics by Negative Externalities and Moral Hazard (Pigou, Coase), and in political philosophy by Benefiting from Injustice (Young, Butt).  
19. **Protective / Mitigating Agency (`hasProtectiveAgent`)**  
    * `skos:definition`: Classifies moral actors and institutions that exercise preventive, rescuing, or restorative agency to shield the Moral Patient (defined in Part 2B).  
    * `skos:scopeNote`: Explicitly separates human and institutional *agents* who bear duties to protect (Henry Shue) from the non-agentic *mechanisms* they deploy.  
20. **Protective & Mitigating Mechanisms (`hasMitigatingMechanism`)**  
    * `skos:definition`: Identifies the non-agentic tools, engineering controls, legal writs, and institutional protocols deployed *by* Protective Agents to block, interrupt, or limit harm.  
    * `skos:scopeNote`: Captures technical, procedural, and legal safeguards (e.g., encryption, kill-switches, writs of *habeas corpus*, safety interlocks) as instruments rather than moral agents.  
21. **Remedial & Accountability Mechanism (`hasAccountabilityMechanism`)**  
    * `skos:definition`: Specifies the ex-post legal, financial, punitive, or structural remedies used to resolve the harm, compensate victims, disgorge unjust gains, and deter future violations.  
    * `skos:scopeNote`: Aligns the remedy with the ontology's diagnosis—matching compensatory damages to counterfactual losses, nominal/punitive damages to rights violations, disgorgement to unjust enrichment, and structural injunctions to systemic harms.

---

## Part 2: Cross-Cutting Sub-Taxonomies

### Part 2A: Taxonomy of Secondary / Complicit Agency  
* `skos:definition`: Evaluates actors who do not directly commit the primary harmful act, yet bear moral or legal responsibility through causation, authorization, omission, or institutional role.  
* `skos:scopeNote`: Top-level harm theories focus on the victim's state, but applied ethics and law must fracture responsibility across complex organizational and social networks where facilitators, supervisors, and gatekeepers enable harm without pulling the trigger.


 **# Master Formal Ontology of Harm (Part 2: Domains 1–3)

  

---

  

### Domain 1: The Experiential Framework (Hedonistic / Phenomenological)

* `skos:definition`: Harm consists fundamentally in negative subjective states—physical pain, psychological suffering, emotional distress, or sensory intrusion.

* `skos:scopeNote`: Grounded in classical hedonism and utilitarianism, this framework treats conscious suffering as the primary moral evil. When translated into law, pure experientialism encounters the Boundary Problem: if every unpleasant feeling justified state coercion, hurt feelings or disgust would become crimes, requiring applied subtypes to separate actionable trauma from protected "mere offense."

* *Foundational Thinkers:* **Jeremy Bentham**, **Epicurus**, **Shelly Kagan**, **Ben Bradley**.

* `dcterms:bibliographicCitation`: Bentham, J. (1789). *An Introduction to the Principles of Morals and Legislation*; Bradley, B. (2012). "Doing Away with Harm." *Philosophy and Phenomenological Research*, 85(2), 390–412; Kagan, S. (1998). *Normative Ethics*. Westview Press. *(Expandable)*

  

#### 1.1 Physical Pain & Suffering (Legal Subtype)

* `skos:definition`: The direct infliction of bodily agony or nociceptive distress, translated by civil law into non-economic damages alongside medical costs.

* `skos:scopeNote`: Bridges Bentham's quantitative measurement of pain intensity and duration with modern tort valuation; extends moral patienthood beyond humans to all sentient animals capable of nociception (Peter Singer).

* *Key Thinkers:* **Jeremy Bentham**, **Peter Singer**.

* `dcterms:bibliographicCitation`: Singer, P. (1975). *Animal Liberation*. HarperCollins; Bentham, J. (1789). *An Introduction to the Principles of Morals and Legislation* (Ch. IV: Value of a Lot of Pleasure or Pain, How to be Measured). *(Expandable)*

* *Domain / Locus:* Personal injury torts, medical malpractice, criminal assault, animal welfare law.

* *Object of Harm:* Physical comfort, bodily homeostasis, sensory tranquility, freedom from nociceptive agony.

* *Moral Patient:* Any sentient being capable of experiencing pain (humans and non-human animals).

* *Consent Status:* Non-consensual (unless valid medical or sporting consent applies).

* *Causal Vector:* Kinetic, chemical, thermal, or biological force.

* *Temporal Profile:* Acute/instantaneous or chronic/persistent.

* *Modality:* Actualized sensory state.

* *Reversibility:* Partially mitigable (via analgesia) to irreversible (chronic neuropathic pain).

* *Consequential & Cascading Harm:* **Direct Consequential** (sleep deprivation, inability to care for dependents); **Cross-Domain Cascade** (chronic pain → clinical depression, opioid dependency, job loss); **Vulnerability Amplification** (*Eggshell Skull* rule).

* *Measurement Metric:* Subjective clinical pain scales paired with objective medical diagnostics.

* *Primary Moral Agent:* Discrete assailants, negligent surgeons, or reckless drivers directly inflicting bodily injury.

* *Secondary Agency:* **Material Facilitation** (weapon suppliers); **Vicarious Agency** (hospitals credentialing incompetent surgeons).

* *Beneficiary Role:* **Direct Perpetrator** (sadistic gratification) or **Principal/Institutional** (employers cutting physical safety corners to increase output speed).

* *Protective Agency:* **Intervening Rescuers** (paramedics, emergency physicians, Good Samaritans); **Restorative Agents** (pain specialists, physical therapists).

* *Protective Mechanisms:* Emergency triage protocols, clinical analgesia, safety barriers, Good Samaritan statutory immunity laws.

* *Accountability Mechanism:* Non-economic compensatory damages ("pain and suffering"), criminal incarceration, regulatory bans.

  

#### 1.2 Psychological & Emotional Harm (Legal Subtype)

* `skos:definition`: Severe mental trauma, terror, or emotional distress, represented by torts like Intentional Infliction of Emotional Distress (IIED) and criminal harassment.

* `skos:scopeNote`: Historically, courts refused to recognize emotional distress unless attached to a physical impact ("parasitic damages") due to fears of fraudulent claims; 20th-century jurists (Magruder, Prosser) established severe emotional trauma as an independent harm.

* *Key Thinkers:* **Calvert Magruder**, **William Prosser**.

* `dcterms:bibliographicCitation`: Magruder, C. (1936). "Mental and Emotional Disturbance in the Law of Torts." *Harvard Law Review*, 49(7), 1033–1067; Prosser, W. L. (1939). "Intentional Infliction of Mental Suffering: A New Tort." *Michigan Law Review*, 37(6), 874–892. *(Expandable)*

* *Domain / Locus:* Civil tort law (IIED), workplace harassment, family law, cyberbullying regulation.

* *Object of Harm:* Emotional equilibrium, psychological security, peace of mind, mental health.

* *Moral Patient:* Conscious individuals with psychological vulnerability.

* *Consent Status:* Non-consensual or coerced.

* *Causal Vector:* Verbal, behavioral, relational, or digital/informational intimidation.

* *Temporal Profile:* Acute shock or cumulative/chronic trauma (e.g., PTSD).

* *Modality:* Actualized psychological state.

* *Reversibility:* Partially mitigable through long-term therapy; often leaves lasting psychological scars.

* *Consequential & Cascading Harm:* **Direct Consequential** (social withdrawal, hypervigilance, somatic illness); **Cross-Domain Cascade** (trauma-induced inability to maintain employment, relationship breakdown, educational dropout).

* *Measurement Metric:* Psychiatric/clinical diagnosis (DSM criteria) and behavioral impact testimony.

* *Primary Moral Agent:* Interpersonal abusers, stalkers, or workplace bullies.

* *Secondary Agency:* **Instigation & Conspiracy** (coordinated doxxing groups); **Gatekeeper Negligence** (HR or school officials ignoring abuse reports).

* *Beneficiary Role:* **Direct Perpetrator** (coercive control) or **Downstream/Market** (engagement-driven platforms monetizing outrage and harassment traffic).

* *Protective Agency:* **Fiduciary Guardians** (school counselors, ombudspersons, family judges); **Restorative Agents** (trauma therapists, crisis responders).

* *Protective Mechanisms:* Anti-harassment reporting hotlines, workplace safe-harbor transfers, psychological first-aid protocols, civil restraining orders.

* *Accountability Mechanism:* Tort damages for mental anguish, protective injunctions, workplace compliance mandates.

  

#### 1.3 Mere Offense vs. Profound Offense (Philosophical/Legal Boundary)

* `skos:definition`: Unpleasant mental states like disgust, shock, or annoyance, generally excluded from criminalization unless inescapable or destructive to public order.

* `skos:scopeNote`: Operationalizes Joel Feinberg's *Offense Principle* against Lord Devlin's *Legal Moralism*—drawing the constitutional line between protected free expression that merely offends sensibilities and inescapable public nuisances.

* *Key Thinkers:* **Joel Feinberg**, **Patrick Devlin**.

* `dcterms:bibliographicCitation`: Feinberg, J. (1985). *Offense to Others: The Moral Limits of the Criminal Law* (Vol. 2). Oxford University Press; Devlin, P. (1965). *The Enforcement of Morals*. Oxford University Press. *(Expandable)*

* *Domain / Locus:* Constitutional free speech law, public nuisance statutes, media/obscenity regulation.

* *Object of Harm:* Sensory peace, aesthetic/moral sensibilities, freedom from unconsented intrusion in shared spaces.

* *Moral Patient:* Captive audiences, unwilling observers, or the general public.

* *Consent Status:* Unwilling/captive exposure (lacking reasonable exit).

* *Causal Vector:* Visual, auditory, olfactory, or broadcast sensory transmission.

* *Temporal Profile:* Transient/episodic during exposure.

* *Modality:* Actualized subjective discomfort.

* *Reversibility:* Fully restorable once exposure ceases.

* *Consequential & Cascading Harm:* **Direct Consequential** (avoidance of public spaces or altered routines); **Remote Cutoff** (lacks severe cascades unless profound offense triggers acute panic or public disorder).

* *Measurement Metric:* Community standards tests and statutory nuisance thresholds.

* *Primary Moral Agent:* Speakers, protesters, public performers, or broadcasters generating the offensive display.

* *Secondary Agency:* **Material Facilitation** (event organizers, venue owners, broadcasters forcing captive exposure).

* *Beneficiary Role:* **Direct Perpetrator** (attention/notoriety) or **Principal/Institutional** (broadcasters/advertisers profiting from shock value).

* *Protective Agency:* **Regulatory Authorities** (municipal zoning boards, broadcast regulators, platform trust-and-safety teams).

* *Protective Mechanisms:* Content warning labels, opt-in user filters, broadcast watershed hours, municipal zoning buffers.

* *Accountability Mechanism:* Time, place, and manner restrictions, public nuisance fines, zoning laws.

  

#### 1.4 Non-Comparative Harm (Philosophical Subtype)

* `skos:definition`: Placing a being in an intrinsically miserable state regardless of any baseline comparison, resolving paradoxes where no "better off" counterfactual exists.

* `skos:scopeNote`: Created specifically to solve Derek Parfit's *Non-Identity Problem* in bioethics and climate policy—explaining why bringing a child into existence with a severe genetic condition or degraded climate is a harm even though the alternative was non-existence.

* *Key Thinkers:* **Derek Parfit**, **Elizabeth Harman**, **Seana Shiffrin**.

* `dcterms:bibliographicCitation`: Parfit, D. (1984). *Reasons and Persons* (Part IV). Oxford University Press; Harman, E. (2004). "Can We Harm and Benefit in Creating?" *Philosophical Perspectives*, 18, 89–113; Shiffrin, S. V. (1999). "Wrongful Life, Procreative Responsibility, and the Significance of Harm." *Legal Theory*, 5(2), 117–148. *(Expandable)*

* *Domain / Locus:* Bioethics, reproductive technology, wrongful life litigation, intergenerational climate ethics.**








**

# Master Formal Ontology of Harm (Part 3: Domains 4–7)

  

---

  

### Domain 4: Epistemic & Cognitive Harm (Information & Mind)

* `skos:definition`: Harm consists in degrading an agent’s capacity to know, reason, perceive reality, or form autonomous beliefs—distinct from emotional distress or reputational damage.

* `skos:scopeNote`: Synthesizes feminist epistemology (Miranda Fricker), behavioral economics (Kahneman, Thaler), and AI/platform ethics (Shoshana Zuboff) to address harms targeting human agency at the cognitive root.

* *Foundational Thinkers:* **Miranda Fricker**, **Cass Sunstein**, **Shoshana Zuboff**.

* `dcterms:bibliographicCitation`: Fricker, M. (2007). *Epistemic Injustice*. Oxford University Press; Zuboff, S. (2019). *The Age of Surveillance Capitalism*. PublicAffairs. *(Expandable)*

  

#### 4.1 Epistemic Injustice (Testimonial & Hermeneutical)

* `skos:definition`: Wronging someone specifically in their capacity as a knower through prejudice-driven credibility deflation (*testimonial injustice*) or conceptual erasure (*hermeneutical injustice*).

* `skos:scopeNote`: Explains why dismissing a patient's symptoms or a witness's testimony due to identity prejudice is a distinct moral injury to rational dignity even before physical or legal consequences materialize.

* *Key Thinkers:* **Miranda Fricker**.

* `dcterms:bibliographicCitation`: Fricker, M. (2007). *Epistemic Injustice: Power and the Ethics of Knowing*. Oxford University Press. *(Expandable)*

* *Domain / Locus:* Judicial testimony, medical diagnosis, academic/scientific institutions, workplace evaluations.

* *Object of Harm:* Epistemic agency, testimonial credibility, shared interpretive concepts, intellectual self-trust.

* *Moral Patient:* Speakers, witnesses, patients, marginalized interpretive communities.

* *Consent Status:* Non-consensual systemic exclusion or dismissal.

* *Causal Vector:* Normative, linguistic, and cognitive bias in interpersonal or institutional evaluation.

* *Temporal Profile:* Acute (dismissed testimony) and cumulative (epistemic marginalization).

* *Modality:* Actualized wrong to epistemic status.

* *Reversibility:* Partially mitigable through institutional validation and conceptual reclamation.

* *Consequential & Cascading Harm:* **Cross-Domain Cascade** (discounted medical testimony → misdiagnosis and physical harm; discounted legal testimony → wrongful conviction or denial of protective orders).

* *Measurement Metric:* Qualitative credibility audits, diagnostic disparity rates, procedural fairness reviews.

* *Primary Moral Agent:* Biased listeners, clinicians, judges, or institutions discounting credible testimony.

* *Secondary Agency:* **Systemic Contribution** (institutions perpetuating biased evidentiary norms or exclusionary curricula).

* *Beneficiary Role:* **Principal/Institutional** (dominant groups retaining disproportionate epistemic authority and institutional credibility).

* *Protective Agency:* **Fiduciary Guardians** (patient/victim advocates); **Whistleblowers** (epistemic allies amplifying marginalized voices).

* *Protective Mechanisms:* Structured diagnostic checklists, blind peer review, corroborative evidentiary rules, inclusive reporting frameworks.

* *Accountability Mechanism:* Procedural reversals, institutional epistemic audits, restorative recognition.

  

#### 4.2 Cognitive Manipulation & Autonomy Subversion

* `skos:definition`: Hijacking human belief formation, attention, or decision-making through deception, algorithmic dark patterns, deepfakes, or neuro-technical tampering without physical coercion.

* `skos:scopeNote`: Addresses modern digital and neuro-technological threats where choice architecture is weaponized to bypass rational deliberation while preserving the illusion of voluntary consent.

* *Key Thinkers:* **Daniel Kahneman**, **Richard Thaler**, **Shoshana Zuboff**.

* `dcterms:bibliographicCitation`: Thaler, R. H., & Sunstein, C. R. (2008). *Nudge*. Yale University Press; Susser, D., Roessler, B., & Nissenbaum, H. (2019). "Online Manipulation: Hidden Influences in a Digital World." *Georgetown Law Technology Review*, 4(1), 1–45. *(Expandable)*

* *Domain / Locus:* AI governance, digital consumer protection, election integrity, neurotechnology.

* *Object of Harm:* Cognitive liberty, rational autonomy, epistemic integrity, authentic preference formation.

* *Moral Patient:* Digital users, voters, consumers, neuro-device users.

* *Consent Status:* Bypassed or subverted (manipulated consent is legally and morally invalid).

* *Causal Vector:* Informational/algorithmic (dark patterns, deepfakes, addictive loops) or neuro-technical.

* *Temporal Profile:* Acute (election interference) or chronic/habitual (behavioral addiction).

* *Modality:* Actualized cognitive distortion or probabilistic behavioral manipulation.

* *Reversibility:* Partially mitigable via debriefing, media literacy, cognitive restoration.

* *Consequential & Cascading Harm:* **Direct Consequential** (impulsive financial losses, compulsive screen addiction); **Cross-Domain Cascade** (algorithmic radicalization or election disinformation → civic polarization and real-world violence).

* *Measurement Metric:* Behavioral A/B manipulation audits, deceptive-design heuristics, provenance verification.

* *Primary Moral Agent:* Malicious disinformation actors, manipulative platform designers, rogue AI systems.

* *Secondary Agency:* **Material Facilitation** (ad-tech networks monetizing outrage); **Instigation** (political operatives funding deepfakes).

* *Beneficiary Role:* **Principal/Institutional** (platforms capturing ad revenue from dark patterns/addiction; political actors gaining power via disinformation).

* *Protective Agency:* **Regulatory Authorities** (consumer protection agencies, election commissions); **Whistleblowers** (tech ethicists, disinformation researchers).

* *Protective Mechanisms:* Content provenance watermarks (C2PA), bans on dark patterns, friction/cooling-off UI prompts, algorithmic transparency rules.

* *Accountability Mechanism:* Deceptive-trade-practice fines, mandatory algorithmic unlearning, platform liability.

  

---

  

### Domain 5: Relational, Care & Existential Harm (Social & Ecological)

* `skos:definition`: Harm destroys essential dependency bonds, cultural continuity, or intrinsic ecological integrity—rather than damaging an isolated individual’s rights or welfare.

* `skos:scopeNote`: Overcomes the hyper-individualism of classical Western legal theory by incorporating Feminist Ethics of Care (Noddings, Kittay), Indigenous/Cultural Rights jurisprudence (Lemkin), and Earth Jurisprudence (Arne Næss, Christopher Stone).

* *Foundational Thinkers:* **Nel Noddings**, **Eva Feder Kittay**, **Arne Næss**, **Christopher Stone**.

* `dcterms:bibliographicCitation`: Kittay, E. F. (1999). *Love's Labor*. Routledge; Stone, C. D. (1972). "Should Trees Have Standing?" *Southern California Law Review*, 45, 450–501. *(Expandable)*

  

#### 5.1 Care & Attachment Harm

* `skos:definition`: Severing essential dependency relationships or abandoning duties of care toward vulnerable dependents (e.g., wrongful family separation or institutional neglect).

* `skos:scopeNote`: Grounded in Feminist Ethics of Care—recognizing that human flourishing depends on asymmetrical networks of dependency and that breaking attachment bonds causes profound developmental harm even without physical violence.

* *Key Thinkers:* **Nel Noddings**, **Eva Feder Kittay**.

* `dcterms:bibliographicCitation`: Noddings, N. (1984). *Caring: A Feminine Approach to Ethics and Moral Education*. University of California Press; Kittay, E. F. (1999). *Love's Labor: Essays on Women, Equality and Dependency*. Routledge. *(Expandable)*

* *Domain / Locus:* Family law, immigration detention, elder care, pediatric medicine, disability institutions.

* *Object of Harm:* Relational attachment, developmental security, dependency support networks.

* *Moral Patient:* Infants, children, elderly persons, severely disabled dependents, caregivers.

* *Consent Status:* Non-consensual; dependents lack capacity to consent to separation or neglect.

* *Causal Vector:* Physical separation, institutional neglect, administrative detention policies.

* *Temporal Profile:* Acute trauma with lifelong developmental consequences.

* *Modality:* Actualized relational rupture.

* *Reversibility:* Partially mitigable via reunification, though developmental trauma may be permanent.

* *Consequential & Cascading Harm:* **Cross-Domain Cascade** (early childhood attachment rupture → lifelong neurodevelopmental impairment, educational difficulties, heightened vulnerability to adult instability).

* *Measurement Metric:* Developmental psychology assessments, attachment scales, care-ratio audits.

* *Primary Moral Agent:* Negligent caregivers, abusive institutions, state officials enforcing family separation.

* *Secondary Agency:* **Vicarious Agency** (agency directors); **Gatekeeper Negligence** (social workers failing welfare checks).

* *Beneficiary Role:* **Principal/Institutional** (for-profit care facilities or detention contractors maximizing margins via understaffing).

* *Protective Agency:* **Fiduciary Guardians** (guardians *ad litem*, family preservation advocates); **Restorative Agents** (child psychologists).

* *Protective Mechanisms:* Family-preservation statutory mandates, mandatory care-staffing ratios, guardianship oversight boards.

* *Accountability Mechanism:* Reunification orders, institutional receivership, custodial negligence damages.

  

#### 5.2 Cultural & Epistemicide Harm

* `skos:definition`: Systematic destruction of a group’s language, sacred heritage, collective memory, or cultural identity—distinct from individual property or bodily injury.

  
**