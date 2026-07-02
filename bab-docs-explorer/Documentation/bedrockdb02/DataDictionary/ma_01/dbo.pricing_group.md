# dbo.pricing_group

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pricing_group_id | smallint | 2 | 0 | YES |  |  |
| pricing_group_code | nvarchar | 20 | 0 |  |  |  |
| pricing_group_description | nvarchar | 60 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.build_pg_time_table_$sp](../../StoredProcedures/me_01/dbo.build_pg_time_table_$sp.md)
- [me_01: dbo.get_retails_MA_$sp](../../StoredProcedures/me_01/dbo.get_retails_MA_$sp.md)
- [me_01: dbo.ib_add_loc_to_pg_$sp](../../StoredProcedures/me_01/dbo.ib_add_loc_to_pg_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_validate_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_$sp.md)

