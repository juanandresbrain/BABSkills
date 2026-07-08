# dbo.store

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | int | 4 | 0 |  |  |  |
| comp_id | smallint | 2 | 0 |  |  |  |
| store_id | int | 4 | 0 |  |  |  |
| effective_date | datetime | 8 | 1 |  |  |  |
| end_date | datetime | 8 | 1 |  |  |  |
| merchant_category | nvarchar | 20 | 1 |  |  |  |
| country | nvarchar | 40 | 1 |  |  |  |
| state_province | nvarchar | 40 | 1 |  |  |  |
| county | nvarchar | 40 | 1 |  |  |  |
| city | nvarchar | 50 | 1 |  |  |  |
| mall | nvarchar | 60 | 1 |  |  |  |
| address | nvarchar | 160 | 1 |  |  |  |
| zip | nvarchar | 18 | 1 |  |  |  |
| connection_type | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
