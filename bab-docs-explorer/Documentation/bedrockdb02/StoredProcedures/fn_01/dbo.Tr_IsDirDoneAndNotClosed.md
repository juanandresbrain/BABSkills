# dbo.Tr_IsDirDoneAndNotClosed

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Tr_IsDirDoneAndNotClosed"]
    dbo_Tr_Directory(["dbo.Tr_Directory"]) --> SP
    dbo_Tr_Parameter(["dbo.Tr_Parameter"]) --> SP
    dbo_Tr_PollFile(["dbo.Tr_PollFile"]) --> SP
    dbo_Tr_PollFileHistory(["dbo.Tr_PollFileHistory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Tr_Directory |
| dbo.Tr_Parameter |
| dbo.Tr_PollFile |
| dbo.Tr_PollFileHistory |

## Stored Procedure Code

```sql

```

