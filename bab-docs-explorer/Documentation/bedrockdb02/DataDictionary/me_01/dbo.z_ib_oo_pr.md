# dbo.z_ib_oo_pr

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| receipt_date | smalldatetime | 4 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| total_on_order_units | int | 4 | 1 |  |  |  |
| total_on_order_cost | decimal | 17 | 1 |  |  |  |
| total_on_order_val_retail | decimal | 17 | 1 |  |  |  |
| total_on_order_selling_retail | decimal | 17 | 1 |  |  |  |
| document_number | varchar | 20 | 0 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |

