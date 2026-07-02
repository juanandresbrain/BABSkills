# dbo.AddDataSet

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddDataSet"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_DataSets(["dbo.DataSets"]) --> SP
    dbo_ExtendEditSessionLifetime(["dbo.ExtendEditSessionLifetime"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
    dbo_TempDataSets(["dbo.TempDataSets"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.DataSets |
| dbo.ExtendEditSessionLifetime |
| dbo.SecData |
| dbo.TempDataSets |

## Stored Procedure Code

```sql

```

