# dbo.Sr_HistoryCleanup

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_HistoryCleanup"]
    dbo_Sr_History(["dbo.Sr_History"]) --> SP
    dbo_Sr_Parameter(["dbo.Sr_Parameter"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_History |
| dbo.Sr_Parameter |

## Stored Procedure Code

```sql

```

