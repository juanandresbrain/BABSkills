# dbo.PayrollWeekStage

**Database:** payroll  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| week_begin_date | datetime | 8 | 1 |  |  |  |
| week_end_date | datetime | 8 | 1 |  |  |  |
| week_actual | decimal | 9 | 1 |  |  |  |
| week_earned | decimal | 9 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| week_id | int | 4 | 1 |  |  |  |
| in_week_facts | bit | 1 | 1 |  |  |  |
