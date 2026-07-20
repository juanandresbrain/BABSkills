# dbo.dim_date2

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| date_key | int | 4 | 1 |  |  |  |
| actual_date | date | 3 | 1 |  |  |  |
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
| FiscalQuarterYear | varchar | 8000 | 1 |  |  |  |
| FiscalMonth | varchar | 8000 | 1 |  |  |  |
| FiscalWeekKey | varchar | 8000 | 1 |  |  |  |
| CalendarYearMonth | varchar | 8000 | 1 |  |  |  |
| FiscalMonthName | varchar | 8000 | 1 |  |  |  |
| SimpleDate | varchar | 8000 | 1 |  |  |  |
| FiscalWeekDisplay | varchar | 8000 | 1 |  |  |  |
| CalendarMonthName | varchar | 8000 | 1 |  |  |  |
| SeasonKey | varchar | 8000 | 1 |  |  |  |
| SeasonDisplay | varchar | 8000 | 1 |  |  |  |
| TimeCalcs | varchar | 8000 | 1 |  |  |  |
| FiscalMonthOfYear | varchar | 8000 | 1 |  |  |  |
| FiscalQuarterOfYear | varchar | 8000 | 1 |  |  |  |
| FiscalWeekOfYear | varchar | 8000 | 1 |  |  |  |
| WeekDayType | varchar | 8000 | 1 |  |  |  |
| MarketingQuarterOfYear | varchar | 8000 | 1 |  |  |  |
| MarketingYearQuarter | varchar | 8000 | 1 |  |  |  |
| AlternateDateKey | int | 4 | 1 |  |  |  |
