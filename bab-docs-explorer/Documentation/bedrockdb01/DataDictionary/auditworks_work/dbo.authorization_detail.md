# dbo.authorization_detail

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| card_type | char | 1 | 0 |  |  |  |
| authorization_no | varchar | 50 | 1 |  |  |  |
| expiry_date | int | 4 | 1 |  |  |  |
| swipe_indicator | tinyint | 1 | 1 |  |  |  |
| approval_message | varchar | 255 | 1 |  |  |  |
| license_no | varchar | 50 | 1 |  |  |  |
| pos_state_code | varchar | 2 | 1 |  |  |  |
| other_id_type | smallint | 2 | 1 |  |  |  |
| other_id | varchar | 50 | 1 |  |  |  |
| deferred_billing_date | smalldatetime | 4 | 1 |  |  |  |
| deferred_billing_plan | numeric | 9 | 1 |  |  |  |
| signature | image | 16 | 1 |  |  |  |
| customer_signature_obtained | tinyint | 1 | 0 |  |  |  |
| offline_flag | tinyint | 1 | 1 |  |  |  |
