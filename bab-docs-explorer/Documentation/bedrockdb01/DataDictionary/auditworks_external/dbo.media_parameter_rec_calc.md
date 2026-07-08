# dbo.media_parameter_rec_calc

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| media_parameter_set_no | smallint | 2 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| rec_side | smallint | 2 | 0 |  |  |  |
| rec_amount_type | tinyint | 1 | 0 |  |  |  |
| rec_amount_subtype | tinyint | 1 | 0 |  |  |  |
| rec_type | smallint | 2 | 0 |  |  |  |
| balancing_method | smallint | 2 | 0 |  |  |  |
| store_no_factor | tinyint | 1 | 0 |  |  |  |
| register_no_factor | tinyint | 1 | 0 |  |  |  |
| till_no_factor | tinyint | 1 | 0 |  |  |  |
| cashier_no_factor | tinyint | 1 | 0 |  |  |  |
| bank_no_factor | tinyint | 1 | 0 |  |  |  |
| multiple_actual_handling_code | smallint | 2 | 0 |  |  |  |
| rec_group_line_object | smallint | 2 | 0 |  |  |  |
| contribution_sign | smallint | 2 | 0 |  |  |  |
| foreign_currency_id | numeric | 9 | 1 |  |  |  |
| convert_to_domestic | tinyint | 1 | 0 |  |  |  |
| track_qty | tinyint | 1 | 0 |  |  |  |
| short_tolerance_amount | money | 8 | 0 |  |  |  |
| short_tolerance_qty | int | 4 | 0 |  |  |  |
| short_tolerance_percent | numeric | 5 | 0 |  |  |  |
| unrec_tolerance_days | smallint | 2 | 0 |  |  |  |
| unrec_tolerance_amount | money | 8 | 0 |  |  |  |
| assumed_rec_action | tinyint | 1 | 1 |  |  |  |
