# dbo.import_asn_system_error

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_asn_system_error_id | smallint | 2 | 0 | YES |  |  |
| error_code | nvarchar | 20 | 0 |  |  |  |
| error_description | nvarchar | 2000 | 0 |  |  |  |
| identifier_sql | nvarchar | 2000 | 0 |  |  |  |
| correction_sql | nvarchar | 2000 | 0 |  |  |  |
| other_correction_sql | nvarchar | 2000 | 1 |  |  |  |
| instruction | nvarchar | 2000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)

