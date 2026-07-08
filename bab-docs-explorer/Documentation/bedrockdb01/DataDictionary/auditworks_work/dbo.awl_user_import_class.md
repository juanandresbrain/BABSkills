# dbo.awl_user_import_class

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| class_description | nvarchar | 60 | 0 |  |  |  |
| department_code | int | 4 | 0 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
| upc_lookup_division | tinyint | 1 | 1 |  |  |  |
| class_short_description | nvarchar | 24 | 1 |  |  |  |
| tax_item_group_id | numeric | 9 | 1 |  |  |  |
