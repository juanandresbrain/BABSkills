# dbo.sysutility_ucp_managed_instances_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| instance_id | int | 4 | 0 |  |  |  |
| instance_name | sysname | 256 | 0 | YES |  |  |
| virtual_server_name | sysname | 256 | 0 |  |  |  |
| date_created | datetimeoffset | 10 | 0 |  |  |  |
| created_by | sysname | 256 | 0 |  |  |  |
| agent_proxy_account | sysname | 256 | 0 |  |  |  |
| cache_directory | nvarchar | 1040 | 1 |  |  |  |
| management_state | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_add_mi](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_add_mi.md)
- [msdb: dbo.sp_sysutility_ucp_remove_mi](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove_mi.md)

