# dbo.bk_employee_type

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_type | char | 1 | 0 |  |  |  |
| employee_type_descr | varchar | 255 | 0 |  |  |  |
| regular_discount_rate | real | 4 | 0 |  |  |  |
| outlet_discount_rate | real | 4 | 0 |  |  |  |
| employee_discount_line_object | smallint | 2 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
