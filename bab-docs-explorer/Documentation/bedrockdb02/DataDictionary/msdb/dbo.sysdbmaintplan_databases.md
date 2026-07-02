# dbo.sysdbmaintplan_databases

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_id | uniqueidentifier | 16 | 0 |  | YES |  |
| database_name | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_maintenance_plan_db](../../StoredProcedures/msdb/dbo.sp_add_maintenance_plan_db.md)
- [msdb: dbo.sp_clear_dbmaintplan_by_db](../../StoredProcedures/msdb/dbo.sp_clear_dbmaintplan_by_db.md)
- [msdb: dbo.sp_delete_maintenance_plan](../../StoredProcedures/msdb/dbo.sp_delete_maintenance_plan.md)
- [msdb: dbo.sp_delete_maintenance_plan_db](../../StoredProcedures/msdb/dbo.sp_delete_maintenance_plan_db.md)
- [msdb: dbo.sp_help_maintenance_plan](../../StoredProcedures/msdb/dbo.sp_help_maintenance_plan.md)

