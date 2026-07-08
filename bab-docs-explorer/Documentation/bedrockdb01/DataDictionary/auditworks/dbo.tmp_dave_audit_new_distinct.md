# dbo.tmp_dave_audit_new_distinct

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| transaction_id | numeric | 9 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| line_sequence | numeric | 5 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| gross_line_amount | numeric | 9 | 1 |  |  |  |
| pos_discount_amount | numeric | 9 | 1 |  |  |  |
| pos_discount_type | smallint | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| line_object_type | tinyint | 1 | 1 |  |  |  |
| line_object_description | varchar | 255 | 1 |  |  |  |
| reference_no | varchar | 80 | 1 |  |  |  |
| reference_no_new | varchar | 80 | 1 |  |  |  |
| line_action | tinyint | 1 | 1 |  |  |  |
| units | numeric | 9 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 1 |  |  |  |
