# dbo.DTA_output

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SessionID | int | 4 | 0 | YES | YES |  |
| TuningResults | ntext | 16 | 0 |  |  |  |
| StopTime | datetime | 8 | 0 |  |  |  |
| FinishStatus | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_get_session_tuning_results](../../StoredProcedures/msdb/dbo.sp_DTA_get_session_tuning_results.md)
- [msdb: dbo.sp_DTA_help_session](../../StoredProcedures/msdb/dbo.sp_DTA_help_session.md)
- [msdb: dbo.sp_DTA_set_outputinformation](../../StoredProcedures/msdb/dbo.sp_DTA_set_outputinformation.md)

