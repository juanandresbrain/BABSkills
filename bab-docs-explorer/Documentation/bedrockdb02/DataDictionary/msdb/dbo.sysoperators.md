# dbo.sysoperators

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| enabled | tinyint | 1 | 0 |  |  |  |
| email_address | nvarchar | 200 | 1 |  |  |  |
| last_email_date | int | 4 | 0 |  |  |  |
| last_email_time | int | 4 | 0 |  |  |  |
| pager_address | nvarchar | 200 | 1 |  |  |  |
| last_pager_date | int | 4 | 0 |  |  |  |
| last_pager_time | int | 4 | 0 |  |  |  |
| weekday_pager_start_time | int | 4 | 0 |  |  |  |
| weekday_pager_end_time | int | 4 | 0 |  |  |  |
| saturday_pager_start_time | int | 4 | 0 |  |  |  |
| saturday_pager_end_time | int | 4 | 0 |  |  |  |
| sunday_pager_start_time | int | 4 | 0 |  |  |  |
| sunday_pager_end_time | int | 4 | 0 |  |  |  |
| pager_days | tinyint | 1 | 0 |  |  |  |
| netsend_address | nvarchar | 200 | 1 |  |  |  |
| last_netsend_date | int | 4 | 0 |  |  |  |
| last_netsend_time | int | 4 | 0 |  |  |  |
| category_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_jobserver](../../StoredProcedures/msdb/dbo.sp_add_jobserver.md)
- [msdb: dbo.sp_add_operator](../../StoredProcedures/msdb/dbo.sp_add_operator.md)
- [msdb: dbo.sp_delete_category](../../StoredProcedures/msdb/dbo.sp_delete_category.md)
- [msdb: dbo.sp_delete_operator](../../StoredProcedures/msdb/dbo.sp_delete_operator.md)
- [msdb: dbo.sp_enlist_tsx](../../StoredProcedures/msdb/dbo.sp_enlist_tsx.md)
- [msdb: dbo.sp_get_composite_job_info](../../StoredProcedures/msdb/dbo.sp_get_composite_job_info.md)
- [msdb: dbo.sp_help_jobhistory_full](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_full.md)
- [msdb: dbo.sp_help_jobhistory_sem](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_sem.md)
- [msdb: dbo.sp_help_jobhistory_summary](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_summary.md)
- [msdb: dbo.sp_help_notification](../../StoredProcedures/msdb/dbo.sp_help_notification.md)
- [msdb: dbo.sp_help_operator](../../StoredProcedures/msdb/dbo.sp_help_operator.md)
- [msdb: dbo.sp_help_operator_jobs](../../StoredProcedures/msdb/dbo.sp_help_operator_jobs.md)
- [msdb: dbo.sp_msx_defect](../../StoredProcedures/msdb/dbo.sp_msx_defect.md)
- [msdb: dbo.sp_notify_operator](../../StoredProcedures/msdb/dbo.sp_notify_operator.md)
- [msdb: dbo.sp_sqlagent_log_jobhistory](../../StoredProcedures/msdb/dbo.sp_sqlagent_log_jobhistory.md)
- [msdb: dbo.sp_update_job](../../StoredProcedures/msdb/dbo.sp_update_job.md)
- [msdb: dbo.sp_update_operator](../../StoredProcedures/msdb/dbo.sp_update_operator.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)
- [msdb: dbo.sp_verify_notification](../../StoredProcedures/msdb/dbo.sp_verify_notification.md)
- [msdb: dbo.sp_verify_operator](../../StoredProcedures/msdb/dbo.sp_verify_operator.md)
- [msdb: dbo.sp_verify_operator_identifiers](../../StoredProcedures/msdb/dbo.sp_verify_operator_identifiers.md)
- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)
- [DBAUtility: dbo.report_running_jobs](../../StoredProcedures/DBAUtility/dbo.report_running_jobs.md)
- [DBAUtility: dbo.spDBA_Blitz](../../StoredProcedures/DBAUtility/dbo.spDBA_Blitz.md)

