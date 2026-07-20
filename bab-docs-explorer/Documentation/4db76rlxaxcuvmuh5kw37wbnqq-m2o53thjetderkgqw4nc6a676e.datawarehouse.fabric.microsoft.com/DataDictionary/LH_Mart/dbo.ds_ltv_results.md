# dbo.ds_ltv_results

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| cohort_name | varchar | 8000 | 1 |  |  |  |
| annual_discount_rate | float | 8 | 1 |  |  |  |
| grace_days | int | 4 | 1 |  |  |  |
| run_ts_utc | datetime2 | 8 | 1 |  |  |  |
| cohort_table | varchar | 8000 | 1 |  |  |  |
| cohort_size | int | 4 | 1 |  |  |  |
| months_observed | int | 4 | 1 |  |  |  |
| tail_gamma_estimate | float | 8 | 1 |  |  |  |
| ltv_per_customer | float | 8 | 1 |  |  |  |
| total_ltv | float | 8 | 1 |  |  |  |
