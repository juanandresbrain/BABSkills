# dbo.input_authorization_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| input_id | numeric | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| customer_signature_obtained | tinyint | 1 | 0 |  |  |  |
| authorization_no | nvarchar | 100 | 1 |  |  |  |
| expiry_date | int | 4 | 1 |  |  |  |
| swipe_indicator | tinyint | 1 | 1 |  |  |  |
| approval_message | nvarchar | 510 | 1 |  |  |  |
| license_no | nvarchar | 100 | 1 |  |  |  |
| pos_state_code | nvarchar | 6 | 1 |  |  |  |
| other_id_type | smallint | 2 | 1 |  |  |  |
| other_id | nvarchar | 100 | 1 |  |  |  |
| card_type | nchar | 2 | 0 |  |  |  |
| deferred_billing_date | smalldatetime | 4 | 1 |  |  |  |
| deferred_billing_plan | billing_plan_datatype | 9 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
| offline_flag | tinyint | 1 | 1 |  |  |  |
