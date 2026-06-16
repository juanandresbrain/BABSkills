# Reporting.SSRSServerUserAccountCleanup

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UserName | nvarchar | 520 | 1 |  |  |  |
| RoleName | nvarchar | 520 | 1 |  |  |  |
| RoleDescription | nvarchar | 1024 | 1 |  |  |  |
| ReportPath | nvarchar | 850 | 1 |  |  |  |
| ReportName | nvarchar | 850 | 1 |  |  |  |
| ReportServer | varchar | 100 | 1 |  |  |  |
| EmployeeADGroup | nvarchar | 8000 | 1 |  |  |  |
| ADUser | nvarchar | 8000 | 1 |  |  |  |
| ADGroupNameJoinField | nvarchar | 8000 | 1 |  |  |  |

