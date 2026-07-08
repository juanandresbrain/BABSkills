# dbo.LD_Giftcard_Activations_mjp

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_sequence | numeric | 5 | 0 |  |  |  |
| transaction_void_flag | smallint | 2 | 0 |  |  |  |
| line_void_flag | tinyint | 1 | 0 |  |  |  |
| gross_line_amount | numeric | 9 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| reference_no | varchar | 80 | 1 |  |  |  |
| line_note | varchar | 4000 | 1 |  |  |  |
