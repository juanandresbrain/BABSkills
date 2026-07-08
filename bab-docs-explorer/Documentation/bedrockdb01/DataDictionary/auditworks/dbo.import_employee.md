# dbo.import_employee

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_type | nchar | 2 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| employee_first_name | nvarchar | 40 | 0 |  |  |  |
| employee_last_name | nvarchar | 40 | 0 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| employee_type | nchar | 2 | 1 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| house_account_no | nvarchar | 40 | 1 |  |  |  |
| date_of_hire | smalldatetime | 4 | 1 |  |  |  |
| date_of_termination | smalldatetime | 4 | 1 |  |  |  |
| employee_department | smallint | 2 | 1 |  |  |  |
| import_id | numeric | 9 | 0 | YES |  |  |
| active_flag | tinyint | 1 | 1 |  |  |  |
