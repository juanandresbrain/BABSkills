# dbo.FlushReportFromCache

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FlushReportFromCache"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_EC(["dbo.EC"]) --> SP
    dbo_ExecutionCache(["dbo.ExecutionCache"]) --> SP
    dbo_SN(["dbo.SN"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.EC |
| dbo.ExecutionCache |
| dbo.SN |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

