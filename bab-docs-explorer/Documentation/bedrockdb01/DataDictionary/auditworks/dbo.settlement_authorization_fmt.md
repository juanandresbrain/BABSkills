# dbo.settlement_authorization_fmt

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| auth_format | tinyint | 1 | 0 |  |  |  |
| auth_format_description | nvarchar | 60 | 0 |  |  |  |
| auth_approval_level | nvarchar | 8 | 1 |  |  |  |
| service_parameters | nvarchar | 60 | 1 |  |  |  |
