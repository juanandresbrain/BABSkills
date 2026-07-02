# dbo.size_category

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| size_category_id | int | 4 | 0 | YES |  |  |
| size_category_code | nvarchar | 16 | 0 |  |  |  |
| size_category_label | nvarchar | 40 | 0 |  |  |  |
| number_of_dimensions | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_generate_upc_state_$sp](../../StoredProcedures/me_01/dbo.dl_generate_upc_state_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.dl_validate_import_upc_$sp](../../StoredProcedures/me_01/dbo.dl_validate_import_upc_$sp.md)
- [me_01: dbo.get_pc_instruction_price_history_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_price_history_$sp.md)
- [me_01: dbo.get_price_change_details_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_$sp.md)
- [me_01: dbo.get_price_change_details_pricing_level_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_pricing_level_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

