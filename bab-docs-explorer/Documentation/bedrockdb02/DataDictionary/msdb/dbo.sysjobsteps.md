# dbo.sysjobsteps

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | uniqueidentifier | 16 | 0 |  |  |  |
| step_id | int | 4 | 0 |  |  |  |
| step_name | sysname | 256 | 0 |  |  |  |
| subsystem | nvarchar | 80 | 0 |  |  |  |
| command | nvarchar | -1 | 1 |  |  |  |
| flags | int | 4 | 0 |  |  |  |
| additional_parameters | nvarchar | -1 | 1 |  |  |  |
| cmdexec_success_code | int | 4 | 0 |  |  |  |
| on_success_action | tinyint | 1 | 0 |  |  |  |
| on_success_step_id | int | 4 | 0 |  |  |  |
| on_fail_action | tinyint | 1 | 0 |  |  |  |
| on_fail_step_id | int | 4 | 0 |  |  |  |
| server | sysname | 256 | 1 |  |  |  |
| database_name | sysname | 256 | 1 |  |  |  |
| database_user_name | sysname | 256 | 1 |  |  |  |
| retry_attempts | int | 4 | 0 |  |  |  |
| retry_interval | int | 4 | 0 |  |  |  |
| os_run_priority | int | 4 | 0 |  |  |  |
| output_file_name | nvarchar | 400 | 1 |  |  |  |
| last_run_outcome | int | 4 | 0 |  |  |  |
| last_run_duration | int | 4 | 0 |  |  |  |
| last_run_retries | int | 4 | 0 |  |  |  |
| last_run_date | int | 4 | 0 |  |  |  |
| last_run_time | int | 4 | 0 |  |  |  |
| proxy_id | int | 4 | 1 |  |  |  |
| step_uid | uniqueidentifier | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_jobserver](../../StoredProcedures/msdb/dbo.sp_add_jobserver.md)
- [msdb: dbo.sp_add_jobstep_internal](../../StoredProcedures/msdb/dbo.sp_add_jobstep_internal.md)
- [msdb: dbo.sp_add_maintenance_plan_job](../../StoredProcedures/msdb/dbo.sp_add_maintenance_plan_job.md)
- [msdb: dbo.sp_addtask](../../StoredProcedures/msdb/dbo.sp_addtask.md)
- [msdb: dbo.sp_check_for_owned_jobsteps](../../StoredProcedures/msdb/dbo.sp_check_for_owned_jobsteps.md)
- [msdb: dbo.sp_delete_all_msx_jobs](../../StoredProcedures/msdb/dbo.sp_delete_all_msx_jobs.md)
- [msdb: dbo.sp_delete_job](../../StoredProcedures/msdb/dbo.sp_delete_job.md)
- [msdb: dbo.sp_delete_jobstep](../../StoredProcedures/msdb/dbo.sp_delete_jobstep.md)
- [msdb: dbo.sp_delete_jobsteplog](../../StoredProcedures/msdb/dbo.sp_delete_jobsteplog.md)
- [msdb: dbo.sp_delete_proxy](../../StoredProcedures/msdb/dbo.sp_delete_proxy.md)
- [msdb: dbo.sp_get_chunked_jobstep_params](../../StoredProcedures/msdb/dbo.sp_get_chunked_jobstep_params.md)
- [msdb: dbo.sp_get_composite_job_info](../../StoredProcedures/msdb/dbo.sp_get_composite_job_info.md)
- [msdb: dbo.sp_help_jobstep](../../StoredProcedures/msdb/dbo.sp_help_jobstep.md)
- [msdb: dbo.sp_help_jobsteplog](../../StoredProcedures/msdb/dbo.sp_help_jobsteplog.md)
- [msdb: dbo.sp_reassign_proxy](../../StoredProcedures/msdb/dbo.sp_reassign_proxy.md)
- [msdb: dbo.sp_sqlagent_log_jobhistory](../../StoredProcedures/msdb/dbo.sp_sqlagent_log_jobhistory.md)
- [msdb: dbo.sp_sqlagent_notify](../../StoredProcedures/msdb/dbo.sp_sqlagent_notify.md)
- [msdb: dbo.sp_sqlagent_refresh_job](../../StoredProcedures/msdb/dbo.sp_sqlagent_refresh_job.md)
- [msdb: dbo.sp_start_job](../../StoredProcedures/msdb/dbo.sp_start_job.md)
- [msdb: dbo.sp_syscollector_update_job_proxy](../../StoredProcedures/msdb/dbo.sp_syscollector_update_job_proxy.md)
- [msdb: dbo.sp_update_job](../../StoredProcedures/msdb/dbo.sp_update_job.md)
- [msdb: dbo.sp_update_jobstep](../../StoredProcedures/msdb/dbo.sp_update_jobstep.md)
- [msdb: dbo.sp_update_replication_job_parameter](../../StoredProcedures/msdb/dbo.sp_update_replication_job_parameter.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)
- [msdb: dbo.sp_verify_jobstep](../../StoredProcedures/msdb/dbo.sp_verify_jobstep.md)
- [msdb: dbo.sp_write_sysjobstep_log](../../StoredProcedures/msdb/dbo.sp_write_sysjobstep_log.md)
- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)
- [DBAUtility: dbo.report_running_jobs](../../StoredProcedures/DBAUtility/dbo.report_running_jobs.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)
- [DBAUtility: dbo.spDBA_IndexOptimize](../../StoredProcedures/DBAUtility/dbo.spDBA_IndexOptimize.md)
- [DBAUtility: dbo.spDBA_IndexOptimize_IntermediateNodes](../../StoredProcedures/DBAUtility/dbo.spDBA_IndexOptimize_IntermediateNodes.md)
- [DBAUtility: dbo.spDBA_JobStatusCheck](../../StoredProcedures/DBAUtility/dbo.spDBA_JobStatusCheck.md)
- [DBAUtility: dbo.spDBA_replDistributorStatusGet](../../StoredProcedures/DBAUtility/dbo.spDBA_replDistributorStatusGet.md)
- [DBAUtility: dbo.spDBA_WhoIsActive](../../StoredProcedures/DBAUtility/dbo.spDBA_WhoIsActive.md)
- [DBAUtility: dbo.spFindReferencesToTable](../../StoredProcedures/DBAUtility/dbo.spFindReferencesToTable.md)

