# dbo.store_audit_status_20230701

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| sales_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| archived_flag | tinyint | 1 | 0 |  |  |  |
| sos_check_complete | tinyint | 1 | 0 |  |  |  |
| short_by_tender_over_limit | tinyint | 1 | 0 |  |  |  |
| opening_drawer_discrepancy | tinyint | 1 | 0 |  |  |  |
| media_rec_verified | tinyint | 1 | 0 |  |  |  |
| update_in_progress | smallint | 2 | 0 |  |  |  |
| process_id | binary | 16 | 0 |  |  |  |
| store_audit_status | smallint | 2 | 0 |  |  |  |
| store_status_date | smalldatetime | 4 | 0 |  |  |  |
| media_short | money | 8 | 1 |  |  |  |
| status_remark | nvarchar | 510 | 1 |  |  |  |
| trickle_in_progress_flag | tinyint | 1 | 1 |  |  |  |
| lp_status | int | 4 | 1 |  |  |  |
| day_end_posting_date | datetime | 8 | 1 |  |  |  |
| completion_date_time | datetime | 8 | 1 |  |  |  |
| status_set_by_user_id | smallint | 2 | 1 |  |  |  |
| auto_accepted | tinyint | 1 | 0 |  |  |  |
| scaleout_move_requested | datetime | 8 | 1 |  |  |  |
