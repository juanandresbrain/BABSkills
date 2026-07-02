# dbo.import_style_retail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_style_retail_id | decimal | 9 | 0 | YES |  |  |
| import_style_id | decimal | 9 | 1 |  |  |  |
| entity_type | nvarchar | 4 | 1 |  |  |  |
| action_type | nchar | 2 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| jurisdiction_code | nvarchar | 40 | 0 |  |  |  |
| compare_at_retail | decimal | 9 | 1 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| original_price_status_code | nvarchar | 6 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| current_price_status_code | nvarchar | 6 | 1 |  |  |  |
| mix_match_rule_code1 | int | 4 | 1 |  |  |  |
| mix_match_rule_code2 | int | 4 | 1 |  |  |  |
| mix_match_rule_code3 | int | 4 | 1 |  |  |  |
| mix_match_rule_code4 | int | 4 | 1 |  |  |  |

