# Reporting.SQLServerUserAccountCleanupArchive

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServerName | nvarchar | 256 | 1 |  |  |  |
| DatabaseName | nvarchar | 256 | 1 |  |  |  |
| DatabaseUserName | nvarchar | 8000 | 1 |  |  |  |
| SecurableObjectName | nvarchar | 256 | 1 |  |  |  |
| SecurablePermissionName | nvarchar | 256 | 1 |  |  |  |
| SecurableStatus | nvarchar | 256 | 1 |  |  |  |
| SchemaName | nvarchar | 256 | 1 |  |  |  |
| SchemaOwner | nvarchar | 256 | 1 |  |  |  |
| ADUser | nvarchar | 8000 | 1 |  |  |  |
| EmployeeADGroup | nvarchar | 8000 | 1 |  |  |  |
| SecurityGroupName | nvarchar | 8000 | 1 |  |  |  |
| Reason | nvarchar | 30 | 1 |  |  |  |
| DropUserCommand | nvarchar | 8000 | 1 |  |  |  |
| DropLoginCommand | nvarchar | 8000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |

