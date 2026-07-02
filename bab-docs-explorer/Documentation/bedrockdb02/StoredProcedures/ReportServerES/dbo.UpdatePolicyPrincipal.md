# dbo.UpdatePolicyPrincipal

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdatePolicyPrincipal"]
    dbo_GetPrincipalID(["dbo.GetPrincipalID"]) --> SP
    dbo_PolicyUserRole(["dbo.PolicyUserRole"]) --> SP
    dbo_Roles(["dbo.Roles"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GetPrincipalID |
| dbo.PolicyUserRole |
| dbo.Roles |

## Stored Procedure Code

```sql

```

