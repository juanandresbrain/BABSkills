# dbo.employee_commission_code_xref

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_no | int | 4 | 0 |  |  |  |
| employee_commission_code | nvarchar | 40 | 0 |  |  |  |
| effective_from_date | datetime | 8 | 0 |  |  |  |
| effective_to_date | datetime | 8 | 1 |  |  |  |
