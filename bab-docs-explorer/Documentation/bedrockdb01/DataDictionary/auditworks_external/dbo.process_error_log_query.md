# dbo.process_error_log_query

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_name | nvarchar | 510 | 0 |  |  |  |
| message_category_from | smallint | 2 | 0 |  |  |  |
| message_category_until | smallint | 2 | 0 |  |  |  |
| last_entry_id | numeric | 9 | 0 |  |  |  |
| process_no | numeric | 9 | 1 |  |  |  |
