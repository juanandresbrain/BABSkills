# dbo.note_type

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| note_type | smallint | 2 | 0 |  |  |  |
| code_type | smallint | 2 | 0 |  |  |  |
| note_type_description | nvarchar | 160 | 0 |  |  |  |
| code_meaning_control | nchar | 2 | 1 |  |  |  |
| par_type | smallint | 2 | 1 |  |  |  |
| par_value_from_range | nvarchar | 100 | 1 |  |  |  |
| par_value_to_range | nvarchar | 100 | 1 |  |  |  |
| par_comment | nvarchar | 510 | 1 |  |  |  |
| par_min_length | smallint | 2 | 1 |  |  |  |
| par_max_length | smallint | 2 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| employee_validation | tinyint | 1 | 1 |  |  |  |
