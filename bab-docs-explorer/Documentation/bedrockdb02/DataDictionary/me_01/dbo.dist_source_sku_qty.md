# dbo.dist_source_sku_qty

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 | YES |  |  |
| available_quantity | int | 4 | 0 |  |  |  |
| reserve_quantity | int | 4 | 0 |  |  |  |
| secondary_quantity | int | 4 | 0 |  |  |  |
| line_id | bigint | 8 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

