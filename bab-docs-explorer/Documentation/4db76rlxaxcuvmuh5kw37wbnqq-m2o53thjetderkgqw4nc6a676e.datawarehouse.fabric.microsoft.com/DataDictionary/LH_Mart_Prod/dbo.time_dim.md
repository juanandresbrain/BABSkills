# dbo.time_dim

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| time_key | int | 4 | 1 |  |  |  |
| hour | int | 4 | 1 |  |  |  |
| minute | int | 4 | 1 |  |  |  |
| daypart | varchar | 8000 | 1 |  |  |  |
| half_hour_id | int | 4 | 1 |  |  |  |
| qtr_hour_id | int | 4 | 1 |  |  |  |
