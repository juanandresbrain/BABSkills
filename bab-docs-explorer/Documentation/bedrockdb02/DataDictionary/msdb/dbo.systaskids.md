# dbo.systaskids

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| task_id | int | 4 | 0 |  |  |  |
| job_id | uniqueidentifier | 16 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_addtask](../../StoredProcedures/msdb/dbo.sp_addtask.md)
- [msdb: dbo.sp_delete_job_references](../../StoredProcedures/msdb/dbo.sp_delete_job_references.md)
- [msdb: dbo.sp_droptask](../../StoredProcedures/msdb/dbo.sp_droptask.md)

