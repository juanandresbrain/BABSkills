# dbo.jumpmind_prm_promotion

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| promotion_id | varchar | 8000 | 1 |  |  |  |
| promotion_name | varchar | 8000 | 1 |  |  |  |
| long_description | varchar | 8000 | 1 |  |  |  |
| promotion_type | varchar | 8000 | 1 |  |  |  |
| single_use | int | 4 | 1 |  |  |  |
| auto_apply | int | 4 | 1 |  |  |  |
| max_uses | decimal | 17 | 1 |  |  |  |
| vendor_funded | int | 4 | 1 |  |  |  |
| reward_application_type_code | varchar | 8000 | 1 |  |  |  |
| qualify_application_type_code | varchar | 8000 | 1 |  |  |  |
| reward_operator_type_code | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| campaign_id | varchar | 8000 | 1 |  |  |  |
| reward_base_price_type_code | varchar | 8000 | 1 |  |  |  |
| external_id | varchar | 8000 | 1 |  |  |  |
