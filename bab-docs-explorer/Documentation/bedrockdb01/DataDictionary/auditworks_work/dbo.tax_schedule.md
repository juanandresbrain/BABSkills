# dbo.tax_schedule

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tax_schedule_id | binary | 16 | 0 |  |  |  |
| tax_schedule_description | varchar | 255 | 0 |  |  |  |
| tax_schedule_type | varchar | 20 | 0 |  |  |  |
| limit_to_tax_jurisdiction | char | 5 | 1 |  |  |  |
