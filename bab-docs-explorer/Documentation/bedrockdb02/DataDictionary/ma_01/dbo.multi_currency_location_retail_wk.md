# dbo.multi_currency_location_retail_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 | YES |  |  |
| effective_from_year_wk | int | 4 | 0 | YES |  |  |
| effective_to_year_wk | int | 4 | 1 |  |  |  |
| retail_exchange_rate | float | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.import_hist_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_group_$sp.md)
- [ma_01: dbo.import_hist_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_style_$sp.md)
- [ma_01: dbo.import_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_styleclr_$sp.md)
- [ma_01: dbo.populate_multi_currency_by_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.populate_multi_currency_by_loc_pd_$sp.md)
- [ma_01: dbo.populate_multi_currency_by_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.populate_multi_currency_by_loc_wk_$sp.md)
- [ma_01: dbo.startup_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_group_loc_wk_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_wk_$sp.md)
- [ma_01: dbo.startup_oh_style_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_wk_$sp.md)
- [ma_01: dbo.startup_oh_styleclr_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_styleclr_loc_wk_$sp.md)
- [ma_01: dbo.startup_oo_all_group_$sp](../../StoredProcedures/ma_01/dbo.startup_oo_all_group_$sp.md)
- [ma_01: dbo.startup_oo_all_style_$sp](../../StoredProcedures/ma_01/dbo.startup_oo_all_style_$sp.md)
- [ma_01: dbo.startup_oo_all_styleclr_$sp](../../StoredProcedures/ma_01/dbo.startup_oo_all_styleclr_$sp.md)
- [ma_01: dbo.startup_plan_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_group_loc_wk_$sp.md)
- [ma_01: dbo.startup_style_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_style_loc_wk_$sp.md)
- [ma_01: dbo.startup_styleclr_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_styleclr_loc_wk_$sp.md)

