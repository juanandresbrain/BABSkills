# dbo.employee_comms_accum_basis

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| accumulation_basis | smallint | 2 | 0 |  |  |  |
| accumulation_basis_desc | nvarchar | 510 | 0 |  |  |  |
| employee_transaction_role | nvarchar | 40 | 0 |  |  |  |
| item_commission_code | nvarchar | 40 | 0 |  |  |  |
| store_commission_code | nvarchar | 40 | 0 |  |  |  |
| transaction_commission_code | nvarchar | 40 | 0 |  |  |  |
| calendar_level | smallint | 2 | 1 |  |  |  |
| accumulation_basis_column | nvarchar | 60 | 0 |  |  |  |
| auto_commission_adj_id | numeric | 5 | 1 |  |  |  |
| payroll_entry_hour_type | smallint | 2 | 1 |  |  |  |
| calendar_period_quantity | smallint | 2 | 0 |  |  |  |
| last_year_flag | tinyint | 1 | 0 |  |  |  |
| reference_amount_type | smallint | 2 | 1 |  |  |  |
