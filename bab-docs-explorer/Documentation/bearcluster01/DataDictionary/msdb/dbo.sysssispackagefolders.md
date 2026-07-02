# dbo.sysssispackagefolders

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| folderid | uniqueidentifier | 16 | 0 | YES |  |  |
| parentfolderid | uniqueidentifier | 16 | 1 |  |  |  |
| foldername | sysname | 256 | 0 |  |  |  |

