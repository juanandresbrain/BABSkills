# dbo.awtrain_authorization_detail

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
| customer_signature_obtained | tinyint | 1 | 0 |  |  |  |
| authorization_no | authorization_datatype | 20 | 1 |  |  |  |
| expiry_date | int | 4 | 1 |  |  |  |
| swipe_indicator | tinyint | 1 | 1 |  |  |  |
| approval_message | varchar | 255 | 1 |  |  |  |
| license_no | varchar | 32 | 1 |  |  |  |
| pos_state_code | varchar | 2 | 1 |  |  |  |
| other_id_type | smallint | 2 | 1 |  |  |  |
| other_id | varchar | 16 | 1 |  |  |  |
| card_type | char | 1 | 0 |  |  |  |
| deferred_billing_date | smalldatetime | 4 | 1 |  |  |  |
| deferred_billing_plan | billing_plan_datatype | 9 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
