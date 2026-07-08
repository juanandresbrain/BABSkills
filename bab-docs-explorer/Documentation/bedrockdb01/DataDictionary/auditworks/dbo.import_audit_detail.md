# dbo.import_audit_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_id | numeric | 9 | 0 |  |  |  |
| column_name | nvarchar | 60 | 0 |  |  |  |
| before_value | nvarchar | 510 | 1 |  |  |  |
| after_value | nvarchar | 510 | 1 |  |  |  |
| before_description | nvarchar | 510 | 1 |  |  |  |
| after_description | nvarchar | 510 | 1 |  |  |  |
