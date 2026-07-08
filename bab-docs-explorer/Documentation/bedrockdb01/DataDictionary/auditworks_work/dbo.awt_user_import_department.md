# dbo.awt_user_import_department

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | char | 1 | 0 |  |  |  |
| department_code | smallint | 2 | 0 |  |  |  |
| department_description | varchar | 30 | 0 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
