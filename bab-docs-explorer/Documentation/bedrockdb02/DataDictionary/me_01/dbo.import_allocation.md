# dbo.import_allocation

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_allocation_id | decimal | 9 | 0 | YES |  |  |
| action_code | nchar | 2 | 0 |  |  |  |
| distribution_code | nvarchar | 20 | 0 |  |  |  |
| multi_distribution_code | nvarchar | 20 | 1 |  |  |  |
| warehouse_code | nvarchar | 40 | 1 |  |  |  |
| distribution_type | nchar | 2 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| rm | nvarchar | 40 | 1 |  |  |  |
| purchase_order_number | nvarchar | 40 | 1 |  |  |  |
| po_line | decimal | 5 | 1 |  |  |  |
| size_method_code | nvarchar | 16 | 1 |  |  |  |
| pack_code | decimal | 9 | 1 |  |  |  |
| pack_name | nvarchar | 40 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| size_code | nvarchar | 16 | 1 |  |  |  |
| nrf_size_code | nvarchar | 10 | 1 |  |  |  |
| dimension_code | nvarchar | 16 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| store_number | nvarchar | 40 | 1 |  |  |  |
| quantity | decimal | 5 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| old_expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |

