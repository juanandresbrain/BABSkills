# dbo.hist_oh_group_loc_yr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| merch_year | smallint | 2 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| price_status_id | smallint | 2 | 0 | YES |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |
| on_hand_retail | decimal | 9 | 0 |  |  |  |
| on_hand_cost | decimal | 9 | 0 |  |  |  |
| on_hand_retail_te | decimal | 9 | 0 |  |  |  |
| on_hand_retail_local | decimal | 9 | 1 |  |  |  |
| on_hand_retail_te_local | decimal | 9 | 1 |  |  |  |
| on_hand_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_binv_group_$sp](../../StoredProcedures/ma_01/dbo.post_binv_group_$sp.md)
- [ma_01: dbo.post_hist_oh_group_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_group_$sp.md)
- [ma_01: dbo.post_oh_group_$sp](../../StoredProcedures/ma_01/dbo.post_oh_group_$sp.md)
- [ma_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_oh_$sp.md)
- [ma_01: dbo.roll_oh_group_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_loc_yr_$sp.md)
- [ma_01: dbo.roll_oh_group_yr_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_yr_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_li_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_li_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_yr_$sp.md)

