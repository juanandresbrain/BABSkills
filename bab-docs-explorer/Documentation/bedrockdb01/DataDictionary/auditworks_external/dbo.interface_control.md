# dbo.interface_control

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| interface_status_flag | tinyint | 1 | 0 |  |  |  |
| if_rejection_rules_overriden | tinyint | 1 | 1 |  |  |  |
