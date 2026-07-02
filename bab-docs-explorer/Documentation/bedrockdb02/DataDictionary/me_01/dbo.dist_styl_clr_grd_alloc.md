# dbo.dist_styl_clr_grd_alloc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| dist_style_color_grd_alloc_id | bigint | 8 | 0 | YES |  |  |
| style_color_id | decimal | 9 | 0 |  |  |  |
| storepack_definition_id | bigint | 8 | 0 |  |  |  |
| instruction | smallint | 2 | 0 |  |  |  |
| suggested_quantity | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

