# dbo.rebuild_request

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| request_id | numeric | 9 | 0 | YES |  |  |
| rebuild_type | smallint | 2 | 0 |  |  |  |
| request_datetime | datetime | 8 | 0 |  |  |  |
| user_name | nvarchar | 100 | 1 |  |  |  |
| rebuild_from_date | smalldatetime | 4 | 0 |  |  |  |
| rebuild_to_date | smalldatetime | 4 | 0 |  |  |  |
| rebuild_from_store | int | 4 | 1 |  |  |  |
| rebuild_to_store | int | 4 | 1 |  |  |  |
| tax_jurisdiction | nchar | 10 | 1 |  |  |  |
| user_id | int | 4 | 1 |  |  |  |
| copied_from_request_id | numeric | 9 | 1 |  |  |  |
