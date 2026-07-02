# dbo.sysmaintplan_logdetail

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| task_detail_id | uniqueidentifier | 16 | 0 |  | YES |  |
| line1 | nvarchar | 512 | 0 |  |  |  |
| line2 | nvarchar | 512 | 1 |  |  |  |
| line3 | nvarchar | 512 | 1 |  |  |  |
| line4 | nvarchar | 512 | 1 |  |  |  |
| line5 | nvarchar | 512 | 1 |  |  |  |
| server_name | sysname | 256 | 0 |  |  |  |
| start_time | datetime | 8 | 1 |  |  |  |
| end_time | datetime | 8 | 1 |  |  |  |
| error_number | int | 4 | 1 |  |  |  |
| error_message | nvarchar | -1 | 1 |  |  |  |
| command | nvarchar | -1 | 1 |  |  |  |
| succeeded | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_maintplan_delete_log](../../StoredProcedures/msdb/dbo.sp_maintplan_delete_log.md)
- [msdb: dbo.sp_maintplan_update_log](../../StoredProcedures/msdb/dbo.sp_maintplan_update_log.md)

