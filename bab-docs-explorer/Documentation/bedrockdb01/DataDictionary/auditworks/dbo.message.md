# dbo.message

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| title | nvarchar | 120 | 0 |  |  |  |
| text | nvarchar | 510 | 0 |  |  |  |
| icon | tinyint | 1 | 0 |  |  |  |
| buttons | tinyint | 1 | 0 |  |  |  |
| defaultbutton | tinyint | 1 | 0 |  |  |  |
| timestamp | timestamp | 8 | 1 |  |  |  |
| resource_id | int | 4 | 1 |  |  |  |
| message_category | smallint | 2 | 1 |  |  |  |
