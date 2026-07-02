# dbo.temp_price_change_style_color

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 1 |  |  |  |
| imp_price_change_id | decimal | 9 | 1 |  |  |  |
| temp_price_change_style_color_id | decimal | 9 | 0 |  |  |  |
| temp_price_change_id | decimal | 9 | 0 |  |  |  |
| temp_price_change_style_id | decimal | 9 | 0 |  |  |  |
| price_change_type | smallint | 2 | 0 |  |  |  |
| calculation_method | smallint | 2 | 0 |  |  |  |
| calculation_value | decimal | 9 | 0 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| base_value | decimal | 9 | 1 |  |  |  |
| old_price | decimal | 9 | 0 |  |  |  |
| new_price | decimal | 9 | 1 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| redundant_flag | bit | 1 | 0 |  |  |  |
| total_cost | decimal | 9 | 1 |  |  |  |
| total_units | int | 4 | 1 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| list_retail | decimal | 9 | 1 |  |  |  |
| last_po_cost | decimal | 9 | 1 |  |  |  |
| total_valuation_cost | decimal | 9 | 1 |  |  |  |
| new_valuation_price | decimal | 9 | 1 |  |  |  |
| current_valuation_retail | decimal | 9 | 1 |  |  |  |
| original_valuation_retail | decimal | 9 | 1 |  |  |  |
| total_affected_units | int | 4 | 1 |  |  |  |
| style_color_id | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_$sp.md)
- [me_01: dbo.import_pc_adjust_temp_pc_id_$sp](../../StoredProcedures/me_01/dbo.import_pc_adjust_temp_pc_id_$sp.md)
- [me_01: dbo.import_pc_batch_tickets_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_tickets_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_from_ib_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_from_ib_$sp.md)
- [me_01: dbo.import_pc_validate_ib_data_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_ib_data_$sp.md)

