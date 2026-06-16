# dbo.sysjobhistory

**Database:** msdb  

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

- [msdb: dbo.sp_help_jobhistory_sem](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_sem.md)
- [IntegrationStaging: dbo.spDynamicActionSQLJobHistoryEmail](../../StoredProcedures/IntegrationStaging/dbo.spDynamicActionSQLJobHistoryEmail.md)
- [IntegrationStaging: dbo.spSalesToDynamicsWeeklyUpdateJobHistoryEmail](../../StoredProcedures/IntegrationStaging/dbo.spSalesToDynamicsWeeklyUpdateJobHistoryEmail.md)
- [IntegrationStaging: NOCDev.spGetSQLJobStatus_All](../../StoredProcedures/IntegrationStaging/NOCDev.spGetSQLJobStatus_All.md)
- [IntegrationStaging: NOCDev.spGetSQLJobStatus_Shipped](../../StoredProcedures/IntegrationStaging/NOCDev.spGetSQLJobStatus_Shipped.md)
- [IntegrationStaging: NOCDev.spGetSQLJobStatus_UpdateDeckStatus](../../StoredProcedures/IntegrationStaging/NOCDev.spGetSQLJobStatus_UpdateDeckStatus.md)
- [IntegrationStaging: NOCDev.spGetSQLJobStatus_Waved](../../StoredProcedures/IntegrationStaging/NOCDev.spGetSQLJobStatus_Waved.md)
- [DBAUtility: dbo.spSqlAgentJobStatus](../../StoredProcedures/DBAUtility/dbo.spSqlAgentJobStatus.md)

