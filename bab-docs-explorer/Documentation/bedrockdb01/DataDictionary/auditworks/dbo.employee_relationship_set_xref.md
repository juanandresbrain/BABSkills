# dbo.employee_relationship_set_xref

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_no | int | 4 | 0 |  |  |  |
| effective_from_date | datetime | 8 | 0 |  |  |  |
| effective_to_date | datetime | 8 | 1 |  |  |  |
| relationship_set_id | numeric | 9 | 0 |  |  |  |
