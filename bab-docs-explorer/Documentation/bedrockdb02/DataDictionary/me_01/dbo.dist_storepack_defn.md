# dbo.dist_storepack_defn

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dist_storepack_definition_id | bigint | 8 | 0 | YES |  |  |
| distribution_id | bigint | 8 | 0 | YES |  |  |
| grade_code | nvarchar | 20 | 1 |  |  |  |
| volume_grade_id | int | 4 | 0 |  |  |  |
| available_quantity | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

