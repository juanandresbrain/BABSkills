# dbo.work_control_interfaces

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| type | nchar | 2 | 0 |  |  |  |
| entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| interface_control_flag | tinyint | 1 | 0 |  |  |  |
| customer_liability_check | tinyint | 1 | 1 |  |  |  |
| line_modified_flag | tinyint | 1 | 1 |  |  |  |
| all_modifications_relevant | tinyint | 1 | 1 |  |  |  |
| effective_date | smalldatetime | 4 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| applicability_method | tinyint | 1 | 1 |  |  |  |
