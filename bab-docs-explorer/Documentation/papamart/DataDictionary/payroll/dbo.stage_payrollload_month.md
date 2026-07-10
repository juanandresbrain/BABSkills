# dbo.stage_payrollload_month

**Database:** payroll  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| month_first_day | datetime | 8 | 1 |  |  |  |
| monthly_adj_actual | decimal | 9 | 1 |  |  |  |
| monthly_adj_earned | decimal | 9 | 1 |  |  |  |
| monthly_actual | decimal | 9 | 1 |  |  |  |
| monthly_earned | decimal | 9 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
