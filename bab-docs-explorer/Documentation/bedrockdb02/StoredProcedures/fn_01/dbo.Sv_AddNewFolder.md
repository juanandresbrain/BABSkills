# dbo.Sv_AddNewFolder

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_AddNewFolder"]
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
    dbo_Sv_UserFolder(["dbo.Sv_UserFolder"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sv_GetNextID |
| dbo.Sv_UserFolder |

## Stored Procedure Code

```sql

```

