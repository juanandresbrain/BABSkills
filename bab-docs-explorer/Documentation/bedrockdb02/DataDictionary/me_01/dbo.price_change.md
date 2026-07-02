# dbo.price_change

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| price_change_id | decimal | 9 | 0 | YES |  |  |
| category_id | decimal | 9 | 1 |  |  |  |
| pricing_rule_id | decimal | 9 | 0 |  |  |  |
| price_change_no | nvarchar | 40 | 0 |  |  |  |
| price_change_status | smallint | 2 | 0 |  |  |  |
| price_change_description | nvarchar | 120 | 1 |  |  |  |
| price_change_duration | smallint | 2 | 1 |  |  |  |
| price_change_document_type | smallint | 2 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| effective_to_date | smalldatetime | 4 | 1 |  |  |  |
| terminate_on_date | smalldatetime | 4 | 1 |  |  |  |
| issue_date | smalldatetime | 4 | 1 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| price_status_override | bit | 1 | 1 |  |  |  |
| location_grouping | smallint | 2 | 0 |  |  |  |
| calculation_method | smallint | 2 | 1 |  |  |  |
| calculation_value | decimal | 9 | 1 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| override_price_exceptions | bit | 1 | 1 |  |  |  |
| disable_print_by_location_flag | bit | 1 | 0 |  |  |  |
| approval_status | smallint | 2 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| status_date | smalldatetime | 4 | 0 |  |  |  |
| last_copy_date | smalldatetime | 4 | 0 |  |  |  |
| calculation_date | smalldatetime | 4 | 1 |  |  |  |
| position_id | decimal | 9 | 0 |  |  |  |
| total_cost | decimal | 9 | 1 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| state_no | smallint | 2 | 0 |  |  |  |
| total_units | int | 4 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| generate_tickets | smallint | 2 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| total_valuation_cost | decimal | 9 | 1 |  |  |  |
| promotional_event_flag | bit | 1 | 0 |  |  |  |
| submitted_by_id | decimal | 9 | 1 |  |  |  |
| total_affected_units | int | 4 | 1 |  |  |  |
| schema_version | tinyint | 1 | 0 |  |  |  |
| total_cost_currency_id | decimal | 9 | 1 |  |  |  |
| total_valuation_cost_currency_id | decimal | 9 | 1 |  |  |  |
| send_price_change_to_webim_flag | bit | 1 | 0 |  |  |  |
| result_id | decimal | 9 | 1 |  |  |  |
| resulting_pos_promotion_type | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.add_promtional_event_$sp](../../StoredProcedures/me_01/dbo.add_promtional_event_$sp.md)
- [me_01: dbo.copy_location_price_change_instruction_details_$sp](../../StoredProcedures/me_01/dbo.copy_location_price_change_instruction_details_$sp.md)
- [me_01: dbo.copy_location_to_ib_price_$sp](../../StoredProcedures/me_01/dbo.copy_location_to_ib_price_$sp.md)
- [me_01: dbo.copy_location_to_price_changes_$sp](../../StoredProcedures/me_01/dbo.copy_location_to_price_changes_$sp.md)
- [me_01: dbo.delete_pc_documents_$sp](../../StoredProcedures/me_01/dbo.delete_pc_documents_$sp.md)
- [me_01: dbo.get_pc_references_$sp](../../StoredProcedures/me_01/dbo.get_pc_references_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)
- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.ins_ib_inventory_perm_pc_effective_$sp](../../StoredProcedures/me_01/dbo.ins_ib_inventory_perm_pc_effective_$sp.md)
- [me_01: dbo.ins_ib_on_order_post_pc_$sp](../../StoredProcedures/me_01/dbo.ins_ib_on_order_post_pc_$sp.md)
- [me_01: dbo.ins_ib_price_issued_pc_$sp](../../StoredProcedures/me_01/dbo.ins_ib_price_issued_pc_$sp.md)
- [me_01: dbo.move_pg_exceptions_to_locations_$sp](../../StoredProcedures/me_01/dbo.move_pg_exceptions_to_locations_$sp.md)
- [me_01: dbo.pc_calc_total_affected_units_$sp](../../StoredProcedures/me_01/dbo.pc_calc_total_affected_units_$sp.md)
- [me_01: dbo.pcm_get_tickets_$sp](../../StoredProcedures/me_01/dbo.pcm_get_tickets_$sp.md)
- [me_01: dbo.pcm_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_issue_pc_$sp.md)
- [me_01: dbo.pcm_pre_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_pre_issue_pc_$sp.md)
- [me_01: dbo.spMerchandisingReportUpcomingPriceChanges](../../StoredProcedures/me_01/dbo.spMerchandisingReportUpcomingPriceChanges.md)
- [me_01: dbo.spPOSPricebookStage_BAK20231101](../../StoredProcedures/me_01/dbo.spPOSPricebookStage_BAK20231101.md)
- [me_01: dbo.spWEBPricebookStage](../../StoredProcedures/me_01/dbo.spWEBPricebookStage.md)
- [me_01: dbo.spWEBPricebookStage_Bak20220705](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_Bak20220705.md)
- [me_01: dbo.spWEBPricebookStage_TCOnDemand](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_TCOnDemand.md)
- [me_01: dbo.upd_cancel_promo_pc_$sp](../../StoredProcedures/me_01/dbo.upd_cancel_promo_pc_$sp.md)
- [me_01: dbo.upd_ib_activity_date_pc_$sp](../../StoredProcedures/me_01/dbo.upd_ib_activity_date_pc_$sp.md)
- [me_01: dbo.upd_im_to_do_worklist_price_change_$sp](../../StoredProcedures/me_01/dbo.upd_im_to_do_worklist_price_change_$sp.md)
- [me_01: dbo.upd_promo_events_$sp](../../StoredProcedures/me_01/dbo.upd_promo_events_$sp.md)
- [me_01: dbo.upd_promo_pc_end_date_$sp](../../StoredProcedures/me_01/dbo.upd_promo_pc_end_date_$sp.md)
- [me_01: dbo.upd_style_retails_pc_$sp](../../StoredProcedures/me_01/dbo.upd_style_retails_pc_$sp.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)
- [USICOAL: dbo.DC_BOOK_PRC_CHG](../../StoredProcedures/USICOAL/dbo.DC_BOOK_PRC_CHG.md)
- [USICOAL: dbo.DC_CALC_PRC_CHG](../../StoredProcedures/USICOAL/dbo.DC_CALC_PRC_CHG.md)
- [USICOAL: dbo.DC_DEL_PRC_CHG](../../StoredProcedures/USICOAL/dbo.DC_DEL_PRC_CHG.md)
- [USICOAL: dbo.DC_UPD_ITM_PRC](../../StoredProcedures/USICOAL/dbo.DC_UPD_ITM_PRC.md)
- [USICOAL: dbo.IM_APPL_PRC_CHG](../../StoredProcedures/USICOAL/dbo.IM_APPL_PRC_CHG.md)

