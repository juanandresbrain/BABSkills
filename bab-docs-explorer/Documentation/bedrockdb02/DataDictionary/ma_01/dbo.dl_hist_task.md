# dbo.dl_hist_task

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_hist_task_id | bigint | 8 | 0 | YES |  |  |
| in_progress_flag | bit | 1 | 0 |  |  |  |
| start_date | smalldatetime | 4 | 0 |  |  |  |
| current_phase | tinyint | 1 | 0 |  |  |  |
| action_type | tinyint | 1 | 0 |  |  |  |
| overlay_flag | bit | 1 | 0 |  |  |  |
| hist_sku_file_name | nvarchar | 510 | 1 |  |  |  |
| hist_oh_sku_file_name | nvarchar | 510 | 1 |  |  |  |
| hist_styleclr_file_name | nvarchar | 510 | 1 |  |  |  |
| hist_oh_styleclr_file_name | nvarchar | 510 | 1 |  |  |  |
| hist_style_file_name | nvarchar | 510 | 1 |  |  |  |
| hist_oh_style_file_name | nvarchar | 510 | 1 |  |  |  |
| hist_group_file_name | nvarchar | 510 | 1 |  |  |  |
| hist_oh_group_file_name | nvarchar | 510 | 1 |  |  |  |
| encoding | tinyint | 1 | 0 |  |  |  |
| max_rejects | bigint | 8 | 0 |  |  |  |
| temp_folder | nvarchar | 510 | 0 |  |  |  |
| threads | int | 4 | 0 |  |  |  |
| max_rows_per_batch | int | 4 | 0 |  |  |  |
| pct_rows_per_batch | float | 8 | 0 |  |  |  |
| total_schema_rejects | bigint | 8 | 0 |  |  |  |
| max_dl_hist_sku_id | bigint | 8 | 0 |  |  |  |
| max_dl_hist_oh_sku_id | bigint | 8 | 0 |  |  |  |
| max_dl_hist_styleclr_id | bigint | 8 | 0 |  |  |  |
| max_dl_hist_oh_styleclr_id | bigint | 8 | 0 |  |  |  |
| max_dl_hist_style_id | bigint | 8 | 0 |  |  |  |
| max_dl_hist_oh_style_id | bigint | 8 | 0 |  |  |  |
| max_dl_hist_group_id | bigint | 8 | 0 |  |  |  |
| max_dl_hist_oh_group_id | bigint | 8 | 0 |  |  |  |
| tot_dl_hist_sku_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_hist_oh_sku_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_hist_styleclr_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_hist_oh_styleclr_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_hist_style_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_hist_oh_style_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_hist_group_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_hist_oh_group_rej | bigint | 8 | 0 |  |  |  |
| last_vld_dl_hist_sku_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_hist_oh_sku_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_hist_styleclr_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_hist_oh_stylecl_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_hist_style_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_hist_oh_style_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_hist_group_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_hist_oh_group_id | bigint | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.dl_hist_group_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_group_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_group_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_group_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_sku_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_sku_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_style_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_style_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_styleclr_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_styleclr_vld_$sp.md)
- [ma_01: dbo.dl_hist_sku_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_sku_vld_$sp.md)
- [ma_01: dbo.dl_hist_style_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_style_vld_$sp.md)
- [ma_01: dbo.dl_hist_styleclr_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_styleclr_vld_$sp.md)
- [ma_01: dbo.dl_hist_task_add_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_add_$sp.md)
- [ma_01: dbo.dl_hist_task_br_term_phs_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_br_term_phs_$sp.md)
- [ma_01: dbo.dl_hist_task_bus_rule_phs_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_bus_rule_phs_$sp.md)
- [ma_01: dbo.dl_hist_task_continue_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_continue_$sp.md)
- [ma_01: dbo.dl_hist_task_end_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_end_$sp.md)
- [ma_01: dbo.dl_hist_task_ld_term_phs_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_ld_term_phs_$sp.md)
- [ma_01: dbo.dl_hist_task_load_phs_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_load_phs_$sp.md)
- [ma_01: dbo.dl_hist_task_sch_term_phs_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_sch_term_phs_$sp.md)

