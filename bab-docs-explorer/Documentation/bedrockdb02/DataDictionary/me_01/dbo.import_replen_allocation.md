# dbo.import_replen_allocation

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_replen_allocation_id | decimal | 9 | 0 | YES |  |  |
| upc_number | decimal | 9 | 1 |  |  |  |
| quantity | decimal | 5 | 1 |  |  |  |
| from_store_number | smallint | 2 | 1 |  |  |  |
| to_store_number | smallint | 2 | 1 |  |  |  |
| from_location_id | smallint | 2 | 1 |  |  |  |
| to_location_id | smallint | 2 | 1 |  |  |  |
| purchase_order_number | nvarchar | 40 | 1 |  |  |  |
| po_line_number | smallint | 2 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| nrf_size_code | nvarchar | 10 | 1 |  |  |  |
| class_code | nvarchar | 6 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_description | nvarchar | 48 | 1 |  |  |  |
| replenish_flag | bit | 1 | 1 |  |  |  |
| po_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| size_method | nvarchar | 16 | 1 |  |  |  |
| department_number | nvarchar | 6 | 1 |  |  |  |
| current_retail | decimal | 9 | 1 |  |  |  |
| number_of_dimensions | tinyint | 1 | 1 |  |  |  |

