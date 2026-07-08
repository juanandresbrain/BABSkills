# dbo.connections

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| connection_id | int | 4 | 0 | YES |  |  |
| connection_name | nvarchar | 100 | 0 |  |  |  |
| connect_point_a | int | 4 | 0 |  |  |  |
| connect_point_b | int | 4 | 0 |  |  |  |
| transport_type | int | 4 | 0 |  |  |  |
| always_connected | int | 4 | 0 |  |  |  |
| add_info_1 | nvarchar | 40 | 1 |  |  |  |
| add_info_2 | nvarchar | 40 | 1 |  |  |  |
| add_info_3 | nvarchar | 40 | 1 |  |  |  |
| next_seq | int | 4 | 1 |  |  |  |
| server_assigned_id | nvarchar | 100 | 1 |  |  |  |
| reconnect_interval | int | 4 | 0 |  |  |  |
| auth_ack_timeout | int | 4 | 0 |  |  |  |
| idle_inactivity_timeout_a | int | 4 | 1 |  |  |  |
| idle_ack_timeout_a | int | 4 | 1 |  |  |  |
| idle_inactivity_timeout_b | int | 4 | 1 |  |  |  |
| idle_ack_timeout_b | int | 4 | 1 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| ADMN_TRNSCTN_TYPE_ID | int | 4 | 0 |  |  |  |
| ADMN_INTRFC_ID | int | 4 | 0 |  |  |  |
| ENBL_IDLE_A | int | 4 | 0 |  |  |  |
| ENBL_IDLE_B | int | 4 | 0 |  |  |  |
| ENBL_ATHNTCTN | int | 4 | 0 |  |  |  |
