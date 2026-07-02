# dbo.imat_receipt_detail_adj

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_receipt_detail_adj_id | decimal | 9 | 0 | YES |  |  |
| imat_receipt_detail_id | decimal | 9 | 0 |  |  |  |
| transaction_type | tinyint | 1 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| gross_transaction_amount | decimal | 9 | 0 |  |  |  |
| net_transaction_amount | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)

