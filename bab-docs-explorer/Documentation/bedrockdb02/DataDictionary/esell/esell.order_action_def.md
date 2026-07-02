# esell.order_action_def

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| action_id | nvarchar | 40 | 0 | YES |  |  |
| prop_name | nvarchar | 100 | 0 | YES |  |  |
| prop_desc | nvarchar | 510 | 0 |  |  |  |
| prop_type | nvarchar | 40 | 0 |  |  |  |
| prop_default | nvarchar | 510 | 0 |  |  |  |
| required | nchar | 2 | 0 |  |  |  |
| multivalue | nchar | 2 | 0 |  |  |  |
| modify_allowed | nchar | 2 | 0 |  |  |  |

