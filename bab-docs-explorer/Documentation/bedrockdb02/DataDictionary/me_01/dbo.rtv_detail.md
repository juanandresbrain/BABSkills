# dbo.rtv_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rtv_detail_id | decimal | 9 | 0 | YES |  |  |
| rtv_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| from_stock_status_id | smallint | 2 | 0 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| units_sent | int | 4 | 1 |  |  |  |
| units_requested | int | 4 | 1 |  |  |  |
| unit_cost | decimal | 9 | 1 |  |  |  |
| returned_date | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_rtv_documents_$sp](../../StoredProcedures/me_01/dbo.delete_rtv_documents_$sp.md)

