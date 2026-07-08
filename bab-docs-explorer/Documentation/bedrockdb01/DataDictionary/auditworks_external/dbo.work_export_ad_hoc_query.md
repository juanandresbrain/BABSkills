# dbo.work_export_ad_hoc_query

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| app_id | smallint | 2 | 0 |  |  |  |
| comp_id | smallint | 2 | 0 |  |  |  |
| user_id | numeric | 9 | 0 |  |  |  |
| request_datetime | datetime | 8 | 0 |  |  |  |
| sql_command | nvarchar | 8000 | 0 |  |  |  |
| output_file_name | nvarchar | 510 | 1 |  |  |  |
