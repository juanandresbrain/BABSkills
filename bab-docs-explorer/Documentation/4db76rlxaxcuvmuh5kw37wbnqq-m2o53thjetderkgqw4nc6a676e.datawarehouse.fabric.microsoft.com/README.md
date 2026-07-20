# 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com

Auto-generated documentation for a **Fabric Data Warehouse/Lakehouse SQL
endpoint** at this hostname, produced by `GenerateServerDocs.py` from the CSV
inventory under `Inventory/4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com/`.

Same Fabric capacity prefix (`4db76rlxaxcuvmuh5kw37wbnqq-`) as the
[other Fabric warehouse server](../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/README.md),
but a distinct workspace/warehouse endpoint (different suffix), referenced
directly by several PowerBI semantic models' Power Query source (e.g. via
`Sql.Database("<this hostname>", "LH_Source"/"LH_Mart"/..., ...)`); those are
cross-linked automatically from `Documentation/PowerBI/SemanticModels/.../Data
Source Cross-References`.

The inventory for this server was extracted directly via T-SQL system catalog
queries (`sys.tables`, `sys.sql_modules`, `sys.parameters`,
`sys.sql_expression_dependencies`) against the live endpoint using
`Get-FabricSqlInventory.ps1` (repo root), authenticated via an Azure AD token
for the `https://database.windows.net/` resource (`Az.Accounts`
`Get-AzAccessToken`, passed to `Invoke-Sqlcmd -AccessToken`).

## Object counts (doc files)

| Section | Count |
|---|---|
| Databases | 17 |
| Tables | 3530 |
| Stored Procedures | 2 |
| Functions | 4 |
| Views | 486 |
| SQL Agent Jobs | 0 |
| SSIS | 0 |

## Sections

| Section | Description |
|---|---|
| DataDictionary | Tables and columns (type, max length, nullable, PK) |
| StoredProcedures | SP code + table dependencies |
| Functions | Scalar/table function code, parameters, return type, dependencies |
| Views | View code + table dependencies |

> Regenerate after an inventory refresh:
> `powershell -File Get-FabricSqlInventory.ps1 -Endpoint "4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com"`
> then `py GenerateServerDocs.py "4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com"`,
> then copy the server's `Documentation/` folder into
> `BABSkills/bab-docs-explorer/Documentation/`.
