# dbo.work_audit_status_flags

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| function_no | tinyint | 1 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| process_id | binary | 16 | 0 |  |  |  |
