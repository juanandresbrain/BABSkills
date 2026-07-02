# dbo.deleted_sku

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 0 |  |  |  |
| style_size_id | decimal | 9 | 0 |  |  |  |
| deleted_date | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.plu_deleted_item_queue_$sp](../../StoredProcedures/me_01/dbo.plu_deleted_item_queue_$sp.md)

