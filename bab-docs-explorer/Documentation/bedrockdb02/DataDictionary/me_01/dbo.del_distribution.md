# dbo.del_distribution

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_number | nvarchar | 40 | 0 |  |  |  |
| status_date | smalldatetime | 4 | 0 |  |  |  |
| deleted_date | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)

