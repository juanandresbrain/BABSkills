# dbo.auditworks_system_flag_bk

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| flag_name | varchar | 30 | 0 |  |  |  |
| flag_datetime_value | datetime | 8 | 1 |  |  |  |
| flag_numeric_value | numeric | 9 | 1 |  |  |  |
| flag_alpha_value | varchar | 255 | 1 |  |  |  |
| flag_comment | varchar | 255 | 1 |  |  |  |
| code_type | tinyint | 1 | 1 |  |  |  |
| flag_datetime_initialize_value | datetime | 8 | 1 |  |  |  |
| flag_numeric_initialize_value | numeric | 9 | 1 |  |  |  |
| flag_alpha_initialize_value | varchar | 255 | 1 |  |  |  |
