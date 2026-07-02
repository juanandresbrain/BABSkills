# dbo.SetPolicy

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetPolicy"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_Policies(["dbo.Policies"]) --> SP
    dbo_PolicyUserRole(["dbo.PolicyUserRole"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.Policies |
| dbo.PolicyUserRole |
| dbo.SecData |

## Stored Procedure Code

```sql

```

