# dbo.sysjobstepslogs

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| log_id | int | 4 | 0 | YES |  |  |
| log | nvarchar | -1 | 0 |  |  |  |
| date_created | datetime | 8 | 0 |  |  |  |
| date_modified | datetime | 8 | 0 |  |  |  |
| log_size | bigint | 8 | 1 |  |  |  |
| step_uid | uniqueidentifier | 16 | 0 |  | YES |  |

