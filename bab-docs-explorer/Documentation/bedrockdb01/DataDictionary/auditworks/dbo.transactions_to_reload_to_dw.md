# dbo.transactions_to_reload_to_dw

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
