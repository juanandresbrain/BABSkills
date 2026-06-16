# dbo.syscollector_execution_stats_internal

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| log_id | bigint | 8 | 0 | YES | YES |  |
| task_name | nvarchar | 256 | 0 | YES |  |  |
| execution_row_count_in | int | 4 | 1 |  |  |  |
| execution_row_count_out | int | 4 | 1 |  |  |  |
| execution_row_count_errors | int | 4 | 1 |  |  |  |
| execution_time_ms | int | 4 | 1 |  |  |  |
| log_time | datetime | 8 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syscollector_event_onstatsupdate](../../StoredProcedures/msdb/dbo.sp_syscollector_event_onstatsupdate.md)

