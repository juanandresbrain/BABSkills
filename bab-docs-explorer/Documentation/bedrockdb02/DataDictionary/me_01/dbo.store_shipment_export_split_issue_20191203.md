# dbo.store_shipment_export_split_issue_20191203

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_number | varchar | 20 | 1 |  |  |  |
| document_number | varchar | 20 | 1 |  |  |  |
| distribution_line_number | int | 4 | 1 |  |  |  |
| warehouse | varchar | 4 | 1 |  |  |  |
| location_code | varchar | 6 | 1 |  |  |  |
| rec_type | varchar | 10 | 1 |  |  |  |
| rec_label | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| release_date | smalldatetime | 4 | 1 |  |  |  |
| short_desc | varchar | 100 | 1 |  |  |  |
| vendor_style | varchar | 52 | 1 |  |  |  |
| color_code | varchar | 3 | 1 |  |  |  |
| exported | int | 4 | 1 |  |  |  |
| expected_ship_date | date | 3 | 1 |  |  |  |
| Cancelled | int | 4 | 1 |  |  |  |

