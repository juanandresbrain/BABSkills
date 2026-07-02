# dbo.AddDataSource

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddDataSource"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_DataSource(["dbo.DataSource"]) --> SP
    dbo_ExtendEditSessionLifetime(["dbo.ExtendEditSessionLifetime"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
    dbo_TempDataSources(["dbo.TempDataSources"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.DataSource |
| dbo.ExtendEditSessionLifetime |
| dbo.SecData |
| dbo.TempDataSources |

## Stored Procedure Code

```sql

```

