# dbo.payroll_week_facts

**Database:** payroll  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 0 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| week_id | int | 4 | 0 |  |  |  |
| actual | decimal | 5 | 1 |  |  |  |
| earned | decimal | 5 | 1 |  |  |  |
| loaded_date | datetime | 8 | 1 |  |  |  |
| updated_date | datetime | 8 | 1 |  |  |  |
