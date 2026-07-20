# 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com

Auto-generated documentation for the **Fabric Data Warehouse/Lakehouse SQL
endpoint** at this hostname, produced by `GenerateServerDocs.py` from the CSV
inventory under `Inventory/4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/`.

This is the backing SQL endpoint for several Fabric Lakehouses/Warehouses used
as Power BI semantic model data sources (`LH_Source`, `LH_Mart`, `LH_D365`,
`LH_Staging`, `WH_Papamart`, etc. - see databases below). Several PowerBI
semantic models' Power Query source connects here directly (e.g. via
`Sql.Database("<this hostname>", "LH_Source", ...)`); those are cross-linked
automatically from `Documentation/PowerBI/SemanticModels/.../Data Source
Cross-References`.

> **Note:** unlike the other SQL servers, this inventory's Stored Procedure /
> Function / View code CSVs are **properly RFC4180-quoted** (embedded commas
> and quotes correctly escaped), rather than the raw unquoted line-based dumps
> used for bedrockdb01/papamart. `GenerateServerDocs.py`'s `parse_code_records`
> auto-detects this and parses it with Python's `csv` module, falling back to
> the legacy line-based parser for servers using the older raw format.

## Object counts (doc files)

| Section | Count |
|---|---|
| Databases | 21 |
| Tables | 2296 |
| Stored Procedures | 24 |
| Functions | 7 |
| Views | 977 |
| SQL Agent Jobs | 0 |
| SSIS | 0 |

## Sections

| Section | Description |
|---|---|
| DataDictionary | Tables and columns (type, max length, nullable, PK) |
| StoredProcedures | SP code + table dependencies |
| Functions | Scalar/table function code, parameters, return type, dependencies |
| Views | View code + table dependencies |

> Regenerate after an inventory refresh: `py GenerateServerDocs.py "4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com"`,
> then copy the server's `Documentation/` folder into
> `BABSkills/bab-docs-explorer/Documentation/`.
