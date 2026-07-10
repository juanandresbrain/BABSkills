# dbo.ld_monitor

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| step | int | 4 | 1 |  |  |  |
| process_name | varchar | 50 | 1 |  |  |  |
| step_name | varchar | 100 | 1 |  |  |  |
| status | varchar | 8 | 1 |  |  |  |
| process_date | datetime | 8 | 1 |  |  |  |
| uid | int | 4 | 0 | YES |  |  |
