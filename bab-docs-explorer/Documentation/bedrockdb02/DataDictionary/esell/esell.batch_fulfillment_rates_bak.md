# esell.batch_fulfillment_rates_bak

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RETAILER_ID | int | 4 | 1 |  |  |  |
| FULFILL_OUTLET_ID | nvarchar | 40 | 1 |  |  |  |
| ORDERS_CREATED | int | 4 | 1 |  |  |  |
| ORD_FULLFILLED_0DAYS | int | 4 | 1 |  |  |  |
| ORD_FULLFILLED_2DAYS | int | 4 | 1 |  |  |  |
| ORD_FULLFILLED_3DAYS | int | 4 | 1 |  |  |  |
| ORD_FULLFILLED_4TO7DAYS | int | 4 | 1 |  |  |  |
| ORD_FULLFILLED_8ONWARDSDAYS | int | 4 | 1 |  |  |  |
| FULFILL_CREATE_TIMESTAMP | datetime | 8 | 1 |  |  |  |

