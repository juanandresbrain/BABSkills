# dbo.syscollector_execution_log_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| log_id | bigint | 8 | 0 | YES |  |  |
| parent_log_id | bigint | 8 | 1 |  |  |  |
| collection_set_id | int | 4 | 0 |  | YES |  |
| collection_item_id | int | 4 | 1 |  |  |  |
| start_time | datetime | 8 | 0 |  |  |  |
| last_iteration_time | datetime | 8 | 1 |  |  |  |
| finish_time | datetime | 8 | 1 |  |  |  |
| runtime_execution_mode | smallint | 2 | 1 |  |  |  |
| status | smallint | 2 | 0 |  |  |  |
| operator | nvarchar | 256 | 0 |  |  |  |
| package_id | uniqueidentifier | 16 | 1 |  |  |  |
| package_execution_id | uniqueidentifier | 16 | 1 |  |  |  |
| failure_message | nvarchar | 4096 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syscollector_event_oncollectionbegin](../../StoredProcedures/msdb/dbo.sp_syscollector_event_oncollectionbegin.md)
- [msdb: dbo.sp_syscollector_event_oncollectionend](../../StoredProcedures/msdb/dbo.sp_syscollector_event_oncollectionend.md)
- [msdb: dbo.sp_syscollector_event_oncollectionstart](../../StoredProcedures/msdb/dbo.sp_syscollector_event_oncollectionstart.md)
- [msdb: dbo.sp_syscollector_event_oncollectionstop](../../StoredProcedures/msdb/dbo.sp_syscollector_event_oncollectionstop.md)
- [msdb: dbo.sp_syscollector_event_onerror](../../StoredProcedures/msdb/dbo.sp_syscollector_event_onerror.md)
- [msdb: dbo.sp_syscollector_event_onpackagebegin](../../StoredProcedures/msdb/dbo.sp_syscollector_event_onpackagebegin.md)
- [msdb: dbo.sp_syscollector_event_onpackageend](../../StoredProcedures/msdb/dbo.sp_syscollector_event_onpackageend.md)
- [msdb: dbo.sp_syscollector_event_onpackageupdate](../../StoredProcedures/msdb/dbo.sp_syscollector_event_onpackageupdate.md)

