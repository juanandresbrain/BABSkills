# dbo.employee_trans_allocation_type

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| allocation_type | nvarchar | 40 | 0 |  |  |  |
| allocation_type_desc | nvarchar | 400 | 0 |  |  |  |
| comparison_type | smallint | 2 | 0 |  |  |  |
| accumulation_basis | smallint | 2 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| last_executed_datetime | datetime | 8 | 1 |  |  |  |
