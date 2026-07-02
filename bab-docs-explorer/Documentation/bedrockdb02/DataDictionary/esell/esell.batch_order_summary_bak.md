# esell.batch_order_summary_bak

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RETAILER_ID | int | 4 | 1 |  |  |  |
| OUTLET_ID | nvarchar | 60 | 1 |  |  |  |
| ORDERS_FULFILLED | int | 4 | 1 |  |  |  |
| ORDERS_OPEN | int | 4 | 1 |  |  |  |
| ORDERS_CANCELLED | int | 4 | 1 |  |  |  |
| ORDERS_FULFILLED_SALES_VALUE | int | 4 | 1 |  |  |  |
| ORDERS_OPEN_SALES_VALUE | int | 4 | 1 |  |  |  |
| ORDERS_CANCELLED_SALES_VALUE | int | 4 | 1 |  |  |  |
| ORDERS_FULFILLED_TOTAL_ITEM | int | 4 | 1 |  |  |  |
| COUNT_UNIQUE_OUTLET | int | 4 | 1 |  |  |  |
| ORDER_DATE | datetime | 8 | 1 |  |  |  |

