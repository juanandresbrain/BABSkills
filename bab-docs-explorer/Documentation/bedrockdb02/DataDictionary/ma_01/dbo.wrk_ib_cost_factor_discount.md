# dbo.wrk_ib_cost_factor_discount

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| ib_cost_factor_discount_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| cost_factor_discount_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| extended_cost | decimal | 9 | 0 |  |  |  |
| extended_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.cleanup_wrk_ib_cost_factor_$sp](../../StoredProcedures/ma_01/dbo.cleanup_wrk_ib_cost_factor_$sp.md)
- [ma_01: dbo.get_max_wrk_ib_cf_id_$sp](../../StoredProcedures/ma_01/dbo.get_max_wrk_ib_cf_id_$sp.md)
- [ma_01: dbo.post_wrk_ib_cost_fact_disc_$sp](../../StoredProcedures/ma_01/dbo.post_wrk_ib_cost_fact_disc_$sp.md)
- [ma_01: dbo.wpost_cf_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_cmp_group_$sp.md)
- [ma_01: dbo.wpost_cf_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_cmp_style_$sp.md)
- [ma_01: dbo.wpost_cf_cmp_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_cmp_style_color_$sp.md)
- [ma_01: dbo.wpost_cf_hist_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_hist_group_$sp.md)
- [ma_01: dbo.wpost_cf_hist_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_hist_style_$sp.md)
- [ma_01: dbo.wprep_cf_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.wprep_cf_cmp_group_$sp.md)
- [ma_01: dbo.wprep_cf_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.wprep_cf_cmp_style_$sp.md)
- [ma_01: dbo.wprep_cf_cmp_style_color_$sp](../../StoredProcedures/ma_01/dbo.wprep_cf_cmp_style_color_$sp.md)
- [ma_01: dbo.wprep_cf_hist_group_$sp](../../StoredProcedures/ma_01/dbo.wprep_cf_hist_group_$sp.md)
- [ma_01: dbo.wprep_cf_hist_style_$sp](../../StoredProcedures/ma_01/dbo.wprep_cf_hist_style_$sp.md)

