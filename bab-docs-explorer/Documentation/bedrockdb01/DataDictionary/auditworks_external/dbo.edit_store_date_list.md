# dbo.edit_store_date_list

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| edit_timestamp | float | 8 | 0 |  |  |  |
| posted_flag | tinyint | 1 | 0 |  |  |  |
| trickle_counts_flag | tinyint | 1 | 0 |  |  |  |
| status_already_existed | tinyint | 1 | 1 |  |  |  |
| processing_request | tinyint | 1 | 1 |  |  |  |
| completion_date_time | datetime | 8 | 1 |  |  |  |
| batch_process_no | tinyint | 1 | 1 |  |  |  |
| batch_started | datetime | 8 | 1 |  |  |  |
| batch_ended | datetime | 8 | 1 |  |  |  |
| sequential_series_present | tinyint | 1 | 1 |  |  |  |
