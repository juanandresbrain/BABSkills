# dbo.awt_post_void_detail

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | char | 1 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| post_voided_register | smallint | 2 | 0 |  |  |  |
| post_voided_trans_no | int | 4 | 0 |  |  |  |
| post_void_successful | tinyint | 1 | 0 |  |  |  |
| post_void_reason_code | smallint | 2 | 0 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
