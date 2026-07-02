# dbo.Ex_ExecutionDone

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Ex_ExecutionDone"]
    dbo_Ex_ExecutionHistory(["dbo.Ex_ExecutionHistory"]) --> SP
    dbo_Ex_ServerMain(["dbo.Ex_ServerMain"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Ex_ExecutionHistory |
| dbo.Ex_ServerMain |

## Stored Procedure Code

```sql

```

