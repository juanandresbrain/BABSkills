# dbo.connection_point

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| connection_point_id | int | 4 | 0 | YES |  |  |
| location_id | int | 4 | 0 |  |  |  |
| device_id | int | 4 | 0 |  |  |  |
| application_id | int | 4 | 0 |  |  |  |
| ip_address | varchar | 15 | 0 |  |  |  |
| ip_port | int | 4 | 1 |  |  |  |
| channel_type | int | 4 | 0 |  |  |  |
| port_type | int | 4 | 0 |  |  |  |
| authentication_timeout | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
