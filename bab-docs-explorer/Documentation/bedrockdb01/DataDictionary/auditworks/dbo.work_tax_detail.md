# dbo.work_tax_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| tax_category | tinyint | 1 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| amount | line_amount_18_4 | 9 | 0 |  |  |  |
| tax_sign | smallint | 2 | 0 |  |  |  |
| gl_effect | smallint | 2 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| combined_tax_rate | numeric | 5 | 0 |  |  |  |
| threshold_amount | money | 8 | 0 |  |  |  |
| tax_on_threshold_excess | tinyint | 1 | 0 |  |  |  |
| tax_on_full_amount | tinyint | 1 | 0 |  |  |  |
| taxable_merchandise_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| taxable_fee_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| taxable_expense_amount | line_amount_18_4 | 9 | 1 |  |  |  |
| nontaxable_merchandise_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| nontaxable_fee_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| tax_amount_collected | line_amount_18_4 | 9 | 0 |  |  |  |
| tax_amount_paid | line_amount_18_4 | 9 | 1 |  |  |  |
| tax_amount_expected | line_amount_18_4 | 9 | 0 |  |  |  |
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
| max_applied_by_line_id | numeric | 5 | 1 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| tax_schedule_id | binary | 16 | 1 |  |  |  |
| transaction_level_tax_calc | tinyint | 1 | 1 |  |  |  |
| compound_order | int | 4 | 0 |  |  |  |
| on_tax_amt_expected | money | 8 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 1 |  |  |  |
| strip_rate | numeric | 5 | 1 |  |  |  |
| penny_adjusted | tinyint | 1 | 1 |  |  |  |
| track_tax | tinyint | 1 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 160 | 0 |  |  |  |
| tax_item_group_id | numeric | 9 | 1 |  |  |  |
| fulfillment_store_no | int | 4 | 1 |  |  |  |
| tax_amount_collected_unrounded | line_amount_18_4 | 9 | 1 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
