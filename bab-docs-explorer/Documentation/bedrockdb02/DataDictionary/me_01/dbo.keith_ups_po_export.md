# dbo.keith_ups_po_export

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_no | varchar | 20 | 0 |  |  |  |
| vendor_name | varchar | 50 | 0 |  |  |  |
| vendor_code | varchar | 20 | 0 |  |  |  |
| location_code | varchar | 20 | 1 |  |  |  |
| fob_description | varchar | 20 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| position_code | varchar | 20 | 0 |  |  |  |
| line_no | decimal | 9 | 1 |  |  |  |
| vendor_style | varchar | 40 | 1 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| long_desc | varchar | 120 | 1 |  |  |  |
| long_desc_2 | varchar | 120 | 1 |  |  |  |
| dept | varchar | 8 | 1 |  |  |  |
| color_code | varchar | 3 | 1 |  |  |  |
| color_short_description | varchar | 8 | 1 |  |  |  |
| upc_number | varchar | 14 | 1 |  |  |  |
| ordered_units_2 | decimal | 17 | 1 |  |  |  |
| first_cost | decimal | 9 | 1 |  |  |  |
| ordered_units | decimal | 17 | 1 |  |  |  |
| current_selling_retail_US | decimal | 9 | 1 |  |  |  |
| current_selling_retail_UK | decimal | 9 | 1 |  |  |  |
| current_selling_retail_EU | decimal | 9 | 1 |  |  |  |
| current_selling_retail_CA | decimal | 9 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| user_defined_date | smalldatetime | 4 | 1 |  |  |  |
| user_defined_date_2 | smalldatetime | 4 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| HTS Code | varchar | 30 | 0 |  |  |  |
| Factory Name | varchar | 30 | 0 |  |  |  |
| Factory Port | nvarchar | 510 | 0 |  |  |  |
| Factory Address | nvarchar | 510 | 0 |  |  |  |
| Factory City | nvarchar | 510 | 0 |  |  |  |
| Factory Province | nvarchar | 510 | 0 |  |  |  |
| Factory Country | nvarchar | 510 | 0 |  |  |  |
| Factory Phone Number | nvarchar | 510 | 0 |  |  |  |
| Factory Container Stuffing | nvarchar | 510 | 0 |  |  |  |

