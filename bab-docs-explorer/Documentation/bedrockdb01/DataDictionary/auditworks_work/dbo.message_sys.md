# dbo.message_sys

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| title | varchar | 60 | 0 |  |  |  |
| text | varchar | 255 | 0 |  |  |  |
| icon | tinyint | 1 | 0 |  |  |  |
| buttons | tinyint | 1 | 0 |  |  |  |
| defaultbutton | tinyint | 1 | 0 |  |  |  |
| timestamp | timestamp | 8 | 1 |  |  |  |
| resource_id | int | 4 | 1 |  |  |  |
