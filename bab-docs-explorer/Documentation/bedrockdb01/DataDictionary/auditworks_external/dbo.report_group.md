# dbo.report_group

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| report_group_code | char | 10 | 0 |  |  |  |
| report_group_description | nvarchar | 40 | 0 |  |  |  |
| feature_code | char | 4 | 0 |  |  |  |
| last_audit_datetime | smalldatetime | 4 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
