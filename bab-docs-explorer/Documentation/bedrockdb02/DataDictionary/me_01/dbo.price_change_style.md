# dbo.price_change_style

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| price_change_style_id | decimal | 9 | 0 | YES |  |  |
| price_change_id | decimal | 9 | 0 |  |  |  |
| price_change_type | smallint | 2 | 0 |  |  |  |
| calculation_method | smallint | 2 | 0 |  |  |  |
| calculation_value | decimal | 9 | 0 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| base_value | decimal | 9 | 1 |  |  |  |
| old_price | decimal | 9 | 0 |  |  |  |
| new_price | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| color_exception_flag | bit | 1 | 0 |  |  |  |
| location_exception_flag | bit | 1 | 0 |  |  |  |
| loc_col_exception_flag | bit | 1 | 0 |  |  |  |
| average_cost | decimal | 9 | 0 |  |  |  |
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
| pricing_grp_exception_flag | bit | 1 | 0 |  |  |  |
| pricing_grp_col_exception_flag | bit | 1 | 0 |  |  |  |
| total_affected_units | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.add_promtional_event_$sp](../../StoredProcedures/me_01/dbo.add_promtional_event_$sp.md)
- [me_01: dbo.delete_pc_documents_$sp](../../StoredProcedures/me_01/dbo.delete_pc_documents_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)
- [me_01: dbo.pc_calc_total_affected_units_$sp](../../StoredProcedures/me_01/dbo.pc_calc_total_affected_units_$sp.md)
- [me_01: dbo.pc_calc_total_au_jur_$sp](../../StoredProcedures/me_01/dbo.pc_calc_total_au_jur_$sp.md)
- [me_01: dbo.pc_calc_total_au_loc_list_$sp](../../StoredProcedures/me_01/dbo.pc_calc_total_au_loc_list_$sp.md)
- [me_01: dbo.pc_calc_total_au_pg_list_$sp](../../StoredProcedures/me_01/dbo.pc_calc_total_au_pg_list_$sp.md)
- [me_01: dbo.pcm_get_tickets_$sp](../../StoredProcedures/me_01/dbo.pcm_get_tickets_$sp.md)
- [me_01: dbo.pcm_pre_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_pre_issue_pc_$sp.md)
- [me_01: dbo.plu_pc_queue_$sp](../../StoredProcedures/me_01/dbo.plu_pc_queue_$sp.md)
- [me_01: dbo.spMerchandisingReportUpcomingPriceChanges](../../StoredProcedures/me_01/dbo.spMerchandisingReportUpcomingPriceChanges.md)
- [me_01: dbo.spPOSPricebookStage_BAK20231101](../../StoredProcedures/me_01/dbo.spPOSPricebookStage_BAK20231101.md)
- [me_01: dbo.spWEBPricebookStage](../../StoredProcedures/me_01/dbo.spWEBPricebookStage.md)
- [me_01: dbo.spWEBPricebookStage_Bak20220705](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_Bak20220705.md)
- [me_01: dbo.spWEBPricebookStage_TCOnDemand](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_TCOnDemand.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)

