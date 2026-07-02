# dbo.dist_location_grade

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| dist_location_grade_id | bigint | 8 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| original_definition_id | bigint | 8 | 1 |  |  |  |
| current_definition_id | bigint | 8 | 1 |  |  |  |
| final_definition_id | bigint | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

