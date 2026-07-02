# dbo.imp_po_line_loc_ship_sku

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_po_line_loc_ship_sku_id | decimal | 9 | 0 |  |  |  |
| imp_po_id | decimal | 9 | 0 |  |  |  |
| action_type | nchar | 2 | 1 |  |  |  |
| po_no | nvarchar | 40 | 1 |  |  |  |
| po_line_number | smallint | 2 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| primary_size_label | nvarchar | 16 | 1 |  |  |  |
| secondary_size_label | nvarchar | 16 | 1 |  |  |  |
| cost | decimal | 9 | 1 |  |  |  |
| upc_number | nvarchar | 40 | 1 |  |  |  |
| receiving_location_code | nvarchar | 40 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| po_line_number_shipment_number | int | 4 | 1 |  |  |  |
| balance_to_receive | int | 4 | 1 |  |  |  |
| received_units | int | 4 | 1 |  |  |  |
| shipment_number | nvarchar | 40 | 1 |  |  |  |
| repeat_order_flag | bit | 1 | 0 |  |  |  |
| ap_plan_style_id | decimal | 9 | 1 |  |  |  |
| ap_plan_id | decimal | 9 | 1 |  |  |  |

