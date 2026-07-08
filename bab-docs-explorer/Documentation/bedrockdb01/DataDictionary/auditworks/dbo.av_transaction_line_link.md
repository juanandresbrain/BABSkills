# dbo.av_transaction_line_link

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| av_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| linked_line_id | numeric | 5 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
