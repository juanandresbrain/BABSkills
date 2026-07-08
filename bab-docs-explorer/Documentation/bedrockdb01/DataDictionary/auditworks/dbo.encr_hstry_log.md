# dbo.encr_hstry_log

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| activity_date | datetime | 8 | 0 |  |  |  |
| return_code | int | 4 | 0 |  |  |  |
| table_name | nvarchar | 160 | 0 |  |  |  |
| rows_found | int | 4 | 0 |  |  |  |
| key_start | nvarchar | 60 | 1 |  |  |  |
| key_end | nvarchar | 60 | 1 |  |  |  |
| action | tinyint | 1 | 1 |  |  |  |
| restart | tinyint | 1 | 1 |  |  |  |
| sql_cmd | nvarchar | 8000 | 1 |  |  |  |
