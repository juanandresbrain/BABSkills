# dbo.CleanOrphanedPolicies

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanOrphanedPolicies"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_ModelItemPolicy(["dbo.ModelItemPolicy"]) --> SP
    dbo_Policies(["dbo.Policies"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.ModelItemPolicy |
| dbo.Policies |

## Stored Procedure Code

```sql

```

