# dbo.z_pcs_on_order_temp

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_number | varchar | 20 | 0 |  |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| total_ordered_units | int | 4 | 1 |  |  |  |
| on_order_units | int | 4 | 1 |  |  |  |

