# dbo.sysschedules

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| schedule_id | int | 4 | 0 | YES |  |  |
| schedule_uid | uniqueidentifier | 16 | 0 |  |  |  |
| originating_server_id | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| owner_sid | varbinary | 85 | 0 |  |  |  |
| enabled | int | 4 | 0 |  |  |  |
| freq_type | int | 4 | 0 |  |  |  |
| freq_interval | int | 4 | 0 |  |  |  |
| freq_subday_type | int | 4 | 0 |  |  |  |
| freq_subday_interval | int | 4 | 0 |  |  |  |
| freq_relative_interval | int | 4 | 0 |  |  |  |
| freq_recurrence_factor | int | 4 | 0 |  |  |  |
| active_start_date | int | 4 | 0 |  |  |  |
| active_end_date | int | 4 | 0 |  |  |  |
| active_start_time | int | 4 | 0 |  |  |  |
| active_end_time | int | 4 | 0 |  |  |  |
| date_created | datetime | 8 | 0 |  |  |  |
| date_modified | datetime | 8 | 0 |  |  |  |
| version_number | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_schedule](../../StoredProcedures/msdb/dbo.sp_add_schedule.md)
- [msdb: dbo.sp_autoadmin_create_notification_job](../../StoredProcedures/msdb/dbo.sp_autoadmin_create_notification_job.md)
- [msdb: dbo.sp_delete_schedule](../../StoredProcedures/msdb/dbo.sp_delete_schedule.md)
- [msdb: dbo.sp_detach_schedule](../../StoredProcedures/msdb/dbo.sp_detach_schedule.md)
- [msdb: dbo.sp_help_jobschedule](../../StoredProcedures/msdb/dbo.sp_help_jobschedule.md)
- [msdb: dbo.sp_update_schedule](../../StoredProcedures/msdb/dbo.sp_update_schedule.md)

