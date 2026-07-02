# dbo.sysjobservers

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | uniqueidentifier | 16 | 0 |  |  |  |
| server_id | int | 4 | 0 |  |  |  |
| last_run_outcome | tinyint | 1 | 0 |  |  |  |
| last_outcome_message | nvarchar | 8000 | 1 |  |  |  |
| last_run_date | int | 4 | 0 |  |  |  |
| last_run_time | int | 4 | 0 |  |  |  |
| last_run_duration | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_jobserver](../../StoredProcedures/msdb/dbo.sp_add_jobserver.md)
- [msdb: dbo.sp_attach_schedule](../../StoredProcedures/msdb/dbo.sp_attach_schedule.md)
- [msdb: dbo.sp_delete_schedule](../../StoredProcedures/msdb/dbo.sp_delete_schedule.md)
- [msdb: dbo.sp_detach_schedule](../../StoredProcedures/msdb/dbo.sp_detach_schedule.md)
- [msdb: dbo.sp_help_jobhistory_sem](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_sem.md)
- [msdb: dbo.sp_update_schedule](../../StoredProcedures/msdb/dbo.sp_update_schedule.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)

