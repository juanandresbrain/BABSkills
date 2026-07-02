# dbo.import_price_exception

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_price_exception_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| location_code | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| original_price_status_code | nvarchar | 6 | 1 |  |  |  |
| mix_match_rule_code1 | nvarchar | 20 | 1 |  |  |  |
| mix_match_rule_code2 | nvarchar | 20 | 1 |  |  |  |
| mix_match_rule_code3 | nvarchar | 20 | 1 |  |  |  |
| mix_match_rule_code4 | nvarchar | 20 | 1 |  |  |  |
| pricing_group_code | nvarchar | 20 | 1 |  |  |  |
| price_exception_type | tinyint | 1 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| current_price_status_code | nvarchar | 6 | 1 |  |  |  |
| exception_color_code | nvarchar | 6 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |
| jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
| size_code | nvarchar | 34 | 1 |  |  |  |

