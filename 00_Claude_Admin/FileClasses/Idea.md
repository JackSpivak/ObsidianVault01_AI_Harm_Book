---
fields:
  - name: type
    type: Select
    options:
      sourceType: ValuesList
      valuesList:
        "1": idea
    path: ""
    id: tYp3ID
  - name: status
    type: Select
    options:
      sourceType: ValuesList
      valuesList:
        "1": stub
        "2": seed
        "3": developing
        "4": stable
        "5": archived
    path: ""
    id: sTat5A
  - name: bookmark
    type: Input
    options: {}
    path: ""
    id: bKm4rK
  - name: canonical_id
    type: Input
    options: {}
    path: ""
    id: cAn0iD
  - name: territory
    type: Select
    options:
      sourceType: ValuesList
      valuesList:
        "1": new
        "2": revisited
    path: ""
    id: tErr1T
  - name: revisits
    type: File
    options: {}
    path: ""
    id: rEv1sT
---

# Idea (fileClass)

This is the **single source of allowed property values for idea notes**. Metadata Menu reads it to show dropdowns. The rules, the skill and the Base all point here, so don't keep a second copy of these lists elsewhere.

- `type`: idea
- `status`: stub → seed → developing → stable → archived
- `bookmark`: free text, but it must be `draft`, `ready`, or an index ID like `GSH-003`. It can't be a fixed dropdown because index IDs keep growing. The "Problems" view in [[GSH Status.base|GSH Status]] checks it.
- `territory`: new | revisited
- `revisits`: link to the page being revisited (only when `territory: revisited`)

To add or rename a field, edit it here (or through Metadata Menu's fileClass view). To rename a property across all notes, use Obsidian's **All properties** view, then update the name here too.
