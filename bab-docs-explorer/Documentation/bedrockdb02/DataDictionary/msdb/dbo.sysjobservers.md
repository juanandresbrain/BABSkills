# dbo.sysjobservers

**Database:** msdb  
**Server:** bedrockdb02  

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
- [msdb: dbo.sp_add_jobstep_internal](../../StoredProcedures/msdb/dbo.sp_add_jobstep_internal.md)
- [msdb: dbo.sp_apply_job_to_targets](../../StoredProcedures/msdb/dbo.sp_apply_job_to_targets.md)
- [msdb: dbo.sp_attach_schedule](../../StoredProcedures/msdb/dbo.sp_attach_schedule.md)
- [msdb: dbo.sp_delete_all_msx_jobs](../../StoredProcedures/msdb/dbo.sp_delete_all_msx_jobs.md)
- [msdb: dbo.sp_delete_job](../../StoredProcedures/msdb/dbo.sp_delete_job.md)
- [msdb: dbo.sp_delete_jobschedule](../../StoredProcedures/msdb/dbo.sp_delete_jobschedule.md)
- [msdb: dbo.sp_delete_jobserver](../../StoredProcedures/msdb/dbo.sp_delete_jobserver.md)
- [msdb: dbo.sp_delete_jobstep](../../StoredProcedures/msdb/dbo.sp_delete_jobstep.md)
- [msdb: dbo.sp_delete_schedule](../../StoredProcedures/msdb/dbo.sp_delete_schedule.md)
- [msdb: dbo.sp_delete_targetserver](../../StoredProcedures/msdb/dbo.sp_delete_targetserver.md)
- [msdb: dbo.sp_detach_schedule](../../StoredProcedures/msdb/dbo.sp_detach_schedule.md)
- [msdb: dbo.sp_generate_target_server_job_assignment_sql](../../StoredProcedures/msdb/dbo.sp_generate_target_server_job_assignment_sql.md)
- [msdb: dbo.sp_get_composite_job_info](../../StoredProcedures/msdb/dbo.sp_get_composite_job_info.md)
- [msdb: dbo.sp_help_jobhistory](../../StoredProcedures/msdb/dbo.sp_help_jobhistory.md)
- [msdb: dbo.sp_help_jobhistory_full](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_full.md)
- [msdb: dbo.sp_help_jobhistory_sem](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_sem.md)
- [msdb: dbo.sp_help_jobhistory_summary](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_summary.md)
- [msdb: dbo.sp_help_jobserver](../../StoredProcedures/msdb/dbo.sp_help_jobserver.md)
- [msdb: dbo.sp_manage_jobs_by_login](../../StoredProcedures/msdb/dbo.sp_manage_jobs_by_login.md)
- [msdb: dbo.sp_multi_server_job_summary](../../StoredProcedures/msdb/dbo.sp_multi_server_job_summary.md)
- [msdb: dbo.sp_post_msx_operation](../../StoredProcedures/msdb/dbo.sp_post_msx_operation.md)
- [msdb: dbo.sp_sqlagent_refresh_job](../../StoredProcedures/msdb/dbo.sp_sqlagent_refresh_job.md)
- [msdb: dbo.sp_start_job](../../StoredProcedures/msdb/dbo.sp_start_job.md)
- [msdb: dbo.sp_stop_job](../../StoredProcedures/msdb/dbo.sp_stop_job.md)
- [msdb: dbo.sp_update_job](../../StoredProcedures/msdb/dbo.sp_update_job.md)
- [msdb: dbo.sp_update_jobschedule](../../StoredProcedures/msdb/dbo.sp_update_jobschedule.md)
- [msdb: dbo.sp_update_jobstep](../../StoredProcedures/msdb/dbo.sp_update_jobstep.md)
- [msdb: dbo.sp_update_schedule](../../StoredProcedures/msdb/dbo.sp_update_schedule.md)
- [msdb: dbo.sp_verify_alert](../../StoredProcedures/msdb/dbo.sp_verify_alert.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)
- [msdb: dbo.sp_verify_jobstep](../../StoredProcedures/msdb/dbo.sp_verify_jobstep.md)
- [DBAUtility: dbo.report_running_jobs](../../StoredProcedures/DBAUtility/dbo.report_running_jobs.md)

