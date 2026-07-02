# dbo.sysdac_history_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| action_id | int | 4 | 0 | YES |  |  |
| sequence_id | int | 4 | 0 | YES |  |  |
| instance_id | uniqueidentifier | 16 | 0 |  |  |  |
| action_type | tinyint | 1 | 0 |  |  |  |
| action_type_name | varchar | 19 | 1 |  |  |  |
| dac_object_type | tinyint | 1 | 0 |  |  |  |
| dac_object_type_name | varchar | 8 | 1 |  |  |  |
| action_status | tinyint | 1 | 0 |  |  |  |
| action_status_name | varchar | 11 | 1 |  |  |  |
| required | bit | 1 | 1 |  |  |  |
| dac_object_name_pretran | sysname | 256 | 0 |  |  |  |
| dac_object_name_posttran | sysname | 256 | 0 |  |  |  |
| sqlscript | nvarchar | -1 | 1 |  |  |  |
| payload | varbinary | -1 | 1 |  |  |  |
| comments | varchar | -1 | 0 |  |  |  |
| error_string | nvarchar | -1 | 1 |  |  |  |
| created_by | sysname | 256 | 0 |  |  |  |
| date_created | datetime | 8 | 0 |  |  |  |
| date_modified | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysdac_add_history_entry](../../StoredProcedures/msdb/dbo.sp_sysdac_add_history_entry.md)
- [msdb: dbo.sp_sysdac_delete_history](../../StoredProcedures/msdb/dbo.sp_sysdac_delete_history.md)
- [msdb: dbo.sp_sysdac_resolve_pending_entry](../../StoredProcedures/msdb/dbo.sp_sysdac_resolve_pending_entry.md)
- [msdb: dbo.sp_sysdac_rollback_all_pending_objects](../../StoredProcedures/msdb/dbo.sp_sysdac_rollback_all_pending_objects.md)
- [msdb: dbo.sp_sysdac_rollback_committed_step](../../StoredProcedures/msdb/dbo.sp_sysdac_rollback_committed_step.md)
- [msdb: dbo.sp_sysdac_rollback_pending_object](../../StoredProcedures/msdb/dbo.sp_sysdac_rollback_pending_object.md)
- [msdb: dbo.sp_sysdac_update_history_entry](../../StoredProcedures/msdb/dbo.sp_sysdac_update_history_entry.md)

