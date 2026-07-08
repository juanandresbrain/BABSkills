# dbo.sa_parameter_node_info

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| par_node_id | int | 4 | 0 |  |  |  |
| par_node_name | nvarchar | 60 | 0 |  |  |  |
| par_node_name_display_descr | nvarchar | 510 | 0 |  |  |  |
| par_node_type | smallint | 2 | 0 |  |  |  |
| parent_par_node_id | int | 4 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
