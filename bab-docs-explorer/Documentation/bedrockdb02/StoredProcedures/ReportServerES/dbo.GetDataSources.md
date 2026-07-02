# dbo.GetDataSources

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDataSources"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_DataSource(["dbo.DataSource"]) --> SP
    dbo_ExtendedDataSources(["dbo.ExtendedDataSources"]) --> SP
    dbo_ModelItemPolicy(["dbo.ModelItemPolicy"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.DataSource |
| dbo.ExtendedDataSources |
| dbo.ModelItemPolicy |
| dbo.SecData |

## Stored Procedure Code

```sql

```

