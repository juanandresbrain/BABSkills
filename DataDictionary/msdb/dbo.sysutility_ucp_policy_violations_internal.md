# dbo.sysutility_ucp_policy_violations_internal

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| health_policy_id | int | 4 | 0 |  |  |  |
| policy_id | int | 4 | 0 | YES |  |  |
| policy_name | sysname | 256 | 1 |  |  |  |
| history_id | int | 4 | 0 | YES |  |  |
| detail_id | int | 4 | 0 | YES |  |  |
| target_query_expression | nvarchar | -1 | 1 |  |  |  |
| target_query_expression_with_id | nvarchar | -1 | 1 |  |  |  |
| execution_date | datetime | 8 | 1 |  |  |  |
| result | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_remove](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove.md)

