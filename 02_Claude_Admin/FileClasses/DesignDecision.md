---
fields:
  - name: type
    type: Select
    options:
      sourceType: ValuesList
      valuesList:
        "1": design-decision
    path: ""
    id: dDtYp1
  - name: status
    type: Select
    options:
      sourceType: ValuesList
      valuesList:
        "1": proposed
        "2": pending
        "3": settled
        "4": superseded
    path: ""
    id: dDsTa2
  - name: decision_id
    type: Input
    options: {}
    path: ""
    id: dDidN3
  - name: bookmark
    type: Input
    options: {}
    path: ""
    id: dDbKm4
  - name: roadmap_id
    type: Input
    options: {}
    path: ""
    id: dDrdM5
  - name: log_row
    type: Input
    options: {}
    path: ""
    id: dDlOg6
  - name: supersedes
    type: File
    options: {}
    path: ""
    id: dDsUp7
---

# DesignDecision (fileClass)

This is the **single source of allowed property values for design decision notes**. A design decision note records a choice about the structure or governance of the ontology (for example, a naming rule, a class design, or a commitment). It is not an idea. Ideas use the [[Idea]] fileClass.

- `type`: design-decision
- `status`: proposed → pending → settled → superseded
  - **proposed:** drafted and awaiting the author's view.
  - **pending:** the author has not chosen between options.
  - **settled:** the author has chosen; the choice is in [[Decisions_Log]].
  - **superseded:** replaced by a later decision (set `supersedes` on the newer note).
- `decision_id`: the roadmap or log identifier (for example `S37`), kept in step with the roadmap row.
- `bookmark`: `draft`, or the ID of the index the note is filed under once confirmed.
- `roadmap_id`: the roadmap row (for example `S38`).
- `log_row`: the Decisions_Log date and short title, filled in only when settled.
- `supersedes`: link to the decision this one replaces.

Rule: a design decision note is never filed as an idea, and an idea is never given `type: design-decision`.
