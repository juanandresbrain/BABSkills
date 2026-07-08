# dbo.oim_attribute

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_attribute_id | numeric | 9 | 0 |  |  |  |
| entity_id | numeric | 9 | 0 |  |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| attribute_code | nvarchar | 12 | 0 |  |  |  |
| attribute_set_code | nvarchar | 12 | 0 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
