# dbo.dbhotfix_tracking

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hotfix_no | nvarchar | 20 | 1 |  |  |  |
| hotfix_issue_date | datetime | 8 | 1 |  |  |  |
| hotfix_description | nvarchar | 2000 | 1 |  |  |  |
| applied_to_db_version | nvarchar | 100 | 1 |  |  |  |
| date_applied | datetime | 8 | 0 |  |  |  |
