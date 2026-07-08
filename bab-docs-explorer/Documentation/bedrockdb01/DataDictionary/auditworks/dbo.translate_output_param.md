# dbo.translate_output_param

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| output_file | char | 1 | 0 |  |  |  |
| output_column | tinyint | 1 | 0 |  |  |  |
| output_datatype | char | 1 | 0 |  |  |  |
| column_max_length | smallint | 2 | 0 |  |  |  |
| column_mandatory_flag | tinyint | 1 | 0 |  |  |  |
| multiple_row_flag | tinyint | 1 | 0 |  |  |  |
| memo | varchar | 50 | 1 |  |  |  |
| default_value | char | 10 | 1 |  |  |  |
