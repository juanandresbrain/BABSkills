# dbo.Ex_ExecutionStart

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Ex_ExecutionStart"]
    dbo_Ex_ExecutionHistory(["dbo.Ex_ExecutionHistory"]) --> SP
    dbo_Ex_ServerMain(["dbo.Ex_ServerMain"]) --> SP
    dbo_Ex_ServerThread(["dbo.Ex_ServerThread"]) --> SP
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Ex_ExecutionHistory |
| dbo.Ex_ServerMain |
| dbo.Ex_ServerThread |
| dbo.Sv_GetNextID |

## Stored Procedure Code

```sql

```

