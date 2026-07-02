# dbo.dl_upc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_upc_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| vendor_style | nvarchar | 80 | 0 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| style_color_short_desc | nvarchar | 16 | 1 |  |  |  |
| style_color_long_desc | nvarchar | 40 | 1 |  |  |  |
| style_color_fashion_flag | bit | 1 | 1 |  |  |  |
| style_color_reorder_flag | bit | 1 | 1 |  |  |  |
| nrf_code | int | 4 | 1 |  |  |  |
| size_category_code | nvarchar | 16 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |
| style_size_ticket_lbl_override | nvarchar | 34 | 1 |  |  |  |
| style_size_reorder_flag | bit | 1 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| upc_type | tinyint | 1 | 0 |  |  |  |
| activation_date | smalldatetime | 4 | 1 |  |  |  |
| upc_first_part_length | tinyint | 1 | 1 |  |  |  |
| style_color_flag | bit | 1 | 0 |  |  |  |
| style_size_flag | bit | 1 | 0 |  |  |  |
| style_size_grid_id | decimal | 9 | 0 |  |  |  |
| style_size_category_id | decimal | 9 | 0 |  |  |  |
| style_color_on_file_flag | bit | 1 | 0 |  |  |  |
| nrf_code_size_category_id | decimal | 9 | 0 |  |  |  |
| nrf_code_size_master_id | int | 4 | 0 |  |  |  |
| size_code_size_category_id | decimal | 9 | 0 |  |  |  |
| size_code_size_master_id | int | 4 | 0 |  |  |  |
| size_category_id | decimal | 9 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| style_size_on_file_flag | bit | 1 | 0 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |
| duplicate_flag | bit | 1 | 0 |  |  |  |
| upc_no_on_file_flag | bit | 1 | 0 |  |  |  |
| vndr_code_vndr_style_fk_valid | tinyint | 1 | 0 |  |  |  |
| color_code_missing_flag | bit | 1 | 0 |  |  |  |
| color_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| new_color_short_desc_chgs_flag | bit | 1 | 0 |  |  |  |
| new_color_long_desc_chgs_flag | bit | 1 | 0 |  |  |  |
| new_color_fashion_flg_chgs_flg | bit | 1 | 0 |  |  |  |
| new_color_reorder_flg_chgs_flg | bit | 1 | 0 |  |  |  |
| nrf_code_missing_flag | bit | 1 | 0 |  |  |  |
| nrf_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| size_cat_code_missing_flag | bit | 1 | 0 |  |  |  |
| size_code_missing_flag | bit | 1 | 0 |  |  |  |
| size_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| nrf_code_size_code_diff_flag | bit | 1 | 0 |  |  |  |
| style_has_no_size_grid_flag | bit | 1 | 0 |  |  |  |
| size_not_in_size_grid_flag | bit | 1 | 0 |  |  |  |
| first_sizes_cat_code_chgs_flag | bit | 1 | 0 |  |  |  |
| new_size_not_in_size_cat_flag | bit | 1 | 0 |  |  |  |
| new_size_has_inactive_cat_flag | bit | 1 | 0 |  |  |  |
| new_size_ticket_label_chgs_flg | bit | 1 | 0 |  |  |  |
| new_size_reorder_flg_chgs_flg | bit | 1 | 0 |  |  |  |
| upc_no_not_a_no_flag | bit | 1 | 0 |  |  |  |
| upc_no_length_invalid_flag | bit | 1 | 0 |  |  |  |
| upc_no_first_digit_invalid_flg | bit | 1 | 0 |  |  |  |
| upc_no_vndr_chck_dgt_invld_flg | bit | 1 | 0 |  |  |  |
| activation_date_missing_flag | bit | 1 | 0 |  |  |  |
| upc_first_part_len_invalid_flg | bit | 1 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_imp_ld_prep_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_ld_prep_$sp.md)
- [me_01: dbo.dl_style_task_imp_trunc_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_trunc_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)

