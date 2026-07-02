# dbo.db_install_module

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_id | smallint | 2 | 0 |  |  |  |
| module_id | smallint | 2 | 0 |  |  |  |
| module_name | varchar | 30 | 0 |  |  |  |
| from_release_no | varchar | 10 | 1 |  |  |  |
| from_build_no | varchar | 10 | 1 |  |  |  |
| to_release_no | varchar | 10 | 0 |  |  |  |
| to_build_no | varchar | 10 | 0 |  |  |  |
| execution_status | smallint | 2 | 0 |  |  |  |
| rerunnable_token_value | nvarchar | 2000 | 1 |  |  |  |

