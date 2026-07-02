# dbo.inventory_status

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| inventory_status_code | nvarchar | 6 | 0 |  |  |  |
| inventory_status_desc | nvarchar | 120 | 0 |  |  |  |
| include_on_hand_totals_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.adjust_future_reserve_$sp](../../StoredProcedures/me_01/dbo.adjust_future_reserve_$sp.md)
- [me_01: dbo.adjust_reserve_remnant_cost_$sp](../../StoredProcedures/me_01/dbo.adjust_reserve_remnant_cost_$sp.md)
- [me_01: dbo.eom_complete_$sp](../../StoredProcedures/me_01/dbo.eom_complete_$sp.md)
- [me_01: dbo.eom_reserve_$sp](../../StoredProcedures/me_01/dbo.eom_reserve_$sp.md)
- [me_01: dbo.es_reserve_$sp](../../StoredProcedures/me_01/dbo.es_reserve_$sp.md)
- [me_01: dbo.import_asn_third_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_third_step_$sp.md)
- [me_01: dbo.pi_post_actual_shrink_loc_$sp](../../StoredProcedures/me_01/dbo.pi_post_actual_shrink_loc_$sp.md)
- [me_01: dbo.pi_post_pending_shrink_loc_$sp](../../StoredProcedures/me_01/dbo.pi_post_pending_shrink_loc_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)
- [me_01: dbo.post_25Nov25_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_25Nov25_cust_order_sale_$sp.md)
- [me_01: dbo.post_cust_order_return_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_return_$sp.md)
- [me_01: dbo.post_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_sale_$sp.md)
- [ma_01: dbo.dl_hist_oh_group_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_group_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_sku_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_sku_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_style_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_style_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_styleclr_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_styleclr_vld_$sp.md)

