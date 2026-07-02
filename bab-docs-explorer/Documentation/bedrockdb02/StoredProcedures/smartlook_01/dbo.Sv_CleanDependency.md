# dbo.Sv_CleanDependency

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_CleanDependency"]
    dbo_Sv_Deleted(["dbo.Sv_Deleted"]) --> SP
    dbo_Sv_DeletedDependency(["dbo.Sv_DeletedDependency"]) --> SP
    dbo_Sv_Object(["dbo.Sv_Object"]) --> SP
    dbo_Sv_ObjectDependency(["dbo.Sv_ObjectDependency"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sv_Deleted |
| dbo.Sv_DeletedDependency |
| dbo.Sv_Object |
| dbo.Sv_ObjectDependency |

## Stored Procedure Code

```sql

```

