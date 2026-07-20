# dbo.post_01_sls_retail_line_item

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| sequence_number | varchar | 8000 | 1 |  |  |  |
| line_sequence_number | varchar | 8000 | 1 |  |  |  |
| pos_item_id | varchar | 8000 | 1 |  |  |  |
| item_id | varchar | 8000 | 1 |  |  |  |
| item_description | varchar | 8000 | 1 |  |  |  |
| item_type | varchar | 8000 | 1 |  |  |  |
| regular_unit_price | varchar | 8000 | 1 |  |  |  |
| actual_unit_price | varchar | 8000 | 1 |  |  |  |
| loyalty_unit_price | varchar | 8000 | 1 |  |  |  |
| quantity | varchar | 8000 | 1 |  |  |  |
| extended_amount | varchar | 8000 | 1 |  |  |  |
| discount_amount | varchar | 8000 | 1 |  |  |  |
| extended_discounted_amount | varchar | 8000 | 1 |  |  |  |
| rtn_extended_discounted_amount | varchar | 8000 | 1 |  |  |  |
| tax_amount | varchar | 8000 | 1 |  |  |  |
| reason_code_group_id | varchar | 8000 | 1 |  |  |  |
| reason_code | varchar | 8000 | 1 |  |  |  |
| disposition_code | varchar | 8000 | 1 |  |  |  |
| gift_receipt | varchar | 8000 | 1 |  |  |  |
| item_returnable | varchar | 8000 | 1 |  |  |  |
| item_taxable | varchar | 8000 | 1 |  |  |  |
| quantity_avail_for_return | varchar | 8000 | 1 |  |  |  |
| item_discountable | varchar | 8000 | 1 |  |  |  |
| employee_discount_allowed | varchar | 8000 | 1 |  |  |  |
| item_price_overridable | varchar | 8000 | 1 |  |  |  |
| discount_applied | varchar | 8000 | 1 |  |  |  |
| damage_discount_applied | varchar | 8000 | 1 |  |  |  |
| tax_included_in_price | varchar | 8000 | 1 |  |  |  |
| tax_group_id | varchar | 8000 | 1 |  |  |  |
| orig_line_sequence_number | varchar | 8000 | 1 |  |  |  |
| orig_sequence_number | varchar | 8000 | 1 |  |  |  |
| orig_business_date | varchar | 8000 | 1 |  |  |  |
| orig_device_id | varchar | 8000 | 1 |  |  |  |
| orig_order_id | varchar | 8000 | 1 |  |  |  |
| orig_username | varchar | 8000 | 1 |  |  |  |
| orig_business_unit_id | varchar | 8000 | 1 |  |  |  |
| return_policy_id | varchar | 8000 | 1 |  |  |  |
| item_returned | varchar | 8000 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| tare_weight | varchar | 8000 | 1 |  |  |  |
| item_weight | varchar | 8000 | 1 |  |  |  |
| item_weight_plus_tare | varchar | 8000 | 1 |  |  |  |
| weight_unit_of_measure | varchar | 8000 | 1 |  |  |  |
| weight_entry_method_code | varchar | 8000 | 1 |  |  |  |
| family_code | varchar | 8000 | 1 |  |  |  |
| item_length | varchar | 8000 | 1 |  |  |  |
| length_unit_of_measure | varchar | 8000 | 1 |  |  |  |
| quantity_modifiable | varchar | 8000 | 1 |  |  |  |
| save_value | varchar | 8000 | 1 |  |  |  |
| save_value_type | varchar | 8000 | 1 |  |  |  |
| coupon_allowed | varchar | 8000 | 1 |  |  |  |
| eletronic_coupon_allowed | varchar | 8000 | 1 |  |  |  |
| coupon_multiply_allowed | varchar | 8000 | 1 |  |  |  |
| username | varchar | 8000 | 1 |  |  |  |
| external_system_id | varchar | 8000 | 1 |  |  |  |
| product_id | varchar | 8000 | 1 |  |  |  |
| item_name | varchar | 8000 | 1 |  |  |  |
| item_long_description | varchar | 8000 | 1 |  |  |  |
| additional_classifiers | varchar | 8000 | 1 |  |  |  |
| order_line_number | varchar | 8000 | 1 |  |  |  |
| order_id | varchar | 8000 | 1 |  |  |  |
| line_item_type | varchar | 8000 | 1 |  |  |  |
| inquiry_method_code | varchar | 8000 | 1 |  |  |  |
| voided | varchar | 8000 | 1 |  |  |  |
| override_user_id | varchar | 8000 | 1 |  |  |  |
| entry_method_code | varchar | 8000 | 1 |  |  |  |
| stuff_info | varchar | 8000 | 1 |  |  |  |
| find_a_bear_id | varchar | 8000 | 1 |  |  |  |
| serialized_coupon_barcode | varchar | 8000 | 1 |  |  |  |
| classifier_class | varchar | 8000 | 1 |  |  |  |
| classifier_style | varchar | 8000 | 1 |  |  |  |
| classifier_brand | varchar | 8000 | 1 |  |  |  |
| classifier_department | varchar | 8000 | 1 |  |  |  |
