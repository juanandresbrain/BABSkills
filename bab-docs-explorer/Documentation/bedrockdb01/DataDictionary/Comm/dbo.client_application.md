# dbo.client_application

**Database:** Comm  
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
| merchant_id_1 | nvarchar | 32 | 0 |  |  |  |
| merchant_id_2 | nvarchar | 32 | 0 |  |  |  |
| merchant_id_3 | nvarchar | 32 | 0 |  |  |  |
| merchant_id_4 | nvarchar | 32 | 0 |  |  |  |
| merchant_id_5 | nvarchar | 32 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
