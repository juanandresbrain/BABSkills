# dbo.employee_commission_rate_def

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_ecp_rate_id | numeric | 9 | 0 | YES |  |  |
| employee_commission_code | nvarchar | 6000 | 0 |  |  |  |
| employee_transaction_role | nvarchar | 6000 | 0 |  |  |  |
| item_commission_code | nvarchar | 6000 | 0 |  |  |  |
| store_commission_code | nvarchar | 6000 | 0 |  |  |  |
| transaction_commission_code | nvarchar | 6000 | 0 |  |  |  |
| tier_accumulation_basis | smallint | 2 | 0 |  |  |  |
| effective_from_date | datetime | 8 | 0 |  |  |  |
| commission_rate | numeric | 5 | 0 |  |  |  |
| commission_amount_per_item | money | 8 | 0 |  |  |  |
| effective_to_date | datetime | 8 | 1 |  |  |  |
| last_modified_datetime | datetime | 8 | 0 |  |  |  |
| employee_ecp_rate_descr | nvarchar | 510 | 1 |  |  |  |
| employee_ecp_rate_comment | nvarchar | 510 | 1 |  |  |  |
| sequence_no | int | 4 | 1 |  |  |  |
