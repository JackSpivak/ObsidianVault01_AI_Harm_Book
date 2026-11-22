# Gap Mapping Benchmarks & Schema Extensions

This reference documents the four institutional gap groups identified by benchmarking the Harm Ontology against real-world evaluative frameworks (CBA, HRIA, EIA, PRA, Capability Approach, Antitrust Economics, Constitutional Review, LCA, Clinical Bioethics, Algorithmic Impact Assessments).

## 1. Institutional Mandate & Enforcement Authority
*Bridges abstract perspective traditions with real institutional power and legal standing.*
- **Classes:** `InstitutionalMandate`, `EnforcementAuthority`, `LegalStanding`
- **Attributes:** 
  - `statutoryBasis` (`xsd:string` / URI reference)
  - `enforcementPower` (`{ advisory · binding · veto · civilPenalties · criminalSanctions }`)
  - `hasEnforcementAuthority` (object property → `EnforcementAuthority`)
  - `jurisdictionalScope` (domain / region reach)

## 2. Methodological Metric Specification (Valuation & Currency)
*Defines how frameworks measure and aggregate trade-offs (e.g., monetization vs. rights thresholds).*
- **Classes:** `ValuationMethodology` (e.g., CostBenefitMonetization, CapabilityIndex, DeontologicalThreshold), `TradeoffRule`
- **Attributes:**
  - `valuationCurrency` (`{ monetary · qaly · ordinalScore · narrative · binaryThreshold }`)
  - `permitsIncommensurableTradeoffs` (`xsd:boolean`)
  - `aggregationFormula` (`xsd:string`)

## 3. Procedural Lifecycle & Trigger Rules
*Captures temporal and operational gating rules mandating when an assessment occurs.*
- **Classes:** `AssessmentTrigger`, `ProceduralMilestone` (`{ PreDeployment · PostIncident · AnnualReview · MergerFiling }`)
- **Attributes:**
  - `mandatoryTrigger` (object property → `AssessmentTrigger`)
  - `triggerThreshold` (`xsd:string` / numeric value)
  - `assessmentTiming` (`{ exAnte · exPost · continuous }`)
  - `deadlineDuration` (`xsd:duration`)

## 4. Remedial Closure & Prescriptive Output
*Connects assessment verdicts (`Harmful / Beneficial`) to mandated organizational or legal corrections.*
- **Classes:** `RemedialObligation`, `PrescriptiveOutput` (`Injunction`, `MandatedMitigation`, `Divestiture`, `ProtocolModification`, `WarningLabel`)
- **Attributes:**
  - `generatesRemedy` (object property → `RemedialObligation`)
  - `remedyEnforceability` (`{ selfRegulating · courtOrdered · statutorilyEnforced }`)
  - `mitigationRequirement` (`xsd:string`)
  - `closureStatus` (`{ Open · UnderReview · Remedied · Closed }`)
