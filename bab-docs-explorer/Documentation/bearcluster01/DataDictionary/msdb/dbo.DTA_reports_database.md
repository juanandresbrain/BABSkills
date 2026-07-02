# dbo.DTA_reports_database

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DatabaseID | int | 4 | 0 | YES |  |  |
| SessionID | int | 4 | 0 |  | YES |  |
| DatabaseName | sysname | 256 | 0 |  |  |  |
| IsDatabaseSelectedToTune | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_DTA_help_session](../../StoredProcedures/msdb/dbo.sp_DTA_help_session.md)

