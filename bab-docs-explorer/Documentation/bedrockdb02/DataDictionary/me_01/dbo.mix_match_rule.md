# dbo.mix_match_rule

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mix_match_rule_id | decimal | 9 | 0 | YES |  |  |
| mix_match_rule_code | int | 4 | 0 |  |  |  |
| mix_match_rule_desc | nvarchar | 80 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| extended_price | decimal | 9 | 1 |  |  |  |
| tolerance_percent | decimal | 5 | 1 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)

