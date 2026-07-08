# dbo.ecp_variable_amt

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| auto_adj_period_end_datetime | datetime | 8 | 0 |  |  |  |
| ecp_variable_id | numeric | 9 | 0 |  |  |  |
| variable_amount | numeric | 9 | 0 |  |  |  |
| comparison_type | smallint | 2 | 1 |  |  |  |
| accumulation_basis | smallint | 2 | 1 |  |  |  |
| accumulation_basis_column | nvarchar | 60 | 1 |  |  |  |
| comp_employee_no | int | 4 | 1 |  |  |  |
| comp_primary_position | nvarchar | 8 | 1 |  |  |  |
| comp_primary_selling_area_no | int | 4 | 1 |  |  |  |
| comp_home_store_no | int | 4 | 1 |  |  |  |
| comp_employee_group_code | nvarchar | 40 | 1 |  |  |  |
| ct_relationship_type | nvarchar | 40 | 1 |  |  |  |
| ct_relationship_position | nvarchar | 8 | 1 |  |  |  |
| comp_transaction_store_no | int | 4 | 1 |  |  |  |
| comp_selling_area_group | int | 4 | 1 |  |  |  |
