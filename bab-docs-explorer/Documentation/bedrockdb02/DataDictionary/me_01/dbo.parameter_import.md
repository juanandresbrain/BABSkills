# dbo.parameter_import

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_import_id | smallint | 2 | 0 |  |  |  |
| parameter_import_name | nvarchar | 60 | 0 |  |  |  |
| parameter_import_value | nvarchar | 1000 | 0 |  |  |  |
| parameter_called_from | nvarchar | 240 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_generate_upc_state_$sp](../../StoredProcedures/me_01/dbo.dl_generate_upc_state_$sp.md)

