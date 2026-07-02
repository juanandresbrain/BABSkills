# dbo.imp_out_xfer_sku

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_out_xfer_sku_id | decimal | 9 | 0 | YES |  |  |
| imp_out_xfer_id | decimal | 9 | 1 |  |  |  |
| action | nchar | 2 | 0 |  |  |  |
| xfer_no | nvarchar | 40 | 0 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| primary_size_label | nvarchar | 16 | 1 |  |  |  |
| secondary_size_label | nvarchar | 16 | 1 |  |  |  |
| reason_code | nvarchar | 10 | 1 |  |  |  |
| units_sent | int | 4 | 0 |  |  |  |

