# dbo.line_object

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| line_object | smallint | 2 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| line_object_description | nvarchar | 510 | 0 |  |  |  |
| default_tax_rate_code | tinyint | 1 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| object_export_code | nvarchar | 40 | 1 |  |  |  |
| tax_item_group_id | numeric | 9 | 1 |  |  |  |
| proration_method | tinyint | 1 | 1 |  |  |  |
| lookup_pos_code | nvarchar | 1000 | 1 |  |  |  |
| pos_description_token_list | nvarchar | 1000 | 1 |  |  |  |
| disregard_pos_descr_change | tinyint | 1 | 0 |  |  |  |
| lookup_partial_pos_code | nvarchar | 1000 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| approval_status_date | smalldatetime | 4 | 0 |  |  |  |
| auto_config_verified | tinyint | 1 | 0 |  |  |  |
| override_pos_mapping | tinyint | 1 | 1 |  |  |  |
