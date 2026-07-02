# dbo.DTA_tuninglog

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SessionID | int | 4 | 0 |  | YES |  |
| RowID | int | 4 | 0 |  |  |  |
| CategoryID | nvarchar | 8 | 0 |  |  |  |
| Event | ntext | 16 | 1 |  |  |  |
| Statement | ntext | 16 | 1 |  |  |  |
| Frequency | int | 4 | 0 |  |  |  |
| Reason | ntext | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_get_tuninglog](../../StoredProcedures/msdb/dbo.sp_DTA_get_tuninglog.md)
- [msdb: dbo.sp_DTA_insert_DTA_tuninglog](../../StoredProcedures/msdb/dbo.sp_DTA_insert_DTA_tuninglog.md)
- [msdb: dbo.sp_DTA_update_tuninglog_errorfrequency](../../StoredProcedures/msdb/dbo.sp_DTA_update_tuninglog_errorfrequency.md)

