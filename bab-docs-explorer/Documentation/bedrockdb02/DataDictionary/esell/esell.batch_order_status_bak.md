# esell.batch_order_status_bak

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CURRENT_STATE | nvarchar | 40 | 1 |  |  |  |
| ORDER_ID | nvarchar | 60 | 1 |  |  |  |
| ORDER_VALUE | int | 4 | 1 |  |  |  |
| NO_OF_ITEMS | int | 4 | 1 |  |  |  |
| ORDER_DATE | datetime | 8 | 1 |  |  |  |
| DAYS_OPEN | int | 4 | 1 |  |  |  |
| DAYS_SINCE_LAST_ACTION | int | 4 | 1 |  |  |  |
| LAST_ACTION_DATE | datetime | 8 | 1 |  |  |  |
| NUMBER_OF_REROUTE | int | 4 | 1 |  |  |  |
| LAST_REROUTE_DATE | datetime | 8 | 1 |  |  |  |
| METHOD_OF_DELIVERY | nvarchar | 200 | 1 |  |  |  |
| FULFILL_OUTLET_ID | nvarchar | 40 | 1 |  |  |  |
| STATE_ID | int | 4 | 1 |  |  |  |

