# dbo.process_error_log_bk

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_no | smallint | 2 | 0 |  |  |  |
| error_code | int | 4 | 0 |  |  |  |
| error_timestamp | datetime | 8 | 0 |  |  |  |
| process_id | int | 4 | 0 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| verified_by | varchar | 25 | 1 |  |  |  |
| support_call_reference_no | int | 4 | 1 |  |  |  |
| error_msg | varchar | 255 | 1 |  |  |  |
| user_name | varchar | 25 | 1 |  |  |  |
| memo1 | varchar | 50 | 1 |  |  |  |
| memo2 | varchar | 50 | 1 |  |  |  |
| memo3 | varchar | 50 | 1 |  |  |  |
| memo_date | smalldatetime | 4 | 1 |  |  |  |
| support_call_id | varchar | 30 | 1 |  |  |  |
| memo_date2 | smalldatetime | 4 | 1 |  |  |  |
| memo_date3 | smalldatetime | 4 | 1 |  |  |  |
| process_name | varchar | 100 | 1 |  |  |  |
| object_name | varchar | 255 | 1 |  |  |  |
| operation_name | varchar | 100 | 1 |  |  |  |
| message_id | int | 4 | 1 |  |  |  |
| entry_id | numeric | 9 | 0 | YES |  |  |
| stream_no | tinyint | 1 | 1 |  |  |  |
