# dbo.sysjobactivity

**Database:** msdb  
**Server:** bedrockdb02  

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

- [me_01: dbo.PiplelineSalesPostingTimeCheck](../../StoredProcedures/me_01/dbo.PiplelineSalesPostingTimeCheck.md)
- [msdb: dbo.sp_help_jobactivity](../../StoredProcedures/msdb/dbo.sp_help_jobactivity.md)
- [msdb: dbo.sp_sqlagent_log_jobhistory](../../StoredProcedures/msdb/dbo.sp_sqlagent_log_jobhistory.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)
- [TXTStaging: MerchandisingPlanning.spTXTDataLoad_RunTimeCheck](../../StoredProcedures/TXTStaging/MerchandisingPlanning.spTXTDataLoad_RunTimeCheck.md)

