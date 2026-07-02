# dbo.syspolicy_policy_execution_history_details_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| detail_id | bigint | 8 | 0 | YES |  |  |
| history_id | bigint | 8 | 0 | YES | YES |  |
| target_query_expression | nvarchar | 8000 | 0 |  |  |  |
| target_query_expression_with_id | nvarchar | 8000 | 0 |  |  |  |
| execution_date | datetime | 8 | 0 |  |  |  |
| result | bit | 1 | 0 |  |  |  |
| result_detail | nvarchar | -1 | 1 |  |  |  |
| exception_message | nvarchar | -1 | 1 |  |  |  |
| exception | nvarchar | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_log_policy_execution_detail](../../StoredProcedures/msdb/dbo.sp_syspolicy_log_policy_execution_detail.md)
- [msdb: dbo.sp_syspolicy_purge_history](../../StoredProcedures/msdb/dbo.sp_syspolicy_purge_history.md)
- [msdb: dbo.sp_sysutility_ucp_get_policy_violations](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_get_policy_violations.md)

