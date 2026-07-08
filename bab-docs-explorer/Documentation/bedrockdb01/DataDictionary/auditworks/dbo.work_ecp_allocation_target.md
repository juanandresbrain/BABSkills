# dbo.work_ecp_allocation_target

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| source_allocation_type | nvarchar | 40 | 0 |  |  |  |
| source_period_end_datetime | datetime | 8 | 0 |  |  |  |
| accum_basis_end_datetime | datetime | 8 | 0 |  |  |  |
| transaction_store_no | int | 4 | 0 |  |  |  |
| primary_position | nvarchar | 8 | 0 |  |  |  |
| primary_selling_area_no | int | 4 | 0 |  |  |  |
| employee_group_code | nvarchar | 40 | 1 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| selling_area_flag | tinyint | 1 | 0 |  |  |  |
| src_employee_no | int | 4 | 0 |  |  |  |
| numerator_amount | money | 8 | 0 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
