# dbo.work_assigned_reg

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 1 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| sequential | tinyint | 1 | 0 |  |  |  |
| by_assigned_reg | tinyint | 1 | 0 |  |  |  |
| valid_register_no | tinyint | 1 | 0 |  |  |  |
| lower_transaction_limit | trno | 4 | 1 |  |  |  |
| upper_transaction_limit | trno | 4 | 1 |  |  |  |
