# dbo.sysssispackages

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | sysname | 256 | 0 | YES |  |  |
| id | uniqueidentifier | 16 | 0 |  |  |  |
| description | nvarchar | 2048 | 1 |  |  |  |
| createdate | datetime | 8 | 0 |  |  |  |
| folderid | uniqueidentifier | 16 | 0 | YES |  |  |
| ownersid | varbinary | 85 | 0 |  |  |  |
| packagedata | image | 16 | 0 |  |  |  |
| packageformat | int | 4 | 0 |  |  |  |
| packagetype | int | 4 | 0 |  |  |  |
| vermajor | int | 4 | 0 |  |  |  |
| verminor | int | 4 | 0 |  |  |  |
| verbuild | int | 4 | 0 |  |  |  |
| vercomments | nvarchar | 2048 | 1 |  |  |  |
| verid | uniqueidentifier | 16 | 0 |  |  |  |
| isencrypted | bit | 1 | 0 |  |  |  |
| readrolesid | varbinary | 85 | 1 |  |  |  |
| writerolesid | varbinary | 85 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syscollector_event_onpackagebegin](../../StoredProcedures/msdb/dbo.sp_syscollector_event_onpackagebegin.md)

