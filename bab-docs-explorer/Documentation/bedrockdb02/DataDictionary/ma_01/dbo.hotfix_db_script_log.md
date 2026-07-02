# dbo.hotfix_db_script_log

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fixed_in_build | nvarchar | 40 | 0 |  |  |  |
| hotfix_number | nvarchar | 40 | 0 |  |  |  |
| defect_number | nvarchar | 40 | 0 |  |  |  |
| defect_abstract | nvarchar | 400 | 0 |  |  |  |
| script_name | nvarchar | 100 | 0 |  |  |  |
| script_run_date | smalldatetime | 4 | 0 |  |  |  |

