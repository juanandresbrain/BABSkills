# dbo.connections

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| connection_id | int | 4 | 0 | YES |  |  |
| connection_name | varchar | 50 | 0 |  |  |  |
| connect_point_a | int | 4 | 0 |  |  |  |
| connect_point_b | int | 4 | 0 |  |  |  |
| transport_type | int | 4 | 0 |  |  |  |
| always_connected | int | 4 | 0 |  |  |  |
| add_info_1 | varchar | 20 | 1 |  |  |  |
| add_info_2 | varchar | 20 | 1 |  |  |  |
| add_info_3 | varchar | 20 | 1 |  |  |  |
| next_seq | int | 4 | 1 |  |  |  |
| server_assigned_id | varchar | 50 | 1 |  |  |  |
| authentication_type | int | 4 | 0 |  |  |  |
| reconnect_interval | int | 4 | 0 |  |  |  |
| auth_ack_timeout | int | 4 | 0 |  |  |  |
| idle_type_a | int | 4 | 0 |  |  |  |
| idle_inactivity_timeout_a | int | 4 | 1 |  |  |  |
| idle_ack_timeout_a | int | 4 | 1 |  |  |  |
| idle_type_b | int | 4 | 0 |  |  |  |
| idle_inactivity_timeout_b | int | 4 | 1 |  |  |  |
| idle_ack_timeout_b | int | 4 | 1 |  |  |  |
| disconnect_timeout | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
