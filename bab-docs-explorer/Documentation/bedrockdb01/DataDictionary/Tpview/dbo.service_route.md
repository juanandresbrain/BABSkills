# dbo.service_route

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| route_id | int | 4 | 0 | YES |  |  |
| tran_type_id | int | 4 | 0 |  |  |  |
| src_location_id | int | 4 | 0 |  |  |  |
| src_device_id | int | 4 | 0 |  |  |  |
| src_application_id | int | 4 | 0 |  |  |  |
| dest_location_id | int | 4 | 0 |  |  |  |
| dest_device_id | int | 4 | 0 |  |  |  |
| dest_application_id | int | 4 | 0 |  |  |  |
| service_seq | int | 4 | 0 |  |  |  |
| test_action | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
