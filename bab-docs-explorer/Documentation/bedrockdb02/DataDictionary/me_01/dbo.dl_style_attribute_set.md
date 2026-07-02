# dbo.dl_style_attribute_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_style_attribute_set_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| action_type | tinyint | 1 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| attribute_code | nvarchar | 12 | 0 |  |  |  |
| attribute_set_code | nvarchar | 12 | 0 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |
| dup_st_cd_att_cd_att_st_cd_add | bit | 1 | 0 |  |  |  |
| dup_stl_cd_excl_att_cd_add_flg | bit | 1 | 0 |  |  |  |
| dup_style_cd_attr_cd_del_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_imp_ld_prep_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_ld_prep_$sp.md)
- [me_01: dbo.dl_style_task_imp_trunc_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_trunc_$sp.md)

