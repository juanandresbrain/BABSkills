# dbo.cust_liab_auto_compl_line

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| units_auto_completed | unit_datatype | 9 | 0 |  |  |  |
| last_auto_completion_datetime | datetime | 8 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
