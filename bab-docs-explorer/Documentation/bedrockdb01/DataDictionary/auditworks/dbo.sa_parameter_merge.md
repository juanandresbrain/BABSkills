# dbo.sa_parameter_merge

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| par_source_table | nvarchar | 60 | 0 |  |  |  |
| par_name | nvarchar | 60 | 0 |  |  |  |
| par_type | smallint | 2 | 0 |  |  |  |
| par_value_from_range | nvarchar | 100 | 1 |  |  |  |
| par_value_to_range | nvarchar | 100 | 1 |  |  |  |
| par_comment | nvarchar | 510 | 1 |  |  |  |
| code_type | smallint | 2 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| par_name_display_descr | nvarchar | 510 | 1 |  |  |  |
| min_compatible_exe | nvarchar | 40 | 1 |  |  |  |
| comment_resource_id | numeric | 9 | 1 |  |  |  |
| par_group_code | nvarchar | 40 | 0 |  |  |  |
| drop_down_query | nvarchar | 4000 | 1 |  |  |  |
| par_node_id | int | 4 | 0 |  |  |  |
| par_nullable_flag | tinyint | 1 | 0 |  |  |  |
| warning_code | nvarchar | 40 | 1 |  |  |  |
