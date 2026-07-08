# dbo.if_interface_control_bkup

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_entry_no | numeric | 9 | 0 |  |  |  |
| interface_id | int | 4 | 0 |  |  |  |
| interface_control_flag | numeric | 9 | 0 |  |  |  |
| effective_date | datetime | 8 | 1 |  |  |  |
| interface_posting_date | datetime | 8 | 1 |  |  |  |
| if_rejection_rules_overriden | numeric | 9 | 1 |  |  |  |
