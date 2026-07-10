# dbo.process_ran_history

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_ran_id | int | 4 | 0 | YES |  |  |
| process_name | varchar | 100 | 0 |  |  |  |
| process_start_date | datetime | 8 | 0 |  |  |  |
| process_end_date | datetime | 8 | 0 |  |  |  |
| process_success_flag | tinyint | 1 | 0 |  |  |  |
