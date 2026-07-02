# dbo.syscollector_blobs_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_name | nvarchar | 256 | 0 | YES |  |  |
| parameter_value | varbinary | -1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syscollector_get_instmdw](../../StoredProcedures/msdb/dbo.sp_syscollector_get_instmdw.md)
- [msdb: dbo.sp_syscollector_upload_instmdw](../../StoredProcedures/msdb/dbo.sp_syscollector_upload_instmdw.md)

