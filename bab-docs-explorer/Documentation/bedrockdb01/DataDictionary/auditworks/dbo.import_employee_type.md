# dbo.import_employee_type

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| employee_type | nchar | 2 | 0 |  |  |  |
| employee_type_descr | nvarchar | 100 | 0 |  |  |  |
| regular_discount_rate | real | 4 | 0 |  |  |  |
| outlet_discount_rate | real | 4 | 0 |  |  |  |
| employee_discount_line_object | smallint | 2 | 1 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
