# dbo.PayrollMonthFacts

**Database:** payroll  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 0 |  |  |  |
| period_id | int | 4 | 0 |  |  |  |
| adj_actual | decimal | 9 | 1 |  |  |  |
| adj_earned | decimal | 9 | 1 |  |  |  |
| actual | decimal | 9 | 1 |  |  |  |
| earned | decimal | 9 | 1 |  |  |  |
| loaded_date | datetime | 8 | 1 |  |  |  |
| updated_date | datetime | 8 | 1 |  |  |  |
