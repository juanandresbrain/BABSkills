# dbo.polling_result

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| register_poll_id | nvarchar | 30 | 0 |  |  |  |
| poll_date | smalldatetime | 4 | 0 |  |  |  |
| poll_attempt_no | tinyint | 1 | 0 |  |  |  |
| poll_status | smallint | 2 | 0 |  |  |  |
| poll_start_time | smalldatetime | 4 | 0 |  |  |  |
| poll_end_time | smalldatetime | 4 | 0 |  |  |  |
| bytes_downloaded | int | 4 | 0 |  |  |  |
| bytes_uploaded | int | 4 | 0 |  |  |  |
| blocks_downloaded | int | 4 | 0 |  |  |  |
| blocks_uploaded | int | 4 | 0 |  |  |  |
| transmission_line | tinyint | 1 | 1 |  |  |  |
| register_type | smallint | 2 | 1 |  |  |  |
| communication_type | nvarchar | 4 | 0 |  |  |  |
