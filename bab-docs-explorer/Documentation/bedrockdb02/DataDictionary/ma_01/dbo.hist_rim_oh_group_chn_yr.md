# dbo.hist_rim_oh_group_chn_yr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| merch_year | int | 4 | 0 | YES |  |  |
| rim_on_hand_retail | decimal | 9 | 1 |  |  |  |
| rim_on_hand_cost | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_hist_group_rim_$sp](../../StoredProcedures/ma_01/dbo.post_hist_group_rim_$sp.md)
- [ma_01: dbo.startup_hist_rim_oh_group_$sp](../../StoredProcedures/ma_01/dbo.startup_hist_rim_oh_group_$sp.md)

