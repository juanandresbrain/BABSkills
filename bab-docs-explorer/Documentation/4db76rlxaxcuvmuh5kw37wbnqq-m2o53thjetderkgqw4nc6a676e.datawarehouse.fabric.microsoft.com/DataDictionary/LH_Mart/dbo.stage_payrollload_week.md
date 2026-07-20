# dbo.stage_payrollload_week

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
