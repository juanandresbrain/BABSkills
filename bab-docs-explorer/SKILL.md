---
name: bab-docs-explorer
description: >-
  Search, navigate, and trace upstream/downstream data lineage across tables, stored procedures, functions, views, SSIS packages, SQL Agent jobs, and PowerBI reports/semantic models in the BAB Engineering Data Architecture documentation, spanning all eight SQL servers (bearcluster01, bedrockdb01, bedrockdb02, papamart, STL-SSIS-P-01, and three Fabric Data Warehouse/Lakehouse endpoints) plus PowerBI (reports, pages, visuals, measures, Power Query source). Useful for debugging data discrepancies and resolving report bugs from ConnectWise tickets.
---

# BAB Data Architecture Explorer

## Overview
This skill provides automated commands to explore the BAB Engineering Data Architecture documentation. It traces data lineage across **8 SQL servers (~124 databases, ~21,720 tables, ~11,967 stored procedures, ~206 functions, ~4,754 views, 265 SSIS packages, 621 SQL Agent jobs) plus PowerBI (433 reports, 85 semantic models, 6,726 DAX measures)**. Use it to investigate data discrepancies, identify where specific tables/columns are populated, determine which SQL Agent jobs or SSIS packages run them, and trace which PowerBI reports/semantic models pull from a given SQL table.

The documentation is **bundled inside this skill** at `Documentation/`, organized by server (SQL) or platform (PowerBI), so no external paths are needed:

| Server | Tables | Stored Procedures | Functions | Views | SSIS | Jobs |
|---|---|---|---|---|---|---|
| bearcluster01 | ~594 | ~762 | ~22 | ~169 | 0 | ~20 |
| bedrockdb01 | ~4,253 | ~2,558 | ~37 | ~781 | 0 | ~83 |
| bedrockdb02 | ~4,971 | ~4,408 | ~35 | ~870 | 0 | ~170 |
| papamart | ~1,676 | ~1,035 | ~76 | ~742 | 0 | ~59 |
| STL-SSIS-P-01 | ~931 | ~547 | ~21 | ~305 | ~265 | ~289 |
| 4db76...ovsykae...fabric.microsoft.com (Fabric DW/Lakehouse) | ~2,296 | ~24 | ~7 | ~977 | 0 | 0 |
| 4db76...m2o53...fabric.microsoft.com (Fabric DW/Lakehouse) | ~3,530 | ~2 | ~4 | ~486 | 0 | 0 |
| 4db76...oxjjwe...fabric.microsoft.com (Fabric DW/Lakehouse) | ~3,391 | ~4 | ~4 | ~410 | 0 | 0 |

> There are **three** Fabric warehouse servers, all sharing the same Fabric capacity prefix `4db76rlxaxcuvmuh5kw37wbnqq-` but with distinct workspace suffixes - `--server 4db76` alone matches all three at once, so use enough of the suffix to disambiguate (e.g. `--server ovsykae`, `--server m2o53`, `--server oxjjwe`). Each is the backing SQL endpoint for several Fabric Lakehouses/Warehouses (`LH_Source`, `LH_Mart`, `LH_D365`, `WH_Papamart`, etc. as their "databases") that PowerBI semantic models connect to directly via Power Query. Their inventories were extracted directly from the live endpoints via T-SQL system catalog queries (`Get-FabricSqlInventory.ps1`, repo root - Azure AD token auth through `Az.Accounts`), not from a pre-collected CSV export like the other servers.

| Platform | Reports | Semantic Models | Measures |
|---|---|---|---|
| PowerBI | 433 (129 full page/visual detail, 240 model-only, 64 not available) | 85 | 6,726 |

> Because names repeat across servers (e.g. `dbo.CommandLog` exists on several, and PowerBI report names repeat across workspaces), most queries return **one result per server/workspace**. Use `--server` to narrow to a single server (also matches `PowerBI`). Run `list-servers` to see the current breakdown.

## Dependencies
Python 3 only. On Windows, if `python` is not found, use the `py` launcher instead (e.g. `py scripts/explore_docs.py ...`).

## Quick Start
To trace the data flow lineage for any table (e.g. `CustomerLeadGenStage`), run from the skill directory:

```bash
python scripts/explore_docs.py trace-lineage CustomerLeadGenStage
```

