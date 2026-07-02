# dbo.startup_multi_currency_main_log

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| startup_main_id | int | 4 | 0 | YES |  |  |
| main_proc_name | nvarchar | 80 | 0 |  |  |  |
| start_time | smalldatetime | 4 | 0 |  |  |  |
| end_time | smalldatetime | 4 | 1 |  |  |  |
| completed_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.startup_correct_disc_ib_$sp](../../StoredProcedures/me_01/dbo.startup_correct_disc_ib_$sp.md)
- [me_01: dbo.startup_ib_$sp](../../StoredProcedures/me_01/dbo.startup_ib_$sp.md)
- [ma_01: dbo.startup_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_group_$sp.md)
- [ma_01: dbo.startup_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_style_$sp.md)
- [ma_01: dbo.startup_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_styleclr_$sp.md)
- [ma_01: dbo.startup_flsh_$sp](../../StoredProcedures/ma_01/dbo.startup_flsh_$sp.md)
- [ma_01: dbo.startup_hist_group_$sp](../../StoredProcedures/ma_01/dbo.startup_hist_group_$sp.md)
- [ma_01: dbo.startup_hist_style_$sp](../../StoredProcedures/ma_01/dbo.startup_hist_style_$sp.md)
- [ma_01: dbo.startup_hist_styleclr_$sp](../../StoredProcedures/ma_01/dbo.startup_hist_styleclr_$sp.md)
- [ma_01: dbo.startup_oh_group_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_$sp.md)
- [ma_01: dbo.startup_oh_style_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_$sp.md)
- [ma_01: dbo.startup_oh_styleclr_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_styleclr_$sp.md)
- [ma_01: dbo.startup_oo_all_$sp](../../StoredProcedures/ma_01/dbo.startup_oo_all_$sp.md)
- [ma_01: dbo.startup_plan_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_$sp.md)

