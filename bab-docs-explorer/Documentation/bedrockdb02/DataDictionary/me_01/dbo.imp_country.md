# dbo.imp_country

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_country_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nvarchar | 2 | 0 |  |  |  |
| country_code | nvarchar | 6 | 0 |  |  |  |
| country_description | nvarchar | 100 | 1 |  |  |  |
| currency_code | nvarchar | 6 | 1 |  |  |  |
| active_flag | nvarchar | 2 | 1 |  |  |  |
| european_union_flag | nvarchar | 2 | 1 |  |  |  |

