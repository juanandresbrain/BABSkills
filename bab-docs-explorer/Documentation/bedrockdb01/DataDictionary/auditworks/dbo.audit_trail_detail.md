# dbo.audit_trail_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_id | numeric | 9 | 0 |  |  |  |
| column_name | varchar | 30 | 0 |  |  |  |
| before_value | varchar | 255 | 1 |  |  |  |
| after_value | varchar | 255 | 1 |  |  |  |
| before_description | varchar | 255 | 1 |  |  |  |
| after_description | varchar | 255 | 1 |  |  |  |
