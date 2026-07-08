# dbo.awl_user_import_department

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| department_code | int | 4 | 0 |  |  |  |
| department_description | nvarchar | 60 | 0 |  |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
