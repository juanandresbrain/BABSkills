# dbo.price_change_attrib_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| price_change_attrib_set_id | decimal | 9 | 0 | YES |  |  |
| price_change_id | decimal | 9 | 0 | YES |  |  |
| attribute_set_id | decimal | 9 | 0 |  |  |  |
| attribute_id | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_pc_documents_$sp](../../StoredProcedures/me_01/dbo.delete_pc_documents_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)

