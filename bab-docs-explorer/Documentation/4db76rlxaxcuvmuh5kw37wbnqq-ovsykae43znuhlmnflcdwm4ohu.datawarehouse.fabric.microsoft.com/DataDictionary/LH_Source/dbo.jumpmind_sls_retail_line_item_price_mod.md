# dbo.jumpmind_sls_retail_line_item_price_mod

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| mod_line_sequence_number | int | 4 | 1 |  |  |  |
| username | varchar | 8000 | 1 |  |  |  |
| reason_code | varchar | 8000 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| mod_by_percentage | decimal | 17 | 1 |  |  |  |
| mod_by_amount | decimal | 17 | 1 |  |  |  |
| modification_total | decimal | 17 | 1 |  |  |  |
| calc_method | varchar | 8000 | 1 |  |  |  |
| promotion_id | varchar | 8000 | 1 |  |  |  |
| promotion_type | varchar | 8000 | 1 |  |  |  |
| promotion_reward_quantity | decimal | 17 | 1 |  |  |  |
| loyalty_promotion_id | varchar | 8000 | 1 |  |  |  |
| applied_coupon_item_ids | varchar | 8000 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| price_mod_type_code | varchar | 8000 | 1 |  |  |  |
| price_mod_source_type_code | varchar | 8000 | 1 |  |  |  |
| price_mod_source_sub_type_code | varchar | 8000 | 1 |  |  |  |
| ref_line_sequence_number | int | 4 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 8000 | 1 |  |  |  |
| entry_method_code | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| promo_code_id | varchar | 8000 | 1 |  |  |  |
| reward_base_price_type_code | varchar | 8000 | 1 |  |  |  |
| vendor_funded_flag | int | 4 | 1 |  |  |  |
| quantity_index | int | 4 | 1 |  |  |  |
| rtn_device_id | varchar | 8000 | 1 |  |  |  |
| rtn_business_date | varchar | 8000 | 1 |  |  |  |
| rtn_sequence_number | bigint | 8 | 1 |  |  |  |
| returned_flag | int | 4 | 1 |  |  |  |
| external_id | varchar | 8000 | 1 |  |  |  |
