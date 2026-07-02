# dbo.SetCacheOptions

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetCacheOptions"]
    dbo_CachePolicy(["dbo.CachePolicy"]) --> SP
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_FlushReportFromCache(["dbo.FlushReportFromCache"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CachePolicy |
| dbo.Catalog |
| dbo.FlushReportFromCache |

## Stored Procedure Code

```sql

```