This analyzes all documentation and writes a tree of the upstream loading path to `explorer_output.md`. The docs path defaults to the bundled `Documentation/` folder automatically — no `--docs-dir` needed.

## Utility Scripts

The `explore_docs.py` utility supports the following subcommands. By default, it writes results as a markdown report to `explorer_output.md`.

### 1. `trace-lineage <table_name>`
Generates a structured, tree-like lineage map tracing who populates the table.
- **Example**:
  ```bash
  python scripts/explore_docs.py trace-lineage CustomerLeadGenStage
  ```
- **Output**: Writes the visual tree and description to `explorer_output.md` showing:
  `Table` 🡨 `View` / `SSIS Package` / `Stored Procedure` 🡨 `SQL Agent Job(s)` 🡨 `Parent Job(s)`

### 2. `trace-table <table_name>`
Finds all Stored Procedures, Functions, Views, SSIS Packages, SQL Agent Jobs, and **PowerBI semantic models** referencing the table (each result tagged with its server/workspace). A PowerBI match comes from either the model's `Data Source Cross-References` table (precise: the Power Query source literally connects to `<server>`/`<database>`) or a loose text match inside the Power Query/M source, and lists which PowerBI report(s) use that semantic model.
- **Example**:
  ```bash
  python scripts/explore_docs.py trace-table CustomerLeadGenStage
  ```

### 3. `find-table <table_name>`
Finds a table schema (columns, types, keys, and descriptions) in the data dictionary.
- **Example**:
  ```bash
  python scripts/explore_docs.py find-table CustomerLeadGenStage
  ```

### 4. `describe-sp <sp_name>`
Inspects stored procedure parameters, table dependencies, and displays the source SQL code snippet.
- **Example**:
  ```bash
  python scripts/explore_docs.py describe-sp sp_BlitzCache
  ```

### 5. `describe-function <function_name>`
Inspects a scalar/table function's type, return type, table dependencies, and displays its source SQL code snippet.
- **Example**:
  ```bash
  python scripts/explore_docs.py describe-function udf_StripHTML
  ```

### 6. `describe-view <view_name>`
Inspects a view's table dependencies and displays its source SQL code snippet.
- **Example**:
  ```bash
  python scripts/explore_docs.py describe-view vw_BAB_POS_Pricebook
  ```

### 7. `describe-package <package_name>`
Inspects an SSIS package: connection managers (with server/catalog, credentials stripped), control-flow outline (indented, preserves loop nesting), data-flow sources/destinations with component names, and — importantly — the package's **business logic**: the `## Variables` section (full expression-bound SQL) and the `## Execute SQL Tasks` section (full `SqlStatementSource`, with runtime property-expression overrides flagged). This is where per-store computations and staging SQL usually live.
- **Example**:
  ```bash
  python scripts/explore_docs.py describe-package HR_StoreForcePosSalesExtract
  ```
- **Note:** SSIS package docs are re-extracted from the raw `.ispac`/`.dtsx` by `GenerateSsisDocs.py` (repo root). Logic stored in package Variables and Execute SQL Task bodies is now indexed by `search-all` — see `KNOWN_LIMITATIONS.md` for the history (ticket 104344).

### 8. `describe-job <job_name>`
Shows step-by-step instructions, subsystems (TSQL, SSIS, CmdExec), and source code commands for a SQL Agent Job.
- **Example**:
  ```bash
  python scripts/explore_docs.py describe-job CustomerTransactionETL
  ```

### 9. `describe-report <report_name>`
Inspects a PowerBI report: workspace, dataset it's built on, field dependencies, pages, and every visual (type + fields used per visual). If the report's own page/visual layout couldn't be extracted (Fabric/Premium storage format, Direct Lake, or viewer-only permissions), shows the reason instead and points to the linked semantic model, which is documented independently via the XMLA endpoint regardless of that limitation.
- **Example**:
  ```bash
  python scripts/explore_docs.py describe-report "GAAP Flash Sales Report"
  ```

### 10. `describe-semantic-model <model_name>`
Inspects a PowerBI semantic model (dataset): tables, DAX measures (full expression), Power Query (M) source per table, shared expressions, and detected SQL data-source cross-references (e.g. a table's Power Query source connecting to `Sql.Database("papamart", "dw")` is linked straight back to that server's data dictionary).
- **Example**:
  ```bash
  python scripts/explore_docs.py describe-semantic-model "GAAP Flash Sales Report"
  ```

