# dbo.Roles

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RoleID | uniqueidentifier | 16 | 0 |  |  |  |
| RoleName | nvarchar | 520 | 0 |  |  |  |
| Description | nvarchar | 1024 | 1 |  |  |  |
| TaskMask | nvarchar | 64 | 0 |  |  |  |
| RoleFlags | tinyint | 1 | 0 |  |  |  |
