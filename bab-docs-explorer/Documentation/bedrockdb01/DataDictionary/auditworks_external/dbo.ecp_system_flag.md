# dbo.ecp_system_flag

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| flag_name | nvarchar | 60 | 0 |  |  |  |
| flag_datetime_value | datetime | 8 | 1 |  |  |  |
| flag_numeric_value | numeric | 9 | 1 |  |  |  |
| flag_alpha_value | nvarchar | 6000 | 1 |  |  |  |
| flag_comment | nvarchar | 510 | 1 |  |  |  |
| code_type | tinyint | 1 | 1 |  |  |  |
| flag_datetime_initialize_value | datetime | 8 | 1 |  |  |  |
| flag_numeric_initialize_value | numeric | 9 | 1 |  |  |  |
| flag_alpha_initialize_value | nvarchar | 510 | 1 |  |  |  |
