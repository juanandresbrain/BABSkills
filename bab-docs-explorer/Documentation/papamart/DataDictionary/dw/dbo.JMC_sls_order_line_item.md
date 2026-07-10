# dbo.JMC_sls_order_line_item

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 128 | 0 |  |  |  |
| line_sequence_number | int | 4 | 0 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 128 | 1 |  |  |  |
| entry_method_code | varchar | 128 | 1 |  |  |  |
| pos_item_id | varchar | 128 | 0 |  |  |  |
| item_id | varchar | 128 | 0 |  |  |  |
| item_description | varchar | 128 | 1 |  |  |  |
| item_type | varchar | 128 | 0 |  |  |  |
| regular_unit_price | numeric | 9 | 1 |  |  |  |
| actual_unit_price | numeric | 9 | 1 |  |  |  |
| loyalty_unit_price | numeric | 9 | 1 |  |  |  |
| quantity | numeric | 9 | 1 |  |  |  |
| extended_amount | numeric | 9 | 1 |  |  |  |
| discount_amount | numeric | 9 | 1 |  |  |  |
| extended_discounted_amount | numeric | 9 | 1 |  |  |  |
| rtn_extended_discounted_amount | numeric | 9 | 1 |  |  |  |
| tax_amount | numeric | 9 | 1 |  |  |  |
| reason_code_group_id | varchar | 128 | 1 |  |  |  |
| reason_code | varchar | 128 | 1 |  |  |  |
| disposition_code | varchar | 128 | 1 |  |  |  |
| gift_receipt | int | 4 | 1 |  |  |  |
| item_returnable | int | 4 | 1 |  |  |  |
| item_taxable | int | 4 | 1 |  |  |  |
| quantity_avail_for_return | numeric | 9 | 1 |  |  |  |
| item_discountable | int | 4 | 1 |  |  |  |
| employee_discount_allowed | int | 4 | 1 |  |  |  |
| item_price_overridable | int | 4 | 1 |  |  |  |
| discount_applied | int | 4 | 1 |  |  |  |
| damage_discount_applied | int | 4 | 1 |  |  |  |
| tax_included_in_price | int | 4 | 1 |  |  |  |
| tax_group_id | varchar | 128 | 1 |  |  |  |
| orig_line_sequence_number | int | 4 | 1 |  |  |  |
| orig_sequence_number | int | 4 | 1 |  |  |  |
| orig_business_date | varchar | 128 | 1 |  |  |  |
| orig_device_id | varchar | 128 | 1 |  |  |  |
| orig_order_id | varchar | 128 | 1 |  |  |  |
| orig_username | varchar | 128 | 1 |  |  |  |
| orig_business_unit_id | varchar | 128 | 1 |  |  |  |
| return_policy_id | varchar | 128 | 1 |  |  |  |
| item_returned | int | 4 | 1 |  |  |  |
| iso_currency_code | varchar | 128 | 1 |  |  |  |
| tare_weight | numeric | 9 | 1 |  |  |  |
| item_weight | numeric | 9 | 1 |  |  |  |
| item_weight_plus_tare | numeric | 9 | 1 |  |  |  |
| weight_unit_of_measure | varchar | 128 | 1 |  |  |  |
| weight_entry_method_code | varchar | 128 | 1 |  |  |  |
| family_code | varchar | 3 | 1 |  |  |  |
| item_length | numeric | 9 | 1 |  |  |  |
| length_unit_of_measure | varchar | 128 | 1 |  |  |  |
| quantity_modifiable | int | 4 | 1 |  |  |  |
| save_value | numeric | 9 | 1 |  |  |  |
| save_value_type | varchar | 128 | 1 |  |  |  |
| coupon_allowed | int | 4 | 1 |  |  |  |
| eletronic_coupon_allowed | int | 4 | 1 |  |  |  |
| coupon_multiply_allowed | int | 4 | 1 |  |  |  |
| username | varchar | 128 | 1 |  |  |  |
| external_system_id | varchar | 128 | 1 |  |  |  |
| product_id | varchar | 128 | 1 |  |  |  |
| item_name | varchar | 128 | 1 |  |  |  |
| item_long_description | varchar | 128 | 1 |  |  |  |
| additional_classifiers | varchar | 2048 | 1 |  |  |  |
| estimated_availability_date | varchar | 128 | 1 |  |  |  |
| actual_availability_date | varchar | 128 | 1 |  |  |  |
| order_item_status_code | varchar | 128 | 1 |  |  |  |
| package_line_sequence_number | int | 4 | 1 |  |  |  |
| create_time | datetime | 8 | 0 |  |  |  |
| create_by | varchar | 50 | 0 |  |  |  |
| last_update_time | timestamp | 8 | 1 |  |  |  |
| last_update_by | varchar | 50 | 0 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
