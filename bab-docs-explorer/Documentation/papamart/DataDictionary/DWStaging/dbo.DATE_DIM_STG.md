# dbo.DATE_DIM_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sequence | int | 4 | 0 | YES |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
| season | varchar | 20 | 1 |  |  |  |
| fiscal_quarter | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| fiscal_week | int | 4 | 1 |  |  |  |
| month | int | 4 | 1 |  |  |  |
| year | int | 4 | 1 |  |  |  |
| month_name | varchar | 20 | 1 |  |  |  |
| day_of_month | int | 4 | 1 |  |  |  |
| day_of_year | int | 4 | 1 |  |  |  |
| day_name | varchar | 20 | 1 |  |  |  |
| weekend_y_n | varchar | 20 | 1 |  |  |  |
| day_of_week | int | 4 | 1 |  |  |  |
| week_of_period | int | 4 | 1 |  |  |  |
| week_of_quarter | int | 4 | 1 |  |  |  |
| period_of_quarter | int | 4 | 1 |  |  |  |
| day_id | int | 4 | 1 |  |  |  |
| holiday_period_code | varchar | 20 | 1 |  |  |  |
| week_id | int | 4 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| quarter_id | int | 4 | 1 |  |  |  |
| org_fiscal_quarter | int | 4 | 1 |  |  |  |
| org_fiscal_period | int | 4 | 1 |  |  |  |
| org_fiscal_week | int | 4 | 1 |  |  |  |
| org_week_of_period | int | 4 | 1 |  |  |  |
| org_week_of_quarter | int | 4 | 1 |  |  |  |
| org_period_of_quarter | int | 4 | 1 |  |  |  |
