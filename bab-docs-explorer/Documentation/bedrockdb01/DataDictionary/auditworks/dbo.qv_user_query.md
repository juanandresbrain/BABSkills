# dbo.qv_user_query

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| query_id | int | 4 | 0 |  |  |  |
| name | nvarchar | 60 | 0 |  |  |  |
| description | nvarchar | 510 | 0 |  |  |  |
| created_by | nvarchar | 60 | 0 |  |  |  |
| user_stored_proc | nvarchar | 100 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
