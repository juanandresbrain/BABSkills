# dbo.job_message

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| message_id | int | 4 | 0 |  |  |  |
| job_type | int | 4 | 0 |  |  |  |
| resource_id | int | 4 | 1 |  |  |  |
| language_id | smallint | 2 | 0 |  |  |  |
| resource_description | nvarchar | 1000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)

