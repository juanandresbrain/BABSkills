# dbo.syspolicy_target_set_levels_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| target_set_level_id | int | 4 | 0 | YES |  |  |
| target_set_id | int | 4 | 0 |  | YES |  |
| type_skeleton | nvarchar | 880 | 0 |  |  |  |
| condition_id | int | 4 | 1 |  | YES |  |
| level_name | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_add_target_set_level](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_target_set_level.md)
- [msdb: dbo.sp_syspolicy_update_target_set_level](../../StoredProcedures/msdb/dbo.sp_syspolicy_update_target_set_level.md)

