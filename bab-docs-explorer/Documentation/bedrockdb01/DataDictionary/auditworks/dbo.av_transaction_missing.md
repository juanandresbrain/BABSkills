# dbo.av_transaction_missing

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| sales_date | smalldatetime | 4 | 0 |  |  |  |
| from_transaction_no | trno | 4 | 0 |  |  |  |
| to_transaction_no | trno | 4 | 0 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| verified_date | smalldatetime | 4 | 1 |  |  |  |
| verification_remark | nvarchar | 510 | 1 |  |  |  |
| verified_by_user_id | int | 4 | 1 |  |  |  |
| override_flag | tinyint | 1 | 1 |  |  |  |
