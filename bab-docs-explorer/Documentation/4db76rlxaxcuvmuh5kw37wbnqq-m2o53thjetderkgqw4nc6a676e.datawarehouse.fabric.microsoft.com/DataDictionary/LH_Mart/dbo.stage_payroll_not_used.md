# dbo.stage_payroll_not_used

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| monthly_id | int | 4 | 1 |  |  |  |
| week1_begin_date | datetime2 | 8 | 1 |  |  |  |
| week1_end_date | datetime2 | 8 | 1 |  |  |  |
| week1_actual | decimal | 9 | 1 |  |  |  |
| week1_earned | decimal | 9 | 1 |  |  |  |
| week2_begin_date | datetime2 | 8 | 1 |  |  |  |
| week2_end_date | datetime2 | 8 | 1 |  |  |  |
| week2_actual | decimal | 9 | 1 |  |  |  |
| week2_earned | decimal | 9 | 1 |  |  |  |
| week3_begin_date | datetime2 | 8 | 1 |  |  |  |
| week3_end_date | datetime2 | 8 | 1 |  |  |  |
| week3_actual | decimal | 9 | 1 |  |  |  |
| week3_earned | decimal | 9 | 1 |  |  |  |
| week4_begin_date | datetime2 | 8 | 1 |  |  |  |
| week4_end_date | datetime2 | 8 | 1 |  |  |  |
| week4_actual | decimal | 9 | 1 |  |  |  |
| week4_earned | decimal | 9 | 1 |  |  |  |
| week5_begin_date | datetime2 | 8 | 1 |  |  |  |
| week5_end_date | datetime2 | 8 | 1 |  |  |  |
| week5_actual | decimal | 9 | 1 |  |  |  |
| week5_earned | decimal | 9 | 1 |  |  |  |
| monthly_adj_actual | decimal | 9 | 1 |  |  |  |
| monthly_adj_earned | decimal | 9 | 1 |  |  |  |
| monthly_actual | decimal | 9 | 1 |  |  |  |
| monthly_earn | decimal | 9 | 1 |  |  |  |
| monthly | int | 4 | 1 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
