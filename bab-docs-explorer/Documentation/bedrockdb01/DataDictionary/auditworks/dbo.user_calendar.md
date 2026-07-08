# dbo.user_calendar

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| calendar_date | smalldatetime | 4 | 0 |  |  |  |
| merchandise_week_no | tinyint | 1 | 0 |  |  |  |
| merchandise_month_no | tinyint | 1 | 0 |  |  |  |
| merchandise_year_no | smallint | 2 | 0 |  |  |  |
| merchandise_season_no | tinyint | 1 | 0 |  |  |  |
| week_end_flag | char | 1 | 1 |  |  |  |
| month_end_flag | char | 1 | 1 |  |  |  |
| year_end_flag | char | 1 | 1 |  |  |  |
| timestamp | timestamp | 8 | 1 |  |  |  |
