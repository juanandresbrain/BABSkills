# dbo.Sr_ServerStart

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_ServerStart"]
    dbo_Sr_History(["dbo.Sr_History"]) --> SP
    dbo_Sr_Parameter(["dbo.Sr_Parameter"]) --> SP
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_History |
| dbo.Sr_Parameter |
| dbo.Sv_GetNextID |

## Stored Procedure Code

```sql

```

