# dbo.Tr_ClosePollFile

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Tr_ClosePollFile"]
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
    dbo_Tr_PollFile(["dbo.Tr_PollFile"]) --> SP
    dbo_Tr_PollFileHistory(["dbo.Tr_PollFileHistory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sv_GetNextID |
| dbo.Tr_PollFile |
| dbo.Tr_PollFileHistory |

## Stored Procedure Code

```sql

```

