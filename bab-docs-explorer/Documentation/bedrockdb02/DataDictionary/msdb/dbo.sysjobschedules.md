# dbo.sysjobschedules

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| schedule_id | int | 4 | 1 |  | YES |  |
| job_id | uniqueidentifier | 16 | 1 |  | YES |  |
| next_run_date | int | 4 | 0 |  |  |  |
| next_run_time | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_attach_schedule](../../StoredProcedures/msdb/dbo.sp_attach_schedule.md)
- [msdb: dbo.sp_delete_all_msx_jobs](../../StoredProcedures/msdb/dbo.sp_delete_all_msx_jobs.md)
- [msdb: dbo.sp_delete_job](../../StoredProcedures/msdb/dbo.sp_delete_job.md)
- [msdb: dbo.sp_delete_jobschedule](../../StoredProcedures/msdb/dbo.sp_delete_jobschedule.md)
- [msdb: dbo.sp_delete_schedule](../../StoredProcedures/msdb/dbo.sp_delete_schedule.md)
- [msdb: dbo.sp_detach_schedule](../../StoredProcedures/msdb/dbo.sp_detach_schedule.md)
- [msdb: dbo.sp_get_composite_job_info](../../StoredProcedures/msdb/dbo.sp_get_composite_job_info.md)
- [msdb: dbo.sp_help_jobcount](../../StoredProcedures/msdb/dbo.sp_help_jobcount.md)
- [msdb: dbo.sp_help_jobschedule](../../StoredProcedures/msdb/dbo.sp_help_jobschedule.md)
- [msdb: dbo.sp_help_schedule](../../StoredProcedures/msdb/dbo.sp_help_schedule.md)
- [msdb: dbo.sp_maintplan_update_subplan_tsx](../../StoredProcedures/msdb/dbo.sp_maintplan_update_subplan_tsx.md)
- [msdb: dbo.sp_post_msx_operation](../../StoredProcedures/msdb/dbo.sp_post_msx_operation.md)
- [msdb: dbo.sp_update_jobschedule](../../StoredProcedures/msdb/dbo.sp_update_jobschedule.md)
- [msdb: dbo.sp_update_schedule](../../StoredProcedures/msdb/dbo.sp_update_schedule.md)
- [msdb: dbo.sp_verify_schedule_identifiers](../../StoredProcedures/msdb/dbo.sp_verify_schedule_identifiers.md)
- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)
- [DBAUtility: dbo.report_running_jobs](../../StoredProcedures/DBAUtility/dbo.report_running_jobs.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)

