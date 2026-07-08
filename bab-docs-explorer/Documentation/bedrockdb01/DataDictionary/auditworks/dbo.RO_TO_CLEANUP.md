# dbo.RO_TO_CLEANUP

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| queue_id | int | 4 | 0 |  |  |  |
| serial_no | numeric | 9 | 0 |  |  |  |
| key_1 | if_entry_datatype | 9 | 0 |  |  |  |
| key_2 | numeric | 9 | 0 |  |  |  |
| key_3 | numeric | 9 | 1 |  |  |  |
| key_4 | numeric | 9 | 1 |  |  |  |
| key_5 | varchar | 255 | 1 |  |  |  |
| key_6 | varchar | 255 | 1 |  |  |  |
| key_7 | varchar | 255 | 1 |  |  |  |
| key_8 | varchar | 255 | 1 |  |  |  |
| key_9 | datetime | 8 | 1 |  |  |  |
| key_10 | datetime | 8 | 1 |  |  |  |
| key_11 | datetime | 8 | 1 |  |  |  |
| key_12 | datetime | 8 | 1 |  |  |  |
| used_by_object_id | int | 4 | 1 |  |  |  |
| stream_no | tinyint | 1 | 1 |  |  |  |
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
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
| deposit_declaration_flag | tinyint | 1 | 0 |  |  |  |
| closeout_flag | tinyint | 1 | 0 |  |  |  |
| media_count_flag | tinyint | 1 | 0 |  |  |  |
| customer_modified_flag | tinyint | 1 | 0 |  |  |  |
| tax_override_flag | tinyint | 1 | 0 |  |  |  |
| pos_tax_jurisdiction | nchar | 10 | 0 |  |  |  |
| edit_timestamp | float | 8 | 0 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| transaction_remark | nvarchar | 2000 | 1 |  |  |  |
| source_process_no | tinyint | 1 | 1 |  |  |  |
| last_modified_date_time | smalldatetime | 4 | 1 |  |  |  |
| in_use_timestamp | smalldatetime | 4 | 1 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
| updated_by_user_id | int | 4 | 1 |  |  |  |
| instance_id | smallint | 2 | 1 |  |  |  |
| instance_if_entry_no | if_entry_datatype | 9 | 1 |  |  |  |
| scaleout_timestamp | int | 4 | 1 |  |  |  |
| edit_stream_no | tinyint | 1 | 1 |  |  |  |
