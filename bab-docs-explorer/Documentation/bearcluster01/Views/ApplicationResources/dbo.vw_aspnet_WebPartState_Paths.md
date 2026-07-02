# dbo.vw_aspnet_WebPartState_Paths

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_aspnet_WebPartState_Paths"]
    dbo_aspnet_Paths(["dbo.aspnet_Paths"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.aspnet_Paths |

## View Code

```sql
CREATE VIEW [dbo].[vw_aspnet_WebPartState_Paths]
  AS SELECT [dbo].[aspnet_Paths].[ApplicationId], [dbo].[aspnet_Paths].[PathId], [dbo].[aspnet_Paths].[Path], [dbo].[aspnet_Paths].[LoweredPath]
  FROM [dbo].[aspnet_Paths]
```

