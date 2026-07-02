# dbo.systargetservers

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server_id | int | 4 | 0 |  |  |  |
| server_name | sysname | 256 | 0 |  |  |  |
| location | nvarchar | 400 | 1 |  |  |  |
| time_zone_adjustment | int | 4 | 0 |  |  |  |
| enlist_date | datetime | 8 | 0 |  |  |  |
| last_poll_date | datetime | 8 | 0 |  |  |  |
| status | int | 4 | 0 |  |  |  |
| local_time_at_last_poll | datetime | 8 | 0 |  |  |  |
| enlisted_by_nt_user | nvarchar | 200 | 0 |  |  |  |
| poll_interval | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_jobserver](../../StoredProcedures/msdb/dbo.sp_add_jobserver.md)
- [msdb: dbo.sp_enlist_tsx](../../StoredProcedures/msdb/dbo.sp_enlist_tsx.md)
- [msdb: dbo.sp_help_jobhistory_sem](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_sem.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)

