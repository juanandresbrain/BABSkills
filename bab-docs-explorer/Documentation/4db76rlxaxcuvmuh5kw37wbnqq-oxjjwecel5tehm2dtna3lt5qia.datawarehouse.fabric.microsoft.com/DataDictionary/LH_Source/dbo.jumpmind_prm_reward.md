# dbo.jumpmind_prm_reward

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reward_id | varchar | 8000 | 1 |  |  |  |
| promotion_id | varchar | 8000 | 1 |  |  |  |
| reward_type | varchar | 8000 | 1 |  |  |  |
| reward | decimal | 17 | 1 |  |  |  |
| max_reward_amount | decimal | 17 | 1 |  |  |  |
| reward_quantity | decimal | 17 | 1 |  |  |  |
| qualification_eligible | int | 4 | 1 |  |  |  |
| qualification_prorate | int | 4 | 1 |  |  |  |
| vendor_funded | int | 4 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| tier | int | 4 | 1 |  |  |  |
