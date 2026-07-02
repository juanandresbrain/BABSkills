# dbo.CUST_ORDER_ACTIONS

**Database:** EJ  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| STORENO | int | 4 | 0 | YES |  |  |
| TILLNO | smallint | 2 | 0 | YES |  |  |
| TRANNO | int | 4 | 0 | YES |  |  |
| DATETIME | datetime | 8 | 0 | YES |  |  |
| SEQNO | smallint | 2 | 0 | YES |  |  |
| CUSTOMER_ORDER_NO | nvarchar | 40 | 1 |  |  |  |
| CUST_ORD_TYPE_CODE | nvarchar | 20 | 1 |  |  |  |
| CUST_ORD_ACTION_CODE | nvarchar | 20 | 1 |  |  |  |

