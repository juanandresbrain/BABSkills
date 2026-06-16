# dbo.sysdbmaintplans

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_id | uniqueidentifier | 16 | 0 | YES |  |  |
| plan_name | sysname | 256 | 0 |  |  |  |
| date_created | datetime | 8 | 0 |  |  |  |
| owner | sysname | 256 | 0 |  |  |  |
| max_history_rows | int | 4 | 0 |  |  |  |
| remote_history_server | sysname | 256 | 0 |  |  |  |
| max_remote_history_rows | int | 4 | 0 |  |  |  |
| user_defined_1 | int | 4 | 1 |  |  |  |
| user_defined_2 | nvarchar | 200 | 1 |  |  |  |
| user_defined_3 | datetime | 8 | 1 |  |  |  |
| user_defined_4 | uniqueidentifier | 16 | 1 |  |  |  |

