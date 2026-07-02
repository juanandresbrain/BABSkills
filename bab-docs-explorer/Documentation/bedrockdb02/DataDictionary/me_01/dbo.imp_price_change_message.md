# dbo.imp_price_change_message

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_price_change_message_id | decimal | 9 | 0 | YES |  |  |
| imp_price_change_id | decimal | 9 | 0 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| message_type_description | nvarchar | 40 | 0 |  |  |  |
| message | nvarchar | 510 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_purge_$sp](../../StoredProcedures/me_01/dbo.import_pc_purge_$sp.md)

