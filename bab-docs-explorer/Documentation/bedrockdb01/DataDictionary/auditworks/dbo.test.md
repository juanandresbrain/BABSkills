# dbo.test

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| transaction_void_flag | smallint | 2 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| gross_line_amount | line_amount | 9 | 0 |  |  |  |
| line_void_flag | tinyint | 1 | 0 |  |  |  |
