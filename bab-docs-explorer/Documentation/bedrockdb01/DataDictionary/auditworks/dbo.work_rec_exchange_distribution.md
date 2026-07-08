# dbo.work_rec_exchange_distribution

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rec_process_id | numeric | 9 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| rec_amount | money | 8 | 0 |  |  |  |
| exchange_amount | money | 8 | 0 |  |  |  |
| exchange_calculated | money | 8 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 0 |  |  |  |
| rec_side | smallint | 2 | 0 |  |  |  |
| rec_amount_subtype | tinyint | 1 | 0 |  |  |  |
