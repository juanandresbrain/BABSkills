# dbo.transaction_category

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_category | tinyint | 1 | 0 |  |  |  |
| description | nvarchar | 510 | 0 |  |  |  |
| update_register_activity | smallint | 2 | 0 |  |  |  |
| archive_handling_method | smallint | 2 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| min_compatible_exe | nvarchar | 40 | 1 |  |  |  |
| system_transaction_category | tinyint | 1 | 0 |  |  |  |
| system_ownership_flag | tinyint | 1 | 0 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
