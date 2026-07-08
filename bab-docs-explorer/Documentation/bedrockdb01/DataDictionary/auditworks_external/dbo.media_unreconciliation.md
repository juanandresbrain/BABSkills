# dbo.media_unreconciliation

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| rec_id | tran_id_datatype | 9 | 0 |  |  |  |
| balancing_entity_id | numeric | 9 | 0 |  |  |  |
| unrec_activity_flag | smallint | 2 | 0 |  |  |  |
| period_from_date_time | datetime | 8 | 1 |  |  |  |
