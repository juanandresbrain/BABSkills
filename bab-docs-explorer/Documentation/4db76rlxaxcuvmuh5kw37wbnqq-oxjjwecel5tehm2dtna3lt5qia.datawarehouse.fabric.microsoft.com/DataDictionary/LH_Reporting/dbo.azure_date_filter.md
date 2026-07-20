# dbo.azure_date_filter

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| date_key | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
| season | varchar | 8000 | 1 |  |  |  |
| fiscal_quarter | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| fiscal_week | int | 4 | 1 |  |  |  |
| month | int | 4 | 1 |  |  |  |
| year | int | 4 | 1 |  |  |  |
| month_name | varchar | 8000 | 1 |  |  |  |
| day_of_month | int | 4 | 1 |  |  |  |
| day_of_year | int | 4 | 1 |  |  |  |
| day_name | varchar | 8000 | 1 |  |  |  |
| weekend_y_n | varchar | 8000 | 1 |  |  |  |
| day_of_week | int | 4 | 1 |  |  |  |
| week_of_period | int | 4 | 1 |  |  |  |
| week_of_quarter | int | 4 | 1 |  |  |  |
| period_of_quarter | int | 4 | 1 |  |  |  |
| day_id | int | 4 | 1 |  |  |  |
| holiday_period_code | varchar | 8000 | 1 |  |  |  |
| week_id | int | 4 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| quarter_id | int | 4 | 1 |  |  |  |
| org_fiscal_quarter | int | 4 | 1 |  |  |  |
| org_fiscal_period | int | 4 | 1 |  |  |  |
| org_fiscal_week | int | 4 | 1 |  |  |  |
| org_week_of_period | int | 4 | 1 |  |  |  |
| org_week_of_quarter | int | 4 | 1 |  |  |  |
| org_period_of_quarter | int | 4 | 1 |  |  |  |
