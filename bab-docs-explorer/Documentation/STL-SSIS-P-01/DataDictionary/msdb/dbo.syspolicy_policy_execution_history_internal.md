# dbo.syspolicy_policy_execution_history_internal

**Database:** msdb  
**Server:** STL-SSIS-P-01  

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

