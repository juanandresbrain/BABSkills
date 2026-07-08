# dbo.work_tax_post_template

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| gross_line_amount | money | 8 | 0 |  |  |  |
| discount_amount | money | 8 | 0 |  |  |  |
| amount_sign | smallint | 2 | 1 |  |  |  |
| gl_effect | smallint | 2 | 1 |  |  |  |
| store_tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| style_reference_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| return_from_store | int | 4 | 1 |  |  |  |
| return_from_date | smalldatetime | 4 | 1 |  |  |  |
| override_tax_category | tinyint | 1 | 1 |  |  |  |
| tax_paid_flag | tinyint | 1 | 1 |  |  |  |
| header_override_flag | tinyint | 1 | 1 |  |  |  |
| all_tax_override_flag | tinyint | 1 | 1 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| transaction_series | nchar | 2 | 1 |  |  |  |
| units | unit_datatype | 9 | 0 |  |  |  |
| track_tax | tinyint | 1 | 0 |  |  |  |
| reference_type | tinyint | 1 | 1 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
