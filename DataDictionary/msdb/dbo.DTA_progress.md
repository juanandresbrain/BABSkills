# dbo.DTA_progress

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProgressEventID | int | 4 | 0 |  |  |  |
| SessionID | int | 4 | 1 |  | YES |  |
| TuningStage | tinyint | 1 | 0 |  |  |  |
| WorkloadConsumption | tinyint | 1 | 0 |  |  |  |
| EstImprovement | int | 4 | 0 |  |  |  |
| ProgressEventTime | datetime | 8 | 0 |  |  |  |
| ConsumingWorkLoadMessage | nvarchar | 512 | 1 |  |  |  |
| PerformingAnalysisMessage | nvarchar | 512 | 1 |  |  |  |
| GeneratingReportsMessage | nvarchar | 512 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_help_session](../../StoredProcedures/msdb/dbo.sp_DTA_help_session.md)

