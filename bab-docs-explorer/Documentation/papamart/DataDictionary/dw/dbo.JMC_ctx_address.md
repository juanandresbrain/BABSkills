# dbo.JMC_ctx_address

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| business_unit_id | varchar | 128 | 0 |  |  |  |
| sequence_number | int | 4 | 0 |  |  |  |
| address_type | varchar | 128 | 1 |  |  |  |
| attention | varchar | 128 | 1 |  |  |  |
| line1 | varchar | 128 | 1 |  |  |  |
| line2 | varchar | 128 | 1 |  |  |  |
| line3 | varchar | 128 | 1 |  |  |  |
| line4 | varchar | 128 | 1 |  |  |  |
| city | varchar | 128 | 1 |  |  |  |
| state_id | varchar | 128 | 1 |  |  |  |
| country_id | varchar | 128 | 1 |  |  |  |
| postal_code | varchar | 128 | 1 |  |  |  |
| primary_address_flag | int | 4 | 1 |  |  |  |
| latitude | varchar | 128 | 1 |  |  |  |
| longitude | varchar | 128 | 1 |  |  |  |
| create_time | datetime | 8 | 1 |  |  |  |
| create_by | varchar | 50 | 1 |  |  |  |
| last_update_time | datetime | 8 | 1 |  |  |  |
| last_update_by | varchar | 50 | 1 |  |  |  |
