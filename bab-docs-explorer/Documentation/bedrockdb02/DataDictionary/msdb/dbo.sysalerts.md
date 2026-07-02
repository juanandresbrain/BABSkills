# dbo.sysalerts

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| event_source | nvarchar | 200 | 0 |  |  |  |
| event_category_id | int | 4 | 1 |  |  |  |
| event_id | int | 4 | 1 |  |  |  |
| message_id | int | 4 | 0 |  |  |  |
| severity | int | 4 | 0 |  |  |  |
| enabled | tinyint | 1 | 0 |  |  |  |
| delay_between_responses | int | 4 | 0 |  |  |  |
| last_occurrence_date | int | 4 | 0 |  |  |  |
| last_occurrence_time | int | 4 | 0 |  |  |  |
| last_response_date | int | 4 | 0 |  |  |  |
| last_response_time | int | 4 | 0 |  |  |  |
| notification_message | nvarchar | 1024 | 1 |  |  |  |
| include_event_description | tinyint | 1 | 0 |  |  |  |
| database_name | nvarchar | 1024 | 1 |  |  |  |
| event_description_keyword | nvarchar | 200 | 1 |  |  |  |
| occurrence_count | int | 4 | 0 |  |  |  |
| count_reset_date | int | 4 | 0 |  |  |  |
| count_reset_time | int | 4 | 0 |  |  |  |
| job_id | uniqueidentifier | 16 | 0 |  |  |  |
| has_notification | int | 4 | 0 |  |  |  |
| flags | int | 4 | 0 |  |  |  |
| performance_condition | nvarchar | 1024 | 1 |  |  |  |
| category_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_alert_internal](../../StoredProcedures/msdb/dbo.sp_add_alert_internal.md)
- [msdb: dbo.sp_add_notification](../../StoredProcedures/msdb/dbo.sp_add_notification.md)
- [msdb: dbo.sp_delete_alert](../../StoredProcedures/msdb/dbo.sp_delete_alert.md)
- [msdb: dbo.sp_delete_category](../../StoredProcedures/msdb/dbo.sp_delete_category.md)
- [msdb: dbo.sp_delete_job_references](../../StoredProcedures/msdb/dbo.sp_delete_job_references.md)
- [msdb: dbo.sp_delete_notification](../../StoredProcedures/msdb/dbo.sp_delete_notification.md)
- [msdb: dbo.sp_get_job_alerts](../../StoredProcedures/msdb/dbo.sp_get_job_alerts.md)
- [msdb: dbo.sp_help_alert](../../StoredProcedures/msdb/dbo.sp_help_alert.md)
- [msdb: dbo.sp_help_notification](../../StoredProcedures/msdb/dbo.sp_help_notification.md)
- [msdb: dbo.sp_sqlagent_get_perf_counters](../../StoredProcedures/msdb/dbo.sp_sqlagent_get_perf_counters.md)
- [msdb: dbo.sp_sqlagent_notify](../../StoredProcedures/msdb/dbo.sp_sqlagent_notify.md)
- [msdb: dbo.sp_update_alert](../../StoredProcedures/msdb/dbo.sp_update_alert.md)
- [msdb: dbo.sp_update_job](../../StoredProcedures/msdb/dbo.sp_update_job.md)
- [msdb: dbo.sp_update_notification](../../StoredProcedures/msdb/dbo.sp_update_notification.md)
- [msdb: dbo.sp_verify_alert](../../StoredProcedures/msdb/dbo.sp_verify_alert.md)
- [msdb: dbo.sp_verify_notification](../../StoredProcedures/msdb/dbo.sp_verify_notification.md)
- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)

