# dbo.imat_receipt_discount

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_receipt_discount_id | decimal | 9 | 0 | YES |  |  |
| imat_receipt_id | int | 4 | 0 |  |  |  |
| discount_id | smallint | 2 | 0 |  |  |  |
| sequence_no | int | 4 | 0 |  |  |  |
| item_specific_discount_flag | bit | 1 | 0 |  |  |  |
| percent_amount | tinyint | 1 | 0 |  |  |  |
| discount_value | float | 8 | 0 |  |  |  |
| calculate_on | tinyint | 1 | 0 |  |  |  |
| reflect_in_discount_cost_flag | bit | 1 | 0 |  |  |  |
| reflect_in_net_cost_flag | bit | 1 | 0 |  |  |  |
| subject_to_terms_flag | bit | 1 | 0 |  |  |  |
| discount_amount | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)
- [me_01: dbo.import_asn_sixth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_sixth_step_$sp.md)

