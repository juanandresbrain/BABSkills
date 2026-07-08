# dbo.import_error_log

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_no | smallint | 2 | 0 |  |  |  |
| error_code | int | 4 | 0 |  |  |  |
| error_timestamp | datetime | 8 | 0 |  |  |  |
| process_id | binary | 16 | 0 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| verified_by | nvarchar | 50 | 1 |  |  |  |
| support_call_reference_no | int | 4 | 1 |  |  |  |
| error_msg | nvarchar | 510 | 1 |  |  |  |
| user_name | nvarchar | 100 | 1 |  |  |  |
| memo1 | nvarchar | 100 | 1 |  |  |  |
| memo2 | nvarchar | 100 | 1 |  |  |  |
| memo3 | nvarchar | 100 | 1 |  |  |  |
| memo_date | smalldatetime | 4 | 1 |  |  |  |
| support_call_id | nvarchar | 60 | 1 |  |  |  |
| memo_date2 | smalldatetime | 4 | 1 |  |  |  |
| memo_date3 | smalldatetime | 4 | 1 |  |  |  |
| process_name | nvarchar | 200 | 1 |  |  |  |
| object_name | nvarchar | 510 | 1 |  |  |  |
| operation_name | nvarchar | 200 | 1 |  |  |  |
| message_id | int | 4 | 1 |  |  |  |
| entry_id | numeric | 9 | 0 |  |  |  |
| stream_no | tinyint | 1 | 1 |  |  |  |
