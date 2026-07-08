# dbo.work_ecp_allocation_source

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
| selling_area_flag | tinyint | 1 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| comparison_type | smallint | 2 | 0 |  |  |  |
| accumulation_basis_column | nvarchar | 60 | 0 |  |  |  |
| accumulation_basis | smallint | 2 | 0 |  |  |  |
| accum_basis_calendar_level | smallint | 2 | 0 |  |  |  |
| relationship_type | nvarchar | 40 | 1 |  |  |  |
| relationship_position | nvarchar | 8 | 1 |  |  |  |
| denominator_amount | money | 8 | 1 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| accum_basis_end_datetime_from | datetime | 8 | 1 |  |  |  |
| accum_basis_CLNDR_LVL_TYPE_ID | binary | 16 | 1 |  |  |  |
| basis_calendar_period_quantity | smallint | 2 | 0 |  |  |  |
