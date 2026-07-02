# dbo.imp_pack_sku

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_pack_sku_id | decimal | 9 | 0 | YES |  |  |
| imp_pack_id | decimal | 9 | 0 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| sku_quantity | smallint | 2 | 0 |  |  |  |

