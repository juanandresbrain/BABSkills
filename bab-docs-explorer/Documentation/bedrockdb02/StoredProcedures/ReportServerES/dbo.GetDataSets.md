# dbo.GetDataSets

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDataSets"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_ExtendedDataSets(["dbo.ExtendedDataSets"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.ExtendedDataSets |
| dbo.SecData |

## Stored Procedure Code

```sql

```

