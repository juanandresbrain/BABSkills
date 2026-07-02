# dbo.dl_style_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_style_location_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| original_price_status_code | nvarchar | 6 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| current_price_status_code | nvarchar | 6 | 1 |  |  |  |
| mix_match_rule_code1 | int | 4 | 1 |  |  |  |
| mix_match_rule_code2 | int | 4 | 1 |  |  |  |
| mix_match_rule_code3 | int | 4 | 1 |  |  |  |
| mix_match_rule_code4 | int | 4 | 1 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |
| duplicate_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_imp_ld_prep_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_ld_prep_$sp.md)
- [me_01: dbo.dl_style_task_imp_trunc_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_trunc_$sp.md)

