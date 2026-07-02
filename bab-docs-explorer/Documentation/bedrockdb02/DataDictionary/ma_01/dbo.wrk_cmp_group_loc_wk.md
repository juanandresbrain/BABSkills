# dbo.wrk_cmp_group_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | decimal | 9 | 0 |  |  |  |
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| component_type_code | smallint | 2 | 0 |  |  |  |
| history_component_id | smallint | 2 | 0 |  |  |  |
| component_units | int | 4 | 0 |  |  |  |
| component_retail | decimal | 9 | 0 |  |  |  |
| component_cost | decimal | 9 | 0 |  |  |  |
| component_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| component_retail_te | decimal | 9 | 0 |  |  |  |
| component_selling_retail_te | decimal | 9 | 0 |  |  |  |
| component_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.cleanup_wrk_cmp_$sp](../../StoredProcedures/ma_01/dbo.cleanup_wrk_cmp_$sp.md)
- [ma_01: dbo.post_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_group_$sp.md)
- [ma_01: dbo.prep_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.prep_cmp_group_$sp.md)
- [ma_01: dbo.prep_wrk_cmp_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_cmp_$sp.md)
- [ma_01: dbo.validate_cmp_$sp](../../StoredProcedures/ma_01/dbo.validate_cmp_$sp.md)
- [ma_01: dbo.wpost_cf_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_cf_cmp_group_$sp.md)
- [ma_01: dbo.wpost_iv_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_iv_cmp_group_$sp.md)

