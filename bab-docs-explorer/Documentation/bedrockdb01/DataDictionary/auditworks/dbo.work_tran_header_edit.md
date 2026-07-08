# dbo.work_tran_header_edit

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| orig_transaction_category | tinyint | 1 | 0 |  |  |  |
| edit_timestamp | float | 8 | 0 |  |  |  |
| transaction_time | smallint | 2 | 0 |  |  |  |
| closeout_flag | tinyint | 1 | 0 |  |  |  |
| duplicate_flag | tinyint | 1 | 0 |  |  |  |
| sa_rejection_flag | tinyint | 1 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| tax_override_flag | tinyint | 1 | 0 |  |  |  |
| employee_on_file_flag | tinyint | 1 | 0 |  |  |  |
| transaction_void_flag | smallint | 2 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| deposit_declaration_flag | tinyint | 1 | 0 |  |  |  |
| pos_tax_jurisdiction | nchar | 10 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| cashier_on_file_flag | int | 4 | 1 |  |  |  |
| tax_jurisdiction_store | int | 4 | 1 |  |  |  |
| orig_transaction_date | smalldatetime | 4 | 1 |  |  |  |
| status_reject_reason | tinyint | 1 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 1 |  |  |  |
| customer_info_exists | int | 4 | 1 |  |  |  |
| media_count_flag | tinyint | 1 | 1 |  |  |  |
| reg_pre_midnight_time | int | 4 | 1 |  |  |  |
| reg_post_midnight_time | int | 4 | 1 |  |  |  |
| completion_date_time | datetime | 8 | 1 |  |  |  |
| transaction_remark | nvarchar | 2000 | 1 |  |  |  |
| line_exists | tinyint | 1 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| lookup_transaction_series | nchar | 2 | 1 |  |  |  |
| open_date | datetime | 8 | 1 |  |  |  |
| open_to_receive_date | datetime | 8 | 1 |  |  |  |
| pos_transaction_series | nvarchar | 1000 | 1 |  |  |  |
