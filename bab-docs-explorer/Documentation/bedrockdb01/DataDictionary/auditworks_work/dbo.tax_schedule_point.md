# dbo.tax_schedule_point

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_schedule_id | binary | 16 | 0 |  |  |  |
| point_no | smallint | 2 | 1 |  |  |  |
| from_threshold_amount | money | 8 | 0 |  |  |  |
| to_threshold_amount | money | 8 | 0 |  |  |  |
| tax_amount | money | 8 | 0 |  |  |  |
| tax_rate | numeric | 5 | 0 |  |  |  |
