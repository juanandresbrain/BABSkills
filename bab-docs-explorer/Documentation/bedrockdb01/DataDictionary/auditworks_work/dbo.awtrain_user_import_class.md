# dbo.awtrain_user_import_class

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | char | 1 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| class_description | varchar | 30 | 0 |  |  |  |
| department_code | smallint | 2 | 0 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
