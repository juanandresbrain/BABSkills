# dbo.employee_10052010

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_no | int | 4 | 0 |  |  |  |
| employee_first_name | varchar | 20 | 0 |  |  |  |
| employee_last_name | varchar | 20 | 0 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| employee_type | char | 1 | 1 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| house_account_no | varchar | 80 | 1 |  |  |  |
| date_of_hire | smalldatetime | 4 | 1 |  |  |  |
| date_of_termination | smalldatetime | 4 | 1 |  |  |  |
| employee_department | smallint | 2 | 1 |  |  |  |
| timestamp | timestamp | 8 | 1 |  |  |  |
| active_flag | tinyint | 1 | 1 |  |  |  |
