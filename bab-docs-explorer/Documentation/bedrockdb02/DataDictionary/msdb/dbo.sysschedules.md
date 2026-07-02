# dbo.sysschedules

**Database:** msdb  
**Server:** bedrockdb02  

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
- [msdb: dbo.sp_delete_all_msx_jobs](../../StoredProcedures/msdb/dbo.sp_delete_all_msx_jobs.md)
- [msdb: dbo.sp_delete_job](../../StoredProcedures/msdb/dbo.sp_delete_job.md)
- [msdb: dbo.sp_delete_jobschedule](../../StoredProcedures/msdb/dbo.sp_delete_jobschedule.md)
- [msdb: dbo.sp_delete_schedule](../../StoredProcedures/msdb/dbo.sp_delete_schedule.md)
- [msdb: dbo.sp_detach_schedule](../../StoredProcedures/msdb/dbo.sp_detach_schedule.md)
- [msdb: dbo.sp_help_jobschedule](../../StoredProcedures/msdb/dbo.sp_help_jobschedule.md)
- [msdb: dbo.sp_post_msx_operation](../../StoredProcedures/msdb/dbo.sp_post_msx_operation.md)
- [msdb: dbo.sp_sqlagent_notify](../../StoredProcedures/msdb/dbo.sp_sqlagent_notify.md)
- [msdb: dbo.sp_syspolicy_add_policy](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_policy.md)
- [msdb: dbo.sp_syspolicy_create_job](../../StoredProcedures/msdb/dbo.sp_syspolicy_create_job.md)
- [msdb: dbo.sp_syspolicy_update_policy](../../StoredProcedures/msdb/dbo.sp_syspolicy_update_policy.md)
- [msdb: dbo.sp_sysutility_ucp_configure_policies](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_configure_policies.md)
- [msdb: dbo.sp_update_jobschedule](../../StoredProcedures/msdb/dbo.sp_update_jobschedule.md)
- [msdb: dbo.sp_update_schedule](../../StoredProcedures/msdb/dbo.sp_update_schedule.md)
- [msdb: dbo.sp_verify_schedule_identifiers](../../StoredProcedures/msdb/dbo.sp_verify_schedule_identifiers.md)
- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)

