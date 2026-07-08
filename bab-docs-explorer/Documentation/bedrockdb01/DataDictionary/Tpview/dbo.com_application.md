# dbo.com_application

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | int | 4 | 0 |  |  |  |
| device_id | int | 4 | 0 |  |  |  |
| application_id | int | 4 | 0 |  |  |  |
| register_id | int | 4 | 1 |  |  |  |
| application_type_id | int | 4 | 0 |  |  |  |
| add_info_1 | varchar | 20 | 1 |  |  |  |
| add_info_2 | varchar | 20 | 1 |  |  |  |
| add_info_3 | varchar | 20 | 1 |  |  |  |
| server_assigned_id | varchar | 50 | 1 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
