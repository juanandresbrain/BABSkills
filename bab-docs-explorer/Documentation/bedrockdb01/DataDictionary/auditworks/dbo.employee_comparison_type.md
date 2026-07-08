# dbo.employee_comparison_type

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| comparison_type | smallint | 2 | 0 | YES |  |  |
| comparison_description | nvarchar | 510 | 0 |  |  |  |
| primary_position_flag | tinyint | 1 | 0 |  |  |  |
| primary_selling_area_no_flag | tinyint | 1 | 0 |  |  |  |
| transaction_store_no_flag | tinyint | 1 | 0 |  |  |  |
| employee_no_flag | tinyint | 1 | 0 |  |  |  |
| relationship_type | nvarchar | 40 | 1 |  |  |  |
| relationship_position | nvarchar | 8 | 1 |  |  |  |
| selling_area_no | nvarchar | 6000 | 1 |  |  |  |
| primary_position | nvarchar | 6000 | 1 |  |  |  |
| include_in_productivity | tinyint | 1 | 0 |  |  |  |
| include_in_allocation | tinyint | 1 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| selling_area_flag | tinyint | 1 | 0 |  |  |  |
| home_store_no_flag | tinyint | 1 | 0 |  |  |  |
