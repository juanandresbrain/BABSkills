# dbo.zzz_rem_cost

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| transaction_units | int | 4 | 1 |  |  |  |
| transaction_cost | decimal | 17 | 1 |  |  |  |
| transaction_valuation_retail | decimal | 17 | 1 |  |  |  |
| transaction_selling_retail | decimal | 17 | 1 |  |  |  |
| transaction_cost_local | decimal | 17 | 1 |  |  |  |

