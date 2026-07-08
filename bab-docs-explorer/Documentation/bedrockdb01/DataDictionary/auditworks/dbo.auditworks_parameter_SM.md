# dbo.auditworks_parameter_SM

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| par_name | varchar | 30 | 0 |  |  |  |
| par_value | varchar | 255 | 0 |  |  |  |
| par_type | smallint | 2 | 0 |  |  |  |
| par_value_from_range | varchar | 50 | 1 |  |  |  |
| par_value_to_range | varchar | 50 | 1 |  |  |  |
| par_comment | varchar | 255 | 1 |  |  |  |
| code_type | tinyint | 1 | 1 |  |  |  |
| resource_id | int | 4 | 1 |  |  |  |
| par_name_display_descr | varchar | 50 | 1 |  |  |  |
| min_compatible_exe | varchar | 20 | 1 |  |  |  |
| comment_resource_id | numeric | 9 | 1 |  |  |  |
