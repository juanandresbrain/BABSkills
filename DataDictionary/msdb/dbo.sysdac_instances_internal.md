# dbo.sysdac_instances_internal

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| instance_id | uniqueidentifier | 16 | 0 | YES |  |  |
| instance_name | sysname | 256 | 0 |  |  |  |
| type_name | sysname | 256 | 0 |  |  |  |
| type_version | nvarchar | 128 | 0 |  |  |  |
| description | nvarchar | 8000 | 1 |  |  |  |
| type_stream | varbinary | -1 | 0 |  |  |  |
| date_created | datetime | 8 | 0 |  |  |  |
| created_by | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysdac_delete_history](../../StoredProcedures/msdb/dbo.sp_sysdac_delete_history.md)

