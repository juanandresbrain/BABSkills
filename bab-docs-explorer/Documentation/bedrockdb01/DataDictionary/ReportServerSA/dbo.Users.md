# dbo.Users

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UserID | uniqueidentifier | 16 | 0 |  |  |  |
| Sid | varbinary | 85 | 1 |  |  |  |
| UserType | int | 4 | 0 |  |  |  |
| AuthType | int | 4 | 0 |  |  |  |
| UserName | nvarchar | 520 | 1 |  |  |  |
