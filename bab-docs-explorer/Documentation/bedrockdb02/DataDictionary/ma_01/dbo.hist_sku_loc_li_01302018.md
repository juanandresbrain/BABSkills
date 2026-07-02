# dbo.hist_sku_loc_li_01302018

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| size_master_id | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| received_units | int | 4 | 0 |  |  |  |
| return_to_vendor_units | int | 4 | 0 |  |  |  |
| distributions_units | int | 4 | 0 |  |  |  |
| transfer_in_units | int | 4 | 0 |  |  |  |
| transfer_out_units | int | 4 | 0 |  |  |  |
| sales_total_units | int | 4 | 0 |  |  |  |
| return_units | int | 4 | 0 |  |  |  |
| shrink_actual_units | int | 4 | 0 |  |  |  |
| adjustments_total_units | int | 4 | 0 |  |  |  |
| shipped_units | int | 4 | 1 |  |  |  |

