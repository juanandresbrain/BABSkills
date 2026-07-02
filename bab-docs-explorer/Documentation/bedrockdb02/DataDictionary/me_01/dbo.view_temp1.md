# dbo.view_temp1

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_id | decimal | 9 | 0 |  |  |  |
| po_line_id | int | 4 | 1 |  |  |  |
| line_no | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| location_code | varchar | 20 | 1 |  |  |  |
| location_name | varchar | 60 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| long_desc | varchar | 120 | 1 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| vendor_style | varchar | 40 | 1 |  |  |  |
| pack_code | varchar | 20 | 1 |  |  |  |
| pack_description | varchar | 50 | 1 |  |  |  |
| pack_short_description | varchar | 20 | 1 |  |  |  |
| vendor_pack_code | varchar | 20 | 1 |  |  |  |
| color_code | varchar | 3 | 1 |  |  |  |
| color_long_description | varchar | 20 | 1 |  |  |  |
| color_short_description | varchar | 8 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| first_cost | decimal | 9 | 1 |  |  |  |
| net_final_cost | decimal | 13 | 1 |  |  |  |
| net_cost | decimal | 9 | 1 |  |  |  |
| total_line_loc_pack_ord_units | int | 4 | 1 |  |  |  |
| total_line_loc_ordered_units | decimal | 17 | 1 |  |  |  |
| total_line_loc_received_units | decimal | 17 | 1 |  |  |  |
| total_line_loc_ordered_cost | decimal | 17 | 1 |  |  |  |
| total_line_loc_received_cost | decimal | 17 | 1 |  |  |  |
| total_line_loc_ordered_retail | decimal | 17 | 1 |  |  |  |
| total_line_loc_ord_retail_notx | decimal | 17 | 1 |  |  |  |
| total_line_loc_received_retail | decimal | 17 | 1 |  |  |  |
| total_line_loc_rec_retail_notx | decimal | 17 | 1 |  |  |  |
| entity_type | int | 4 | 0 |  |  |  |

