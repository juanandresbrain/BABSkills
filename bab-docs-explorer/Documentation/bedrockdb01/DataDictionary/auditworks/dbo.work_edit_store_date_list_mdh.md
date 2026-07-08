# dbo.work_edit_store_date_list_mdh

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| posted_flag | tinyint | 1 | 1 |  |  |  |
| trickle_counts_flag | tinyint | 1 | 1 |  |  |  |
| status_already_existed | tinyint | 1 | 1 |  |  |  |
| processing_request | tinyint | 1 | 1 |  |  |  |
| sequential_series_present | tinyint | 1 | 1 |  |  |  |
