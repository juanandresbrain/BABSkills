# dbo.hist_cmp_group_loc_pd

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| merch_year_pd | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| component_type_code | smallint | 2 | 0 | YES |  |  |
| history_component_id | smallint | 2 | 0 | YES |  |  |
| component_units | int | 4 | 0 |  |  |  |
| component_retail | decimal | 9 | 0 |  |  |  |
| component_cost | decimal | 9 | 0 |  |  |  |
| component_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| component_retail_te | decimal | 9 | 0 |  |  |  |
| component_sellcurr_retail_te | decimal | 9 | 0 |  |  |  |
| component_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_group_$sp.md)
- [ma_01: dbo.post_hist_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.post_hist_cmp_group_$sp.md)
- [ma_01: dbo.reclass_hist_cmp_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_cmp_$sp.md)
- [ma_01: dbo.reclass_oh_post_adjust_cmp_$sp](../../StoredProcedures/ma_01/dbo.reclass_oh_post_adjust_cmp_$sp.md)
- [ma_01: dbo.startup_cmp_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_group_loc_pd_$sp.md)
- [ma_01: dbo.startup_cmp_group_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_group_loc_yr_$sp.md)
- [ma_01: dbo.summarize_hist_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.summarize_hist_cmp_group_$sp.md)

