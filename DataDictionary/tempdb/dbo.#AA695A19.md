# dbo.#AA695A19

**Database:** tempdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | uniqueidentifier | 16 | 0 |  |  |  |
| job_name | sysname | 256 | 0 |  |  |  |
| start_execution_date | datetime | 8 | 1 |  |  |  |
| current_executed_step_id | int | 4 | 1 |  |  |  |
| step_name | sysname | 256 | 0 |  |  |  |
| RunningMinutes | int | 4 | 1 |  |  |  |

