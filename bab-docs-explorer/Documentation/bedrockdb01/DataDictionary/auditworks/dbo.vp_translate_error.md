# dbo.vp_translate_error

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| translate_error_id | numeric | 9 | 0 |  |  |  |
| transl_reject_reason | smallint | 2 | 0 |  |  |  |
| posting_start_date_time | smalldatetime | 4 | 1 |  |  |  |
| posting_end_date_time | smalldatetime | 4 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| transaction_series | char | 1 | 0 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| output_file_code | char | 1 | 1 |  |  |  |
| output_file_column | tinyint | 1 | 1 |  |  |  |
| file_name | varchar | 255 | 1 |  |  |  |
| file_size | int | 4 | 1 |  |  |  |
| transaction_count | int | 4 | 1 |  |  |  |
| bad_data_pos | varchar | 255 | 1 |  |  |  |
| bad_data_output | varchar | 255 | 1 |  |  |  |
| transl_error_msg | varchar | 100 | 1 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| verified_by | varchar | 25 | 1 |  |  |  |
| support_call_reference_no | int | 4 | 1 |  |  |  |
| verification_remark | varchar | 255 | 1 |  |  |  |
| support_call_id | varchar | 30 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| transaction_id | numeric | 9 | 1 |  |  |  |
