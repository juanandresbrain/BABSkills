# dbo.dw_move_request_queue

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| user_id | int | 4 | 1 |  |  |  |
| request_id | numeric | 9 | 0 | YES |  |  |
| from_store_no | int | 4 | 0 |  |  |  |
| from_transaction_date | smalldatetime | 4 | 1 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| to_store_no | int | 4 | 0 |  |  |  |
| to_transaction_date | smalldatetime | 4 | 1 |  |  |  |
| request_date | datetime | 8 | 0 |  |  |  |
| from_instance_id | smallint | 2 | 0 |  |  |  |
| to_instance_id | smallint | 2 | 0 |  |  |  |
| move_status | smallint | 2 | 0 |  |  |  |
| last_processed_date | datetime | 8 | 1 |  |  |  |
| all_trans_flag | tinyint | 1 | 0 |  |  |  |
| cancellation_requested | tinyint | 1 | 1 |  |  |  |
| parent_request_id | numeric | 9 | 1 |  |  |  |
| move_started | datetime | 8 | 1 |  |  |  |
| move_ended | datetime | 8 | 1 |  |  |  |
| cancel_user_id | int | 4 | 1 |  |  |  |
