# dbo.client_application

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tran_type_id | int | 4 | 0 |  |  |  |
| location_id | int | 4 | 0 |  |  |  |
| device_id | int | 4 | 0 |  |  |  |
| application_id | int | 4 | 0 |  |  |  |
| effective_date | datetime | 8 | 1 |  |  |  |
| end_date | datetime | 8 | 1 |  |  |  |
| merchant_id_1 | varchar | 16 | 0 |  |  |  |
| merchant_id_2 | varchar | 16 | 0 |  |  |  |
| merchant_id_3 | varchar | 16 | 0 |  |  |  |
| merchant_id_4 | varchar | 16 | 0 |  |  |  |
| merchant_id_5 | varchar | 16 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
