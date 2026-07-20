# dbo.me_01_view_po_line_wl

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_id | decimal | 9 | 1 |  |  |  |
| po_line_id | int | 4 | 1 |  |  |  |
| line_no | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_code | varchar | 8000 | 1 |  |  |  |
| long_desc | varchar | 8000 | 1 |  |  |  |
| short_desc | varchar | 8000 | 1 |  |  |  |
| vendor_style | varchar | 8000 | 1 |  |  |  |
| pack_code | varchar | 8000 | 1 |  |  |  |
| pack_description | varchar | 8000 | 1 |  |  |  |
| pack_short_description | varchar | 8000 | 1 |  |  |  |
| vendor_pack_code | varchar | 8000 | 1 |  |  |  |
| color_code | varchar | 8000 | 1 |  |  |  |
| color_long_description | varchar | 8000 | 1 |  |  |  |
| color_short_description | varchar | 8000 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| hierarchy_group_code | varchar | 8000 | 1 |  |  |  |
| hierarchy_group_short_label | varchar | 8000 | 1 |  |  |  |
| hierarchy_group_label | varchar | 8000 | 1 |  |  |  |
| total_line_first_cost | decimal | 13 | 1 |  |  |  |
| total_line_net_cost | decimal | 13 | 1 |  |  |  |
| total_line_net_final_cost | decimal | 17 | 1 |  |  |  |
| total_ordered_retail | float | 8 | 1 |  |  |  |
| repeat_order_flag | bit | 1 | 1 |  |  |  |
| store_pack_flag | bit | 1 | 1 |  |  |  |
| total_units | int | 4 | 1 |  |  |  |
| total_pack_units | int | 4 | 1 |  |  |  |
