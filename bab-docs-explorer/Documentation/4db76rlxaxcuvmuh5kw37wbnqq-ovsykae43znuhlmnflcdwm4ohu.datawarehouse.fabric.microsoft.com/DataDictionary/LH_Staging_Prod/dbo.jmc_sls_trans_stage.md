# dbo.jmc_sls_trans_stage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| business_date | datetime2 | 8 | 1 |  |  |  |
| business_unit_id | varchar | 8000 | 1 |  |  |  |
| device_id | varchar | 8000 | 1 |  |  |  |
| trans_type | varchar | 8000 | 1 |  |  |  |
| trans_status | varchar | 8000 | 1 |  |  |  |
| total | decimal | 9 | 1 |  |  |  |
| subtotal | decimal | 9 | 1 |  |  |  |
| tax_total | decimal | 9 | 1 |  |  |  |
| discount_total | decimal | 9 | 1 |  |  |  |
| trans_nbr | bigint | 8 | 1 |  |  |  |
| customer_id | varchar | 8000 | 1 |  |  |  |
| loyalty_card_number | varchar | 8000 | 1 |  |  |  |
| username | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
