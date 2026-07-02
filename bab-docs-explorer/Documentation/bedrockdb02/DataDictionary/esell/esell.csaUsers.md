# esell.csaUsers

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES | YES |  |
| id | nvarchar | 100 | 0 | YES |  |  |
| first_name | nvarchar | 100 | 0 |  |  |  |
| last_name | nvarchar | 100 | 0 |  |  |  |
| email | nvarchar | 100 | 1 |  |  |  |
| password | nvarchar | 1024 | 0 |  |  |  |
| default_group_id | nvarchar | 40 | 1 |  | YES |  |

