# dbo.dl_style_attachment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_style_attachment_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| attachment_type_code | nvarchar | 6 | 0 |  |  |  |
| attachment_desc | nvarchar | 100 | 0 |  |  |  |
| attachment_date | smalldatetime | 4 | 0 |  |  |  |
| primary_flag | bit | 1 | 0 |  |  |  |
| url | nvarchar | 510 | 0 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_imp_ld_prep_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_ld_prep_$sp.md)
- [me_01: dbo.dl_style_task_imp_trunc_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_trunc_$sp.md)

