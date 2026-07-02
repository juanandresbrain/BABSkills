# dbo.sysdbmaintplans

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_id | uniqueidentifier | 16 | 0 | YES |  |  |
| plan_name | sysname | 256 | 0 |  |  |  |
| date_created | datetime | 8 | 0 |  |  |  |
| owner | sysname | 256 | 0 |  |  |  |
| max_history_rows | int | 4 | 0 |  |  |  |
| remote_history_server | sysname | 256 | 0 |  |  |  |
| max_remote_history_rows | int | 4 | 0 |  |  |  |
| user_defined_1 | int | 4 | 1 |  |  |  |
| user_defined_2 | nvarchar | 200 | 1 |  |  |  |
| user_defined_3 | datetime | 8 | 1 |  |  |  |
| user_defined_4 | uniqueidentifier | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_maintenance_plan](../../StoredProcedures/msdb/dbo.sp_add_maintenance_plan.md)
- [msdb: dbo.sp_add_maintenance_plan_db](../../StoredProcedures/msdb/dbo.sp_add_maintenance_plan_db.md)
- [msdb: dbo.sp_add_maintenance_plan_job](../../StoredProcedures/msdb/dbo.sp_add_maintenance_plan_job.md)
- [msdb: dbo.sp_clear_dbmaintplan_by_db](../../StoredProcedures/msdb/dbo.sp_clear_dbmaintplan_by_db.md)
- [msdb: dbo.sp_delete_maintenance_plan](../../StoredProcedures/msdb/dbo.sp_delete_maintenance_plan.md)
- [msdb: dbo.sp_help_maintenance_plan](../../StoredProcedures/msdb/dbo.sp_help_maintenance_plan.md)

