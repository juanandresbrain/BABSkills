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
| Views | View code and table dependencies |
| SSIS Packages | Package architecture, connections, control flow, data flow sources/destinations |
| SQL Agent Jobs | Job schedules, steps, and commands with architecture diagrams |

## System Stats

| Server | Databases | Tables | SPs | Views | SSIS | Jobs |
|---|---|---|---|---|---|---|
| bearcluster01 | 14 | 635 | 761 | 169 | 0 | 20 |
| bedrockdb02 | 17 | 5008 | 7036 | 880 | 0 | 170 |
| STL-SSIS-P-01 | 6 | 931 | 547 | 309 | 239 | 290 |
| **Grand Total** | **37** | **6574** | **8344** | **1358** | **239** | **480** |
