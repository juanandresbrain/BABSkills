# dbo.input_transaction_line

**Database:** auditworks  
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
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| gross_line_amount | numeric | 9 | 0 |  |  |  |
| line_object_lookup_flag | smallint | 2 | 0 |  |  |  |
| line_amount_divider | smallint | 2 | 0 |  |  |  |
| pos_discount_amount | numeric | 9 | 0 |  |  |  |
| gross_line_amount_sign | unit_datatype | 9 | 0 |  |  |  |
| line_void_flag | tinyint | 1 | 0 |  |  |  |
| voiding_reversal_flag | smallint | 2 | 0 |  |  |  |
| attachment_qty | tinyint | 1 | 0 |  |  |  |
| line_object_adjustment | smallint | 2 | 0 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
| lookup_pos_code | nvarchar | 1000 | 1 |  |  |  |
| pos_description_token_list | nvarchar | 1000 | 1 |  |  |  |
| invalid_reference_no | nvarchar | 160 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
