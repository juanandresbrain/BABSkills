# dbo.tblDBA_SecurityReport

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InstanceName | nvarchar | 256 | 1 |  |  |  |
| DatabaseName | nvarchar | 256 | 1 |  |  |  |
| UserName | nvarchar | 256 | 1 |  |  |  |
| gid | smallint | 2 | 1 |  |  |  |
| ObjectName | nvarchar | 256 | 1 |  |  |  |
| ObjectType | char | 2 | 1 |  |  |  |
| ObjectID | int | 4 | 1 |  |  |  |
| SELECT | varchar | 15 | 1 |  |  |  |
| INSERT | varchar | 15 | 1 |  |  |  |
| UPDATE | varchar | 15 | 1 |  |  |  |
| DELETE | varchar | 15 | 1 |  |  |  |
| EXECUTE | varchar | 15 | 1 |  |  |  |
