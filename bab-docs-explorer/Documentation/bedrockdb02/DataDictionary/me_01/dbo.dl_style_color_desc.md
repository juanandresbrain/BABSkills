# dbo.dl_style_color_desc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_style_color_desc_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |
| locale_identifier | smallint | 2 | 0 |  |  |  |
| long_desc | nvarchar | 40 | 0 |  |  |  |
| short_desc | nvarchar | 16 | 0 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |
| duplicate_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_imp_ld_prep_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_ld_prep_$sp.md)
- [me_01: dbo.dl_style_task_imp_trunc_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_trunc_$sp.md)

