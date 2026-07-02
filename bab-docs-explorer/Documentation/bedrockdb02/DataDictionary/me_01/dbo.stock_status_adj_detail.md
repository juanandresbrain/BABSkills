# dbo.stock_status_adj_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| stock_status_adj_detail_id | decimal | 9 | 0 | YES |  |  |
| stock_status_adjustment_id | decimal | 9 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| from_stock_status_id | smallint | 2 | 0 |  |  |  |
| to_stock_status_id | smallint | 2 | 0 |  |  |  |
| units_to_adjust | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_ss_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_ss_adj_documents_$sp.md)

