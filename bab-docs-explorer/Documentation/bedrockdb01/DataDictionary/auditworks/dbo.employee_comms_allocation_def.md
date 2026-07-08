# dbo.employee_comms_allocation_def

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_ecp_alloc_id | numeric | 9 | 0 | YES |  |  |
| employee_commission_code | nvarchar | 6000 | 0 |  |  |  |
| employee_transaction_role | nvarchar | 6000 | 0 |  |  |  |
| item_commission_code | nvarchar | 6000 | 0 |  |  |  |
| store_commission_code | nvarchar | 6000 | 0 |  |  |  |
| transaction_commission_code | nvarchar | 6000 | 0 |  |  |  |
| effective_from_date | datetime | 8 | 0 |  |  |  |
| allocation_type | nvarchar | 40 | 0 |  |  |  |
| allocation_percent | numeric | 5 | 0 |  |  |  |
| effective_to_date | datetime | 8 | 1 |  |  |  |
| last_modified_datetime | datetime | 8 | 0 |  |  |  |
