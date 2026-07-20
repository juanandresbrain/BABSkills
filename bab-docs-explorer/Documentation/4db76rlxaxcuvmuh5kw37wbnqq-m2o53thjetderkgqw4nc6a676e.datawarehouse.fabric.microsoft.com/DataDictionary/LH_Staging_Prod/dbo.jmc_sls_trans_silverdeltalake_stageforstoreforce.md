# dbo.jmc_sls_trans_silverdeltalake_stageforstoreforce

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BusinessDate | date | 3 | 1 |  |  |  |
| StoreID | int | 4 | 1 |  |  |  |
| RegisterNumber | int | 4 | 1 |  |  |  |
| device_id | varchar | 8000 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| pos_item_id | varchar | 8000 | 1 |  |  |  |
| item_id | varchar | 8000 | 1 |  |  |  |
| item_description | varchar | 8000 | 1 |  |  |  |
| item_type | varchar | 8000 | 1 |  |  |  |
| regular_unit_price | decimal | 17 | 1 |  |  |  |
| actual_unit_price | decimal | 17 | 1 |  |  |  |
| loyalty_unit_price | decimal | 17 | 1 |  |  |  |
| quantity | decimal | 17 | 1 |  |  |  |
| extended_amount | decimal | 17 | 1 |  |  |  |
| discount_amount | decimal | 17 | 1 |  |  |  |
| extended_discounted_amount | decimal | 17 | 1 |  |  |  |
| rtn_extended_discounted_amount | decimal | 17 | 1 |  |  |  |
| tax_amount | decimal | 17 | 1 |  |  |  |
| reason_code_group_id | varchar | 8000 | 1 |  |  |  |
| reason_code | varchar | 8000 | 1 |  |  |  |
| disposition_code | varchar | 8000 | 1 |  |  |  |
| gift_receipt | int | 4 | 1 |  |  |  |
| item_returnable | int | 4 | 1 |  |  |  |
| item_taxable | int | 4 | 1 |  |  |  |
| quantity_avail_for_return | decimal | 17 | 1 |  |  |  |
| item_discountable | int | 4 | 1 |  |  |  |
| employee_discount_allowed | int | 4 | 1 |  |  |  |
| item_price_overridable | int | 4 | 1 |  |  |  |
| discount_applied | int | 4 | 1 |  |  |  |
| damage_discount_applied | int | 4 | 1 |  |  |  |
| tax_included_in_price | int | 4 | 1 |  |  |  |
| tax_group_id | varchar | 8000 | 1 |  |  |  |
| orig_line_sequence_number | int | 4 | 1 |  |  |  |
| orig_sequence_number | bigint | 8 | 1 |  |  |  |
| orig_business_date | varchar | 8000 | 1 |  |  |  |
| orig_device_id | varchar | 8000 | 1 |  |  |  |
| orig_order_id | varchar | 8000 | 1 |  |  |  |
| orig_username | varchar | 8000 | 1 |  |  |  |
| orig_business_unit_id | varchar | 8000 | 1 |  |  |  |
| return_policy_id | varchar | 8000 | 1 |  |  |  |
| item_returned | int | 4 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| item_weight | decimal | 17 | 1 |  |  |  |
| item_weight_plus_tare | decimal | 17 | 1 |  |  |  |
| weight_unit_of_measure | varchar | 8000 | 1 |  |  |  |
| weight_entry_method_code | varchar | 8000 | 1 |  |  |  |
| family_code | varchar | 8000 | 1 |  |  |  |
| item_length | decimal | 17 | 1 |  |  |  |
| length_unit_of_measure | varchar | 8000 | 1 |  |  |  |
| quantity_modifiable | int | 4 | 1 |  |  |  |
| save_value | decimal | 17 | 1 |  |  |  |
| save_value_type | varchar | 8000 | 1 |  |  |  |
| coupon_allowed | int | 4 | 1 |  |  |  |
| eletronic_coupon_allowed | int | 4 | 1 |  |  |  |
| coupon_multiply_allowed | int | 4 | 1 |  |  |  |
| username | varchar | 8000 | 1 |  |  |  |
| external_system_id | varchar | 8000 | 1 |  |  |  |
| product_id | varchar | 8000 | 1 |  |  |  |
| item_name | varchar | 8000 | 1 |  |  |  |
| item_long_description | varchar | 8000 | 1 |  |  |  |
| additional_classifiers | varchar | 8000 | 1 |  |  |  |
| order_line_number | int | 4 | 1 |  |  |  |
| order_id | varchar | 8000 | 1 |  |  |  |
| line_item_type | varchar | 8000 | 1 |  |  |  |
| inquiry_method_code | varchar | 8000 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 8000 | 1 |  |  |  |
| entry_method_code | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| stuff_info | varchar | 8000 | 1 |  |  |  |
| find_a_bear_id | varchar | 8000 | 1 |  |  |  |
| serialized_coupon_barcode | varchar | 8000 | 1 |  |  |  |
| classifier_class | varchar | 8000 | 1 |  |  |  |
| classifier_style | varchar | 8000 | 1 |  |  |  |
| classifier_brand | varchar | 8000 | 1 |  |  |  |
| classifier_department | varchar | 8000 | 1 |  |  |  |
