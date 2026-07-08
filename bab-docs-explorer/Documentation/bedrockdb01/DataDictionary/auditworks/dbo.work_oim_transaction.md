# dbo.work_oim_transaction

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| interface_id | tinyint | 1 | 0 |  |  |  |
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_void_flag | smallint | 2 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| interface_control_flag | numeric | 9 | 0 |  |  |  |
| if_rejection_rules_overriden | numeric | 9 | 1 |  |  |  |
| location_id | numeric | 5 | 1 |  |  |  |
