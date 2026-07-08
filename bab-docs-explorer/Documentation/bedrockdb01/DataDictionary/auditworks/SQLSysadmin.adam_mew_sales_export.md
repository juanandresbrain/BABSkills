# SQLSysadmin.adam_mew_sales_export

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| identity_no | numeric | 13 | 0 |  |  |  |
| if_entry_no | numeric | 9 | 0 |  |  |  |
| transaction_line_id | numeric | 5 | 0 |  |  |  |
| transaction_date | datetime | 8 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| location_id | numeric | 5 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| reference_no | varchar | 20 | 1 |  |  |  |
| transaction_type | tinyint | 1 | 0 |  |  |  |
| style_id | style_ref_id_datatype | 9 | 0 |  |  |  |
| sku_id | numeric | 9 | 0 |  |  |  |
| upc_no | numeric | 9 | 0 |  |  |  |
| price_override_flag | tinyint | 1 | 0 |  |  |  |
| reason_code | smallint | 2 | 1 |  |  |  |
| units | numeric | 9 | 0 |  |  |  |
| sold_at_price | line_amount | 9 | 0 |  |  |  |
| pos_disc_type_code | numeric | 9 | 1 |  |  |  |
| pos_disc_type_desc | varchar | 30 | 1 |  |  |  |
| pos_disc_type_amt | line_amount | 9 | 1 |  |  |  |
| applied_by_line_id | numeric | 9 | 1 |  |  |  |
| record_type | varchar | 1 | 0 |  |  |  |
| reference_type | tinyint | 1 | 1 |  |  |  |
| originating_store_no | int | 4 | 1 |  |  |  |
| tax_amount | line_amount | 9 | 1 |  |  |  |
