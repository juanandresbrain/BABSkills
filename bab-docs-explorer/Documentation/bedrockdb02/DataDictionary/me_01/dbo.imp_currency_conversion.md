# dbo.imp_currency_conversion

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_currency_conversion_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| currency_conversion_type | smallint | 2 | 0 |  |  |  |
| from_currency_code | nvarchar | 6 | 0 |  |  |  |
| to_currency_code | nvarchar | 6 | 0 |  |  |  |
| effective_from_date | smalldatetime | 4 | 0 |  |  |  |
| exchange_rate | float | 8 | 1 |  |  |  |

