# dbo.av_authorization_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| av_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| card_type | nchar | 2 | 0 |  |  |  |
| authorization_no | nvarchar | 100 | 1 |  |  |  |
| expiry_date | int | 4 | 1 |  |  |  |
| swipe_indicator | tinyint | 1 | 1 |  |  |  |
| approval_message | nvarchar | 510 | 1 |  |  |  |
| license_no | nvarchar | 100 | 1 |  |  |  |
| pos_state_code | nvarchar | 6 | 1 |  |  |  |
| other_id_type | smallint | 2 | 1 |  |  |  |
| other_id | nvarchar | 100 | 1 |  |  |  |
| deferred_billing_date | smalldatetime | 4 | 1 |  |  |  |
| deferred_billing_plan | billing_plan_datatype | 9 | 1 |  |  |  |
| signature | image | 16 | 1 |  |  |  |
| customer_signature_obtained | tinyint | 1 | 0 |  |  |  |
| offline_flag | tinyint | 1 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
