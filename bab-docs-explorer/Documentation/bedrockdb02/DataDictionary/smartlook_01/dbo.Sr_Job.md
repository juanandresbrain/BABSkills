# dbo.Sr_Job

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 | YES |  |  |
| server_id | int | 4 | 0 |  |  |  |
| sequence_number | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| object_id | int | 4 | 0 |  |  |  |
| object_type | smallint | 2 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| interval_count | int | 4 | 1 |  |  |  |
| interval_type | smallint | 2 | 1 |  |  |  |
| start_date_time | datetime | 8 | 1 |  |  |  |
| end_date_time | datetime | 8 | 1 |  |  |  |
| schedule_details | varchar | 255 | 1 |  |  |  |
| last_date_time | datetime | 8 | 1 |  |  |  |
| next_date_time | datetime | 8 | 1 |  |  |  |
| locked | int | 4 | 0 |  |  |  |
| scheduled_executions | int | 4 | 0 |  |  |  |
| done_executions | int | 4 | 0 |  |  |  |
| auto_execute | bit | 1 | 0 |  |  |  |
| execution_id | int | 4 | 0 |  |  |  |
| active | bit | 1 | 0 |  |  |  |
| avg_duration | int | 4 | 1 |  |  |  |
| label | varchar | 80 | 1 |  |  |  |
| cmd_line | varchar | 255 | 1 |  |  |  |
| cmd_line_parameters | varchar | 255 | 1 |  |  |  |
| data | text | 16 | 1 |  |  |  |
| previous_status | tinyint | 1 | 1 |  |  |  |
| next_job_id | int | 4 | 0 |  |  |  |
| debug_level | smallint | 2 | 0 |  |  |  |
| created_date_time | datetime | 8 | 1 |  |  |  |
| scheduling_mode | int | 4 | 1 |  |  |  |
| max_threads | int | 4 | 0 |  |  |  |
| job_flags | int | 4 | 1 |  |  |  |
| machine_id | int | 4 | 0 |  |  |  |
| pid | int | 4 | 0 |  |  |  |
| data_ext | varchar | 255 | 1 |  |  |  |
| compatibility_version | int | 4 | 1 |  |  |  |
| wizard_id | int | 4 | 1 |  |  |  |
| kill_job | int | 4 | 1 |  |  |  |
| exit_code | varchar | 255 | 1 |  |  |  |
| need_rerun | bit | 1 | 0 |  |  |  |
| auto_recovery | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingUpdatePickReviewParameters](../../StoredProcedures/me_01/dbo.spMerchandisingUpdatePickReviewParameters.md)
- [me_01: dbo.spMerchandisingWhsePickReviewSummary](../../StoredProcedures/me_01/dbo.spMerchandisingWhsePickReviewSummary.md)
- [fn_01: dbo.Sr_ActivateJob](../../StoredProcedures/fn_01/dbo.Sr_ActivateJob.md)
- [fn_01: dbo.Sr_ActivateObject](../../StoredProcedures/fn_01/dbo.Sr_ActivateObject.md)
- [fn_01: dbo.Sr_AddJob](../../StoredProcedures/fn_01/dbo.Sr_AddJob.md)
- [fn_01: dbo.Sr_CompatibilityCheck](../../StoredProcedures/fn_01/dbo.Sr_CompatibilityCheck.md)
- [fn_01: dbo.Sr_ExecutionDone](../../StoredProcedures/fn_01/dbo.Sr_ExecutionDone.md)
- [fn_01: dbo.Sr_ExecutionStart](../../StoredProcedures/fn_01/dbo.Sr_ExecutionStart.md)
- [fn_01: dbo.Sr_GetNextJob](../../StoredProcedures/fn_01/dbo.Sr_GetNextJob.md)
- [fn_01: dbo.Sr_JobNeedRerun](../../StoredProcedures/fn_01/dbo.Sr_JobNeedRerun.md)
- [fn_01: dbo.Sr_KillJob](../../StoredProcedures/fn_01/dbo.Sr_KillJob.md)
- [fn_01: dbo.Sr_LockJob](../../StoredProcedures/fn_01/dbo.Sr_LockJob.md)
- [fn_01: dbo.Sr_RemoveJob](../../StoredProcedures/fn_01/dbo.Sr_RemoveJob.md)
- [fn_01: dbo.Sr_RemoveServer](../../StoredProcedures/fn_01/dbo.Sr_RemoveServer.md)
- [fn_01: dbo.Sr_StandAlone](../../StoredProcedures/fn_01/dbo.Sr_StandAlone.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [fn_01: dbo.Tr_ProcessError](../../StoredProcedures/fn_01/dbo.Tr_ProcessError.md)
- [smartlook_01: dbo.Sr_ActivateJob](../../StoredProcedures/smartlook_01/dbo.Sr_ActivateJob.md)
- [smartlook_01: dbo.Sr_ActivateObject](../../StoredProcedures/smartlook_01/dbo.Sr_ActivateObject.md)
- [smartlook_01: dbo.Sr_AddJob](../../StoredProcedures/smartlook_01/dbo.Sr_AddJob.md)
- [smartlook_01: dbo.Sr_CompatibilityCheck](../../StoredProcedures/smartlook_01/dbo.Sr_CompatibilityCheck.md)
- [smartlook_01: dbo.Sr_ExecutionDone](../../StoredProcedures/smartlook_01/dbo.Sr_ExecutionDone.md)
- [smartlook_01: dbo.Sr_ExecutionStart](../../StoredProcedures/smartlook_01/dbo.Sr_ExecutionStart.md)
- [smartlook_01: dbo.Sr_GetNextJob](../../StoredProcedures/smartlook_01/dbo.Sr_GetNextJob.md)
- [smartlook_01: dbo.Sr_JobNeedRerun](../../StoredProcedures/smartlook_01/dbo.Sr_JobNeedRerun.md)
- [smartlook_01: dbo.Sr_KillJob](../../StoredProcedures/smartlook_01/dbo.Sr_KillJob.md)
- [smartlook_01: dbo.Sr_LockJob](../../StoredProcedures/smartlook_01/dbo.Sr_LockJob.md)
- [smartlook_01: dbo.Sr_RemoveJob](../../StoredProcedures/smartlook_01/dbo.Sr_RemoveJob.md)
- [smartlook_01: dbo.Sr_RemoveServer](../../StoredProcedures/smartlook_01/dbo.Sr_RemoveServer.md)
- [smartlook_01: dbo.Sr_StandAlone](../../StoredProcedures/smartlook_01/dbo.Sr_StandAlone.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Tr_ProcessError](../../StoredProcedures/smartlook_01/dbo.Tr_ProcessError.md)

