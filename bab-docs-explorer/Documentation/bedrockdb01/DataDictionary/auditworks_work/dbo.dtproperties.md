# dbo.dtproperties

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| objectid | int | 4 | 1 |  |  |  |
| property | varchar | 64 | 0 |  |  |  |
| value | varchar | 255 | 1 |  |  |  |
| uvalue | nvarchar | 510 | 1 |  |  |  |
| lvalue | image | 16 | 1 |  |  |  |
| version | int | 4 | 0 |  |  |  |
