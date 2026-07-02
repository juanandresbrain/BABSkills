# dbo.ranking_group_import

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ranking_group_import_id | int | 4 | 0 | YES |  |  |
| path_file | nvarchar | 1000 | 0 |  |  |  |
| import_data | nvarchar | -1 | 0 |  |  |  |
| import_type | tinyint | 1 | 0 |  |  |  |
| import_status | tinyint | 1 | 0 |  |  |  |
| description | nvarchar | 100 | 1 |  |  |  |
| executed_by | nvarchar | 200 | 1 |  |  |  |
| execution_date | smalldatetime | 4 | 1 |  |  |  |
| scheduled_date | smalldatetime | 4 | 1 |  |  |  |
| import_errors | nvarchar | -1 | 1 |  |  |  |

