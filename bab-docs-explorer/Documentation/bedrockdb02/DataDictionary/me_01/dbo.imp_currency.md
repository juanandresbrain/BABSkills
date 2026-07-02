# dbo.imp_currency

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_currency_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nvarchar | 2 | 0 |  |  |  |
| currency_code | nvarchar | 6 | 0 |  |  |  |
| currency_description | nvarchar | 100 | 1 |  |  |  |
| currency_symbol | nvarchar | 6 | 1 |  |  |  |
| active_flag | nvarchar | 2 | 1 |  |  |  |

