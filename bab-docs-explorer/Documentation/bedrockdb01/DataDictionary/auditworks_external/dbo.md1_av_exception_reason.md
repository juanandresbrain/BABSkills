# dbo.md1_av_exception_reason

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| av_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| violated_exception_rule | smallint | 2 | 0 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| exception_type | tinyint | 1 | 0 |  |  |  |
| verified_date | smalldatetime | 4 | 1 |  |  |  |
| verification_remark | nvarchar | 510 | 1 |  |  |  |
| verified_by_user_id | int | 4 | 1 |  |  |  |
| override_flag | tinyint | 1 | 1 |  |  |  |
| memo1 | nvarchar | 510 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
