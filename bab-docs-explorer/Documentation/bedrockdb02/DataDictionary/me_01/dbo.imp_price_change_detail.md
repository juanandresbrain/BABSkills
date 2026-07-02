# dbo.imp_price_change_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_price_change_detail_id | decimal | 9 | 0 | YES |  |  |
| imp_price_change_id | decimal | 9 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| location_code | nvarchar | 40 | 1 |  |  |  |
| pricing_group_code | nvarchar | 20 | 1 |  |  |  |
| new_price | decimal | 9 | 1 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| calculation_method | smallint | 2 | 1 |  |  |  |
| calculation_value | decimal | 9 | 1 |  |  |  |
| result_price_status | nvarchar | 6 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_purge_$sp](../../StoredProcedures/me_01/dbo.import_pc_purge_$sp.md)
- [me_01: dbo.import_pc_validate_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_$sp.md)

