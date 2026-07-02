# dbo.dist_grp_instruction

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| dist_grp_instruction_id | int | 4 | 0 | YES |  |  |
| dist_volume_grade_id | int | 4 | 0 |  |  |  |
| dist_sell_thru_grade_id | int | 4 | 0 |  |  |  |
| instruction | smallint | 2 | 0 |  |  |  |
| instruction_value | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

