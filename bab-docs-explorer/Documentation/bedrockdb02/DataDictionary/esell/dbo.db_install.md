# dbo.db_install

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_id | smallint | 2 | 0 | YES |  |  |
| install_id | binary | 16 | 0 |  |  |  |
| original_filename | varchar | 100 | 0 |  |  |  |
| generated_by | varchar | 50 | 0 |  |  |  |
| executed_by | varchar | 50 | 0 |  |  |  |
| execution_date | smalldatetime | 4 | 0 |  |  |  |
| execution_status | smallint | 2 | 0 |  |  |  |
| application_name | varchar | 30 | 0 |  |  |  |

