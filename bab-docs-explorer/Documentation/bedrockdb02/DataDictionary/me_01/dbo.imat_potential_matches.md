# dbo.imat_potential_matches

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_potential_matches_id | decimal | 9 | 0 | YES |  |  |
| imat_process_detail_id | decimal | 9 | 0 |  |  |  |
| imat_receipt_id | decimal | 9 | 0 |  |  |  |
| imat_flow_id | int | 4 | 0 |  |  |  |
| imat_match_option_id | tinyint | 1 | 0 |  |  |  |
| imat_match_result_id | tinyint | 1 | 0 |  |  |  |
| gross_unmatched_amount | decimal | 9 | 0 |  |  |  |
| net_unmatched_amount | decimal | 9 | 0 |  |  |  |
| discount_total | decimal | 9 | 0 |  |  |  |
| imat_process_header_id | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)

