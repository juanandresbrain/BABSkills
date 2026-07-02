# dbo.DTA_output

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SessionID | int | 4 | 0 | YES | YES |  |
| TuningResults | nvarchar | -1 | 0 |  |  |  |
| StopTime | datetime | 8 | 0 |  |  |  |
| FinishStatus | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_help_session](../../StoredProcedures/msdb/dbo.sp_DTA_help_session.md)

