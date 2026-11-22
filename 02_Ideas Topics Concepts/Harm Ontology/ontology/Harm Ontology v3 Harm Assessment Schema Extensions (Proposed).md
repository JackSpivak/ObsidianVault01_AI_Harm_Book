# Harm Ontology v3 Harm Assessment Schema Extensions (Proposed)
*A schema extension mapping the 4 real-world institutional gaps to new classes, subclasses, and camelCase attributes, compatible with Harm Ontology v3's editor-first and three-layer pattern.*

---

## Visual Schema Depiction

```text
PerspectiveType (v3 Core Tradition / Lens)
│
├── [Gap 1: Mandate & Authority] ──────────────────────────────────────────
│   ├── statutoryBasis (xsd:string / URI)
│   ├── enforcementPower { advisory · binding · veto · civilPenalties · criminalSanctions }
│   ├── hasEnforcementAuthority → EnforcementAuthority
│   └── jurisdictionalScope → Domain / Region
│
├── [Gap 2: Metric & Valuation] ──────────────────────────────────────────
│   ├── valuationCurrency { monetary · qaly · ordinalScore · narrative · binaryThreshold }
│   ├── permitsIncommensurableTradeoffs (xsd:boolean)
│   └── valuationMethodology → ValuationMethodology
│
├── [Gap 3: Procedural Lifecycle] ─────────────────────────────────────────
│   ├── mandatoryTrigger → AssessmentTrigger
│   ├── triggerThreshold (xsd:string / numeric value)
│   ├── assessmentTiming { exAnte · exPost · continuous }
│   └── deadlineDuration (xsd:duration)
│
└── [Gap 4: Remedial Closure] ─────────────────────────────────────────────
    └── generatesRemedy → RemedialObligation
        ├── remedyEnforceability { selfRegulating · courtOrdered · statutorilyEnforced }
        ├── mitigationRequirement (xsd:string)
        └── closureStatus { Open · UnderReview · Remedied · Closed }
```

---

## Detailed Schema Breakdown by Category
*Bridges abstract perspective traditions (`PerspectiveType`) with real-world institutional power, legal standing, and statutory binding force.*

### New Classes & Subclasses
- `InstitutionalMandate` (Subclass of `PerspectiveType` or linked via property)
- `EnforcementAuthority` (Class representing the governing or regulatory body)
- `LegalStanding` (Class representing the rights/authorization to bring or enforce an assessment)

### New Attributes (camelCase)
- `statutoryBasis` (datatype: `xsd:string` / URI reference to legislation)
- `enforcementPower` (datatype: `xsd:string` — e.g., `{ advisory · binding · veto · civilPenalties · criminalSanctions }`)
- `hasEnforcementAuthority` (object property linking `PerspectiveType` → `EnforcementAuthority`)
- `jurisdictionalScope` (object property or datatype defining geographic/domain reach)

---

## Category 2: Methodological Metric Specification (Valuation & Currency)
*Defines how a framework measures and aggregates trade-offs (e.g., monetization vs. rights thresholds).*

### New Classes & Subclasses
- `ValuationMethodology` (Class: e.g., `CostBenefitMonetization`, `CapabilityIndex`, `DeontologicalThreshold`, `RiskScoringMatrix`)
- `TradeoffRule` (Class governing whether incommensurable values can be traded off against each other)

### New Attributes (camelCase)
- `valuationCurrency` (datatype: `xsd:string` — e.g., `{ monetary · qaly · ordinalScore · narrative · binaryThreshold }`)
- `permitsIncommensurableTradeoffs` (datatype: `xsd:boolean`)
- `aggregationFormula` (datatype: `xsd:string` or reference to formal rule)

---

## Category 3: Procedural Lifecycle & Trigger Rules
*Captures the temporal and operational gating rules that dictate when an assessment is legally or organizationally mandatory.*

### New Classes & Subclasses
- `AssessmentTrigger` (Class representing the event or condition that mandates an assessment)
- `ProceduralMilestone` (Class: e.g., `{ PreDeployment · PostIncident · AnnualReview · MergerFiling }`)

### New Attributes (camelCase)
- `mandatoryTrigger` (object property linking `PerspectiveType` → `AssessmentTrigger`)
- `triggerThreshold` (datatype: `xsd:string` — e.g., financial revenue threshold, user scale count, hazard classification)
- `assessmentTiming` (datatype: `xsd:string` — e.g., `{ exAnte · exPost · continuous }`)
- `deadlineDuration` (datatype: `xsd:duration` specifying required completion window)

---

## Category 4: Remedial Closure & Prescriptive Output
*Connects an assessment verdict (`Harmful / Beneficial`) to mandated organizational or legal corrections.*

### New Classes & Subclasses
- `RemedialObligation` (Class representing the required corrective action resulting from an assessment)
- `PrescriptiveOutput` (Class: e.g., `Injunction`, `MandatedMitigation`, `Divestiture`, `ProtocolModification`, `WarningLabel`)

### New Attributes (camelCase)
- `generatesRemedy` (object property linking `Assessment` → `RemedialObligation`)
- `remedyEnforceability` (datatype: `xsd:string` — e.g., `{ selfRegulating · courtOrdered · statutorilyEnforced }`)
- `mitigationRequirement` (datatype: `xsd:string` specifying mandatory safety buffers or offsets)
- `closureStatus` (datatype: `xsd:string` — e.g., `{ Open · UnderReview · Remedied · Closed }`)
