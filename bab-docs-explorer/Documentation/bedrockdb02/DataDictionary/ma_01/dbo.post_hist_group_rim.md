# dbo.post_hist_group_rim

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| inventory_reductions_cost | decimal | 9 | 1 |  |  |  |
| shrink_total_cost | decimal | 9 | 1 |  |  |  |
| markdown_cost | decimal | 9 | 1 |  |  |  |
| markdown_promo_cost | decimal | 9 | 1 |  |  |  |
| rim_additions_cost | decimal | 9 | 1 |  |  |  |
| distribution_net_retail | decimal | 9 | 1 |  |  |  |
| rim_on_hand_retail | decimal | 9 | 1 |  |  |  |
| purchase_net_retail | decimal | 9 | 1 |  |  |  |
| transfer_net_retail | decimal | 9 | 1 |  |  |  |
| markups_retail | decimal | 9 | 1 |  |  |  |
| rim_on_hand_cost | decimal | 9 | 1 |  |  |  |
| inventory_reductions_cost_local | decimal | 9 | 1 |  |  |  |
| shrink_total_cost_local | decimal | 9 | 1 |  |  |  |
| markdown_cost_local | decimal | 9 | 1 |  |  |  |
| markdown_promo_cost_local | decimal | 9 | 1 |  |  |  |
| rim_additions_cost_local | decimal | 9 | 1 |  |  |  |
| distribution_net_retail_local | decimal | 9 | 1 |  |  |  |
| rim_on_hand_retail_local | decimal | 9 | 1 |  |  |  |
| purchase_net_retail_local | decimal | 9 | 1 |  |  |  |
| transfer_net_retail_local | decimal | 9 | 1 |  |  |  |
| markups_retail_local | decimal | 9 | 1 |  |  |  |
| rim_on_hand_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_hist_group_rim_$sp](../../StoredProcedures/ma_01/dbo.post_hist_group_rim_$sp.md)

