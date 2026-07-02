# dbo.dist_sku_grade_alloc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| sku_id | bigint | 8 | 0 | YES |  |  |
| dist_style_color_grd_alloc_id | bigint | 8 | 0 | YES |  |  |
| distributed_quantity | int | 4 | 0 |  |  |  |
| suggested_quantity | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

