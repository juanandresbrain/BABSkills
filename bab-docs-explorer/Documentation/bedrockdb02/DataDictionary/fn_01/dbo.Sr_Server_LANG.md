# dbo.Sr_Server_LANG

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server_id | int | 4 | 0 | YES |  |  |
| machine_id | int | 4 | 0 | YES |  |  |
| lang_id | smallint | 2 | 0 | YES |  |  |
| server_name | nvarchar | 60 | 1 |  |  |  |
| reporting_server_description | nvarchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sr_RemoveServer](../../StoredProcedures/fn_01/dbo.Sr_RemoveServer.md)

