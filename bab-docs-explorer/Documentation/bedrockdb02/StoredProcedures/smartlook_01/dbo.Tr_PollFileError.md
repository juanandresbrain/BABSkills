# dbo.Tr_PollFileError

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Tr_PollFileError"]
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
    dbo_Tr_Directory(["dbo.Tr_Directory"]) --> SP
    dbo_Tr_PollFileHistory(["dbo.Tr_PollFileHistory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sv_GetNextID |
| dbo.Tr_Directory |
| dbo.Tr_PollFileHistory |

## Stored Procedure Code

```sql

```

