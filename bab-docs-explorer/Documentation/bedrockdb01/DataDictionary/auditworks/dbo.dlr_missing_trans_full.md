# dbo.dlr_missing_trans_full

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_sequence | numeric | 5 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| gross_line_amount | numeric | 9 | 0 |  |  |  |
| pos_discount_amount | numeric | 9 | 0 |  |  |  |
| pos_discount_type | smallint | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| line_object_description | varchar | 255 | 0 |  |  |  |
| reference_no | varchar | 80 | 1 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| units | numeric | 9 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
