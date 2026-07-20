# dbo.staging_crmrewardtransaction

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reward_transaction_id | int | 4 | 1 |  |  |  |
| customer_id | int | 4 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| reward_category | varchar | 8000 | 1 |  |  |  |
| points_posted | decimal | 5 | 1 |  |  |  |
| points_available | decimal | 5 | 1 |  |  |  |
| reason_type_code | varchar | 8000 | 1 |  |  |  |
| comments | varchar | 8000 | 1 |  |  |  |
| total_net_retail | decimal | 9 | 1 |  |  |  |
| total_net_units | real | 4 | 1 |  |  |  |
| regular_points | decimal | 5 | 1 |  |  |  |
| header_bonus_points | decimal | 5 | 1 |  |  |  |
| detail_bonus_points | decimal | 5 | 1 |  |  |  |
| tender_bonus_points | decimal | 5 | 1 |  |  |  |
| date_points_posted | datetime2 | 8 | 1 |  |  |  |
| reference_no | bigint | 8 | 1 |  |  |  |
| original_reward_tran_id | int | 4 | 1 |  |  |  |
| transaction_time | datetime2 | 8 | 1 |  |  |  |
| total_net_retail_central | decimal | 9 | 1 |  |  |  |
| exchange_rate | decimal | 9 | 1 |  |  |  |
| currency_code | varchar | 8000 | 1 |  |  |  |
| redemption_reversed | bit | 1 | 1 |  |  |  |
| amount | decimal | 9 | 1 |  |  |  |
| country_code | varchar | 8000 | 1 |  |  |  |
