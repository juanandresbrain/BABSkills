# dbo.Tr_GetNextPollFile

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Tr_GetNextPollFile"]
    dbo_Tr_Directory(["dbo.Tr_Directory"]) --> SP
    dbo_Tr_PollFile(["dbo.Tr_PollFile"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Tr_Directory |
| dbo.Tr_PollFile |

## Stored Procedure Code

```sql

```

