# dbo.startup_multi_currency_style_log

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| startup_style_id | int | 4 | 0 |  |  |  |
| time_dim_name | nvarchar | 6 | 0 |  |  |  |
| time_dim_value | int | 4 | 0 |  |  |  |
| module | nvarchar | 20 | 0 |  |  |  |
| proc_name | nvarchar | 100 | 0 |  |  |  |
| start_style_id | decimal | 9 | 1 |  |  |  |
| end_style_id | decimal | 9 | 1 |  |  |  |
| end_time | datetime | 8 | 1 |  |  |  |
| completed_flag | bit | 1 | 0 |  |  |  |
| date_dim_value | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.startup_cmp_style_loc_li_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_style_loc_li_$sp.md)
- [ma_01: dbo.startup_cmp_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_style_loc_pd_$sp.md)
- [ma_01: dbo.startup_cmp_style_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_style_loc_wk_$sp.md)
- [ma_01: dbo.startup_cmp_style_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_style_loc_yr_$sp.md)
- [ma_01: dbo.startup_flsh_style_loc_da_$sp](../../StoredProcedures/ma_01/dbo.startup_flsh_style_loc_da_$sp.md)
- [ma_01: dbo.startup_oh_style_loc_li_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_li_$sp.md)
- [ma_01: dbo.startup_oh_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_pd_$sp.md)
- [ma_01: dbo.startup_oh_style_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_wk_$sp.md)
- [ma_01: dbo.startup_oh_style_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_yr_$sp.md)
- [ma_01: dbo.startup_oo_all_style_$sp](../../StoredProcedures/ma_01/dbo.startup_oo_all_style_$sp.md)
- [ma_01: dbo.startup_style_loc_li_$sp](../../StoredProcedures/ma_01/dbo.startup_style_loc_li_$sp.md)
- [ma_01: dbo.startup_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_style_loc_pd_$sp.md)
- [ma_01: dbo.startup_style_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_style_loc_wk_$sp.md)
- [ma_01: dbo.startup_style_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_style_loc_yr_$sp.md)

