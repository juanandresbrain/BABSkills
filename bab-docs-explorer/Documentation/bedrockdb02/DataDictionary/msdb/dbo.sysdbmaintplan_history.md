# dbo.sysdbmaintplan_history

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sequence_id | int | 4 | 0 |  |  |  |
| plan_id | uniqueidentifier | 16 | 0 |  |  |  |
| plan_name | sysname | 256 | 0 |  |  |  |
| database_name | sysname | 256 | 1 |  |  |  |
| server_name | sysname | 256 | 0 |  |  |  |
| activity | nvarchar | 256 | 1 |  |  |  |
| succeeded | bit | 1 | 0 |  |  |  |
| end_time | datetime | 8 | 0 |  |  |  |
| duration | int | 4 | 1 |  |  |  |
| start_time | datetime | 8 | 1 |  |  |  |
| error_number | int | 4 | 0 |  |  |  |
| message | nvarchar | 1024 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_clear_dbmaintplan_by_db](../../StoredProcedures/msdb/dbo.sp_clear_dbmaintplan_by_db.md)

