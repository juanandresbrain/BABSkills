# dbo.TempJobTable

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | varchar | 1000 | 1 |  |  |  |
| originating_server | varchar | 100 | 1 |  |  |  |
| name | varchar | 100 | 1 |  |  |  |
| enabled | int | 4 | 1 |  |  |  |
| current_execution_status | int | 4 | 1 |  |  |  |

