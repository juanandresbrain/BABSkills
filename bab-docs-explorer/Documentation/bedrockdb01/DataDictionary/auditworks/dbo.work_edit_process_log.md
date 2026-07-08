# dbo.work_edit_process_log

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| stream_no | int | 4 | 0 |  |  |  |
| process_no | int | 4 | 0 |  |  |  |
| start_time | datetime | 8 | 0 |  |  |  |
| end_time | datetime | 8 | 0 |  |  |  |
| duration | numeric | 9 | 0 |  |  |  |
| transaction_count | int | 4 | 0 |  |  |  |
| session_id | int | 4 | 0 |  |  |  |
| status | int | 4 | 0 |  |  |  |
