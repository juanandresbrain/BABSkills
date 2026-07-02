# dbo.sysjobsteps

**Database:** msdb  
**Server:** bearcluster01  

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

- [WebOrderProcessing: dbo.spDBA_WhoIsActive](../../StoredProcedures/WebOrderProcessing/dbo.spDBA_WhoIsActive.md)
- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)
- [DBAUtility: dbo.report_running_jobs](../../StoredProcedures/DBAUtility/dbo.report_running_jobs.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)
- [DBAUtility: dbo.spDBA_IndexOptimize](../../StoredProcedures/DBAUtility/dbo.spDBA_IndexOptimize.md)
- [DBAUtility: dbo.spDBA_IndexOptimize_IntermediateNodes](../../StoredProcedures/DBAUtility/dbo.spDBA_IndexOptimize_IntermediateNodes.md)
- [msdb: dbo.sp_add_jobserver](../../StoredProcedures/msdb/dbo.sp_add_jobserver.md)
- [msdb: dbo.sp_delete_proxy](../../StoredProcedures/msdb/dbo.sp_delete_proxy.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)

