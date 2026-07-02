# dbo.dl_hist_oh_sku

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_hist_oh_sku_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| inventory_status_code | nvarchar | 6 | 0 |  |  |  |
| price_status_code | nvarchar | 6 | 0 |  |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |
| dup_upc_wk_loc_is_ps_flag | bit | 1 | 0 |  |  |  |
| dup_sku_wk_loc_is_ps_flag | bit | 1 | 0 |  |  |  |
| upc_no_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| merch_year_wk_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| location_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| inv_status_code_fk_invld_flag | bit | 1 | 0 |  |  |  |
| price_status_code_fk_invld_flg | bit | 1 | 0 |  |  |  |
| hist_past_cutoff_week | tinyint | 1 | 0 |  |  |  |
| already_on_file_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.dl_hist_oh_sku_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_sku_vld_$sp.md)
- [ma_01: dbo.dl_hist_task_imp_ld_prep_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_imp_ld_prep_$sp.md)
- [ma_01: dbo.dl_hist_task_imp_trunc_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_imp_trunc_$sp.md)

