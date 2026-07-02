# dbo.vw_aspnet_Profiles

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_aspnet_Profiles"]
    dbo_aspnet_Profile(["dbo.aspnet_Profile"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.aspnet_Profile |

## View Code

```sql
CREATE VIEW [dbo].[vw_aspnet_Profiles]
  AS SELECT [dbo].[aspnet_Profile].[UserId], [dbo].[aspnet_Profile].[LastUpdatedDate],
      [DataSize]=  DATALENGTH([dbo].[aspnet_Profile].[PropertyNames])
                 + DATALENGTH([dbo].[aspnet_Profile].[PropertyValuesString])
                 + DATALENGTH([dbo].[aspnet_Profile].[PropertyValuesBinary])
  FROM [dbo].[aspnet_Profile]
```

