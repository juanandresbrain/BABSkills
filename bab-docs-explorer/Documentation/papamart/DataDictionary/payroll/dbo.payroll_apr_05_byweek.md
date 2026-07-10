# dbo.payroll_apr_05_byweek

**Database:** payroll  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| week_id | int | 4 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| storeid | int | 4 | 1 |  |  |  |
| Actual | decimal | 5 | 1 |  |  |  |
| Earned | decimal | 5 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
