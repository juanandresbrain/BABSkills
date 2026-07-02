# dbo.dl_pack_upc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_pack_upc_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| activation_date | smalldatetime | 4 | 0 |  |  |  |
| pack_code | nvarchar | 40 | 0 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |
| duplicate_flag | bit | 1 | 0 |  |  |  |
| upc_no_on_file_flag | bit | 1 | 0 |  |  |  |
| upc_no_not_a_no_flag | bit | 1 | 0 |  |  |  |
| upc_no_length_invalid_flag | bit | 1 | 0 |  |  |  |
| upc_no_first_digit_invalid_flg | bit | 1 | 0 |  |  |  |
| upc_no_vndr_chck_dgt_invld_flg | bit | 1 | 0 |  |  |  |
| pack_code_invalid_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_imp_ld_prep_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_ld_prep_$sp.md)
- [me_01: dbo.dl_style_task_imp_trunc_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_trunc_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)

