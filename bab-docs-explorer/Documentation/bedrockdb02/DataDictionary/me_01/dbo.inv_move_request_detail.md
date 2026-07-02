# dbo.inv_move_request_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inv_move_request_detail_id | decimal | 9 | 0 | YES |  |  |
| inventory_move_request_id | decimal | 9 | 0 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| units_requested | int | 4 | 1 |  |  |  |
| comparison_operator | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)

