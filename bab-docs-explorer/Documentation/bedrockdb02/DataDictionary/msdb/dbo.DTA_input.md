# dbo.DTA_input

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SessionName | sysname | 256 | 0 |  |  |  |
| SessionID | int | 4 | 0 | YES |  |  |
| TuningOptions | ntext | 16 | 0 |  |  |  |
| CreationTime | datetime | 8 | 0 |  |  |  |
| ScheduledStartTime | datetime | 8 | 0 |  |  |  |
| ScheduledJobName | sysname | 256 | 0 |  |  |  |
| InteractiveStatus | tinyint | 1 | 0 |  |  |  |
| LogTableName | nvarchar | 2560 | 0 |  |  |  |
| GlobalSessionID | uniqueidentifier | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_add_session](../../StoredProcedures/msdb/dbo.sp_DTA_add_session.md)
- [msdb: dbo.sp_DTA_delete_session](../../StoredProcedures/msdb/dbo.sp_DTA_delete_session.md)
- [msdb: dbo.sp_DTA_get_interactivestatus](../../StoredProcedures/msdb/dbo.sp_DTA_get_interactivestatus.md)
- [msdb: dbo.sp_DTA_get_tuninglog](../../StoredProcedures/msdb/dbo.sp_DTA_get_tuninglog.md)
- [msdb: dbo.sp_DTA_get_tuningoptions](../../StoredProcedures/msdb/dbo.sp_DTA_get_tuningoptions.md)
- [msdb: dbo.sp_DTA_help_session](../../StoredProcedures/msdb/dbo.sp_DTA_help_session.md)
- [msdb: dbo.sp_DTA_set_interactivestatus](../../StoredProcedures/msdb/dbo.sp_DTA_set_interactivestatus.md)
- [msdb: dbo.sp_DTA_set_tuninglogtablename](../../StoredProcedures/msdb/dbo.sp_DTA_set_tuninglogtablename.md)
- [msdb: dbo.sp_DTA_update_session](../../StoredProcedures/msdb/dbo.sp_DTA_update_session.md)

