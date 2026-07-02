# dbo.syspolicy_management_facets

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| management_facet_id | int | 4 | 0 | YES |  |  |
| name | nvarchar | -1 | 0 |  |  |  |
| execution_mode | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_add_condition](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_condition.md)
- [msdb: dbo.sp_syspolicy_add_object_set](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_object_set.md)
- [msdb: dbo.sp_syspolicy_update_condition](../../StoredProcedures/msdb/dbo.sp_syspolicy_update_condition.md)

