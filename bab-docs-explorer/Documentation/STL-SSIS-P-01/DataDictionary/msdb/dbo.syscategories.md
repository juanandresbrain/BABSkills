# dbo.syscategories

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| category_id | int | 4 | 0 |  |  |  |
| category_class | int | 4 | 0 |  |  |  |
| category_type | tinyint | 1 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_jobserver](../../StoredProcedures/msdb/dbo.sp_add_jobserver.md)
- [msdb: dbo.sp_verify_category_identifiers](../../StoredProcedures/msdb/dbo.sp_verify_category_identifiers.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)

