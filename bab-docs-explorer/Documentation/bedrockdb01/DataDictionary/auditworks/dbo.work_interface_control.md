# dbo.work_interface_control

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| interface_status_flag | tinyint | 1 | 0 |  |  |  |
| original_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
