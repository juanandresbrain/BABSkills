# dbo.price_change_message

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| price_change_message_id | decimal | 9 | 0 | YES |  |  |
| price_change_id | decimal | 9 | 0 | YES |  |  |
| parent_id | decimal | 9 | 0 |  |  |  |
| parent_type | smallint | 2 | 0 |  |  |  |
| message_type_id | decimal | 9 | 0 |  |  |  |
| message | nvarchar | 510 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_pc_documents_$sp](../../StoredProcedures/me_01/dbo.delete_pc_documents_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)
- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)

