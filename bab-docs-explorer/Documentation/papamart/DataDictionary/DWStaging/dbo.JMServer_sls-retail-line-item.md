# dbo.JMServer_sls-retail-line-item

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 50 | 1 |  |  |  |
| business_date | varchar | 50 | 1 |  |  |  |
| sequence_number | varchar | 50 | 1 |  |  |  |
| line_sequence_number | varchar | 50 | 1 |  |  |  |
| pos_item_id | varchar | 50 | 1 |  |  |  |
| item_id | varchar | 50 | 1 |  |  |  |
| item_description | varchar | 50 | 1 |  |  |  |
| item_type | varchar | 50 | 1 |  |  |  |
| regular_unit_price | varchar | 50 | 1 |  |  |  |
| actual_unit_price | varchar | 50 | 1 |  |  |  |
| loyalty_unit_price | varchar | 50 | 1 |  |  |  |
| quantity | varchar | 50 | 1 |  |  |  |
| extended_amount | varchar | 50 | 1 |  |  |  |
| discount_amount | varchar | 50 | 1 |  |  |  |
| extended_discounted_amount | varchar | 50 | 1 |  |  |  |
| rtn_extended_discounted_amount | varchar | 50 | 1 |  |  |  |
| tax_amount | varchar | 50 | 1 |  |  |  |
| reason_code_group_id | varchar | 50 | 1 |  |  |  |
| reason_code | varchar | 50 | 1 |  |  |  |
| disposition_code | varchar | 50 | 1 |  |  |  |
| gift_receipt | varchar | 50 | 1 |  |  |  |
| item_returnable | varchar | 50 | 1 |  |  |  |
| item_taxable | varchar | 50 | 1 |  |  |  |
| quantity_avail_for_return | varchar | 50 | 1 |  |  |  |
| item_discountable | varchar | 50 | 1 |  |  |  |
| employee_discount_allowed | varchar | 50 | 1 |  |  |  |
| item_price_overridable | varchar | 50 | 1 |  |  |  |
| discount_applied | varchar | 50 | 1 |  |  |  |
| damage_discount_applied | varchar | 50 | 1 |  |  |  |
| tax_included_in_price | varchar | 50 | 1 |  |  |  |
| tax_group_id | varchar | 50 | 1 |  |  |  |
| orig_line_sequence_number | varchar | 50 | 1 |  |  |  |
| orig_sequence_number | varchar | 50 | 1 |  |  |  |
| orig_business_date | varchar | 50 | 1 |  |  |  |
| orig_device_id | varchar | 50 | 1 |  |  |  |
| orig_order_id | varchar | 50 | 1 |  |  |  |
| orig_username | varchar | 50 | 1 |  |  |  |
| orig_business_unit_id | varchar | 50 | 1 |  |  |  |
| return_policy_id | varchar | 50 | 1 |  |  |  |
| item_returned | varchar | 50 | 1 |  |  |  |
| iso_currency_code | varchar | 50 | 1 |  |  |  |
| tare_weight | varchar | 50 | 1 |  |  |  |
| item_weight | varchar | 50 | 1 |  |  |  |
| item_weight_plus_tare | varchar | 50 | 1 |  |  |  |
| weight_unit_of_measure | varchar | 50 | 1 |  |  |  |
| weight_entry_method_code | varchar | 50 | 1 |  |  |  |
| family_code | varchar | 50 | 1 |  |  |  |
| item_length | varchar | 50 | 1 |  |  |  |
| length_unit_of_measure | varchar | 50 | 1 |  |  |  |
| quantity_modifiable | varchar | 50 | 1 |  |  |  |
| save_value | varchar | 50 | 1 |  |  |  |
| save_value_type | varchar | 50 | 1 |  |  |  |
| coupon_allowed | varchar | 50 | 1 |  |  |  |
| eletronic_coupon_allowed | varchar | 50 | 1 |  |  |  |
| coupon_multiply_allowed | varchar | 50 | 1 |  |  |  |
| username | varchar | 50 | 1 |  |  |  |
| external_system_id | varchar | 50 | 1 |  |  |  |
| product_id | varchar | 50 | 1 |  |  |  |
| item_name | varchar | 50 | 1 |  |  |  |
| item_long_description | varchar | 50 | 1 |  |  |  |
| additional_classifiers | varchar | 50 | 1 |  |  |  |
| order_line_number | varchar | 50 | 1 |  |  |  |
| order_id | varchar | 50 | 1 |  |  |  |
| line_item_type | varchar | 50 | 1 |  |  |  |
| inquiry_method_code | varchar | 50 | 1 |  |  |  |
| voided | varchar | 50 | 1 |  |  |  |
| override_user_id | varchar | 50 | 1 |  |  |  |
| entry_method_code | varchar | 50 | 1 |  |  |  |
| stuff_info | varchar | 50 | 1 |  |  |  |
| find_a_bear_id | varchar | 50 | 1 |  |  |  |
| serialized_coupon_barcode | varchar | 50 | 1 |  |  |  |
| classifier_class | varchar | 50 | 1 |  |  |  |
| classifier_style | varchar | 50 | 1 |  |  |  |
| classifier_brand | varchar | 50 | 1 |  |  |  |
| classifier_department | varchar | 50 | 1 |  |  |  |
