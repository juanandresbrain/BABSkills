# dbo.dl_style_vendor

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_style_vendor_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| current_cost | decimal | 9 | 1 |  |  |  |
| currency_code | nvarchar | 6 | 1 |  |  |  |
| pseudo_flag | bit | 1 | 0 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |
| dup_style_code_vendor_code_flg | bit | 1 | 0 |  |  |  |
| dup_vndr_code_vndr_style_flag | bit | 1 | 0 |  |  |  |
| stl_cd_vndr_cd_in_dl_stl_flag | bit | 1 | 0 |  |  |  |
| vndr_cd_vndr_stl_in_dl_stl_flg | bit | 1 | 0 |  |  |  |
| style_cd_vndr_cd_on_file_flag | bit | 1 | 0 |  |  |  |
| vndr_cd_vndr_style_on_file_flg | bit | 1 | 0 |  |  |  |
| style_code_fk_valid | tinyint | 1 | 0 |  |  |  |
| vendor_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| vendor_style_missing_flag | bit | 1 | 0 |  |  |  |
| vendor_style_for_pseudo_flag | bit | 1 | 0 |  |  |  |
| current_cost_for_pseudo_flag | bit | 1 | 0 |  |  |  |
| curr_cost_curn_cd_fk_invld_flg | bit | 1 | 0 |  |  |  |
| curr_cost_curn_cd_for_psdo_flg | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_imp_ld_prep_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_ld_prep_$sp.md)
- [me_01: dbo.dl_style_task_imp_trunc_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_trunc_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)

