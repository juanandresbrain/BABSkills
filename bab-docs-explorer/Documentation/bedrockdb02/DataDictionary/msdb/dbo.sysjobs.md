# dbo.sysjobs

**Database:** msdb  
**Server:** bedrockdb02  

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

- [msdb: dbo.sp_add_job](../../StoredProcedures/msdb/dbo.sp_add_job.md)
- [msdb: dbo.sp_add_jobschedule](../../StoredProcedures/msdb/dbo.sp_add_jobschedule.md)
- [msdb: dbo.sp_add_jobserver](../../StoredProcedures/msdb/dbo.sp_add_jobserver.md)
- [msdb: dbo.sp_add_jobstep_internal](../../StoredProcedures/msdb/dbo.sp_add_jobstep_internal.md)
- [msdb: dbo.sp_add_log_shipping_monitor_jobs](../../StoredProcedures/msdb/dbo.sp_add_log_shipping_monitor_jobs.md)
- [msdb: dbo.sp_add_maintenance_plan_job](../../StoredProcedures/msdb/dbo.sp_add_maintenance_plan_job.md)
- [msdb: dbo.sp_delete_all_msx_jobs](../../StoredProcedures/msdb/dbo.sp_delete_all_msx_jobs.md)
- [msdb: dbo.sp_delete_category](../../StoredProcedures/msdb/dbo.sp_delete_category.md)
- [msdb: dbo.sp_delete_job](../../StoredProcedures/msdb/dbo.sp_delete_job.md)
- [msdb: dbo.sp_delete_jobschedule](../../StoredProcedures/msdb/dbo.sp_delete_jobschedule.md)
- [msdb: dbo.sp_delete_jobstep](../../StoredProcedures/msdb/dbo.sp_delete_jobstep.md)
- [msdb: dbo.sp_delete_log_shipping_monitor_jobs](../../StoredProcedures/msdb/dbo.sp_delete_log_shipping_monitor_jobs.md)
- [msdb: dbo.sp_delete_operator](../../StoredProcedures/msdb/dbo.sp_delete_operator.md)
- [msdb: dbo.sp_detach_schedule](../../StoredProcedures/msdb/dbo.sp_detach_schedule.md)
- [msdb: dbo.sp_help_jobhistory](../../StoredProcedures/msdb/dbo.sp_help_jobhistory.md)
- [msdb: dbo.sp_manage_jobs_by_login](../../StoredProcedures/msdb/dbo.sp_manage_jobs_by_login.md)
- [msdb: dbo.sp_multi_server_job_summary](../../StoredProcedures/msdb/dbo.sp_multi_server_job_summary.md)
- [msdb: dbo.sp_sqlagent_log_jobhistory](../../StoredProcedures/msdb/dbo.sp_sqlagent_log_jobhistory.md)
- [msdb: dbo.sp_start_job](../../StoredProcedures/msdb/dbo.sp_start_job.md)
- [msdb: dbo.sp_syscollector_cleanup_collector](../../StoredProcedures/msdb/dbo.sp_syscollector_cleanup_collector.md)
- [msdb: dbo.sp_syspolicy_create_job](../../StoredProcedures/msdb/dbo.sp_syspolicy_create_job.md)
- [msdb: dbo.sp_syspolicy_create_purge_job](../../StoredProcedures/msdb/dbo.sp_syspolicy_create_purge_job.md)
- [msdb: dbo.sp_sysutility_mi_create_cache_directory](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_create_cache_directory.md)
- [msdb: dbo.sp_sysutility_mi_create_job_validate_wmi](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_create_job_validate_wmi.md)
- [msdb: dbo.sp_sysutility_mi_disable_collection](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_disable_collection.md)
- [msdb: dbo.sp_sysutility_mi_initialize_collection](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_initialize_collection.md)
- [msdb: dbo.sp_sysutility_mi_validate_proxy_account](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_validate_proxy_account.md)
- [msdb: dbo.sp_uniquetaskname](../../StoredProcedures/msdb/dbo.sp_uniquetaskname.md)
- [msdb: dbo.sp_update_job](../../StoredProcedures/msdb/dbo.sp_update_job.md)
- [msdb: dbo.sp_update_jobschedule](../../StoredProcedures/msdb/dbo.sp_update_jobschedule.md)
- [msdb: dbo.sp_update_jobstep](../../StoredProcedures/msdb/dbo.sp_update_jobstep.md)
- [msdb: dbo.sp_update_replication_job_parameter](../../StoredProcedures/msdb/dbo.sp_update_replication_job_parameter.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)
- [msdb: dbo.sp_verify_jobstep](../../StoredProcedures/msdb/dbo.sp_verify_jobstep.md)
- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)
- [DBAUtility: dbo.spDBA_IndexOptimize](../../StoredProcedures/DBAUtility/dbo.spDBA_IndexOptimize.md)
- [DBAUtility: dbo.spDBA_IndexOptimize_IntermediateNodes](../../StoredProcedures/DBAUtility/dbo.spDBA_IndexOptimize_IntermediateNodes.md)
- [DBAUtility: dbo.spDBA_JobStatusCheck](../../StoredProcedures/DBAUtility/dbo.spDBA_JobStatusCheck.md)
- [DBAUtility: dbo.spDBA_ObjectVersionLog](../../StoredProcedures/DBAUtility/dbo.spDBA_ObjectVersionLog.md)
- [DBAUtility: dbo.spDBA_replDistributorStatusGet](../../StoredProcedures/DBAUtility/dbo.spDBA_replDistributorStatusGet.md)
- [DBAUtility: dbo.spDBA_replLogReaderStatusGet](../../StoredProcedures/DBAUtility/dbo.spDBA_replLogReaderStatusGet.md)
- [DBAUtility: dbo.spDBA_StartAgentJobAndWait](../../StoredProcedures/DBAUtility/dbo.spDBA_StartAgentJobAndWait.md)
- [DBAUtility: dbo.spDBA_WhoIsActive](../../StoredProcedures/DBAUtility/dbo.spDBA_WhoIsActive.md)
- [DBAUtility: dbo.spFindReferencesToTable](../../StoredProcedures/DBAUtility/dbo.spFindReferencesToTable.md)
- [DBAUtility: dbo.spPOLL_StatusPipeLineSalesPosting](../../StoredProcedures/DBAUtility/dbo.spPOLL_StatusPipeLineSalesPosting.md)
- [USICOAL: dbo.RPL_ADD_DISTR_SCHED](../../StoredProcedures/USICOAL/dbo.RPL_ADD_DISTR_SCHED.md)
- [USICOAL: dbo.RPL_RUN_SNAPSHOT_AGENTS](../../StoredProcedures/USICOAL/dbo.RPL_RUN_SNAPSHOT_AGENTS.md)
- [ReportServerES: dbo.Get_sqlagent_job_status](../../StoredProcedures/ReportServerES/dbo.Get_sqlagent_job_status.md)

