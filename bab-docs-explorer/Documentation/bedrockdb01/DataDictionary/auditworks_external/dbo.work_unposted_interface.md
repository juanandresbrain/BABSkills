# dbo.work_unposted_interface

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| interface_control_flag | numeric | 9 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
