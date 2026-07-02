# dbo.sysjobs

**Database:** msdb  
**Server:** STL-SSIS-P-01  

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

- [DBAUtility: dbo.spDBA_WhoIsActive](../../StoredProcedures/DBAUtility/dbo.spDBA_WhoIsActive.md)
- [DBAUtility: dbo.spSqlAgentJobStatus](../../StoredProcedures/DBAUtility/dbo.spSqlAgentJobStatus.md)
- [IntegrationStaging: dbo.spDynamicActionSQLJobHistoryEmail](../../StoredProcedures/IntegrationStaging/dbo.spDynamicActionSQLJobHistoryEmail.md)
- [IntegrationStaging: dbo.spSalesToDynamicsWeeklyUpdateJobHistoryEmail](../../StoredProcedures/IntegrationStaging/dbo.spSalesToDynamicsWeeklyUpdateJobHistoryEmail.md)
- [IntegrationStaging: NOCDev.spGetSQLJobStatus_All](../../StoredProcedures/IntegrationStaging/NOCDev.spGetSQLJobStatus_All.md)
- [IntegrationStaging: NOCDev.spGetSQLJobStatus_Shipped](../../StoredProcedures/IntegrationStaging/NOCDev.spGetSQLJobStatus_Shipped.md)
- [IntegrationStaging: NOCDev.spGetSQLJobStatus_UpdateDeckStatus](../../StoredProcedures/IntegrationStaging/NOCDev.spGetSQLJobStatus_UpdateDeckStatus.md)
- [IntegrationStaging: NOCDev.spGetSQLJobStatus_Waved](../../StoredProcedures/IntegrationStaging/NOCDev.spGetSQLJobStatus_Waved.md)
- [msdb: dbo.sp_add_jobserver](../../StoredProcedures/msdb/dbo.sp_add_jobserver.md)
- [msdb: dbo.sp_autoadmin_create_notification_job](../../StoredProcedures/msdb/dbo.sp_autoadmin_create_notification_job.md)
- [msdb: dbo.sp_detach_schedule](../../StoredProcedures/msdb/dbo.sp_detach_schedule.md)
- [msdb: dbo.sp_sysutility_mi_create_cache_directory](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_create_cache_directory.md)
- [msdb: dbo.sp_sysutility_mi_create_job_validate_wmi](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_create_job_validate_wmi.md)
- [msdb: dbo.sp_sysutility_mi_validate_proxy_account](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_validate_proxy_account.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)

