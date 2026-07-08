# dbo.work_configuration_review_list

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_id | numeric | 9 | 0 | YES |  |  |
| session_id | binary | 16 | 0 |  |  |  |
| item_type | smallint | 2 | 0 |  |  |  |
| item_code | smallint | 2 | 0 |  |  |  |
| config_type | tinyint | 1 | 0 |  |  |  |
| review_start_time | datetime | 8 | 0 |  |  |  |
| selected_flag | tinyint | 1 | 0 |  |  |  |
| auto_config_verified | tinyint | 1 | 0 |  |  |  |
