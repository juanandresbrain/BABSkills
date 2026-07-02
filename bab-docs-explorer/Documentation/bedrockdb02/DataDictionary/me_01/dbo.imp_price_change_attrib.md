# dbo.imp_price_change_attrib

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_price_change_attrib_id | decimal | 9 | 0 | YES |  |  |
| imp_price_change_id | decimal | 9 | 0 |  |  |  |
| attribute_code | nvarchar | 12 | 0 |  |  |  |
| attribute_set_code | nvarchar | 12 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_purge_$sp](../../StoredProcedures/me_01/dbo.import_pc_purge_$sp.md)
- [me_01: dbo.import_pc_validate_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_$sp.md)

