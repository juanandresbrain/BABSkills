# dbo.im_attribute

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| im_attribute_id | decimal | 9 | 0 | YES |  |  |
| attribute_set_id | decimal | 9 | 0 |  |  |  |
| attribute_id | decimal | 9 | 0 |  |  |  |
| parent_id | decimal | 9 | 0 |  |  |  |
| parent_type | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)
- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.delete_rtv_documents_$sp](../../StoredProcedures/me_01/dbo.delete_rtv_documents_$sp.md)
- [me_01: dbo.delete_transfer_documents_$sp](../../StoredProcedures/me_01/dbo.delete_transfer_documents_$sp.md)
- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)

