# dbo.payroll_payrollweekstage

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| week_begin_date | datetime2 | 8 | 1 |  |  |  |
| week_end_date | datetime2 | 8 | 1 |  |  |  |
| week_actual | decimal | 9 | 1 |  |  |  |
| week_earned | decimal | 9 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| week_id | int | 4 | 1 |  |  |  |
| in_week_facts | bit | 1 | 1 |  |  |  |
