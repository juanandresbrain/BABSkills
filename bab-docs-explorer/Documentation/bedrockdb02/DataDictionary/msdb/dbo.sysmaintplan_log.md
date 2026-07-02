# dbo.sysmaintplan_log

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| task_detail_id | uniqueidentifier | 16 | 0 | YES |  |  |
| plan_id | uniqueidentifier | 16 | 1 |  |  |  |
| subplan_id | uniqueidentifier | 16 | 1 |  | YES |  |
| start_time | datetime | 8 | 1 |  |  |  |
| end_time | datetime | 8 | 1 |  |  |  |
| succeeded | bit | 1 | 1 |  |  |  |
| logged_remotely | bit | 1 | 0 |  |  |  |
| source_server_name | nvarchar | 256 | 1 |  |  |  |
| plan_name | nvarchar | 256 | 1 |  |  |  |
| subplan_name | nvarchar | 256 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_maintplan_close_logentry](../../StoredProcedures/msdb/dbo.sp_maintplan_close_logentry.md)
- [msdb: dbo.sp_maintplan_delete_log](../../StoredProcedures/msdb/dbo.sp_maintplan_delete_log.md)
- [msdb: dbo.sp_maintplan_open_logentry](../../StoredProcedures/msdb/dbo.sp_maintplan_open_logentry.md)

