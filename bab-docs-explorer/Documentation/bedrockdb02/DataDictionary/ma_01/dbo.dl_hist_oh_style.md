# dbo.dl_hist_oh_style

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_hist_oh_style_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| inventory_status_code | nvarchar | 6 | 0 |  |  |  |
| price_status_code | nvarchar | 6 | 0 |  |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |
| on_hand_retail | decimal | 9 | 0 |  |  |  |
| on_hand_cost | decimal | 9 | 0 |  |  |  |
| on_hand_retail_te | decimal | 9 | 0 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |
| duplicate_flag | bit | 1 | 0 |  |  |  |
| style_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| merch_year_wk_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| location_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| inv_status_code_fk_invld_flag | bit | 1 | 0 |  |  |  |
| price_status_code_fk_invld_flg | bit | 1 | 0 |  |  |  |
| hist_past_cutoff_week | tinyint | 1 | 0 |  |  |  |
| already_on_file_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.dl_hist_oh_style_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_style_vld_$sp.md)
- [ma_01: dbo.dl_hist_task_imp_ld_prep_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_imp_ld_prep_$sp.md)
- [ma_01: dbo.dl_hist_task_imp_trunc_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_imp_trunc_$sp.md)

