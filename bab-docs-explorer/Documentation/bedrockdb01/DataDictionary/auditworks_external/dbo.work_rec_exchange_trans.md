# dbo.work_rec_exchange_trans

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_process_id | numeric | 9 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 0 |  |  |  |
| rec_side | smallint | 2 | 0 |  |  |  |
| rec_amount_subtype | tinyint | 1 | 0 |  |  |  |
| rec_amount | money | 8 | 0 |  |  |  |
| exchange_amount | money | 8 | 0 |  |  |  |
| calculated_exchange_amount | money | 8 | 0 |  |  |  |
| void_flag | smallint | 2 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| date_reconciled | smalldatetime | 4 | 1 |  |  |  |
