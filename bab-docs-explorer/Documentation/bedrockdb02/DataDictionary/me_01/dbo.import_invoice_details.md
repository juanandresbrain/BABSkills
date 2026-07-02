# dbo.import_invoice_details

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_invoice_details_id | decimal | 9 | 0 | YES |  |  |
| import_invoice_header_id | decimal | 9 | 0 |  |  |  |
| action_code | nchar | 2 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| color_long_description | nvarchar | 40 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |
| units | int | 4 | 0 |  |  |  |
| gross_price | decimal | 9 | 1 |  |  |  |
| net_price | decimal | 9 | 1 |  |  |  |
| invoice_no | nvarchar | 44 | 0 |  |  |  |
| style_type | tinyint | 1 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| pack_code | nvarchar | 40 | 1 |  |  |  |

