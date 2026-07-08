# BAB Engineering - Data Architecture Documentation

> Auto-generated documentation covering all databases, stored procedures, views, SSIS packages, and SQL Agent jobs across every server.

## Skill

The [`bab-docs-explorer`](bab-docs-explorer/SKILL.md) skill searches, navigates, and traces data lineage across this documentation set. The docs are bundled with the skill at [`bab-docs-explorer/Documentation/`](bab-docs-explorer/Documentation/), organized by server:

```
bab-docs-explorer/Documentation/<server>/{DataDictionary,StoredProcedures,Views,SSIS,Jobs}/
```

Run `python bab-docs-explorer/scripts/explore_docs.py list-servers` for the live breakdown (use `py` on Windows if `python` is unavailable).

## Sections (per server)

| Section | Description |
|---|---|
| Data Dictionary | All tables and columns with types, keys, cross-references to SPs |
| Stored Procedures | SP code, parameters, table dependencies with architecture diagrams |
| Functions | Scalar/table function code, parameters, return type, table dependencies |
| Views | View code and table dependencies |
| SSIS Packages | Package architecture, connections, control flow, data flow sources/destinations |
| SQL Agent Jobs | Job schedules, steps, and commands with architecture diagrams |

## System Stats

(Object counts as loaded by the skill; run `list-servers` for the live breakdown.)

| Server | Tables | SPs | Functions | Views | SSIS | Jobs |
|---|---|---|---|---|---|---|
| bearcluster01 | 594 | 762 | 22 | 169 | 0 | 20 |
| bedrockdb01 | 4253 | 2558 | 37 | 781 | 0 | 83 |
| bedrockdb02 | 4971 | 4408 | 35 | 870 | 0 | 170 |
| STL-SSIS-P-01 | 931 | 547 | 21 | 305 | 265 | 289 |
| **Grand Total** | **10749** | **8275** | **115** | **2125** | **265** | **562** |
