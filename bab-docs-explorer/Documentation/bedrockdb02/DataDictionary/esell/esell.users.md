# esell.users

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| user_id | numeric | 5 | 0 | YES |  |  |
| first_name | nvarchar | 60 | 0 |  |  |  |
| last_name | nvarchar | 80 | 0 |  |  |  |
| logon_id | nvarchar | 96 | 0 |  |  |  |
| password | nvarchar | 256 | 1 |  |  |  |
| status_code | nchar | 2 | 1 |  |  |  |
| user_type | int | 4 | 1 |  |  |  |
| last_logon_date | datetime | 8 | 1 |  |  |  |
| rec_update_date | datetime | 8 | 0 |  |  |  |
| rec_create_date | datetime | 8 | 0 |  |  |  |
| rec_update_id | int | 4 | 0 |  |  |  |

