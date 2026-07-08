# dbo.Ld_Media_Reconciliation_Log

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 1 |  |  |  |
| transaction_type | nchar | 20 | 1 |  |  |  |
| transaction_date | datetime | 8 | 1 |  |  |  |
| amount | decimal | 9 | 1 |  |  |  |
| process_name | varchar | 100 | 1 |  |  |  |
| process_date | datetime | 8 | 1 |  |  |  |
| uid | int | 4 | 0 | YES |  |  |
