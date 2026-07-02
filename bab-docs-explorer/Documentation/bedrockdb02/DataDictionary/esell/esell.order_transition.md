# esell.order_transition

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| retailer_id | int | 4 | 0 | YES |  |  |
| order_type | nvarchar | 40 | 0 | YES |  |  |
| order_event | nvarchar | 40 | 0 | YES |  |  |
| current_state | nvarchar | 40 | 0 | YES |  |  |
| next_state | nvarchar | 40 | 0 |  |  |  |
| transition_desc | nvarchar | 510 | 0 |  |  |  |
| modify_allowed | nchar | 2 | 0 |  |  |  |

