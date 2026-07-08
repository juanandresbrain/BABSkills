# dbo.extract_history

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| queue_id | int | 4 | 0 |  |  |  |
| extract_date | nvarchar | 18 | 0 |  |  |  |
| extract_time | nvarchar | 10 | 0 |  |  |  |
| actual_time | nvarchar | 10 | 1 |  |  |  |
| last_extract | tinyint | 1 | 0 |  |  |  |
