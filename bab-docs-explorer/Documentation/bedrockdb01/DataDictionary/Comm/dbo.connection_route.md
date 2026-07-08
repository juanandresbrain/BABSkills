# dbo.connection_route

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| route_id | int | 4 | 0 |  |  |  |
| connection_id | int | 4 | 0 |  |  |  |
| tran_type_id | int | 4 | 0 |  |  |  |
| interface_id | int | 4 | 0 |  |  |  |
| reverse_on_write_err | int | 4 | 0 |  |  |  |
| reverse_on_seq_num | int | 4 | 0 |  |  |  |
| reverse_on_read_to | int | 4 | 0 |  |  |  |
| reverse_allowed | int | 4 | 0 |  |  |  |
| reverse_on_same_conn | int | 4 | 0 |  |  |  |
| reverse_on_reply_ack_to | int | 4 | 0 |  |  |  |
| reverse_retry | int | 4 | 0 |  |  |  |
| reverse_retry_interval | int | 4 | 0 |  |  |  |
| disconnect_on_reverse_to | int | 4 | 0 |  |  |  |
| dyn_tout_travel | int | 4 | 0 |  |  |  |
| dyn_tout_min | int | 4 | 0 |  |  |  |
| static_tout | int | 4 | 0 |  |  |  |
| route_usage | int | 4 | 0 |  |  |  |
| reply_ack_timeout | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
