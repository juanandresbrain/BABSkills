# dbo.work_ecp_auto_adj_basis

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_no | int | 4 | 0 |  |  |  |
| comparison_type | smallint | 2 | 0 |  |  |  |
| accumulation_basis | smallint | 2 | 1 |  |  |  |
| accumulation_basis_column | nvarchar | 60 | 1 |  |  |  |
| comp_primary_position | nvarchar | 8 | 1 |  |  |  |
| comp_primary_selling_area_no | int | 4 | 1 |  |  |  |
| comp_home_store_no | int | 4 | 1 |  |  |  |
| comp_employee_no | int | 4 | 1 |  |  |  |
| comp_employee_group_code | nvarchar | 40 | 1 |  |  |  |
| ct_relationship_type | nvarchar | 40 | 1 |  |  |  |
| ct_relationship_position | nvarchar | 8 | 1 |  |  |  |
| basis_calendar_level | smallint | 2 | 1 |  |  |  |
| basis_CLNDR_LVL_TYPE_ID | binary | 16 | 1 |  |  |  |
| basis_CLNDR_LVL_SEQ | smallint | 2 | 1 |  |  |  |
| comp_transaction_store_no | int | 4 | 1 |  |  |  |
| comp_selling_area_group | int | 4 | 1 |  |  |  |
| basis_reference_amount_type | smallint | 2 | 1 |  |  |  |
