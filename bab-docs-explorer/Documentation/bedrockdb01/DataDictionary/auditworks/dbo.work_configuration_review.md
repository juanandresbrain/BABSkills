# dbo.work_configuration_review

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| session_id | binary | 16 | 0 |  |  |  |
| detail_flag | tinyint | 1 | 0 |  |  |  |
| work_list_entry_id | numeric | 9 | 1 |  |  |  |
| config_type | tinyint | 1 | 0 |  |  |  |
| item_code | smallint | 2 | 0 |  |  |  |
| item_type | smallint | 2 | 0 |  |  |  |
| table_maintenance_area_id | numeric | 5 | 0 |  |  |  |
| group1_setting | nvarchar | 510 | 1 |  |  |  |
| group2_setting | nvarchar | 510 | 1 |  |  |  |
| field_code | nvarchar | 510 | 1 |  |  |  |
| field_setting | nvarchar | 510 | 1 |  |  |  |
| field_priority_no | smallint | 2 | 0 |  |  |  |
| config_count | int | 4 | 1 |  |  |  |
| config_fcount | int | 4 | 1 |  |  |  |
| review_start_time | datetime | 8 | 0 |  |  |  |
| auto_config_verified | tinyint | 1 | 1 |  |  |  |
