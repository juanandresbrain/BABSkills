# dbo.merch_group_parent_full

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_level_id | int | 4 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| parent_hierarchy_level_id | int | 4 | 0 | YES |  |  |
| parent_hierarchy_group_id | int | 4 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_pc_references_$sp](../../StoredProcedures/me_01/dbo.get_pc_references_$sp.md)
- [me_01: dbo.get_tax_rate_$sp](../../StoredProcedures/me_01/dbo.get_tax_rate_$sp.md)
- [me_01: dbo.plu_common_dept_$sp](../../StoredProcedures/me_01/dbo.plu_common_dept_$sp.md)
- [me_01: dbo.plu_dept_params_$sp](../../StoredProcedures/me_01/dbo.plu_dept_params_$sp.md)
- [me_01: dbo.plu_hg_regen_dept_$sp](../../StoredProcedures/me_01/dbo.plu_hg_regen_dept_$sp.md)
- [me_01: dbo.plu_regen_dept_$sp](../../StoredProcedures/me_01/dbo.plu_regen_dept_$sp.md)
- [me_01: dbo.plu_update_dept_$sp](../../StoredProcedures/me_01/dbo.plu_update_dept_$sp.md)
- [me_01: dbo.plu_update_item_dept_$sp](../../StoredProcedures/me_01/dbo.plu_update_item_dept_$sp.md)

