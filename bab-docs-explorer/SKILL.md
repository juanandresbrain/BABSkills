---
name: bab-docs-explorer
description: >-
  Search, navigate, and trace upstream/downstream data lineage across tables, stored procedures, views, SSIS packages, and SQL Agent jobs in the BAB Engineering Data Architecture documentation. Useful for debugging data discrepancies and resolving report bugs from ConnectWise tickets.
---

# BAB Data Architecture Explorer

## Overview
This skill provides automated commands to explore the BAB Engineering Data Architecture documentation. It is designed to trace data lineage across 6 databases, 931 tables, 547 stored procedures, 308 views, 239 SSIS projects, and 290 SQL Agent jobs. Use this skill to investigate data discrepancies, identify where specific tables/columns are populated, and determine which SQL Agent jobs or SSIS packages run them.

## Dependencies
None.

## Quick Start
To trace the data flow lineage for any table (e.g. `CustomerLeadGenStage` or `BlitzCache`), execute the following command in the workspace root:

```bash
python .agents/skills/bab-docs-explorer/scripts/explore_docs.py trace-lineage CustomerLeadGenStage
```

This will analyze all documentation markdown files and output a tree representation of the upstream loading path to `explorer_output.md`.

## Utility Scripts

The `explore_docs.py` utility supports the following subcommands. By default, it writes results as a markdown report to `explorer_output.md`.

### 1. `trace-lineage <table_name>`
Generates a structured, tree-like lineage map tracing who populates the table.
- **Example**:
  ```bash
  python .agents/skills/bab-docs-explorer/scripts/explore_docs.py trace-lineage CustomerLeadGenStage
  ```
- **Output**: Writes the visual tree and description to `explorer_output.md` showing:
  `Table` 🡨 `View` / `SSIS Package` / `Stored Procedure` 🡨 `SQL Agent Job(s)` 🡨 `Parent Job(s)`

### 2. `trace-table <table_name>`
Finds all Stored Procedures, Views, SSIS Packages, and SQL Agent Jobs referencing the table.
- **Example**:
  ```bash
  python .agents/skills/bab-docs-explorer/scripts/explore_docs.py trace-table CustomerLeadGenStage
  ```

### 3. `find-table <table_name>`
Finds a table schema (columns, types, keys, and descriptions) in the data dictionary.
- **Example**:
  ```bash
  python .agents/skills/bab-docs-explorer/scripts/explore_docs.py find-table CustomerLeadGenStage
  ```

### 4. `describe-sp <sp_name>`
Inspects stored procedure parameters, table dependencies, and displays the source SQL code snippet.
- **Example**:
  ```bash
  python .agents/skills/bab-docs-explorer/scripts/explore_docs.py describe-sp sp_BlitzCache
  ```

### 5. `describe-view <view_name>`
Inspects a view's table dependencies and displays its source SQL code snippet.
- **Example**:
  ```bash
  python .agents/skills/bab-docs-explorer/scripts/explore_docs.py describe-view vw_BAB_POS_Pricebook
  ```

### 6. `describe-package <package_name>`
Inspects SSIS connection managers, control flow tasks, sources, and destinations.
- **Example**:
  ```bash
  python .agents/skills/bab-docs-explorer/scripts/explore_docs.py describe-package ExactTargetLeadGen
  ```

### 7. `describe-job <job_name>`
Shows step-by-step instructions, subsystems (TSQL, SSIS, CmdExec), and source code commands for a SQL Agent Job.
- **Example**:
  ```bash
  python .agents/skills/bab-docs-explorer/scripts/explore_docs.py describe-job CustomerTransactionETL
  ```

### 8. `search-all <keyword>`
Searches for text references in names, column descriptions, and code blocks across all components — including Views.
- **Example**:
  ```bash
  python .agents/skills/bab-docs-explorer/scripts/explore_docs.py search-all "FirstData"
  ```

## Key Flags
- `--json`: Outputs JSON data instead of markdown (defaults to markdown).
- `--output <path>`: Specifies a custom output file path instead of `explorer_output.md`.
- `--docs-dir <path>`: Explicitly points to the documentation directory (defaults to current directory `.`).

## Common Mistakes
1. **Wrong Schema Context**: Forgetting that tables are matched loosely (e.g. typing `CustomerLeadGenStage` matches `dbo.CustomerLeadGenStage` automatically). Do not type unnecessary brackets or quotes.
2. **Missing Out-of-Doc references**: Tracing will highlight if a Stored Procedure, View, or Job command references an object that has no dedicated documentation file (it will note it as a reference, but won't be able to fetch its columns).
3. **Checking stdout instead of output files**: The script writes details to `explorer_output.md` to prevent terminal output truncation. Always view the generated file to read the full report.

