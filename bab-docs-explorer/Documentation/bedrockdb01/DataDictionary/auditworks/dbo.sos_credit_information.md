# dbo.sos_credit_information

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| account_no | nvarchar | 160 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| return_amount | money | 8 | 0 |  |  |  |
| post_void_amount | money | 8 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 1 |  |  |  |
| transaction_series | nchar | 2 | 1 |  |  |  |
