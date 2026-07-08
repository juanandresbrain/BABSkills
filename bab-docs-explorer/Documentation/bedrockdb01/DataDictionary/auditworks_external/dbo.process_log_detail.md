# dbo.process_log_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| log_entry_datetime | datetime | 8 | 0 |  |  |  |
| process_no | smallint | 2 | 0 |  |  |  |
| log_entry_id | numeric | 9 | 0 | YES |  |  |
| process_name | nvarchar | 100 | 0 |  |  |  |
| process_info_type | nvarchar | 2000 | 1 |  |  |  |
| process_info_string | nvarchar | 4000 | 1 |  |  |  |
| process_info_number | numeric | 13 | 1 |  |  |  |
| process_info_binary | binary | 16 | 1 |  |  |  |
| process_info_date | datetime | 8 | 1 |  |  |  |
| spid | int | 4 | 1 |  |  |  |
