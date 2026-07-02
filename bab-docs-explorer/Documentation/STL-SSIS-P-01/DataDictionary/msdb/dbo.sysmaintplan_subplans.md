# dbo.sysmaintplan_subplans

**Database:** msdb  
**Server:** STL-SSIS-P-01  

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
- [msdb: dbo.sp_detach_schedule](../../StoredProcedures/msdb/dbo.sp_detach_schedule.md)

