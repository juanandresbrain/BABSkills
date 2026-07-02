# dbo.ib_price

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_price_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| pricing_group_id | smallint | 2 | 1 |  |  |  |
| temp_price_flag | bit | 1 | 0 |  |  |  |
| start_date | smalldatetime | 4 | 0 |  |  |  |
| end_date | smalldatetime | 4 | 1 |  |  |  |
| valuation_retail_price | decimal | 9 | 0 |  |  |  |
| selling_retail_price | decimal | 9 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| document_number | nvarchar | 40 | 1 |  |  |  |
| cancel_promo_flag | bit | 1 | 0 |  |  |  |
| effective_date | smalldatetime | 4 | 1 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| insert_guid | uniqueidentifier | 16 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.copy_location_perm_prices_$sp](../../StoredProcedures/me_01/dbo.copy_location_perm_prices_$sp.md)
- [me_01: dbo.copy_location_prices_validation_$sp](../../StoredProcedures/me_01/dbo.copy_location_prices_validation_$sp.md)
- [me_01: dbo.copy_location_to_ib_price_$sp](../../StoredProcedures/me_01/dbo.copy_location_to_ib_price_$sp.md)
- [me_01: dbo.get_crnt_perm_price_no_prec_out_$sp](../../StoredProcedures/me_01/dbo.get_crnt_perm_price_no_prec_out_$sp.md)
- [me_01: dbo.get_current_retail_$sp](../../StoredProcedures/me_01/dbo.get_current_retail_$sp.md)
- [me_01: dbo.get_pc_instruction_price_history_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_price_history_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_pricing_$sp](../../StoredProcedures/me_01/dbo.get_pricing_$sp.md)
- [me_01: dbo.get_pricing_history_$sp](../../StoredProcedures/me_01/dbo.get_pricing_history_$sp.md)
- [me_01: dbo.get_pricing_pg_$sp](../../StoredProcedures/me_01/dbo.get_pricing_pg_$sp.md)
- [me_01: dbo.ib_add_loc_to_pg_$sp](../../StoredProcedures/me_01/dbo.ib_add_loc_to_pg_$sp.md)
- [me_01: dbo.ib_rmv_loc_from_pg_$sp](../../StoredProcedures/me_01/dbo.ib_rmv_loc_from_pg_$sp.md)
- [me_01: dbo.ins_ib_inventory_perm_pc_effective_$sp](../../StoredProcedures/me_01/dbo.ins_ib_inventory_perm_pc_effective_$sp.md)
- [me_01: dbo.ins_ib_price_issued_pc_$sp](../../StoredProcedures/me_01/dbo.ins_ib_price_issued_pc_$sp.md)
- [me_01: dbo.insert_ib_price_$sp](../../StoredProcedures/me_01/dbo.insert_ib_price_$sp.md)
- [me_01: dbo.pi_get_retails_$sp](../../StoredProcedures/me_01/dbo.pi_get_retails_$sp.md)
- [me_01: dbo.populate_fixed_average_cost_by_location_$sp](../../StoredProcedures/me_01/dbo.populate_fixed_average_cost_by_location_$sp.md)
- [me_01: dbo.populate_ib_price_short_$sp](../../StoredProcedures/me_01/dbo.populate_ib_price_short_$sp.md)
- [me_01: dbo.rebuild_ib_price_short_$sp](../../StoredProcedures/me_01/dbo.rebuild_ib_price_short_$sp.md)
- [me_01: dbo.spDW_CurrentRetail](../../StoredProcedures/me_01/dbo.spDW_CurrentRetail.md)
- [me_01: dbo.spPOSPricebookStage_BAK20231101](../../StoredProcedures/me_01/dbo.spPOSPricebookStage_BAK20231101.md)
- [me_01: dbo.spWEBPricebookStage](../../StoredProcedures/me_01/dbo.spWEBPricebookStage.md)
- [me_01: dbo.spWEBPricebookStage_Bak20220705](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_Bak20220705.md)
- [me_01: dbo.spWEBPricebookStage_TCOnDemand](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_TCOnDemand.md)
- [me_01: dbo.upd_cancel_promo_pc_$sp](../../StoredProcedures/me_01/dbo.upd_cancel_promo_pc_$sp.md)
- [me_01: dbo.upd_promo_pc_end_date_$sp](../../StoredProcedures/me_01/dbo.upd_promo_pc_end_date_$sp.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)
- [DBAUtility: dbo.spDM_MaintainProducts](../../StoredProcedures/DBAUtility/dbo.spDM_MaintainProducts.md)

