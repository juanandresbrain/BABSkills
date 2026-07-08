# dbo.ecp_import_reference_amt

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| effective_datetime | datetime | 8 | 0 |  |  |  |
| reference_amount_type | smallint | 2 | 0 |  |  |  |
| reference_amount | money | 8 | 0 |  |  |  |
| time_interval_duration_minutes | unit_datatype | 9 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| selling_area_no | int | 4 | 1 |  |  |  |
| employee_last_name | nvarchar | 200 | 1 |  |  |  |
| employee_first_name | nvarchar | 200 | 1 |  |  |  |
| position_code | nvarchar | 8 | 1 |  |  |  |
| entry_id | numeric | 9 | 0 | YES |  |  |
