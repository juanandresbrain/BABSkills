# 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com

Auto-generated documentation for a **Fabric Data Warehouse/Lakehouse SQL
endpoint** at this hostname, produced by `GenerateServerDocs.py` from the CSV
inventory under `Inventory/4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com/`.

Same Fabric capacity prefix (`4db76rlxaxcuvmuh5kw37wbnqq-`) as the other two
Fabric warehouse servers
([ovsykae43znuhlmnflcdwm4ohu](../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/README.md),
[m2o53thjetderkgqw4nc6a676e](../4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com/README.md)),
but a distinct workspace/warehouse endpoint, referenced directly by several
PowerBI semantic models' Power Query source (e.g. via
`Sql.Database("<this hostname>", "LH_Source"/"LH_Mart"/"WH_Papamart"/...,
...)`); those are cross-linked automatically from
`Documentation/PowerBI/SemanticModels/.../Data Source Cross-References`.

The inventory for this server was extracted directly via T-SQL system catalog
queries (`sys.tables`, `sys.sql_modules`, `sys.parameters`,
`sys.sql_expression_dependencies`) against the live endpoint using
`Get-FabricSqlInventory.ps1` (repo root), authenticated via an Azure AD token
for the `https://database.windows.net/` resource (`Az.Accounts`
`Get-AzAccessToken`, passed to `Invoke-Sqlcmd -AccessToken`).

## Object counts (doc files)

| Section | Count |
|---|---|
| Databases | 20 |
| Tables | 3391 |
| Stored Procedures | 4 |
| Functions | 4 |
| Views | 410 |
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
> `powershell -File Get-FabricSqlInventory.ps1 -Endpoint "4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com"`
> then `py GenerateServerDocs.py "4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com"`,
> then copy the server's `Documentation/` folder into
> `BABSkills/bab-docs-explorer/Documentation/`.
