# dbo.syspolicy_policy_execution_history_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| history_id | bigint | 8 | 0 | YES |  |  |
| policy_id | int | 4 | 0 |  | YES |  |
| start_date | datetime | 8 | 0 |  |  |  |
| end_date | datetime | 8 | 1 |  |  |  |
| result | bit | 1 | 0 |  |  |  |
| is_full_run | bit | 1 | 0 |  |  |  |
| exception_message | nvarchar | -1 | 1 |  |  |  |
| exception | nvarchar | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_delete_policy_execution_history](../../StoredProcedures/msdb/dbo.sp_syspolicy_delete_policy_execution_history.md)
- [msdb: dbo.sp_syspolicy_log_policy_execution_detail](../../StoredProcedures/msdb/dbo.sp_syspolicy_log_policy_execution_detail.md)
- [msdb: dbo.sp_syspolicy_log_policy_execution_end](../../StoredProcedures/msdb/dbo.sp_syspolicy_log_policy_execution_end.md)
- [msdb: dbo.sp_syspolicy_log_policy_execution_start](../../StoredProcedures/msdb/dbo.sp_syspolicy_log_policy_execution_start.md)
- [msdb: dbo.sp_syspolicy_purge_history](../../StoredProcedures/msdb/dbo.sp_syspolicy_purge_history.md)
- [msdb: dbo.sp_sysutility_ucp_get_policy_violations](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_get_policy_violations.md)

