# dbo.temp_price_change_attrib_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 1 |  |  |  |
| imp_price_change_id | decimal | 9 | 1 |  |  |  |
| temp_price_change_attrib_set_id | decimal | 9 | 0 |  |  |  |
| temp_price_change_id | decimal | 9 | 0 |  |  |  |
| attribute_set_id | decimal | 9 | 0 |  |  |  |
| attribute_id | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_adjust_temp_pc_id_$sp](../../StoredProcedures/me_01/dbo.import_pc_adjust_temp_pc_id_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)

