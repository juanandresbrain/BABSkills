# dbo.sysmanagement_shared_registered_servers_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server_id | int | 4 | 0 | YES |  |  |
| server_group_id | int | 4 | 1 |  | YES |  |
| name | sysname | 256 | 0 |  |  |  |
| server_name | sysname | 256 | 0 |  |  |  |
| description | nvarchar | 4096 | 0 |  |  |  |
| server_type | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysmanagement_add_shared_registered_server](../../StoredProcedures/msdb/dbo.sp_sysmanagement_add_shared_registered_server.md)
- [msdb: dbo.sp_sysmanagement_delete_shared_registered_server](../../StoredProcedures/msdb/dbo.sp_sysmanagement_delete_shared_registered_server.md)
- [msdb: dbo.sp_sysmanagement_move_shared_registered_server](../../StoredProcedures/msdb/dbo.sp_sysmanagement_move_shared_registered_server.md)
- [msdb: dbo.sp_sysmanagement_rename_shared_registered_server](../../StoredProcedures/msdb/dbo.sp_sysmanagement_rename_shared_registered_server.md)
- [msdb: dbo.sp_sysmanagement_update_shared_registered_server](../../StoredProcedures/msdb/dbo.sp_sysmanagement_update_shared_registered_server.md)

