# dbo.hist_oh_group_chn_pd

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| merch_year_pd | int | 4 | 0 | YES |  |  |
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| price_status_id | smallint | 2 | 0 | YES |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |
| on_hand_retail | decimal | 9 | 0 |  |  |  |
| on_hand_cost | decimal | 9 | 0 |  |  |  |
| on_hand_retail_te | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.create_initial_history_partitions_$sp](../../StoredProcedures/ma_01/dbo.create_initial_history_partitions_$sp.md)
- [ma_01: dbo.nsb_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_chain_$sp.md)
- [ma_01: dbo.nsb_par_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_$sp.md)
- [ma_01: dbo.nsb_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_rim_$sp.md)
- [ma_01: dbo.post_binv_group_$sp](../../StoredProcedures/ma_01/dbo.post_binv_group_$sp.md)
- [ma_01: dbo.post_hist_oh_group_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_group_$sp.md)
- [ma_01: dbo.post_oh_group_$sp](../../StoredProcedures/ma_01/dbo.post_oh_group_$sp.md)
- [ma_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_oh_$sp.md)
- [ma_01: dbo.roll_oh_group_chn_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_chn_pd_$sp.md)
- [ma_01: dbo.roll_oh_group_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_pd_$sp.md)
- [ma_01: dbo.rpt_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_chain_$sp.md)
- [ma_01: dbo.rpt_par_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_chain_$sp.md)
- [ma_01: dbo.rpt_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_chain_rim_$sp.md)

