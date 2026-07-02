# dbo.hist_oh_style_chn_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| merch_year_wk | int | 4 | 0 | YES |  |  |
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| price_status_id | smallint | 2 | 0 | YES |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |
| on_hand_retail | decimal | 9 | 0 |  |  |  |
| on_hand_cost | decimal | 9 | 0 |  |  |  |
| on_hand_retail_te | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_style_delete_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_oh_$sp.md)
- [ma_01: dbo.nsb_vendor_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_vendor_analysis_$sp.md)
- [ma_01: dbo.post_binv_style_$sp](../../StoredProcedures/ma_01/dbo.post_binv_style_$sp.md)
- [ma_01: dbo.post_hist_oh_style_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_style_$sp.md)
- [ma_01: dbo.post_oh_style_$sp](../../StoredProcedures/ma_01/dbo.post_oh_style_$sp.md)
- [ma_01: dbo.roll_oh_style_chn_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_chn_wk_$sp.md)
- [ma_01: dbo.roll_oh_style_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_wk_$sp.md)
- [ma_01: dbo.rpt_vendor_analysis_$sp](../../StoredProcedures/ma_01/dbo.rpt_vendor_analysis_$sp.md)

