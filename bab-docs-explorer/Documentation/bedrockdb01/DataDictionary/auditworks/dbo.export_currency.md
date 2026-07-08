# dbo.export_currency

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| currency_id | numeric | 9 | 0 |  |  |  |
| currency_code | varchar | 3 | 0 |  |  |  |
| currency_description | varchar | 50 | 0 |  |  |  |
| active_flag | numeric | 5 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| display_mask | varchar | 20 | 1 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |
