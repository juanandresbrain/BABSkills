# dbo.sysjobs

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | uniqueidentifier | 16 | 0 |  |  |  |
| originating_server_id | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| enabled | tinyint | 1 | 0 |  |  |  |
| description | nvarchar | 1024 | 1 |  |  |  |
| start_step_id | int | 4 | 0 |  |  |  |
| category_id | int | 4 | 0 |  |  |  |
| owner_sid | varbinary | 85 | 0 |  |  |  |
| notify_level_eventlog | int | 4 | 0 |  |  |  |
| notify_level_email | int | 4 | 0 |  |  |  |
| notify_level_netsend | int | 4 | 0 |  |  |  |
| notify_level_page | int | 4 | 0 |  |  |  |
| notify_email_operator_id | int | 4 | 0 |  |  |  |
| notify_netsend_operator_id | int | 4 | 0 |  |  |  |
| notify_page_operator_id | int | 4 | 0 |  |  |  |
| delete_level | int | 4 | 0 |  |  |  |
| date_created | datetime | 8 | 0 |  |  |  |
| date_modified | datetime | 8 | 0 |  |  |  |
| version_number | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spDBA_WhoIsActive](../../StoredProcedures/WebOrderProcessing/dbo.spDBA_WhoIsActive.md)
- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)
- [DBAUtility: dbo.spDBA_IndexOptimize](../../StoredProcedures/DBAUtility/dbo.spDBA_IndexOptimize.md)
- [DBAUtility: dbo.spDBA_IndexOptimize_IntermediateNodes](../../StoredProcedures/DBAUtility/dbo.spDBA_IndexOptimize_IntermediateNodes.md)
- [DBAUtility: dbo.spDBA_ObjectVersionLog](../../StoredProcedures/DBAUtility/dbo.spDBA_ObjectVersionLog.md)
- [DBAUtility: dbo.spPOLL_StatusPipeLineSalesPosting](../../StoredProcedures/DBAUtility/dbo.spPOLL_StatusPipeLineSalesPosting.md)
- [ReportServerBIRPT02: dbo.Get_sqlagent_job_status](../../StoredProcedures/ReportServerBIRPT02/dbo.Get_sqlagent_job_status.md)
- [msdb: dbo.sp_add_jobserver](../../StoredProcedures/msdb/dbo.sp_add_jobserver.md)
- [msdb: dbo.sp_autoadmin_create_notification_job](../../StoredProcedures/msdb/dbo.sp_autoadmin_create_notification_job.md)
- [msdb: dbo.sp_detach_schedule](../../StoredProcedures/msdb/dbo.sp_detach_schedule.md)
- [msdb: dbo.sp_sysutility_mi_create_cache_directory](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_create_cache_directory.md)
- [msdb: dbo.sp_sysutility_mi_create_job_validate_wmi](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_create_job_validate_wmi.md)
- [msdb: dbo.sp_sysutility_mi_validate_proxy_account](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_validate_proxy_account.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)

