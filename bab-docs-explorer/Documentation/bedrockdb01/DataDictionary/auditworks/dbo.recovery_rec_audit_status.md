# dbo.recovery_rec_audit_status

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_process_id | numeric | 9 | 0 |  |  |  |
| process_id | binary | 16 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| actual_flag | tinyint | 1 | 0 |  |  |  |
| unrec_flag | tinyint | 1 | 0 |  |  |  |
| media_short | money | 8 | 1 |  |  |  |
| short_by_tender_over_limit | tinyint | 1 | 1 |  |  |  |
| unreconciled_media_present | tinyint | 1 | 1 |  |  |  |
| media_rec_only_lock | tinyint | 1 | 0 |  |  |  |
| prior_audit_status | smallint | 2 | 1 |  |  |  |
| prior_media_short | money | 8 | 1 |  |  |  |
| posting_date_time | datetime | 8 | 1 |  |  |  |
| locked_by_edit | tinyint | 1 | 1 |  |  |  |
| prior_unrec_media_present | tinyint | 1 | 1 |  |  |  |
