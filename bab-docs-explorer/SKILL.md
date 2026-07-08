---
name: bab-docs-explorer
description: >-
  Search, navigate, and trace upstream/downstream data lineage across tables, stored procedures, functions, views, SSIS packages, and SQL Agent jobs in the BAB Engineering Data Architecture documentation, spanning all three servers (bearcluster01, bedrockdb02, STL-SSIS-P-01). Useful for debugging data discrepancies and resolving report bugs from ConnectWise tickets.
---

# BAB Data Architecture Explorer

## Overview
This skill provides automated commands to explore the BAB Engineering Data Architecture documentation. It traces data lineage across **3 servers, 37 databases, ~6,496 tables, ~8,344 stored procedures, ~78 functions, ~1,344 views, 265 SSIS packages, and 479 SQL Agent jobs**. Use it to investigate data discrepancies, identify where specific tables/columns are populated, and determine which SQL Agent jobs or SSIS packages run them.

The documentation is **bundled inside this skill** at `Documentation/`, organized by server, so no external paths are needed:

| Server | Tables | Stored Procedures | Functions | Views | SSIS | Jobs |
|---|---|---|---|---|---|---|
| bearcluster01 | ~594 | ~762 | ~22 | ~169 | 0 | ~20 |
| bedrockdb02 | ~4,971 | ~4,408 | ~35 | ~870 | 0 | ~170 |
| STL-SSIS-P-01 | ~931 | ~547 | ~21 | ~305 | ~265 | ~289 |

> Because names repeat across servers (e.g. `dbo.CommandLog` exists on all three), most queries return **one result per server**. Use `--server` to narrow to a single server. Run `list-servers` to see the current breakdown.

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
Finds all Stored Procedures, Functions, Views, SSIS Packages, and SQL Agent Jobs referencing the table (each result tagged with its server).
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

### 9. `search-all <keyword>`
Searches for text references in names, column descriptions, and code blocks across all components (Tables, SPs, Functions, Views, SSIS, Jobs) on every server. Results include the server column.
- **Example**:
  ```bash
  python scripts/explore_docs.py search-all "FirstData"
  ```

### 10. `list-servers`
Lists the servers found in the documentation set and per-server object counts. Useful to confirm coverage before filtering with `--server`.
- **Example**:
  ```bash
  python scripts/explore_docs.py list-servers
  ```

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
