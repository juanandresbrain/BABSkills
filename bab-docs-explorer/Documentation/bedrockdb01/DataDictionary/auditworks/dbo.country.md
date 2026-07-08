# dbo.country

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| country_id | numeric | 9 | 0 |  |  |  |
| currency_id | numeric | 9 | 0 |  |  |  |
| country_code | varchar | 3 | 0 |  |  |  |
| country_description | varchar | 255 | 0 |  |  |  |
| active_flag | numeric | 5 | 0 |  |  |  |
| updatestamp | timestamp | 8 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
