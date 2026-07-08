# dbo.audit_workflow_item

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| audit_workflow_code | smallint | 2 | 0 |  |  |  |
| workflow_issue_type | smallint | 2 | 0 |  |  |  |
| workflow_issue_code | smallint | 2 | 0 |  |  |  |
| workflow_issue_code_qualifier | nvarchar | 40 | 0 |  |  |  |
| sequence_no | smallint | 2 | 0 |  |  |  |
| audit_workflow_item_group | smallint | 2 | 0 |  |  |  |
| instructions | nvarchar | 4000 | 1 |  |  |  |
| last_update_datetime | datetime | 8 | 0 |  |  |  |
| workflow_item_no | nvarchar | 64 | 1 |  |  |  |
