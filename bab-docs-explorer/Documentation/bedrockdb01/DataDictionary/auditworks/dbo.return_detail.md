# dbo.return_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| return_reason_message | nvarchar | 80 | 1 |  |  |  |
| return_reason_code | smallint | 2 | 1 |  |  |  |
| mdse_disposition_code | smallint | 2 | 1 |  |  |  |
| via_warehouse_flag | tinyint | 1 | 0 |  |  |  |
| original_salesperson | int | 4 | 1 |  |  |  |
| original_salesperson2 | int | 4 | 1 |  |  |  |
| return_from_store | int | 4 | 1 |  |  |  |
| return_from_reg | smallint | 2 | 1 |  |  |  |
| return_from_date | smalldatetime | 4 | 1 |  |  |  |
| return_from_transno | int | 4 | 1 |  |  |  |
| without_receipt_flag | tinyint | 1 | 1 |  |  |  |
