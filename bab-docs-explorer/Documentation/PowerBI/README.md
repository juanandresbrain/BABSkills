# PowerBI - Data Architecture Documentation

> Auto-generated documentation of Power BI report/page/visual/field
> structure and underlying semantic model (tables/measures/Power
> Query source), produced by `GeneratePowerBIDocs.py` from the CSV
> inventory under `Inventory/PowerBI/` (itself produced by
> `Get-PowerBIReportInventory.ps1`, `Get-PowerBIFullInventory.ps1`,
> and `Get-PowerBISemanticModelInventory.ps1`).

## Workspaces

| Workspace | Reports | Documented | Model Only | Not Available | Visuals | Datasets | Model Tables | Measures |
|---|---|---|---|---|---|---|---|---|
| [BI-Accounting](DataDictionary/BI-Accounting/_index.md) | 68 | 27 | 38 | 3 | 827 | [34](SemanticModels/BI-Accounting/_index.md) | 370 | 4 |
| [BI-International](DataDictionary/BI-International/_index.md) | 3 | 1 | 0 | 2 | 89 | 0 | 0 | 0 |
| [BI-Bearhouse](DataDictionary/BI-Bearhouse/_index.md) | 11 | 3 | 1 | 7 | 13 | [1](SemanticModels/BI-Bearhouse/_index.md) | 2 | 0 |
| [BI-Information Technology](DataDictionary/BI-Information Technology/_index.md) | 5 | 2 | 1 | 2 | 181 | [3](SemanticModels/BI-Information Technology/_index.md) | 44 | 1 |
| [Enterprise Analytics Dev](DataDictionary/Enterprise Analytics Dev/_index.md) | 122 | 72 | 41 | 9 | 2309 | [21](SemanticModels/Enterprise Analytics Dev/_index.md) | 441 | 3537 |
| [Enterprise Analytics Prod](DataDictionary/Enterprise Analytics Prod/_index.md) | 76 | 3 | 71 | 2 | 37 | [12](SemanticModels/Enterprise Analytics Prod/_index.md) | 337 | 1809 |
| [Enterprise Analytics QA](DataDictionary/Enterprise Analytics QA/_index.md) | 148 | 21 | 88 | 39 | 697 | [14](SemanticModels/Enterprise Analytics QA/_index.md) | 617 | 1375 |

## Grand Totals

| Metric | Count |
|---|---|
| Workspaces | 7 |
| Reports | 433 |
| Documented (full: pages/visuals/fields) | 129 |
| Model Only (visual layout unavailable, semantic model documented) | 240 |
| Not Available (nothing extractable) | 64 |
| Visuals | 4153 |
| Semantic Models (Datasets) | 85 |
| Model Tables | 1811 |
| Measures | 6726 |

> "Documented" reports have full page/visual/field detail from the PBIX
> export. "Model Only" reports couldn't produce a readable .pbix (see
> the workspace `_index.md` Status column for why: e.g. Fabric/Premium
> "Files" storage format, Direct Lake semantic model, viewer-only
> permissions) but their underlying semantic model - tables, measures,
> Power Query source - was still pulled via the XMLA endpoint, which
> works regardless of the PBIX export limitation, and is linked from
> their doc. "Not Available" reports have neither (mostly auto-generated
> Usage Metrics reports or dataset name collisions XMLA can't resolve).
