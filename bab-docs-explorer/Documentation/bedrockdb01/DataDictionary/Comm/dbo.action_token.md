# dbo.action_token

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | int | 4 | 0 |  |  |  |
| device_id | int | 4 | 0 |  |  |  |
| application_id | int | 4 | 0 |  |  |  |
| session_id | varchar | 50 | 0 |  |  |  |
| expiry_time | datetime | 8 | 0 |  |  |  |
| token_type | int | 4 | 0 |  |  |  |
