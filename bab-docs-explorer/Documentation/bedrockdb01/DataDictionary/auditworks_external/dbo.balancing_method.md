# dbo.balancing_method

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| balancing_method | smallint | 2 | 0 |  |  |  |
| balancing_method_description | nvarchar | 510 | 0 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| store_no_factor | tinyint | 1 | 0 |  |  |  |
| register_no_factor | tinyint | 1 | 0 |  |  |  |
| till_no_factor | tinyint | 1 | 0 |  |  |  |
| cashier_no_factor | tinyint | 1 | 0 |  |  |  |
| bank_no_factor | tinyint | 1 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
