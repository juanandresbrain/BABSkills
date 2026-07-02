# dbo.sysdownloadlist

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| instance_id | int | 4 | 0 |  |  |  |
| source_server | sysname | 256 | 0 |  |  |  |
| operation_code | tinyint | 1 | 0 |  |  |  |
| object_type | tinyint | 1 | 0 |  |  |  |
| object_id | uniqueidentifier | 16 | 0 |  |  |  |
| target_server | sysname | 256 | 0 |  |  |  |
| error_message | nvarchar | 2048 | 1 |  |  |  |
| date_posted | datetime | 8 | 0 |  |  |  |
| date_downloaded | datetime | 8 | 1 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| deleted_object_name | sysname | 256 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_enlist_tsx](../../StoredProcedures/msdb/dbo.sp_enlist_tsx.md)

