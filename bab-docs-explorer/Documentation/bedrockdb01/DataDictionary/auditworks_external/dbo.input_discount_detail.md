# dbo.input_discount_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| input_id | numeric | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_id_adj | smallint | 2 | 0 |  |  |  |
| pos_discount_level | smallint | 2 | 0 |  |  |  |
| pos_discount_type | smallint | 2 | 0 |  |  |  |
| pos_discount_amount | numeric | 9 | 0 |  |  |  |
| pos_discount_amount_adj | numeric | 9 | 0 |  |  |  |
| discount_amount_sign | smallint | 2 | 0 |  |  |  |
| discount_applied_flag | tinyint | 1 | 0 |  |  |  |
| applied_by_line_id | numeric | 5 | 1 |  |  |  |
| pos_discount_serial_no | nvarchar | 40 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
