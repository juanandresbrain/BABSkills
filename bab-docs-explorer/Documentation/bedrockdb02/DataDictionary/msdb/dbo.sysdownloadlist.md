# dbo.sysdownloadlist

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| instance_id | int | 4 | 0 |  |  |  |
| source_server | sysname | 256 | 0 |  |  |  |
| operation_code | tinyint | 1 | 0 |  |  |  |
| object_type | tinyint | 1 | 0 |  |  |  |
| object_id | uniqueidentifier | 16 | 0 |  |  |  |
| target_server | sysname | 256 | 0 |  |  |  |
| error_message | nvarchar | 2048 | 1 |  |  |  |
| date_posted | datetime | 8 | 0 |  |  |  |
| date_downloaded | datetime | 8 | 1 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| deleted_object_name | sysname | 256 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_delete_job](../../StoredProcedures/msdb/dbo.sp_delete_job.md)
- [msdb: dbo.sp_delete_targetserver](../../StoredProcedures/msdb/dbo.sp_delete_targetserver.md)
- [msdb: dbo.sp_downloaded_row_limiter](../../StoredProcedures/msdb/dbo.sp_downloaded_row_limiter.md)
- [msdb: dbo.sp_enlist_tsx](../../StoredProcedures/msdb/dbo.sp_enlist_tsx.md)
- [msdb: dbo.sp_help_downloadlist](../../StoredProcedures/msdb/dbo.sp_help_downloadlist.md)
- [msdb: dbo.sp_help_targetserver](../../StoredProcedures/msdb/dbo.sp_help_targetserver.md)
- [msdb: dbo.sp_multi_server_job_summary](../../StoredProcedures/msdb/dbo.sp_multi_server_job_summary.md)
- [msdb: dbo.sp_post_msx_operation](../../StoredProcedures/msdb/dbo.sp_post_msx_operation.md)
- [msdb: dbo.sp_resync_targetserver](../../StoredProcedures/msdb/dbo.sp_resync_targetserver.md)
- [msdb: dbo.sp_sqlagent_probe_msx](../../StoredProcedures/msdb/dbo.sp_sqlagent_probe_msx.md)
- [msdb: dbo.sp_target_server_summary](../../StoredProcedures/msdb/dbo.sp_target_server_summary.md)

