# esell.outlet_query_log

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RETAILER_ID | int | 4 | 0 | YES |  |  |
| GROUP_ID | nvarchar | 40 | 0 | YES |  |  |
| OUTLET_ID | nvarchar | 40 | 0 | YES |  |  |
| REQUEST_ID | nvarchar | 96 | 0 | YES |  |  |
| SKU_ID | nvarchar | 48 | 0 | YES |  |  |
| REQUEST_TYPE_ID | nvarchar | 40 | 1 |  |  |  |
| QUERY_COMPLETION_DATE | datetime | 8 | 1 |  |  |  |
| SKU_QTY_REQUESTED | int | 4 | 1 |  |  |  |
| SKU_QTY_FOUND | int | 4 | 1 |  |  |  |

