# dbo.jumpmind_sls_retail_line_item_price_mod_uat

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | int | 4 | 1 |  |  |  |
| sequence_number | int | 4 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| mod_line_sequence_number | int | 4 | 1 |  |  |  |
| username | varchar | 8000 | 1 |  |  |  |
| reason_code | int | 4 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| mod_by_percentage | float | 8 | 1 |  |  |  |
| mod_by_amount | float | 8 | 1 |  |  |  |
| modification_total | float | 8 | 1 |  |  |  |
| calc_method | varchar | 8000 | 1 |  |  |  |
| promotion_id | varchar | 8000 | 1 |  |  |  |
| promotion_type | varchar | 8000 | 1 |  |  |  |
| promotion_reward_quantity | float | 8 | 1 |  |  |  |
| loyalty_promotion_id | bigint | 8 | 1 |  |  |  |
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
| promo_code_id | bigint | 8 | 1 |  |  |  |
| reward_base_price_type_code | varchar | 8000 | 1 |  |  |  |
| vendor_funded_flag | int | 4 | 1 |  |  |  |
| quantity_index | int | 4 | 1 |  |  |  |
| rtn_device_id | varchar | 8000 | 1 |  |  |  |
| rtn_business_date | int | 4 | 1 |  |  |  |
| rtn_sequence_number | int | 4 | 1 |  |  |  |
| returned_flag | int | 4 | 1 |  |  |  |
| external_id | varchar | 8000 | 1 |  |  |  |
