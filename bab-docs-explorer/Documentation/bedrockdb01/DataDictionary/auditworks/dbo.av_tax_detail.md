# dbo.av_tax_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| av_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| tax_category | smallint | 2 | 0 |  |  |  |
| tax_rate_code | tinyint | 1 | 0 |  |  |  |
| taxable_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| tax_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| combined_rate | numeric | 5 | 0 |  |  |  |
| nontaxable_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| tax_amount_expected | line_amount_18_4 | 9 | 0 |  |  |  |
| tax_on_tax_level | tinyint | 1 | 0 |  |  |  |
| tax_on_combined_rate | numeric | 5 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| tax_strip_flag | tinyint | 1 | 1 |  |  |  |
| gl_effect | smallint | 2 | 1 |  |  |  |
| max_applied_by_line_id | numeric | 5 | 1 |  |  |  |
| track_tax | tinyint | 1 | 0 |  |  |  |
| tax_item_group_id | numeric | 9 | 1 |  |  |  |
| fulfillment_store_no | int | 4 | 1 |  |  |  |
| originating_date | datetime | 8 | 1 |  |  |  |
| above_threshold_flag | tinyint | 1 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| applied_by_line_id | numeric | 5 | 1 |  |  |  |
