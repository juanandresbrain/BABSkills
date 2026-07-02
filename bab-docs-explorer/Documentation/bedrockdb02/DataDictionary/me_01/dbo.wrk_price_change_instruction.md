# dbo.wrk_price_change_instruction

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| wrk_price_change_id | decimal | 9 | 0 | YES |  |  |
| price_change_instruction_id | decimal | 9 | 0 | YES |  |  |
| merch_instruction_type | smallint | 2 | 0 |  |  |  |
| merch_hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| location_instruction_type | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 1 |  |  |  |
| calculation_method | smallint | 2 | 0 |  |  |  |
| calculation_value | decimal | 9 | 0 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_wrk_price_change_calc_$sp](../../StoredProcedures/me_01/dbo.delete_wrk_price_change_calc_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)

