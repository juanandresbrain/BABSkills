# dbo.imat_item

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_item_id | decimal | 9 | 0 | YES |  |  |
| imat_header_id | decimal | 9 | 0 |  |  |  |
| discount_applicability | smallint | 2 | 0 |  |  |  |
| line_number | int | 4 | 0 |  |  |  |
| units | int | 4 | 0 |  |  |  |
| gross_unit_price | decimal | 9 | 0 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| color_description | nvarchar | 40 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |
| style_description | nvarchar | 240 | 1 |  |  |  |
| style_type | tinyint | 1 | 0 |  |  |  |
| pack_code | nvarchar | 40 | 1 |  |  |  |
| pack_description | nvarchar | 100 | 1 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| tax_amount | decimal | 9 | 0 |  |  |  |

