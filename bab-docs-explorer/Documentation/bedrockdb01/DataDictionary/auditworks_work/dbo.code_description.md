# dbo.code_description

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| code_type | tinyint | 1 | 0 |  |  |  |
| code | smallint | 2 | 0 |  |  |  |
| code_display_descr | varchar | 80 | 0 |  |  |  |
| code_meaning_control | char | 1 | 0 |  |  |  |
| code_system_descr | varchar | 255 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
