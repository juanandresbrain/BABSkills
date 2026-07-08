# dbo.Z_auditworks_parameter_05132015

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| par_name | varchar | 30 | 0 |  |  |  |
| par_value | nvarchar | 2000 | 1 |  |  |  |
| par_type | smallint | 2 | 0 |  |  |  |
| par_value_from_range | nvarchar | 100 | 1 |  |  |  |
| par_value_to_range | nvarchar | 100 | 1 |  |  |  |
| par_comment | nvarchar | 510 | 1 |  |  |  |
| code_type | smallint | 2 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| par_name_display_descr | nvarchar | 510 | 1 |  |  |  |
| min_compatible_exe | nvarchar | 40 | 1 |  |  |  |
| comment_resource_id | numeric | 9 | 1 |  |  |  |
| par_bin_value | binary | 16 | 1 |  |  |  |
| par_group_code | nvarchar | 40 | 0 |  |  |  |
| drop_down_query | nvarchar | 4000 | 1 |  |  |  |
| par_node_id | int | 4 | 0 |  |  |  |
| par_nullable_flag | tinyint | 1 | 0 |  |  |  |
| warning_code | varchar | 20 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
