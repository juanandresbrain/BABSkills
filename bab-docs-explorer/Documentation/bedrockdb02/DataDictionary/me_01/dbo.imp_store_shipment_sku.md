# dbo.imp_store_shipment_sku

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_store_shipment_sku_id | decimal | 9 | 0 | YES |  |  |
| imp_store_shipment_id | decimal | 9 | 0 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| units_sent | int | 4 | 0 |  |  |  |
| allocation_no | nvarchar | 40 | 0 |  |  |  |
| distribution_no | nvarchar | 40 | 1 |  |  |  |

