# esell.batch_sku_demand

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SKU_ID | nvarchar | 48 | 1 |  |  |  |
| DESCRIPTION | nvarchar | 510 | 1 |  |  |  |
| OUTLETID | nvarchar | 48 | 1 |  |  |  |
| NOQUERIES | int | 4 | 1 |  |  |  |
| NOSKUQTY | int | 4 | 1 |  |  |  |
| NOSKUFOUND | int | 4 | 1 |  |  |  |
| NOSKUNOTLOCATED | int | 4 | 1 |  |  |  |
| QTYORDERED | int | 4 | 1 |  |  |  |
| QUERY_COMPLETION_DATE | datetime | 8 | 1 |  |  |  |

