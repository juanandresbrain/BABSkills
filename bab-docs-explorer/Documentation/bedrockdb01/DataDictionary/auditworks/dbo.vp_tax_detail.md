# dbo.vp_tax_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | int | 4 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_jurisdiction | char | 5 | 0 |  |  |  |
| tax_category | tinyint | 1 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| amount | line_amount | 9 | 0 |  |  |  |
| tax_sign | smallint | 2 | 0 |  |  |  |
| gl_effect | smallint | 2 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| combined_tax_rate | numeric | 5 | 0 |  |  |  |
| threshold_amount | smallmoney | 4 | 0 |  |  |  |
| tax_on_threshold_excess | tinyint | 1 | 0 |  |  |  |
| tax_on_full_amount | tinyint | 1 | 0 |  |  |  |
| taxable_merchandise_amount | line_amount | 9 | 0 |  |  |  |
| taxable_fee_amount | line_amount | 9 | 0 |  |  |  |
| taxable_expense_amount | line_amount | 9 | 1 |  |  |  |
| nontaxable_merchandise_amount | line_amount | 9 | 0 |  |  |  |
| nontaxable_fee_amount | line_amount | 9 | 0 |  |  |  |
| tax_amount_collected | line_amount | 9 | 0 |  |  |  |
| tax_amount_paid | line_amount | 9 | 1 |  |  |  |
| tax_amount_expected | line_amount | 9 | 0 |  |  |  |
| tax_on_tax_level | tinyint | 1 | 0 |  |  |  |
| tax_on_tax_rate_code | tinyint | 1 | 0 |  |  |  |
| tax_on_combined_rate | numeric | 5 | 0 |  |  |  |
| taxable | tinyint | 1 | 1 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 0 |  |  |  |
| below_threshold_combined_rate | numeric | 5 | 0 |  |  |  |
| return_from_date | smalldatetime | 4 | 1 |  |  |  |
| override_tax_category | tinyint | 1 | 1 |  |  |  |
| tax_paid_flag | tinyint | 1 | 1 |  |  |  |
| header_override_flag | tinyint | 1 | 1 |  |  |  |
| item_tax_strip_flag | tinyint | 1 | 0 |  |  |  |
| all_tax_override_flag | tinyint | 1 | 1 |  |  |  |
