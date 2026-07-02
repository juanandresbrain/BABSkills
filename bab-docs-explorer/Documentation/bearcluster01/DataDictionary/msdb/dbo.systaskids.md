# dbo.systaskids

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| task_id | int | 4 | 0 |  |  |  |
| job_id | uniqueidentifier | 16 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_droptask](../../StoredProcedures/msdb/dbo.sp_droptask.md)

