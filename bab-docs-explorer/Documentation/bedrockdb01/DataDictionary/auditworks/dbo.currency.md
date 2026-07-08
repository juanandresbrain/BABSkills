# dbo.currency

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| currency_id | numeric | 9 | 0 |  |  |  |
| currency_code | nvarchar | 6 | 0 |  |  |  |
| currency_description | nvarchar | 100 | 0 |  |  |  |
| active_flag | numeric | 5 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| display_mask | nvarchar | 40 | 1 |  |  |  |
| currency_symbol | nvarchar | 50 | 1 |  |  |  |
