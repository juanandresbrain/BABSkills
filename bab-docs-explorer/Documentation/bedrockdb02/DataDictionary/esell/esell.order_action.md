# esell.order_action

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| action_id | nvarchar | 40 | 0 | YES |  |  |
| action_name | nvarchar | 100 | 0 |  |  |  |
| action_desc | nvarchar | 510 | 0 |  |  |  |
| action_classname | nvarchar | 510 | 0 |  |  |  |
| modify_allowed | nchar | 2 | 0 |  |  |  |

