# dbo.transaction_event

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tran_event_id | int | 4 | 0 | YES |  |  |
| location_id | int | 4 | 0 |  |  |  |
| device_id | int | 4 | 0 |  |  |  |
| application_id | int | 4 | 0 |  |  |  |
| route_id | int | 4 | 1 |  |  |  |
| connection_id | int | 4 | 1 |  |  |  |
| tran_type_id | int | 4 | 1 |  |  |  |
| interface_id | int | 4 | 1 |  |  |  |
| tran_event_time | datetime | 8 | 0 |  |  |  |
| request_detail | varbinary | 1024 | 1 |  |  |  |
| reply_detail | varbinary | 1024 | 1 |  |  |  |
