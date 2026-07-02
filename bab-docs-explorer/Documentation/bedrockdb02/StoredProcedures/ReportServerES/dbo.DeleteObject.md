# dbo.DeleteObject

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteObject"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_CleanOrphanedPolicies(["dbo.CleanOrphanedPolicies"]) --> SP
    dbo_DataSets(["dbo.DataSets"]) --> SP
    dbo_DataSource(["dbo.DataSource"]) --> SP
    dbo_ExecutionCache(["dbo.ExecutionCache"]) --> SP
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_History(["dbo.History"]) --> SP
    dbo_ModelDrill(["dbo.ModelDrill"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
    dbo_TempCatalog(["dbo.TempCatalog"]) --> SP
    dbo_TempDataSets(["dbo.TempDataSets"]) --> SP
    dbo_TempDataSources(["dbo.TempDataSources"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.CleanOrphanedPolicies |
| dbo.DataSets |
| dbo.DataSource |
| dbo.ExecutionCache |
| dbo.GetUserID |
| dbo.History |
| dbo.ModelDrill |
| dbo.SnapshotData |
| dbo.TempCatalog |
| dbo.TempDataSets |
| dbo.TempDataSources |

## Stored Procedure Code

```sql

```

