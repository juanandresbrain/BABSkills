# dbo.export_series

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_series | nchar | 2 | 0 |  |  |  |
| description | nvarchar | 510 | 0 |  |  |  |
| sequential | tinyint | 1 | 0 |  |  |  |
| comments | nvarchar | 510 | 1 |  |  |  |
| code_meaning_control | nchar | 2 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| archived_series | nchar | 2 | 1 |  |  |  |
| by_assigned_reg | tinyint | 1 | 1 |  |  |  |
