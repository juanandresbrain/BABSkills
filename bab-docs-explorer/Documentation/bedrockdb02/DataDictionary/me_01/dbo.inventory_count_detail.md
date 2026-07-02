# dbo.inventory_count_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_count_detail_id | decimal | 9 | 0 | YES |  |  |
| inventory_control_loc_id | decimal | 9 | 0 |  |  |  |
| inventory_control_id | decimal | 9 | 0 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| units_counted | int | 4 | 0 |  |  |  |
| book_pack_units | int | 4 | 1 |  |  |  |
| extended_units_counted | int | 4 | 1 |  |  |  |
| cost | decimal | 9 | 1 |  |  |  |
| total_cost | decimal | 9 | 1 |  |  |  |
| total_retail | decimal | 9 | 1 |  |  |  |
| total_valuation_retail | decimal | 9 | 1 |  |  |  |
| total_oh_book_units | int | 4 | 1 |  |  |  |
| total_oh_book_cost | decimal | 9 | 1 |  |  |  |
| total_oh_book_val_retail | decimal | 9 | 1 |  |  |  |
| total_oh_book_sell_retail | decimal | 9 | 1 |  |  |  |
| total_oh_in_transit_units | int | 4 | 1 |  |  |  |
| total_oh_in_transit_cost | decimal | 9 | 1 |  |  |  |
| total_oh_in_tran_val_retail | decimal | 9 | 1 |  |  |  |
| total_oh_in_tran_sell_retail | decimal | 9 | 1 |  |  |  |
| average_cost | decimal | 9 | 1 |  |  |  |
| valuation_unit_retail | decimal | 9 | 1 |  |  |  |
| selling_unit_retail | decimal | 9 | 1 |  |  |  |
| price_status_id | int | 4 | 1 |  |  |  |
| effective_date | smalldatetime | 4 | 1 |  |  |  |
| shrink_units | int | 4 | 1 |  |  |  |
| shrink_cost | decimal | 9 | 1 |  |  |  |
| shrink_valuation_retail | decimal | 9 | 1 |  |  |  |
| shrink_selling_retail | decimal | 9 | 1 |  |  |  |
| pack_shrink_units | int | 4 | 1 |  |  |  |
| discrepancy_units | int | 4 | 1 |  |  |  |
| discrepancy_cost | decimal | 9 | 1 |  |  |  |
| discrepancy_val_retail | decimal | 9 | 1 |  |  |  |
| discrepancy_sell_retail | decimal | 9 | 1 |  |  |  |
| pending_shrink_units | int | 4 | 1 |  |  |  |
| pending_shrink_cost | decimal | 9 | 1 |  |  |  |
| pending_shrink_val_retail | decimal | 9 | 1 |  |  |  |
| pending_shrink_sell_retail | decimal | 9 | 1 |  |  |  |
| cost_local | decimal | 9 | 1 |  |  |  |
| total_cost_local | decimal | 9 | 1 |  |  |  |
| total_oh_book_cost_local | decimal | 9 | 1 |  |  |  |
| total_oh_in_transit_cost_local | decimal | 9 | 1 |  |  |  |
| average_cost_local | decimal | 9 | 1 |  |  |  |
| shrink_cost_local | decimal | 9 | 1 |  |  |  |
| discrepancy_cost_local | decimal | 9 | 1 |  |  |  |
| pending_shrink_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_inv_control_documents_$sp](../../StoredProcedures/me_01/dbo.delete_inv_control_documents_$sp.md)
- [me_01: dbo.extend_pack_skus_$sp](../../StoredProcedures/me_01/dbo.extend_pack_skus_$sp.md)
- [me_01: dbo.ins_missing_skus_depart_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_depart_$sp.md)
- [me_01: dbo.ins_missing_skus_enterpr_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_enterpr_$sp.md)
- [me_01: dbo.ins_missing_skus_style_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_style_$sp.md)
- [me_01: dbo.insert_packs_$sp](../../StoredProcedures/me_01/dbo.insert_packs_$sp.md)
- [me_01: dbo.insert_packs_bi_$sp](../../StoredProcedures/me_01/dbo.insert_packs_bi_$sp.md)
- [me_01: dbo.insert_pseudo_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_$sp.md)
- [me_01: dbo.insert_pseudo_bi_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_$sp.md)
- [me_01: dbo.insert_pseudo_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_ols_$sp.md)
- [me_01: dbo.insert_pseudo_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_ols_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_bi_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_$sp.md)
- [me_01: dbo.insert_skus_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_ols_$sp.md)
- [me_01: dbo.insert_skus_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_ols_$sp.md)
- [me_01: dbo.pi_get_retails_$sp](../../StoredProcedures/me_01/dbo.pi_get_retails_$sp.md)
- [me_01: dbo.pi_load_retail_data_loc_$sp](../../StoredProcedures/me_01/dbo.pi_load_retail_data_loc_$sp.md)
- [me_01: dbo.pi_move_store_count_$sp](../../StoredProcedures/me_01/dbo.pi_move_store_count_$sp.md)
- [me_01: dbo.pi_process_loc_$sp](../../StoredProcedures/me_01/dbo.pi_process_loc_$sp.md)
- [me_01: dbo.pi_process_loc_ols_$sp](../../StoredProcedures/me_01/dbo.pi_process_loc_ols_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)
- [me_01: dbo.post_beg_inv_loc_$sp](../../StoredProcedures/me_01/dbo.post_beg_inv_loc_$sp.md)
- [me_01: dbo.post_inventory_loc_$sp](../../StoredProcedures/me_01/dbo.post_inventory_loc_$sp.md)
- [me_01: dbo.post_pending_loc_$sp](../../StoredProcedures/me_01/dbo.post_pending_loc_$sp.md)

