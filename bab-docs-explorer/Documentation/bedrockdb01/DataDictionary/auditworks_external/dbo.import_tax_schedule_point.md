# dbo.import_tax_schedule_point

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| tax_schedule_id | binary | 16 | 0 |  |  |  |
| from_threshold_amount | money | 8 | 0 |  |  |  |
| to_threshold_amount | money | 8 | 0 |  |  |  |
| tax_amount | money | 8 | 0 |  |  |  |
| tax_rate | numeric | 5 | 0 |  |  |  |
| entry_id | numeric | 9 | 0 | YES |  |  |
