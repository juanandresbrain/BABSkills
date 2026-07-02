# dbo.syspolicy_object_sets_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| object_set_id | int | 4 | 0 | YES |  |  |
| object_set_name | sysname | 256 | 0 |  |  |  |
| facet_id | int | 4 | 1 |  | YES |  |
| is_system | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_add_object_set](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_object_set.md)
- [msdb: dbo.sp_syspolicy_delete_object_set](../../StoredProcedures/msdb/dbo.sp_syspolicy_delete_object_set.md)
- [msdb: dbo.sp_syspolicy_mark_system](../../StoredProcedures/msdb/dbo.sp_syspolicy_mark_system.md)

