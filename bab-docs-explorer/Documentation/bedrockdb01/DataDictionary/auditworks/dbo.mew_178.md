# dbo.mew_178

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 | YES |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| transaction_void_flag | smallint | 2 | 0 |  |  |  |
| customer_info_exists | tinyint | 1 | 0 |  |  |  |
| exception_flag | tinyint | 1 | 0 |  |  |  |
| sa_rejection_flag | tinyint | 1 | 0 |  |  |  |
| if_rejection_flag | tinyint | 1 | 0 |  |  |  |
| deposit_declaration_flag | tinyint | 1 | 0 |  |  |  |
| closeout_flag | tinyint | 1 | 0 |  |  |  |
| media_count_flag | tinyint | 1 | 0 |  |  |  |
| customer_modified_flag | tinyint | 1 | 0 |  |  |  |
| tax_override_flag | tinyint | 1 | 0 |  |  |  |
| pos_tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| edit_progress_flag | tinyint | 1 | 0 |  |  |  |
| edit_timestamp | float | 8 | 0 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| transaction_remark | nvarchar | 2000 | 1 |  |  |  |
| copy_transaction_id | if_entry_datatype | 9 | 1 |  |  |  |
| last_modified_date_time | smalldatetime | 4 | 1 |  |  |  |
| in_use_timestamp | smalldatetime | 4 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| move_source_date | smalldatetime | 4 | 1 |  |  |  |
| updated_by_user_id | int | 4 | 1 |  |  |  |
