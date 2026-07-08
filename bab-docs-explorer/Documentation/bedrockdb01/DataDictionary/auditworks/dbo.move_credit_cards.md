# dbo.move_credit_cards

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| orig_line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| orig_card_type | nchar | 2 | 0 |  |  |  |
| calculated_card_type | nchar | 2 | 0 |  |  |  |
| calculated_line_object | smallint | 2 | 0 |  |  |  |
| card_no | numeric | 13 | 0 |  |  |  |
