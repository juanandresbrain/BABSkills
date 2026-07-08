# dbo.import_tax_schedule

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| tax_schedule_id | binary | 16 | 0 |  |  |  |
| tax_schedule_description | nvarchar | 510 | 0 |  |  |  |
| tax_schedule_type | nvarchar | 40 | 0 |  |  |  |
| limit_to_tax_jurisdiction | nchar | 10 | 1 |  |  |  |
| entry_id | numeric | 9 | 0 | YES |  |  |
