# dbo.work_scale_int_del

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| min_transaction_date | smalldatetime | 4 | 1 |  |  |  |
| max_transaction_date | smalldatetime | 4 | 1 |  |  |  |
