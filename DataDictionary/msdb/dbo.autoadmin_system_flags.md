# dbo.autoadmin_system_flags

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | nvarchar | 256 | 0 |  |  |  |
| value | nvarchar | -1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.autoadmin_fetch_system_flags](../../StoredProcedures/msdb/dbo.autoadmin_fetch_system_flags.md)
- [msdb: dbo.autoadmin_set_system_flag](../../StoredProcedures/msdb/dbo.autoadmin_set_system_flag.md)
- [msdb: dbo.sp_autoadmin_notification_job_send_email](../../StoredProcedures/msdb/dbo.sp_autoadmin_notification_job_send_email.md)
- [msdb: dbo.sp_check_smartadmin_notification_enabled](../../StoredProcedures/msdb/dbo.sp_check_smartadmin_notification_enabled.md)

