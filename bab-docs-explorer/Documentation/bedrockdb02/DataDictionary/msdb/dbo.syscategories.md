# dbo.syscategories

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| category_id | int | 4 | 0 |  |  |  |
| category_class | int | 4 | 0 |  |  |  |
| category_type | tinyint | 1 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_alert_internal](../../StoredProcedures/msdb/dbo.sp_add_alert_internal.md)
- [msdb: dbo.sp_add_category](../../StoredProcedures/msdb/dbo.sp_add_category.md)
- [msdb: dbo.sp_add_jobserver](../../StoredProcedures/msdb/dbo.sp_add_jobserver.md)
- [msdb: dbo.sp_add_operator](../../StoredProcedures/msdb/dbo.sp_add_operator.md)
- [msdb: dbo.sp_addtask](../../StoredProcedures/msdb/dbo.sp_addtask.md)
- [msdb: dbo.sp_delete_category](../../StoredProcedures/msdb/dbo.sp_delete_category.md)
- [msdb: dbo.sp_get_composite_job_info](../../StoredProcedures/msdb/dbo.sp_get_composite_job_info.md)
- [msdb: dbo.sp_help_category](../../StoredProcedures/msdb/dbo.sp_help_category.md)
- [msdb: dbo.sp_help_job](../../StoredProcedures/msdb/dbo.sp_help_job.md)
- [msdb: dbo.sp_help_operator](../../StoredProcedures/msdb/dbo.sp_help_operator.md)
- [msdb: dbo.sp_multi_server_job_summary](../../StoredProcedures/msdb/dbo.sp_multi_server_job_summary.md)
- [msdb: dbo.sp_sysutility_mi_disable_collection](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_disable_collection.md)
- [msdb: dbo.sp_sysutility_mi_initialize_collection](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_initialize_collection.md)
- [msdb: dbo.sp_update_alert](../../StoredProcedures/msdb/dbo.sp_update_alert.md)
- [msdb: dbo.sp_update_category](../../StoredProcedures/msdb/dbo.sp_update_category.md)
- [msdb: dbo.sp_update_job](../../StoredProcedures/msdb/dbo.sp_update_job.md)
- [msdb: dbo.sp_update_operator](../../StoredProcedures/msdb/dbo.sp_update_operator.md)
- [msdb: dbo.sp_verify_alert](../../StoredProcedures/msdb/dbo.sp_verify_alert.md)
- [msdb: dbo.sp_verify_category_identifiers](../../StoredProcedures/msdb/dbo.sp_verify_category_identifiers.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)
- [msdb: dbo.sp_verify_operator](../../StoredProcedures/msdb/dbo.sp_verify_operator.md)
- [DBAUtility: dbo.report_running_jobs](../../StoredProcedures/DBAUtility/dbo.report_running_jobs.md)
- [USICOAL: dbo.RPL_ADD_DISTR_SCHED](../../StoredProcedures/USICOAL/dbo.RPL_ADD_DISTR_SCHED.md)

