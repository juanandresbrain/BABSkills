# dbo.sysssislog

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| event | sysname | 256 | 0 |  |  |  |
| computer | nvarchar | 256 | 0 |  |  |  |
| operator | nvarchar | 256 | 0 |  |  |  |
| source | nvarchar | 2048 | 0 |  |  |  |
| sourceid | uniqueidentifier | 16 | 0 |  |  |  |
| executionid | uniqueidentifier | 16 | 0 |  |  |  |
| starttime | datetime | 8 | 0 |  |  |  |
| endtime | datetime | 8 | 0 |  |  |  |
| datacode | int | 4 | 0 |  |  |  |
| databytes | image | 16 | 1 |  |  |  |
| message | nvarchar | 4096 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syscollector_event_onerror](../../StoredProcedures/msdb/dbo.sp_syscollector_event_onerror.md)

