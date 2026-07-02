# esell.order_action_prop

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| order_type | nvarchar | 40 | 0 | YES |  |  |
| order_event | nvarchar | 40 | 0 | YES |  |  |
| current_state | nvarchar | 40 | 0 | YES |  |  |
| trans_action_type | nvarchar | 40 | 0 | YES |  |  |
| action_seq | decimal | 9 | 0 | YES |  |  |
| action_id | nvarchar | 40 | 0 | YES |  |  |
| prop_name | nvarchar | 100 | 0 | YES |  |  |
| prop_value | nvarchar | 510 | 0 |  |  |  |
| group_id | nvarchar | 40 | 0 | YES |  |  |

