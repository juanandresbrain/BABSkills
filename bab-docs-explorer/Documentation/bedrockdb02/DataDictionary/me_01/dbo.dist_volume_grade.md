# dbo.dist_volume_grade

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| dist_volume_grade_id | int | 4 | 0 | YES |  |  |
| grade_code | nvarchar | 20 | 0 |  |  |  |
| sales_lower_limit | decimal | 5 | 0 |  |  |  |
| minimum | int | 4 | 0 |  |  |  |
| maximum | int | 4 | 0 |  |  |  |
| weight | decimal | 5 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

