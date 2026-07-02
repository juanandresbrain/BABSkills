# dbo.plu_tps_profile_setting_4676

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| thin_pos_server_id | int | 4 | 0 | YES |  |  |
| prompt_form_name | nvarchar | 80 | 1 |  |  |  |
| prompt_for_price | bit | 1 | 1 |  |  |  |
| validate | bit | 1 | 1 |  |  |  |
| accumulate | bit | 1 | 1 |  |  |  |
| prompt_for_additional_data | bit | 1 | 1 |  |  |  |
| quantity_required | bit | 1 | 1 |  |  |  |
| limited_quantity | decimal | 9 | 1 |  |  |  |
| allow_returns | bit | 1 | 1 |  |  |  |
| allow_layaways | bit | 1 | 1 |  |  |  |
| allow_discounts | bit | 1 | 1 |  |  |  |
| allow_employee_discounts | bit | 1 | 1 |  |  |  |
| allow_quantity_key | bit | 1 | 1 |  |  |  |
| allow_zero_price | bit | 1 | 1 |  |  |  |
| prompt_id | decimal | 9 | 1 |  |  |  |
| tax_group_code | decimal | 9 | 1 |  |  |  |
| generate_coupon_id | decimal | 9 | 1 |  |  |  |
| commissions_id | decimal | 9 | 1 |  |  |  |
| print_additional_copy | bit | 1 | 1 |  |  |  |
| print_retail | bit | 1 | 1 |  |  |  |
| print_suggested_retail | bit | 1 | 1 |  |  |  |
| photo | nvarchar | 510 | 1 |  |  |  |
| sound_file | nvarchar | 510 | 1 |  |  |  |
| gst_tax | bit | 1 | 1 |  |  |  |
| pst_state_tax | bit | 1 | 1 |  |  |  |
| threshold_tax_1 | bit | 1 | 1 |  |  |  |
| threshold_tax_2 | bit | 1 | 1 |  |  |  |
| vat_tax | bit | 1 | 1 |  |  |  |
| user_defined_tax_6 | bit | 1 | 1 |  |  |  |
| user_defined_tax_7 | bit | 1 | 1 |  |  |  |
| user_defined_tax_8 | bit | 1 | 1 |  |  |  |
| user_defined_tax_9 | bit | 1 | 1 |  |  |  |
| user_defined_tax_10 | bit | 1 | 1 |  |  |  |
| user_defined_tax_11 | bit | 1 | 1 |  |  |  |
| user_defined_tax_12 | bit | 1 | 1 |  |  |  |
| user_defined_tax_13 | bit | 1 | 1 |  |  |  |
| user_defined_tax_14 | bit | 1 | 1 |  |  |  |
| user_defined_tax_15 | bit | 1 | 1 |  |  |  |
| user_defined_tax_16 | bit | 1 | 1 |  |  |  |
| user_defined_flag_1 | nvarchar | 20 | 1 |  |  |  |
| user_defined_flag_2 | nvarchar | 20 | 1 |  |  |  |
| user_defined_flag_3 | nvarchar | 20 | 1 |  |  |  |
| user_defined_flag_4 | nvarchar | 20 | 1 |  |  |  |
| linked_item_group_id | int | 4 | 1 |  |  |  |

