# dbo.work_ecp_tier_amount_current

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tier_accumulation_basis | smallint | 2 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| calendar_level | smallint | 2 | 0 |  |  |  |
| pay_period_end_datetime | datetime | 8 | 0 |  |  |  |
| accumulation_basis_column | nvarchar | 60 | 0 |  |  |  |
| current_transaction_net_amount | money | 8 | 0 |  |  |  |
| current_transaction_units | numeric | 9 | 0 |  |  |  |
