# dbo.Sr_MachineStart

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_MachineStart"]
    dbo_Sr_History(["dbo.Sr_History"]) --> SP
    dbo_Sr_Machine(["dbo.Sr_Machine"]) --> SP
    dbo_Sr_Parameter(["dbo.Sr_Parameter"]) --> SP
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_History |
| dbo.Sr_Machine |
| dbo.Sr_Parameter |
| dbo.Sv_GetNextID |

## Stored Procedure Code

```sql

```

