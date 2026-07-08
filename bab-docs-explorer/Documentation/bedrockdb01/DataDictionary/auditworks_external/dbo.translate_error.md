# dbo.translate_error

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| translate_error_id | numeric | 9 | 0 | YES |  |  |
| transl_reject_reason | smallint | 2 | 0 |  |  |  |
| posting_start_date_time | smalldatetime | 4 | 1 |  |  |  |
| posting_end_date_time | smalldatetime | 4 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| output_file_code | nchar | 2 | 1 |  |  |  |
| output_file_column | tinyint | 1 | 1 |  |  |  |
| file_name | nvarchar | 510 | 1 |  |  |  |
| file_size | int | 4 | 1 |  |  |  |
| transaction_count | int | 4 | 1 |  |  |  |
| bad_data_pos | nvarchar | 510 | 1 |  |  |  |
| bad_data_output | nvarchar | 510 | 1 |  |  |  |
| transl_error_msg | nvarchar | 200 | 1 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| support_call_reference_no | int | 4 | 1 |  |  |  |
| verification_remark | nvarchar | 510 | 1 |  |  |  |
| support_call_id | nvarchar | 60 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
| verified_date | smalldatetime | 4 | 1 |  |  |  |
| verified_by_user_id | int | 4 | 1 |  |  |  |
| override_flag | tinyint | 1 | 1 |  |  |  |
