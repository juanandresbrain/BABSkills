# dbo.auditworks_parameter

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| par_name | varchar | 30 | 0 |  |  |  |
| par_value | varchar | 1000 | 1 |  |  |  |
| par_type | smallint | 2 | 0 |  |  |  |
| par_value_from_range | varchar | 50 | 1 |  |  |  |
| par_value_to_range | varchar | 50 | 1 |  |  |  |
| par_comment | varchar | 255 | 1 |  |  |  |
| code_type | smallint | 2 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| par_name_display_descr | varchar | 255 | 1 |  |  |  |
| min_compatible_exe | varchar | 20 | 1 |  |  |  |
| comment_resource_id | numeric | 9 | 1 |  |  |  |
| par_bin_value | binary | 16 | 1 |  |  |  |
| par_group_code | varchar | 20 | 0 |  |  |  |
| drop_down_query | nvarchar | 4000 | 1 |  |  |  |
| par_node_id | int | 4 | 0 |  |  |  |
| par_nullable_flag | tinyint | 1 | 0 |  |  |  |
| warning_code | nvarchar | 40 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
