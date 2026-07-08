# dbo.work_impacted_interfaces

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| old_interface_status_flag | tinyint | 1 | 1 |  |  |  |
| new_interface_status_flag | tinyint | 1 | 0 |  |  |  |
