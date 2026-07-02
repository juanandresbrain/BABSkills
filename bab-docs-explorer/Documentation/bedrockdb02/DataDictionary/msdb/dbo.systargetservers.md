# dbo.systargetservers

**Database:** msdb  
**Server:** bedrockdb02  

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
- [msdb: dbo.sp_add_targetsvrgrp_member](../../StoredProcedures/msdb/dbo.sp_add_targetsvrgrp_member.md)
- [msdb: dbo.sp_apply_job_to_targets](../../StoredProcedures/msdb/dbo.sp_apply_job_to_targets.md)
- [msdb: dbo.sp_delete_jobserver](../../StoredProcedures/msdb/dbo.sp_delete_jobserver.md)
- [msdb: dbo.sp_delete_operator](../../StoredProcedures/msdb/dbo.sp_delete_operator.md)
- [msdb: dbo.sp_delete_targetserver](../../StoredProcedures/msdb/dbo.sp_delete_targetserver.md)
- [msdb: dbo.sp_delete_targetsvrgrp_member](../../StoredProcedures/msdb/dbo.sp_delete_targetsvrgrp_member.md)
- [msdb: dbo.sp_enlist_tsx](../../StoredProcedures/msdb/dbo.sp_enlist_tsx.md)
- [msdb: dbo.sp_generate_target_server_job_assignment_sql](../../StoredProcedures/msdb/dbo.sp_generate_target_server_job_assignment_sql.md)
- [msdb: dbo.sp_get_composite_job_info](../../StoredProcedures/msdb/dbo.sp_get_composite_job_info.md)
- [msdb: dbo.sp_get_sqlagent_properties](../../StoredProcedures/msdb/dbo.sp_get_sqlagent_properties.md)
- [msdb: dbo.sp_help_downloadlist](../../StoredProcedures/msdb/dbo.sp_help_downloadlist.md)
- [msdb: dbo.sp_help_jobhistory_full](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_full.md)
- [msdb: dbo.sp_help_jobhistory_sem](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_sem.md)
- [msdb: dbo.sp_help_jobhistory_summary](../../StoredProcedures/msdb/dbo.sp_help_jobhistory_summary.md)
- [msdb: dbo.sp_help_targetserver](../../StoredProcedures/msdb/dbo.sp_help_targetserver.md)
- [msdb: dbo.sp_help_targetservergroup](../../StoredProcedures/msdb/dbo.sp_help_targetservergroup.md)
- [msdb: dbo.sp_msx_enlist](../../StoredProcedures/msdb/dbo.sp_msx_enlist.md)
- [msdb: dbo.sp_post_msx_operation](../../StoredProcedures/msdb/dbo.sp_post_msx_operation.md)
- [msdb: dbo.sp_resync_targetserver](../../StoredProcedures/msdb/dbo.sp_resync_targetserver.md)
- [msdb: dbo.sp_sqlagent_probe_msx](../../StoredProcedures/msdb/dbo.sp_sqlagent_probe_msx.md)
- [msdb: dbo.sp_start_job](../../StoredProcedures/msdb/dbo.sp_start_job.md)
- [msdb: dbo.sp_stop_job](../../StoredProcedures/msdb/dbo.sp_stop_job.md)
- [msdb: dbo.sp_target_server_summary](../../StoredProcedures/msdb/dbo.sp_target_server_summary.md)
- [msdb: dbo.sp_update_operator](../../StoredProcedures/msdb/dbo.sp_update_operator.md)
- [msdb: dbo.sp_verify_job](../../StoredProcedures/msdb/dbo.sp_verify_job.md)
- [msdb: dbo.sp_verify_notification](../../StoredProcedures/msdb/dbo.sp_verify_notification.md)
- [DBAUtility: dbo.report_running_jobs](../../StoredProcedures/DBAUtility/dbo.report_running_jobs.md)

