# dbo.merch_datasource_execution_log

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| datasource_id | int | 4 | 1 |  |  |  |
| datasource_name | nvarchar | 60 | 1 |  |  |  |
| username | nvarchar | 140 | 1 |  |  |  |
| execution_duration | float | 8 | 1 |  |  |  |
| row_count | int | 4 | 1 |  |  |  |
| column_count | int | 4 | 1 |  |  |  |
| criteria_list | nvarchar | 4000 | 1 |  |  |  |
| execution_date | smalldatetime | 4 | 1 |  |  |  |

