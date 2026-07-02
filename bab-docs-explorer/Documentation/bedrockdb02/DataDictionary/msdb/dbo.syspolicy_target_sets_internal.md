# dbo.syspolicy_target_sets_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| target_set_id | int | 4 | 0 | YES |  |  |
| object_set_id | int | 4 | 0 |  | YES |  |
| type_skeleton | nvarchar | 880 | 0 |  |  |  |
| type | sysname | 256 | 0 |  |  |  |
| enabled | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_add_target_set](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_target_set.md)
- [msdb: dbo.sp_syspolicy_delete_target_set](../../StoredProcedures/msdb/dbo.sp_syspolicy_delete_target_set.md)
- [msdb: dbo.sp_syspolicy_update_target_set](../../StoredProcedures/msdb/dbo.sp_syspolicy_update_target_set.md)

