# dbo.transaction_generation_source

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_no | tinyint | 1 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| display_flag | smallint | 2 | 1 |  |  |  |
