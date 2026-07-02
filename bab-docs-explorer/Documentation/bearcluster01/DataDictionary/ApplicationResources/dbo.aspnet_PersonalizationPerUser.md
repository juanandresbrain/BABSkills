# dbo.aspnet_PersonalizationPerUser

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | uniqueidentifier | 16 | 0 | YES |  |  |
| PathId | uniqueidentifier | 16 | 1 |  | YES |  |
| UserId | uniqueidentifier | 16 | 1 |  | YES |  |
| PageSettings | image | 6000 | 0 |  |  |  |
| LastUpdatedDate | datetime | 8 | 0 |  |  |  |

