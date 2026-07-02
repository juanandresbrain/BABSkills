# dbo.sysjobhistory

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| instance_id | int | 4 | 0 |  |  |  |
| job_id | uniqueidentifier | 16 | 0 |  |  |  |
| step_id | int | 4 | 0 |  |  |  |
| step_name | sysname | 256 | 0 |  |  |  |
| sql_message_id | int | 4 | 0 |  |  |  |
| sql_severity | int | 4 | 0 |  |  |  |
| message | nvarchar | 8000 | 1 |  |  |  |
| run_status | int | 4 | 0 |  |  |  |
| run_date | int | 4 | 0 |  |  |  |
| run_time | int | 4 | 0 |  |  |  |
| run_duration | int | 4 | 0 |  |  |  |
| operator_id_emailed | int | 4 | 0 |  |  |  |
| operator_id_netsent | int | 4 | 0 |  |  |  |
| operator_id_paged | int | 4 | 0 |  |  |  |
| retries_attempted | int | 4 | 0 |  |  |  |
| server | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.DBSchenkerPOExportTimeCheck](../../StoredProcedures/me_01/dbo.DBSchenkerPOExportTimeCheck.md)
- [me_01: dbo.PiplelineSalesPostingTimeCheck](../../StoredProcedures/me_01/dbo.PiplelineSalesPostingTimeCheck.md)
- [me_01: dbo.spMerchandisingDistroExportRunCheck](../../StoredProcedures/me_01/dbo.spMerchandisingDistroExportRunCheck.md)
- [msdb: dbo.sp_delete_all_msx_jobs](../../StoredProcedures/msdb/dbo.sp_delete_all_msx_jobs.md)
- [msdb: dbo.sp_delete_job](../../StoredProcedures/msdb/dbo.sp_delete_job.md)
- [msdb: dbo.sp_help_jobactivity](../../StoredProcedures/msdb/dbo.sp_help_jobactivity.md)
- [msdb: dbo.sp_help_jobhistory_full](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_full.md)
- [msdb: dbo.sp_help_jobhistory_sem](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_sem.md)
- [msdb: dbo.sp_help_jobhistory_summary](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_summary.md)
- [msdb: dbo.sp_jobhistory_row_limiter](../../StoredProcedures/msdb/dbo.sp_jobhistory_row_limiter.md)
- [msdb: dbo.sp_purge_jobhistory](../../StoredProcedures/msdb/dbo.sp_purge_jobhistory.md)
- [msdb: dbo.sp_sqlagent_log_jobhistory](../../StoredProcedures/msdb/dbo.sp_sqlagent_log_jobhistory.md)
- [DBAUtility: dbo.spDBA_Delete_JobHistory](../../StoredProcedures/DBAUtility/dbo.spDBA_Delete_JobHistory.md)
- [DBAUtility: dbo.spDBA_JobStatusCheck](../../StoredProcedures/DBAUtility/dbo.spDBA_JobStatusCheck.md)
- [DBAUtility: dbo.spDBA_StartAgentJobAndWait](../../StoredProcedures/DBAUtility/dbo.spDBA_StartAgentJobAndWait.md)
- [DBAUtility: dbo.spPOLL_StatusPipeLineSalesPosting](../../StoredProcedures/DBAUtility/dbo.spPOLL_StatusPipeLineSalesPosting.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_RunTimeCheck](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_RunTimeCheck.md)

