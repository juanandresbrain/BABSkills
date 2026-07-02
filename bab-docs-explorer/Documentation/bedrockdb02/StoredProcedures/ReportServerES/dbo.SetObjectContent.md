# dbo.SetObjectContent

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetObjectContent"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_ExtendEditSessionLifetime(["dbo.ExtendEditSessionLifetime"]) --> SP
    dbo_FlushCacheById(["dbo.FlushCacheById"]) --> SP
    dbo_FlushReportFromCache(["dbo.FlushReportFromCache"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
    dbo_TempCatalog(["dbo.TempCatalog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.ExtendEditSessionLifetime |
| dbo.FlushCacheById |
| dbo.FlushReportFromCache |
| dbo.SnapshotData |
| dbo.TempCatalog |

## Stored Procedure Code

```sql

```

