# dbo.work_ecp_variable_amt

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
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
| variable_amount | numeric | 9 | 0 |  |  |  |
| comp_transaction_store_no | int | 4 | 1 |  |  |  |
| comp_selling_area_group | int | 4 | 1 |  |  |  |
| ecp_variable_id | numeric | 9 | 0 | YES |  |  |
