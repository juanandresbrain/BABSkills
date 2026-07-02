# dbo.syspolicy_conditions_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| condition_id | int | 4 | 0 | YES |  |  |
| name | sysname | 256 | 0 |  |  |  |
| date_created | datetime | 8 | 1 |  |  |  |
| description | nvarchar | -1 | 0 |  |  |  |
| created_by | sysname | 256 | 0 |  |  |  |
| modified_by | sysname | 256 | 1 |  |  |  |
| date_modified | datetime | 8 | 1 |  |  |  |
| facet_id | int | 4 | 1 |  | YES |  |
| expression | nvarchar | -1 | 1 |  |  |  |
| is_name_condition | smallint | 2 | 1 |  |  |  |
| obj_name | sysname | 256 | 1 |  |  |  |
| is_system | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_add_condition](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_condition.md)
- [msdb: dbo.sp_syspolicy_add_policy](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_policy.md)
- [msdb: dbo.sp_syspolicy_delete_condition](../../StoredProcedures/msdb/dbo.sp_syspolicy_delete_condition.md)
- [msdb: dbo.sp_syspolicy_dispatch_event](../../StoredProcedures/msdb/dbo.sp_syspolicy_dispatch_event.md)
- [msdb: dbo.sp_syspolicy_mark_system](../../StoredProcedures/msdb/dbo.sp_syspolicy_mark_system.md)
- [msdb: dbo.sp_syspolicy_rename_condition](../../StoredProcedures/msdb/dbo.sp_syspolicy_rename_condition.md)
- [msdb: dbo.sp_syspolicy_update_condition](../../StoredProcedures/msdb/dbo.sp_syspolicy_update_condition.md)
- [msdb: dbo.sp_syspolicy_update_policy](../../StoredProcedures/msdb/dbo.sp_syspolicy_update_policy.md)

