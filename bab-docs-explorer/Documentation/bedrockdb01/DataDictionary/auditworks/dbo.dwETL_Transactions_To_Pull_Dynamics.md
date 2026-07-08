# dbo.dwETL_Transactions_To_Pull_Dynamics

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| transaction_series | char | 1 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
