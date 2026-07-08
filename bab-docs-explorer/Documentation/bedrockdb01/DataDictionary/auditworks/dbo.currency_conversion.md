# dbo.currency_conversion

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| currency_conversion_id | int | 4 | 0 |  |  |  |
| currency_conversion_type_id | int | 4 | 0 |  |  |  |
| currency_id | numeric | 9 | 0 |  |  |  |
| effective_date_from | smalldatetime | 4 | 0 |  |  |  |
| effective_date_to | smalldatetime | 4 | 1 |  |  |  |
| exchange_rate | numeric | 9 | 0 |  |  |  |
