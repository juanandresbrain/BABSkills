# dbo.startup_multi_currency_group_log

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| startup_group_id | int | 4 | 0 |  |  |  |
| time_dim_name | nvarchar | 6 | 0 |  |  |  |
| time_dim_value | int | 4 | 0 |  |  |  |
| module | nvarchar | 20 | 0 |  |  |  |
| proc_name | nvarchar | 100 | 0 |  |  |  |
| start_group_id | decimal | 9 | 1 |  |  |  |
| end_group_id | decimal | 9 | 1 |  |  |  |
| end_time | datetime | 8 | 1 |  |  |  |
| completed_flag | bit | 1 | 0 |  |  |  |
| date_dim_value | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.startup_cmp_group_loc_li_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_group_loc_li_$sp.md)
- [ma_01: dbo.startup_cmp_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_group_loc_pd_$sp.md)
- [ma_01: dbo.startup_cmp_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_group_loc_wk_$sp.md)
- [ma_01: dbo.startup_cmp_group_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_group_loc_yr_$sp.md)
- [ma_01: dbo.startup_flsh_group_loc_da_$sp](../../StoredProcedures/ma_01/dbo.startup_flsh_group_loc_da_$sp.md)
- [ma_01: dbo.startup_flsh_loc_da_$sp](../../StoredProcedures/ma_01/dbo.startup_flsh_loc_da_$sp.md)
- [ma_01: dbo.startup_group_loc_li_$sp](../../StoredProcedures/ma_01/dbo.startup_group_loc_li_$sp.md)
- [ma_01: dbo.startup_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_group_loc_pd_$sp.md)
- [ma_01: dbo.startup_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_group_loc_wk_$sp.md)
- [ma_01: dbo.startup_group_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_group_loc_yr_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_li_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_li_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_pd_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_wk_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_yr_$sp.md)
- [ma_01: dbo.startup_oo_all_group_$sp](../../StoredProcedures/ma_01/dbo.startup_oo_all_group_$sp.md)
- [ma_01: dbo.startup_plan_group_chn_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_group_chn_$sp.md)
- [ma_01: dbo.startup_plan_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_group_loc_pd_$sp.md)
- [ma_01: dbo.startup_plan_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_group_loc_wk_$sp.md)

