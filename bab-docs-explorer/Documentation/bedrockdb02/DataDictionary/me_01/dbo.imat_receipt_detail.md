# dbo.imat_receipt_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_receipt_detail_id | decimal | 9 | 0 | YES |  |  |
| imat_receipt_id | int | 4 | 0 |  |  |  |
| receipt_detail_id | decimal | 9 | 0 |  |  |  |
| units_received | int | 4 | 0 |  |  |  |
| gross_unit_price | decimal | 9 | 0 |  |  |  |
| net_unit_price | decimal | 9 | 0 |  |  |  |
| units_matched | int | 4 | 0 |  |  |  |
| units_damaged | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)
- [me_01: dbo.import_asn_sixth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_sixth_step_$sp.md)

