# dbo.vw_aspnet_WebPartState_User

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_aspnet_WebPartState_User"]
    dbo_aspnet_PersonalizationPerUser(["dbo.aspnet_PersonalizationPerUser"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.aspnet_PersonalizationPerUser |

## View Code

```sql
CREATE VIEW [dbo].[vw_aspnet_WebPartState_User]
  AS SELECT [dbo].[aspnet_PersonalizationPerUser].[PathId], [dbo].[aspnet_PersonalizationPerUser].[UserId], [DataSize]=DATALENGTH([dbo].[aspnet_PersonalizationPerUser].[PageSettings]), [dbo].[aspnet_PersonalizationPerUser].[LastUpdatedDate]
  FROM [dbo].[aspnet_PersonalizationPerUser]
```

