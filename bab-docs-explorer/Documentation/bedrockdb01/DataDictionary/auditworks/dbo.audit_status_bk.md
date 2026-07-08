# dbo.audit_status_bk

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| sales_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| audit_status | smallint | 2 | 0 |  |  |  |
| status_date | smalldatetime | 4 | 0 |  |  |  |
| sos_check_complete | tinyint | 1 | 0 |  |  |  |
| short_by_tender_over_limit | tinyint | 1 | 0 |  |  |  |
| opening_drawer_discrepancy | tinyint | 1 | 0 |  |  |  |
| media_rec_verified | tinyint | 1 | 0 |  |  |  |
| exceptions_verified | tinyint | 1 | 0 |  |  |  |
| duplicate_verified | tinyint | 1 | 0 |  |  |  |
| translate_error_verified | tinyint | 1 | 0 |  |  |  |
| missing_verified | tinyint | 1 | 0 |  |  |  |
| transaction_rollover_flag | tinyint | 1 | 0 |  |  |  |
| archived_flag | tinyint | 1 | 0 |  |  |  |
| update_in_progress | smallint | 2 | 0 |  |  |  |
| sa_reject_qty | smallint | 2 | 0 |  |  |  |
| if_reject_qty | smallint | 2 | 0 |  |  |  |
| translate_error_qty | smallint | 2 | 0 |  |  |  |
| missing_qty | numeric | 9 | 0 |  |  |  |
| exception_qty | smallint | 2 | 0 |  |  |  |
| duplicate_qty | smallint | 2 | 0 |  |  |  |
| media_short | money | 8 | 1 |  |  |  |
| valid_qty | smallint | 2 | 0 |  |  |  |
| first_transaction_no | trno | 4 | 1 |  |  |  |
| last_transaction_no | trno | 4 | 1 |  |  |  |
| status_remark | nvarchar | 510 | 1 |  |  |  |
| register_poll_id | nvarchar | 30 | 1 |  |  |  |
| edited_date | smalldatetime | 4 | 1 |  |  |  |
| trickle_in_progress_flag | tinyint | 1 | 1 |  |  |  |
| completion_date_time | datetime | 8 | 1 |  |  |  |
| unreconciled_media_present | tinyint | 1 | 1 |  |  |  |
| status_set_by_user_id | int | 4 | 1 |  |  |  |
