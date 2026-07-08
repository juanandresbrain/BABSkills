# dbo.awt_error

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | char | 1 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| transl_reject_reason | smallint | 2 | 0 |  |  |  |
| output_file_code | char | 1 | 1 |  |  |  |
| output_file_column | tinyint | 1 | 1 |  |  |  |
| posting_start_date_time | datetime | 8 | 1 |  |  |  |
| posting_end_date_time | datetime | 8 | 0 |  |  |  |
| file_name | varchar | 255 | 1 |  |  |  |
| file_size | int | 4 | 1 |  |  |  |
| transaction_count | int | 4 | 1 |  |  |  |
| bad_data_pos | varchar | 255 | 1 |  |  |  |
| bad_data_output | varchar | 255 | 1 |  |  |  |
| transl_error_msg | varchar | 100 | 1 |  |  |  |
