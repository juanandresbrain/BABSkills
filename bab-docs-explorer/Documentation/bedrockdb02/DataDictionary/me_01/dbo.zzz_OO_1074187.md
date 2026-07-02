# dbo.zzz_OO_1074187

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_on_order_id | decimal | 9 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| receipt_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| on_order_cost | decimal | 9 | 0 |  |  |  |
| on_order_valuation_retail | decimal | 9 | 0 |  |  |  |
| on_order_selling_retail | decimal | 9 | 0 |  |  |  |
| document_number | nvarchar | 40 | 0 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| po_receipt_id | decimal | 9 | 1 |  |  |  |
| actual_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| received_quantity | int | 4 | 1 |  |  |  |
| on_order_cost_local | decimal | 9 | 1 |  |  |  |
| po_id | decimal | 9 | 1 |  |  |  |
| po_shipment_id | smallint | 2 | 1 |  |  |  |

