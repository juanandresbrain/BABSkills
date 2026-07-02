# dbo.im_to_do_worklist

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_type | smallint | 2 | 0 | YES |  |  |
| document_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_asn_documents_$sp](../../StoredProcedures/me_01/dbo.delete_asn_documents_$sp.md)
- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)
- [me_01: dbo.delete_inv_control_documents_$sp](../../StoredProcedures/me_01/dbo.delete_inv_control_documents_$sp.md)
- [me_01: dbo.delete_pc_documents_$sp](../../StoredProcedures/me_01/dbo.delete_pc_documents_$sp.md)
- [me_01: dbo.import_asn_first_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_first_step_$sp.md)
- [me_01: dbo.pcm_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_issue_pc_$sp.md)
- [me_01: dbo.upd_cancel_promo_pc_$sp](../../StoredProcedures/me_01/dbo.upd_cancel_promo_pc_$sp.md)
- [me_01: dbo.upd_im_to_do_worklist_price_change_$sp](../../StoredProcedures/me_01/dbo.upd_im_to_do_worklist_price_change_$sp.md)
- [me_01: dbo.upd_promo_pc_end_date_$sp](../../StoredProcedures/me_01/dbo.upd_promo_pc_end_date_$sp.md)

