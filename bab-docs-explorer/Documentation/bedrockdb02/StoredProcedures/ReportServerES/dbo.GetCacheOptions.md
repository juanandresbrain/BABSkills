# dbo.GetCacheOptions

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetCacheOptions"]
    dbo_CachePolicy(["dbo.CachePolicy"]) --> SP
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_reportschedule(["dbo.reportschedule"]) --> SP
    dbo_Schedule(["dbo.Schedule"]) --> SP
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CachePolicy |
| dbo.Catalog |
| dbo.reportschedule |
| dbo.Schedule |
| dbo.Users |

## Stored Procedure Code

```sql

```

