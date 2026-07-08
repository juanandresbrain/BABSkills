# dbo.input_return_detail

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
| via_warehouse_flag | tinyint | 1 | 0 |  |  |  |
| return_reason_message | nvarchar | 80 | 1 |  |  |  |
| return_reason_code | smallint | 2 | 1 |  |  |  |
| mdse_disposition_code | smallint | 2 | 1 |  |  |  |
| return_from_store | int | 4 | 1 |  |  |  |
| return_from_reg | smallint | 2 | 1 |  |  |  |
| return_from_date | smalldatetime | 4 | 1 |  |  |  |
| return_from_transno | int | 4 | 1 |  |  |  |
| original_salesperson | int | 4 | 1 |  |  |  |
| original_salesperson2 | int | 4 | 1 |  |  |  |
| without_receipt_flag | tinyint | 1 | 1 |  |  |  |
| lookup_pos_code | nvarchar | 40 | 1 |  |  |  |
| pos_description | nvarchar | 510 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
