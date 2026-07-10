# dbo.JMC_SLS_TRANS_SilverDeltaLake_StageforStoreforce

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BusinessDate | date | 3 | 1 |  |  |  |
| StoreID | int | 4 | 1 |  |  |  |
| RegisterNumber | int | 4 | 1 |  |  |  |
| device_id | nvarchar | -1 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| pos_item_id | nvarchar | -1 | 1 |  |  |  |
| item_id | nvarchar | -1 | 1 |  |  |  |
| item_description | nvarchar | -1 | 1 |  |  |  |
| item_type | nvarchar | -1 | 1 |  |  |  |
| regular_unit_price | numeric | 17 | 1 |  |  |  |
| actual_unit_price | numeric | 17 | 1 |  |  |  |
| loyalty_unit_price | numeric | 17 | 1 |  |  |  |
| quantity | numeric | 17 | 1 |  |  |  |
| extended_amount | numeric | 17 | 1 |  |  |  |
| discount_amount | numeric | 17 | 1 |  |  |  |
| extended_discounted_amount | numeric | 17 | 1 |  |  |  |
| rtn_extended_discounted_amount | numeric | 17 | 1 |  |  |  |
| tax_amount | numeric | 17 | 1 |  |  |  |
| reason_code_group_id | nvarchar | -1 | 1 |  |  |  |
| reason_code | nvarchar | -1 | 1 |  |  |  |
| disposition_code | nvarchar | -1 | 1 |  |  |  |
| gift_receipt | int | 4 | 1 |  |  |  |
| item_returnable | int | 4 | 1 |  |  |  |
| item_taxable | int | 4 | 1 |  |  |  |
| quantity_avail_for_return | numeric | 17 | 1 |  |  |  |
| item_discountable | int | 4 | 1 |  |  |  |
| employee_discount_allowed | int | 4 | 1 |  |  |  |
| item_price_overridable | int | 4 | 1 |  |  |  |
| discount_applied | int | 4 | 1 |  |  |  |
| damage_discount_applied | int | 4 | 1 |  |  |  |
| tax_included_in_price | int | 4 | 1 |  |  |  |
| tax_group_id | nvarchar | -1 | 1 |  |  |  |
| orig_line_sequence_number | int | 4 | 1 |  |  |  |
| orig_sequence_number | bigint | 8 | 1 |  |  |  |
| orig_business_date | nvarchar | -1 | 1 |  |  |  |
| orig_device_id | nvarchar | -1 | 1 |  |  |  |
| orig_order_id | nvarchar | -1 | 1 |  |  |  |
| orig_username | nvarchar | -1 | 1 |  |  |  |
| orig_business_unit_id | nvarchar | -1 | 1 |  |  |  |
| return_policy_id | nvarchar | -1 | 1 |  |  |  |
| item_returned | int | 4 | 1 |  |  |  |
| iso_currency_code | nvarchar | -1 | 1 |  |  |  |
| item_weight | numeric | 17 | 1 |  |  |  |
| item_weight_plus_tare | numeric | 17 | 1 |  |  |  |
| weight_unit_of_measure | nvarchar | -1 | 1 |  |  |  |
| weight_entry_method_code | nvarchar | -1 | 1 |  |  |  |
| family_code | nvarchar | -1 | 1 |  |  |  |
| item_length | numeric | 17 | 1 |  |  |  |
| length_unit_of_measure | nvarchar | -1 | 1 |  |  |  |
| quantity_modifiable | int | 4 | 1 |  |  |  |
| save_value | numeric | 17 | 1 |  |  |  |
| save_value_type | nvarchar | -1 | 1 |  |  |  |
| coupon_allowed | int | 4 | 1 |  |  |  |
| eletronic_coupon_allowed | int | 4 | 1 |  |  |  |
| coupon_multiply_allowed | int | 4 | 1 |  |  |  |
| username | nvarchar | -1 | 1 |  |  |  |
| external_system_id | nvarchar | -1 | 1 |  |  |  |
| product_id | nvarchar | -1 | 1 |  |  |  |
| item_name | nvarchar | -1 | 1 |  |  |  |
| item_long_description | nvarchar | -1 | 1 |  |  |  |
| additional_classifiers | nvarchar | -1 | 1 |  |  |  |
| order_line_number | int | 4 | 1 |  |  |  |
| order_id | nvarchar | -1 | 1 |  |  |  |
| line_item_type | nvarchar | -1 | 1 |  |  |  |
| inquiry_method_code | nvarchar | -1 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | nvarchar | -1 | 1 |  |  |  |
| entry_method_code | nvarchar | -1 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | nvarchar | -1 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | nvarchar | -1 | 1 |  |  |  |
| stuff_info | nvarchar | -1 | 1 |  |  |  |
| find_a_bear_id | nvarchar | -1 | 1 |  |  |  |
| serialized_coupon_barcode | nvarchar | -1 | 1 |  |  |  |
| classifier_class | nvarchar | -1 | 1 |  |  |  |
| classifier_style | nvarchar | -1 | 1 |  |  |  |
| classifier_brand | nvarchar | -1 | 1 |  |  |  |
| classifier_department | nvarchar | -1 | 1 |  |  |  |
