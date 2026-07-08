# dbo.oim_message

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| oim_message_id | numeric | 9 | 0 | YES |  |  |
| entity_id | numeric | 9 | 0 |  |  |  |
| entity_code | smallint | 2 | 0 |  |  |  |
| message_type_description | nvarchar | 40 | 0 |  |  |  |
| message_text | nvarchar | 510 | 0 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