### 11. `search-all <keyword>`
Searches for text references in names, column descriptions, and code blocks across all components (Tables, SPs, Functions, Views, SSIS, Jobs, PowerBI Reports, PowerBI Semantic Models) on every server/workspace. Results include the server column.
- **Example**:
  ```bash
  python scripts/explore_docs.py search-all "FirstData"
  ```

### 12. `list-servers`
Lists the servers/platforms found in the documentation set and per-server object counts (including PowerBI report/semantic-model counts). Useful to confirm coverage before filtering with `--server`.
- **Example**:
  ```bash
  python scripts/explore_docs.py list-servers
  ```

## Regenerating Documentation
This skill's `Documentation/` folder is a **manually-synced copy** of the master copy at the repo root (`BABEngineering/Documentation/`) — the same pattern used for SSIS. After refreshing any inventory and regenerating docs, copy the updated folder(s) in:
- SQL servers: `py GenerateServerDocs.py <server>` / `py GenerateFunctionDocs.py` / `py GenerateSsisDocs.py`, then copy the changed `Documentation/<server>/...` subfolder into `bab-docs-explorer/Documentation/<server>/...`.
- Fabric warehouse servers specifically: their CSV inventory isn't hand-collected - refresh it live with `powershell -File Get-FabricSqlInventory.ps1 -Endpoint <hostname>` (queries `sys.tables`/`sys.sql_modules`/`sys.parameters`/`sys.sql_expression_dependencies` directly via an Azure AD token for `https://database.windows.net/`), then run `GenerateServerDocs.py <hostname>` and copy as above. If a *new* Fabric endpoint turns up (e.g. referenced in a PowerBI semantic model's Power Query source but not yet in `Inventory/`), this is also how to onboard it - same script, just point `-Endpoint` at the new hostname.
- PowerBI: `py GeneratePowerBIDocs.py` (reads `Inventory/PowerBI/*.csv`, itself refreshed via `Get-PowerBIReportInventory.ps1` / `Get-PowerBIFullInventory.ps1` / `Get-PowerBISemanticModelInventory.ps1`), then copy `Documentation/PowerBI/` into `bab-docs-explorer/Documentation/PowerBI/`. If you add a new SQL server (Fabric or otherwise), also add its hostname to the `SQL_SERVERS` list in `GeneratePowerBIDocs.py` so its Data Source Cross-References resolve instead of showing "not found."

## Key Flags
- `--server <name>`: Restrict results to a single server (loose/substring match), e.g. `--server bedrockdb02`, `--server bearcluster01`, `--server STL`. Applies to every command above.
- `--json`: Outputs JSON data instead of markdown (defaults to markdown).
- `--output <path>`: Specifies a custom output file path instead of `explorer_output.md`.
- `--docs-dir <path>`: Overrides the documentation directory. Defaults to the `Documentation/` folder bundled with the skill; only needed if pointing at an external docs set.

## Common Mistakes
1. **Ignoring cross-server duplicates**: The same object name often exists on multiple servers, so a query can return several results. Read the `**Server:**` line on each result, and pass `--server` when you only care about one server.
2. **Wrong Schema Context**: Tables are matched loosely (e.g. typing `CustomerLeadGenStage` matches `dbo.CustomerLeadGenStage` automatically). Do not type unnecessary brackets or quotes.
3. **Missing Out-of-Doc references**: Tracing highlights when a Stored Procedure, View, or Job command references an object that has no dedicated documentation file (noted as a reference, but its columns can't be fetched).
4. **Checking stdout instead of output files**: The script writes details to `explorer_output.md` to prevent terminal output truncation. Always view the generated file to read the full report.
5. **`python` not found on Windows**: Use the `py` launcher instead (`py scripts/explore_docs.py ...`).
6. **PowerBI report names repeat across workspaces even more than SQL objects do** (e.g. "GAAP Flash Sales Report" exists in multiple workspaces with different data) — always check the `**Workspace:**` line on each result.
7. **A PowerBI report with no page/visual detail isn't necessarily undocumented** — check its `**Semantic Model:**` link; tables, measures, and Power Query source are often still fully documented even when the report's own layout couldn't be extracted (see the "Model Only" count in `list-servers`/the workspace `_index.md`).
