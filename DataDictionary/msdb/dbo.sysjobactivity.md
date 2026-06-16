# dbo.sysjobactivity

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| session_id | int | 4 | 0 |  | YES |  |
| job_id | uniqueidentifier | 16 | 0 |  | YES |  |
| run_requested_date | datetime | 8 | 1 |  |  |  |
| run_requested_source | sysname | 256 | 1 |  |  |  |
| queued_date | datetime | 8 | 1 |  |  |  |
| start_execution_date | datetime | 8 | 1 |  |  |  |
| last_executed_step_id | int | 4 | 1 |  |  |  |
| last_executed_step_date | datetime | 8 | 1 |  |  |  |
| stop_execution_date | datetime | 8 | 1 |  |  |  |
| job_history_id | int | 4 | 1 |  |  |  |
| next_scheduled_run_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spRestartHungSQLAgentJobs](../../StoredProcedures/IntegrationStaging/dbo.spRestartHungSQLAgentJobs.md)
- [IntegrationStaging: WEB.spRunWEBPricebookExports](../../StoredProcedures/IntegrationStaging/WEB.spRunWEBPricebookExports.md)
- [DBAUtility: dbo.spSqlAgentJobStatus](../../StoredProcedures/DBAUtility/dbo.spSqlAgentJobStatus.md)

