# dbo.sales_import_error

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| error_id | smallint | 2 | 0 |  |  |  |
| identity_no | decimal | 13 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| transaction_line | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| register | smallint | 2 | 1 |  |  |  |
| reference_no | nvarchar | 40 | 1 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| vendor_code | nvarchar | 40 | 1 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |
| is_price_override | bit | 1 | 0 |  |  |  |
| units | int | 4 | 0 |  |  |  |
| sold_at_price | decimal | 9 | 0 |  |  |  |
| pos_discount_type_code | smallint | 2 | 1 |  |  |  |
| pos_discount_amount | decimal | 9 | 1 |  |  |  |
| originating_location_code | nvarchar | 40 | 1 |  |  |  |
| credit_originating_store | bit | 1 | 0 |  |  |  |
| is_markup | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)

