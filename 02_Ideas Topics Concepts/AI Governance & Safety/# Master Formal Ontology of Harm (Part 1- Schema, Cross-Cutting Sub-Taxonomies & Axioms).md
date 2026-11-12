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

