# dbo.edit_OMS_trans_rcpt_ack

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| edit_timestamp | float | 8 | 0 |  |  |  |
| edit_stream_no | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| process_start_time | datetime | 8 | 0 |  |  |  |
| process_start_time_formatted | nvarchar | 68 | 0 |  |  |  |
