# dbo.sysmaintplan_subplans

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| subplan_id | uniqueidentifier | 16 | 0 | YES |  |  |
| subplan_name | sysname | 256 | 0 |  |  |  |
| subplan_description | nvarchar | 1024 | 1 |  |  |  |
| plan_id | uniqueidentifier | 16 | 0 |  |  |  |
| job_id | uniqueidentifier | 16 | 0 |  | YES |  |
| msx_job_id | uniqueidentifier | 16 | 1 |  | YES |  |
| schedule_id | int | 4 | 1 |  | YES |  |
| msx_plan | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_attach_schedule](../../StoredProcedures/msdb/dbo.sp_attach_schedule.md)
- [msdb: dbo.sp_delete_job_references](../../StoredProcedures/msdb/dbo.sp_delete_job_references.md)
- [msdb: dbo.sp_detach_schedule](../../StoredProcedures/msdb/dbo.sp_detach_schedule.md)
- [msdb: dbo.sp_maintplan_delete_plan](../../StoredProcedures/msdb/dbo.sp_maintplan_delete_plan.md)
- [msdb: dbo.sp_maintplan_delete_subplan](../../StoredProcedures/msdb/dbo.sp_maintplan_delete_subplan.md)
- [msdb: dbo.sp_maintplan_start](../../StoredProcedures/msdb/dbo.sp_maintplan_start.md)
- [msdb: dbo.sp_maintplan_subplans_by_job](../../StoredProcedures/msdb/dbo.sp_maintplan_subplans_by_job.md)
- [msdb: dbo.sp_maintplan_update_subplan](../../StoredProcedures/msdb/dbo.sp_maintplan_update_subplan.md)
- [msdb: dbo.sp_maintplan_update_subplan_tsx](../../StoredProcedures/msdb/dbo.sp_maintplan_update_subplan_tsx.md)

