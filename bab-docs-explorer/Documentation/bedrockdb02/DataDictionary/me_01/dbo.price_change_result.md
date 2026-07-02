# dbo.price_change_result

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| result_id | decimal | 9 | 0 |  |  |  |
| price_change_instruction_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| on_order_units | int | 4 | 1 |  |  |  |
| total_on_hand_units | int | 4 | 1 |  |  |  |
| original_retail_price | decimal | 9 | 1 |  |  |  |
| current_retail_price | decimal | 9 | 1 |  |  |  |
| selling_retail_price | decimal | 9 | 1 |  |  |  |
| calculation_method | smallint | 2 | 0 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| calculation_value | decimal | 9 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| current_valuation_retail_price | decimal | 9 | 1 |  |  |  |
| valuation_retail_price | decimal | 9 | 1 |  |  |  |
| is_pseudo_instruction | bit | 1 | 0 |  |  |  |
| final_exception_level | tinyint | 1 | 1 |  |  |  |
| alternate_exception_level | tinyint | 1 | 1 |  |  |  |
| original_valuation_retail_price | decimal | 9 | 1 |  |  |  |
| old_exception_level | tinyint | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.copy_location_price_change_instruction_details_$sp](../../StoredProcedures/me_01/dbo.copy_location_price_change_instruction_details_$sp.md)
- [me_01: dbo.delete_pc_documents_$sp](../../StoredProcedures/me_01/dbo.delete_pc_documents_$sp.md)
- [me_01: dbo.delete_wrk_price_change_calc_$sp](../../StoredProcedures/me_01/dbo.delete_wrk_price_change_calc_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_pc_totals_$sp](../../StoredProcedures/me_01/dbo.get_pc_totals_$sp.md)
- [me_01: dbo.ins_ib_on_order_post_pc_$sp](../../StoredProcedures/me_01/dbo.ins_ib_on_order_post_pc_$sp.md)
- [me_01: dbo.ins_ib_price_issued_pc_$sp](../../StoredProcedures/me_01/dbo.ins_ib_price_issued_pc_$sp.md)
- [me_01: dbo.upd_ib_activity_date_pc_$sp](../../StoredProcedures/me_01/dbo.upd_ib_activity_date_pc_$sp.md)
- [me_01: dbo.upd_im_to_do_worklist_price_change_$sp](../../StoredProcedures/me_01/dbo.upd_im_to_do_worklist_price_change_$sp.md)
- [me_01: dbo.upd_promo_events_$sp](../../StoredProcedures/me_01/dbo.upd_promo_events_$sp.md)
- [me_01: dbo.upd_style_retails_pc_$sp](../../StoredProcedures/me_01/dbo.upd_style_retails_pc_$sp.md)

