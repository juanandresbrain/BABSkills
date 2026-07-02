# dbo.syspolicy_system_health_state_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| health_state_id | bigint | 8 | 0 | YES |  |  |
| policy_id | int | 4 | 0 |  | YES |  |
| last_run_date | datetime | 8 | 0 |  |  |  |
| target_query_expression_with_id | nvarchar | 800 | 0 |  |  |  |
| target_query_expression | nvarchar | -1 | 0 |  |  |  |
| result | bit | 1 | 0 |  |  |  |

