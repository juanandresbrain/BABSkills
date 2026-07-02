# dbo.Tr_AddPollFile

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Tr_AddPollFile"]
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
    dbo_Tr_Directory(["dbo.Tr_Directory"]) --> SP
    dbo_Tr_PollFile(["dbo.Tr_PollFile"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sv_GetNextID |
| dbo.Tr_Directory |
| dbo.Tr_PollFile |

## Stored Procedure Code

```sql

```

