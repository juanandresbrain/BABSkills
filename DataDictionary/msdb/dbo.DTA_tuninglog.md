# dbo.DTA_tuninglog

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SessionID | int | 4 | 0 |  | YES |  |
| RowID | int | 4 | 0 |  |  |  |
| CategoryID | nvarchar | 8 | 0 |  |  |  |
| Event | nvarchar | -1 | 1 |  |  |  |
| Statement | nvarchar | -1 | 1 |  |  |  |
| Frequency | int | 4 | 0 |  |  |  |
| Reason | nvarchar | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_get_tuninglog](../../StoredProcedures/msdb/dbo.sp_DTA_get_tuninglog.md)

