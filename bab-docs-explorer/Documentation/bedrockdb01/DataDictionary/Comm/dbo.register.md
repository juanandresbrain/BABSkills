# dbo.register

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | int | 4 | 0 |  |  |  |
| register_id | int | 4 | 0 |  |  |  |
| effective_date | datetime | 8 | 1 |  |  |  |
| end_date | datetime | 8 | 1 |  |  |  |
| ip_address | varchar | 15 | 0 |  |  |  |
| version_id | int | 4 | 0 |  |  |  |
| computer_name | nvarchar | 100 | 0 |  |  |  |
| is_a_server | int | 4 | 0 |  |  |  |
| setup_type | nvarchar | 100 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
