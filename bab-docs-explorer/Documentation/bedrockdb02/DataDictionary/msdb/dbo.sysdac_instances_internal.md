# dbo.sysdac_instances_internal

**Database:** msdb  
**Server:** bedrockdb02  

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

- [msdb: dbo.sp_sysdac_add_instance](../../StoredProcedures/msdb/dbo.sp_sysdac_add_instance.md)
- [msdb: dbo.sp_sysdac_delete_history](../../StoredProcedures/msdb/dbo.sp_sysdac_delete_history.md)
- [msdb: dbo.sp_sysdac_delete_instance](../../StoredProcedures/msdb/dbo.sp_sysdac_delete_instance.md)
- [msdb: dbo.sp_sysdac_resolve_pending_entry](../../StoredProcedures/msdb/dbo.sp_sysdac_resolve_pending_entry.md)
- [msdb: dbo.sp_sysdac_rollback_committed_step](../../StoredProcedures/msdb/dbo.sp_sysdac_rollback_committed_step.md)
- [msdb: dbo.sp_sysdac_update_instance](../../StoredProcedures/msdb/dbo.sp_sysdac_update_instance.md)
- [msdb: dbo.sp_sysdac_upgrade_instance](../../StoredProcedures/msdb/dbo.sp_sysdac_upgrade_instance.md)

