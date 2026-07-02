# dbo.GetModelsAndPerspectives

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetModelsAndPerspectives"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_ModelPerspective(["dbo.ModelPerspective"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.ModelPerspective |
| dbo.SecData |

## Stored Procedure Code

```sql

```

