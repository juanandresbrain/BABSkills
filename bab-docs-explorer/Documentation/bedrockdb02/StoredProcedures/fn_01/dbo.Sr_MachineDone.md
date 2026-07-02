# dbo.Sr_MachineDone

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_MachineDone"]
    dbo_Sr_History(["dbo.Sr_History"]) --> SP
    dbo_Sr_Machine(["dbo.Sr_Machine"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_History |
| dbo.Sr_Machine |

## Stored Procedure Code

```sql

```

