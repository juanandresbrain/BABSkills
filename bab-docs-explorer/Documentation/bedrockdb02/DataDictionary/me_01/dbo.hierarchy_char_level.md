# dbo.hierarchy_char_level

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_char_level_id | smallint | 2 | 0 | YES |  |  |
| hierarchy_id | smallint | 2 | 0 |  |  |  |
| goal_imu_level_id | int | 4 | 0 |  |  |  |
| imu_tolerance_level_id | int | 4 | 0 |  |  |  |
| plu_description_level_id | int | 4 | 0 |  |  |  |
| shrinkage_provision_level_id | int | 4 | 0 |  |  |  |
| ticket_format_code_level_id | int | 4 | 0 |  |  |  |
| leased_flag_level_id | int | 4 | 0 |  |  |  |
| pos_merch_group_key_level_id | int | 4 | 0 |  |  |  |
| pos_merch_group_key_length | smallint | 2 | 0 |  |  |  |
| sl_minimum_cost_level_id | int | 4 | 0 |  |  |  |
| sl_maximum_cost_level_id | int | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| pos_dept_group_key_length | smallint | 2 | 1 |  |  |  |
| pos_dept_group_key_level_id | int | 4 | 1 |  |  |  |
| plu_dept_group_desc_level_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.es_reserve_$sp](../../StoredProcedures/me_01/dbo.es_reserve_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)
- [me_01: dbo.plu_common_dept_$sp](../../StoredProcedures/me_01/dbo.plu_common_dept_$sp.md)
- [me_01: dbo.plu_hg_regen_dept_$sp](../../StoredProcedures/me_01/dbo.plu_hg_regen_dept_$sp.md)
- [me_01: dbo.plu_regen_dept_$sp](../../StoredProcedures/me_01/dbo.plu_regen_dept_$sp.md)
- [me_01: dbo.plu_update_dept_$sp](../../StoredProcedures/me_01/dbo.plu_update_dept_$sp.md)
- [me_01: dbo.plu_update_item_dept_$sp](../../StoredProcedures/me_01/dbo.plu_update_item_dept_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_by_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_by_jurisdiction_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_for_pseudo_style_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_for_pseudo_style_$sp.md)
- [me_01: dbo.populate_dynamic_average_cost_$sp](../../StoredProcedures/me_01/dbo.populate_dynamic_average_cost_$sp.md)
- [me_01: dbo.populate_fixed_average_cost_by_location_$sp](../../StoredProcedures/me_01/dbo.populate_fixed_average_cost_by_location_$sp.md)

