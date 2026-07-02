# dbo.imp_invoice_detail_tax

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_invoice_detail_tax_id | decimal | 9 | 0 | YES |  |  |
| import_invoice_header_id | decimal | 9 | 0 |  |  |  |
| import_invoice_details_id | decimal | 9 | 0 |  |  |  |
| action_code | nvarchar | 2 | 0 |  |  |  |
| invoice_no | nvarchar | 44 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| pack_code | nvarchar | 40 | 1 |  |  |  |
| color_long_description | nvarchar | 40 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |
| tax_type_code | nvarchar | 10 | 0 |  |  |  |
| tax_rate_code | nvarchar | 12 | 0 |  |  |  |

