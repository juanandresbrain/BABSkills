# dbo.work_transaction_move

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| from_store_flag | tinyint | 1 | 0 |  |  |  |
| other_store_flag | tinyint | 1 | 0 |  |  |  |
| employee_flag | tinyint | 1 | 0 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| cashier_on_file_flag | int | 4 | 1 |  |  |  |
| orig_sa_reject_flag | tinyint | 1 | 0 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| sa_rejection_flag | tinyint | 1 | 1 |  |  |  |
| transaction_void_flag | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 1 |  |  |  |
| customer_info_exists | tinyint | 1 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
