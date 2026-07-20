# dbo.certificates_redeemed_facts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| date_key | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| reward_certificate_key | int | 4 | 1 |  |  |  |
| customer_key | int | 4 | 1 |  |  |  |
| customer_geography_key | int | 4 | 1 |  |  |  |
| customer_demographics_key | int | 4 | 1 |  |  |  |
| visit_count_key_12months | int | 4 | 1 |  |  |  |
| visit_count_key_24months | int | 4 | 1 |  |  |  |
| visit_count_key_36months | int | 4 | 1 |  |  |  |
| sfs_transaction_type_key | int | 4 | 1 |  |  |  |
| transaction_id | decimal | 9 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| reference_no | varchar | 8000 | 1 |  |  |  |
| redeemed_value | decimal | 9 | 1 |  |  |  |
| reward_transaction_id | int | 4 | 1 |  |  |  |
| communication_channel_key | int | 4 | 1 |  |  |  |
| communication_date_key | int | 4 | 1 |  |  |  |
