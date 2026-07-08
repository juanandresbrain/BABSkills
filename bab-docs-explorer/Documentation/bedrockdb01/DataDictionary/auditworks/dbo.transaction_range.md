# dbo.transaction_range

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| first_transaction_no | trno | 4 | 0 |  |  |  |
| last_transaction_no | trno | 4 | 0 |  |  |  |
