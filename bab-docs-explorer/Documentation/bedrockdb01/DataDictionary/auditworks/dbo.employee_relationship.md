# dbo.employee_relationship

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| relationship_type | nvarchar | 40 | 0 |  |  |  |
| employee_group_code | nvarchar | 40 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| relationship_position | nvarchar | 8 | 1 |  |  |  |
| effective_from_date | datetime | 8 | 0 |  |  |  |
| effective_to_date | datetime | 8 | 1 |  |  |  |
