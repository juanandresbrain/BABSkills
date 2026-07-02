# dbo.imat_receipt

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_receipt_id | int | 4 | 0 | YES |  |  |
| receipt_id | decimal | 9 | 0 |  |  |  |
| transaction_type | tinyint | 1 | 0 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |
| po_no | nvarchar | 40 | 1 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| match_status_code | smallint | 2 | 0 |  |  |  |
| exchange_rate | float | 8 | 0 |  |  |  |
| original_gross_amount | decimal | 9 | 0 |  |  |  |
| original_net_amount | decimal | 9 | 0 |  |  |  |
| gross_transaction_amount | decimal | 9 | 0 |  |  |  |
| net_transaction_amount | decimal | 9 | 0 |  |  |  |
| gross_matched_amount | decimal | 9 | 0 |  |  |  |
| net_matched_amount | decimal | 9 | 0 |  |  |  |
| summary_level_match | bit | 1 | 0 |  |  |  |
| total_units | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| im_document_status | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)
- [me_01: dbo.import_asn_sixth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_sixth_step_$sp.md)

