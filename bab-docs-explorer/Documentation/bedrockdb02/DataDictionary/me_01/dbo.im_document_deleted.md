# dbo.im_document_deleted

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| im_document_id | decimal | 9 | 0 | YES |  |  |
| im_document_no | nvarchar | 40 | 0 |  |  |  |
| document_type | tinyint | 1 | 0 | YES |  |  |
| document_status | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_asn_documents_$sp](../../StoredProcedures/me_01/dbo.delete_asn_documents_$sp.md)
- [me_01: dbo.delete_avg_cost_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_avg_cost_adj_documents_$sp.md)
- [me_01: dbo.delete_im_documents_$sp](../../StoredProcedures/me_01/dbo.delete_im_documents_$sp.md)
- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)
- [me_01: dbo.delete_inv_control_documents_$sp](../../StoredProcedures/me_01/dbo.delete_inv_control_documents_$sp.md)
- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.delete_rtv_documents_$sp](../../StoredProcedures/me_01/dbo.delete_rtv_documents_$sp.md)
- [me_01: dbo.delete_shrink_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_shrink_adj_documents_$sp.md)
- [me_01: dbo.delete_ss_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_ss_adj_documents_$sp.md)
- [me_01: dbo.delete_store_shipment_documents_$sp](../../StoredProcedures/me_01/dbo.delete_store_shipment_documents_$sp.md)
- [me_01: dbo.delete_transfer_documents_$sp](../../StoredProcedures/me_01/dbo.delete_transfer_documents_$sp.md)
- [me_01: dbo.delete_udt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_udt_documents_$sp.md)
- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)

