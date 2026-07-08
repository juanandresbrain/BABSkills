# dbo.function_status_express_add

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | int | 4 | 0 |  |  |  |
| user_id | int | 4 | 1 |  |  |  |
| function_no | tinyint | 1 | 0 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| entry_date | smalldatetime | 4 | 0 |  |  |  |
| lock_flag | tinyint | 1 | 0 |  |  |  |
| lock_by_user | nvarchar | 50 | 1 |  |  |  |
| lock_by_spid | int | 4 | 1 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| date_reject_id | tinyint | 1 | 1 |  |  |  |
| to_store_no | numeric | 9 | 1 |  |  |  |
| to_register_no | smallint | 2 | 1 |  |  |  |
| to_transaction_date | smalldatetime | 4 | 1 |  |  |  |
| from_transaction_no | trno | 4 | 1 |  |  |  |
| to_transaction_no | trno | 4 | 1 |  |  |  |
| move_flag | tinyint | 1 | 0 |  |  |  |
| register_no_cursor | smallint | 2 | 1 |  |  |  |
| glc_type | tinyint | 1 | 1 |  |  |  |
| tracking_id | smallint | 2 | 1 |  |  |  |
| reference_type | tinyint | 1 | 1 |  |  |  |
| transaction_series | nchar | 2 | 1 |  |  |  |
| frontend_populated | tinyint | 1 | 0 |  |  |  |
| file_name | nchar | 510 | 1 |  |  |  |
| rec_process_id | numeric | 9 | 1 |  |  |  |
| to_till_no | smallint | 2 | 1 |  |  |  |
| to_cashier_no | int | 4 | 1 |  |  |  |
