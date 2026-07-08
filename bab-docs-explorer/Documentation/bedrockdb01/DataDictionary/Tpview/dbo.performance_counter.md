# dbo.performance_counter

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| start_time | datetime | 8 | 0 |  |  |  |
| log_time | datetime | 8 | 0 |  |  |  |
| transaction_count | int | 4 | 1 |  |  |  |
| average_response | decimal | 9 | 1 |  |  |  |
| total_with_no_route | int | 4 | 1 |  |  |  |
| total_service_down | int | 4 | 1 |  |  |  |
| total_service_timeout | int | 4 | 1 |  |  |  |
| total_connection | int | 4 | 1 |  |  |  |
| total_disconnection | int | 4 | 1 |  |  |  |
| total_unknown_message | int | 4 | 1 |  |  |  |
