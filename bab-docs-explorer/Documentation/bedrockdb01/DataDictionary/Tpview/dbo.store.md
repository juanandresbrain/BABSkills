# dbo.store

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | int | 4 | 0 |  |  |  |
| comp_id | smallint | 2 | 0 |  |  |  |
| store_id | int | 4 | 0 |  |  |  |
| effective_date | datetime | 8 | 1 |  |  |  |
| end_date | datetime | 8 | 1 |  |  |  |
| merchant_category | varchar | 10 | 1 |  |  |  |
| country | varchar | 20 | 1 |  |  |  |
| state_province | varchar | 20 | 1 |  |  |  |
| county | varchar | 20 | 1 |  |  |  |
| city | varchar | 25 | 1 |  |  |  |
| mall | varchar | 30 | 1 |  |  |  |
| address | varchar | 80 | 1 |  |  |  |
| zip | varchar | 9 | 1 |  |  |  |
| connection_type | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
