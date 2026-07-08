# dbo.audit_comment

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| comment_id | numeric | 9 | 0 | YES |  |  |
| user_name | nvarchar | 60 | 0 |  |  |  |
| last_update_datetime | datetime | 8 | 0 |  |  |  |
| comment_text | text | 16 | 0 |  |  |  |
