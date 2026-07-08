# dbo.export_code_descr

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| code_type | tinyint | 1 | 0 |  |  |  |
| code | smallint | 2 | 0 |  |  |  |
| code_display_descr | nvarchar | 510 | 0 |  |  |  |
| code_meaning_control | nchar | 2 | 0 |  |  |  |
| code_system_descr | nvarchar | 510 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| min_compatible_exe | nvarchar | 40 | 1 |  |  |  |
| alpha_code | nvarchar | 40 | 1 |  |  |  |
